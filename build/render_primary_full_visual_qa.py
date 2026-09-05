#!/usr/bin/env python3
"""Render and inventory every page of the accepted Standard-Farsi PDF.

This is a read-only PDF QA helper.  It renders bounded batches with Poppler,
computes simple pixel/geometry diagnostics for every page, and assembles
no-resize 4x4 inspection sheets.  It does not modify or rewrite the PDF.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw
from pypdf import PdfReader


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha256(rows: list[dict]) -> str:
    payload = json.dumps(rows, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def command_version(executable: str) -> str:
    completed = subprocess.run(
        [executable, "-v"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return completed.stdout.strip().splitlines()[0]


def ink_count(image: Image.Image, threshold: int) -> int:
    histogram = image.histogram()
    return sum(histogram[:threshold])


def ink_bbox(image: Image.Image, threshold: int) -> tuple[int, int, int, int] | None:
    mask = image.point(lambda value: 255 if value < threshold else 0, mode="1")
    return mask.getbbox()


def edge_ink_count(gray: Image.Image, width: int, threshold: int) -> dict[str, int]:
    page_width, page_height = gray.size
    return {
        "left": ink_count(gray.crop((0, 0, width, page_height)), threshold),
        "right": ink_count(gray.crop((page_width - width, 0, page_width, page_height)), threshold),
        "top": ink_count(gray.crop((0, 0, page_width, width)), threshold),
        "bottom": ink_count(gray.crop((0, page_height - width, page_width, page_height)), threshold),
    }


def colour_pixel_count(rgb: Image.Image, chroma_threshold: int = 18, white_threshold: int = 248) -> int:
    red, green, blue = rgb.split()
    maximum = ImageChops.lighter(ImageChops.lighter(red, green), blue)
    minimum = ImageChops.darker(ImageChops.darker(red, green), blue)
    chroma = ImageChops.subtract(maximum, minimum)
    chroma_mask = chroma.point(lambda value: 255 if value >= chroma_threshold else 0, mode="1")
    visible_mask = minimum.point(lambda value: 255 if value < white_threshold else 0, mode="1")
    combined = ImageChops.multiply(chroma_mask.convert("L"), visible_mask.convert("L"))
    return sum(combined.histogram()[1:])


def render_batches(pdf: Path, page_dir: Path, executable: str, dpi: int, page_count: int, batch_size: int) -> None:
    page_dir.mkdir(parents=True, exist_ok=True)
    existing = sorted(page_dir.glob("page-*.png"))
    if len(existing) == page_count:
        print(f"Reusing {len(existing)} existing page rasters", flush=True)
        return
    if existing:
        raise RuntimeError(f"Refusing partial raster reuse: found {len(existing)} of {page_count}")

    for first in range(1, page_count + 1, batch_size):
        last = min(page_count, first + batch_size - 1)
        prefix = page_dir / f"batch-{first:04d}-{last:04d}"
        command = [
            executable,
            "-png",
            "-r",
            str(dpi),
            "-f",
            str(first),
            "-l",
            str(last),
            str(pdf),
            str(prefix),
        ]
        subprocess.run(command, check=True)
        batch_files = sorted(page_dir.glob(f"{prefix.name}-*.png"))
        expected = last - first + 1
        if len(batch_files) != expected:
            raise RuntimeError(
                f"Poppler batch {first}-{last} produced {len(batch_files)} PNGs, expected {expected}"
            )
        for offset, source in enumerate(batch_files):
            target = page_dir / f"page-{first + offset:04d}.png"
            source.replace(target)
        print(f"Rendered pages {first}-{last} of {page_count}", flush=True)


def page_geometry(reader: PdfReader, page_number: int) -> dict:
    page = reader.pages[page_number - 1]
    media = [float(value) for value in page.mediabox]
    crop = [float(value) for value in page.cropbox]
    annotations_object = page.get("/Annots")
    if annotations_object is None:
        annotations = []
    else:
        try:
            annotations = annotations_object.get_object()
        except AttributeError:
            annotations = annotations_object
    link_count = 0
    for reference in annotations:
        try:
            annotation = reference.get_object()
            if str(annotation.get("/Subtype")) == "/Link":
                link_count += 1
        except Exception:
            continue
    return {
        "media_box_points": media,
        "crop_box_points": crop,
        "rotate_degrees": int(page.get("/Rotate", 0) or 0) % 360,
        "annotation_count": len(annotations),
        "link_annotation_count": link_count,
    }


def analyse_pages(page_dir: Path, reader: PdfReader, page_count: int, expected_pixels: tuple[int, int]) -> list[dict]:
    rows: list[dict] = []
    for page_number in range(1, page_count + 1):
        path = page_dir / f"page-{page_number:04d}.png"
        with Image.open(path) as opened:
            rgb = opened.convert("RGB")
            gray = rgb.convert("L")
            width, height = gray.size
            pixels = width * height
            nonwhite = ink_count(gray, 250)
            ink = ink_count(gray, 245)
            dark = ink_count(gray, 48)
            near_black = ink_count(gray, 12)
            bbox = ink_bbox(gray, 245)
            edge = edge_ink_count(gray, 3, 245)
            colour = colour_pixel_count(rgb)

        flags: list[str] = []
        if (width, height) != expected_pixels:
            flags.append("UNEXPECTED_RASTER_DIMENSIONS")
        if nonwhite / pixels < 0.0002:
            flags.append("BLANK_CANDIDATE")
        elif nonwhite / pixels < 0.006:
            flags.append("SPARSE_PAGE_CANDIDATE")
        if dark / pixels > 0.45:
            flags.append("EXCESSIVE_DARKNESS_CANDIDATE")
        if bbox and (bbox[0] <= 1 or bbox[1] <= 1 or bbox[2] >= width - 1 or bbox[3] >= height - 1):
            flags.append("CONTENT_TOUCHES_RASTER_EDGE")
        if any(value > max(16, int(pixels * 0.00006)) for value in edge.values()):
            flags.append("EDGE_INK_CANDIDATE")

        geometry = page_geometry(reader, page_number)
        if geometry["rotate_degrees"] != 0:
            flags.append("NONZERO_PDF_ROTATION")
        if geometry["media_box_points"] != geometry["crop_box_points"]:
            flags.append("MEDIA_CROP_BOX_DIFFERENCE")

        row = {
            "page_one_based": page_number,
            "file": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "dimensions_pixels": [width, height],
            "pixel_metrics": {
                "nonwhite_fraction_lt250": round(nonwhite / pixels, 8),
                "ink_fraction_lt245": round(ink / pixels, 8),
                "dark_fraction_lt48": round(dark / pixels, 8),
                "near_black_fraction_lt12": round(near_black / pixels, 8),
                "colour_fraction_chroma18": round(colour / pixels, 8),
                "ink_bbox_lt245": list(bbox) if bbox else None,
                "edge_ink_lt245_three_pixels": edge,
            },
            "pdf_geometry": geometry,
            "automatic_flags": flags,
        }
        rows.append(row)
        if page_number % 100 == 0 or page_number == page_count:
            print(f"Analysed pages 1-{page_number} of {page_count}", flush=True)
    return rows


def assemble_sheets(
    page_dir: Path,
    sheet_dir: Path,
    page_count: int,
    columns: int,
    rows: int,
    expected_pixels: tuple[int, int],
) -> list[dict]:
    sheet_dir.mkdir(parents=True, exist_ok=True)
    page_width, page_height = expected_pixels
    label_height = 28
    gutter = 12
    tile_height = label_height + page_height
    sheet_width = gutter + columns * (page_width + gutter)
    sheet_height = gutter + rows * (tile_height + gutter)
    pages_per_sheet = columns * rows
    inventory: list[dict] = []

    for sheet_number, first in enumerate(range(1, page_count + 1, pages_per_sheet), start=1):
        last = min(page_count, first + pages_per_sheet - 1)
        target = sheet_dir / f"sheet-{sheet_number:03d}-pages-{first:04d}-{last:04d}.png"
        canvas = Image.new("RGB", (sheet_width, sheet_height), (192, 192, 192))
        draw = ImageDraw.Draw(canvas)
        for offset, page_number in enumerate(range(first, last + 1)):
            column = offset % columns
            row = offset // columns
            x = gutter + column * (page_width + gutter)
            y = gutter + row * (tile_height + gutter)
            draw.rectangle((x, y, x + page_width - 1, y + label_height - 1), fill=(28, 28, 28))
            draw.text((x + 6, y + 7), f"PHYSICAL PAGE {page_number:04d}", fill=(255, 255, 255))
            with Image.open(page_dir / f"page-{page_number:04d}.png") as page:
                canvas.paste(page.convert("RGB"), (x, y + label_height))
        canvas.save(target, format="PNG", compress_level=6)
        inventory.append(
            {
                "sheet": sheet_number,
                "file": target.name,
                "page_range_one_based": [first, last],
                "page_count": last - first + 1,
                "bytes": target.stat().st_size,
                "sha256": sha256(target),
                "dimensions_pixels": [sheet_width, sheet_height],
            }
        )
        print(f"Assembled sheet {sheet_number}/{math.ceil(page_count / pages_per_sheet)}", flush=True)
    return inventory


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--page-dir", required=True, type=Path)
    parser.add_argument("--sheet-dir", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--dpi", type=int, default=96)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--columns", type=int, default=4)
    parser.add_argument("--rows", type=int, default=4)
    args = parser.parse_args()

    pdf = args.pdf.resolve()
    if not pdf.is_file():
        raise FileNotFoundError(pdf)
    executable = shutil.which("pdftoppm")
    if executable is None:
        raise RuntimeError("pdftoppm not found")
    executable_path = Path(executable).resolve()

    identity_before = {"bytes": pdf.stat().st_size, "sha256": sha256(pdf)}
    reader = PdfReader(str(pdf))
    page_count = len(reader.pages)
    first_media = [float(value) for value in reader.pages[0].mediabox]
    expected_width = round((first_media[2] - first_media[0]) * args.dpi / 72)
    expected_height = round((first_media[3] - first_media[1]) * args.dpi / 72)
    expected_pixels = (expected_width, expected_height)

    render_batches(pdf, args.page_dir.resolve(), str(executable_path), args.dpi, page_count, args.batch_size)
    page_rows = analyse_pages(args.page_dir.resolve(), reader, page_count, expected_pixels)
    sheet_rows = assemble_sheets(
        args.page_dir.resolve(),
        args.sheet_dir.resolve(),
        page_count,
        args.columns,
        args.rows,
        expected_pixels,
    )
    identity_after = {"bytes": pdf.stat().st_size, "sha256": sha256(pdf)}
    if identity_before != identity_after:
        raise RuntimeError("Source PDF identity changed during read-only rendering")

    flagged_pages = [
        {"page_one_based": row["page_one_based"], "automatic_flags": row["automatic_flags"]}
        for row in page_rows
        if row["automatic_flags"]
    ]
    manifest = {
        "schema": "farsi-standard-primary-full-visual-render-manifest-v1",
        "created_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "status": "RENDER_COMPLETE_PENDING_HUMAN_VISUAL_INSPECTION",
        "read_only_pdf_operation": True,
        "source_pdf": {
            "path": pdf.as_posix(),
            "page_count": page_count,
            "identity_before": identity_before,
            "identity_after": identity_after,
            "unchanged": identity_before == identity_after,
        },
        "renderer": {
            "path": executable_path.as_posix(),
            "bytes": executable_path.stat().st_size,
            "sha256": sha256(executable_path),
            "version": command_version(str(executable_path)),
            "arguments": ["-png", "-r", str(args.dpi)],
            "dpi": args.dpi,
            "expected_page_dimensions_pixels": list(expected_pixels),
            "batch_size": args.batch_size,
        },
        "page_rasters": {
            "directory": args.page_dir.resolve().as_posix(),
            "count": len(page_rows),
            "contiguous_pages_one_based": [1, page_count],
            "canonical_inventory_sha256": canonical_sha256(page_rows),
            "inventory": page_rows,
        },
        "inspection_sheets": {
            "directory": args.sheet_dir.resolve().as_posix(),
            "layout": {
                "columns": args.columns,
                "rows": args.rows,
                "pages_per_sheet": args.columns * args.rows,
                "page_images_resized": False,
                "label_height_pixels": 28,
                "gutter_pixels": 12,
            },
            "count": len(sheet_rows),
            "canonical_inventory_sha256": canonical_sha256(sheet_rows),
            "inventory": sheet_rows,
        },
        "automatic_diagnostics": {
            "flagged_page_count": len(flagged_pages),
            "flagged_pages": flagged_pages,
            "thresholds": {
                "blank_nonwhite_fraction_lt250": 0.0002,
                "sparse_nonwhite_fraction_lt250": 0.006,
                "excessive_dark_fraction_lt48": 0.45,
                "content_bbox_edge_distance_pixels": 1,
                "edge_strip_width_pixels": 3,
            },
            "disposition": "Candidates require visual review; automatic flags are not defects by themselves.",
        },
        "limitations": [
            "This manifest proves rendering and deterministic inventory, not human visual acceptance.",
            "The final receipt must bind contact-sheet review and higher-resolution samples or flagged pages.",
        ],
    }
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.manifest.resolve()}", flush=True)
    print(f"Flagged {len(flagged_pages)} pages for focused review", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
