#!/usr/bin/env python3
"""Render selected full-reader risk/sample pages at high resolution."""

from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageDraw
from pypdf import PdfReader

from render_primary_full_visual_qa import canonical_sha256, command_version, sha256


def parse_page_spec(spec: str) -> set[int]:
    pages: set[int] = set()
    for token in spec.split(","):
        token = token.strip()
        if not token:
            continue
        if "-" in token:
            first_text, last_text = token.split("-", 1)
            first, last = int(first_text), int(last_text)
            if first > last:
                raise ValueError(f"Descending page range: {token}")
            pages.update(range(first, last + 1))
        else:
            pages.add(int(token))
    return pages


def contiguous_runs(pages: list[int]) -> list[tuple[int, int]]:
    if not pages:
        return []
    runs: list[tuple[int, int]] = []
    first = previous = pages[0]
    for page in pages[1:]:
        if page == previous + 1:
            previous = page
            continue
        runs.append((first, previous))
        first = previous = page
    runs.append((first, previous))
    return runs


def render_pages(pdf: Path, output: Path, executable: str, dpi: int, pages: list[int]) -> None:
    output.mkdir(parents=True, exist_ok=True)
    existing = sorted(output.glob("page-*.png"))
    if len(existing) == len(pages) and {int(path.stem.split("-")[-1]) for path in existing} == set(pages):
        print(f"Reusing {len(existing)} selected high-resolution rasters", flush=True)
        return
    if existing:
        raise RuntimeError("Refusing partial or mismatched selected-page raster reuse")

    for first, last in contiguous_runs(pages):
        prefix = output / f"batch-{first:04d}-{last:04d}"
        subprocess.run(
            [
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
            ],
            check=True,
        )
        generated = sorted(output.glob(f"{prefix.name}-*.png"))
        expected = last - first + 1
        if len(generated) != expected:
            raise RuntimeError(f"Run {first}-{last}: expected {expected} PNGs, got {len(generated)}")
        for offset, source in enumerate(generated):
            source.replace(output / f"page-{first + offset:04d}.png")
        print(f"Rendered high-resolution pages {first}-{last}", flush=True)


def assemble_sheets(page_dir: Path, sheet_dir: Path, pages: list[int], expected: tuple[int, int]) -> list[dict]:
    sheet_dir.mkdir(parents=True, exist_ok=True)
    columns = rows = 2
    label_height = 34
    gutter = 14
    page_width, page_height = expected
    tile_height = label_height + page_height
    sheet_width = gutter + columns * (page_width + gutter)
    sheet_height = gutter + rows * (tile_height + gutter)
    inventory: list[dict] = []
    for sheet_number, offset in enumerate(range(0, len(pages), 4), start=1):
        sheet_pages = pages[offset : offset + 4]
        target = sheet_dir / (
            f"risk-sheet-{sheet_number:03d}-pages-" + "-".join(f"{page:04d}" for page in sheet_pages) + ".png"
        )
        canvas = Image.new("RGB", (sheet_width, sheet_height), (192, 192, 192))
        draw = ImageDraw.Draw(canvas)
        for tile, page_number in enumerate(sheet_pages):
            column = tile % 2
            row = tile // 2
            x = gutter + column * (page_width + gutter)
            y = gutter + row * (tile_height + gutter)
            draw.rectangle((x, y, x + page_width - 1, y + label_height - 1), fill=(28, 28, 28))
            draw.text((x + 8, y + 9), f"PHYSICAL PAGE {page_number:04d} - 180 DPI", fill=(255, 255, 255))
            with Image.open(page_dir / f"page-{page_number:04d}.png") as page:
                if page.size != expected:
                    raise RuntimeError(f"Unexpected dimensions for physical page {page_number}: {page.size}")
                canvas.paste(page.convert("RGB"), (x, y + label_height))
        canvas.save(target, format="PNG", compress_level=6)
        inventory.append(
            {
                "sheet": sheet_number,
                "file": target.name,
                "physical_pages": sheet_pages,
                "bytes": target.stat().st_size,
                "sha256": sha256(target),
                "dimensions_pixels": [sheet_width, sheet_height],
            }
        )
        print(f"Assembled high-resolution sheet {sheet_number}/{math.ceil(len(pages) / 4)}", flush=True)
    return inventory


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--render-manifest", required=True, type=Path)
    parser.add_argument("--risk-map", required=True, type=Path)
    parser.add_argument("--page-dir", required=True, type=Path)
    parser.add_argument("--sheet-dir", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--extra-pages", default="1-16,1187-1201")
    parser.add_argument("--dpi", type=int, default=180)
    args = parser.parse_args()

    pdf = args.pdf.resolve()
    render_manifest_path = args.render_manifest.resolve()
    risk_map_path = args.risk_map.resolve()
    render_manifest = json.loads(render_manifest_path.read_text(encoding="utf-8"))
    risk_map = json.loads(risk_map_path.read_text(encoding="utf-8"))
    reader = PdfReader(str(pdf))
    page_count = len(reader.pages)

    risk_pages = set(risk_map["high_resolution_review_pages_one_based"])
    sparse_pages = {
        item["page_one_based"]
        for item in render_manifest["automatic_diagnostics"]["flagged_pages"]
    }
    extra_pages = parse_page_spec(args.extra_pages)
    pages = sorted(risk_pages | sparse_pages | extra_pages)
    invalid = [page for page in pages if page < 1 or page > page_count]
    if invalid:
        raise ValueError(f"Pages outside PDF: {invalid}")

    executable = shutil.which("pdftoppm")
    if executable is None:
        raise RuntimeError("pdftoppm not found")
    executable_path = Path(executable).resolve()
    identity_before = {"bytes": pdf.stat().st_size, "sha256": sha256(pdf)}
    render_pages(pdf, args.page_dir.resolve(), str(executable_path), args.dpi, pages)

    page_inventory = []
    for page in pages:
        path = args.page_dir.resolve() / f"page-{page:04d}.png"
        with Image.open(path) as image:
            dimensions = list(image.size)
        page_inventory.append(
            {
                "physical_page": page,
                "file": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "dimensions_pixels": dimensions,
                "selection_reasons": sorted(
                    reason
                    for reason, selected in {
                        "final_log_risk_mapping": page in risk_pages,
                        "automatic_sparse_or_other_pixel_flag": page in sparse_pages,
                        "systematic_front_or_end_matter_sample": page in extra_pages,
                    }.items()
                    if selected
                ),
            }
        )

    media = [float(value) for value in reader.pages[0].mediabox]
    expected = (
        round((media[2] - media[0]) * args.dpi / 72),
        round((media[3] - media[1]) * args.dpi / 72),
    )
    sheets = assemble_sheets(args.page_dir.resolve(), args.sheet_dir.resolve(), pages, expected)
    identity_after = {"bytes": pdf.stat().st_size, "sha256": sha256(pdf)}
    if identity_before != identity_after:
        raise RuntimeError("Source PDF identity changed during high-resolution rendering")

    result = {
        "schema": "farsi-standard-primary-visual-risk-pages-v1",
        "created_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "status": "HIGH_RESOLUTION_RENDER_COMPLETE_PENDING_VISUAL_ADJUDICATION",
        "source_pdf": {
            "path": pdf.as_posix(),
            "physical_pages": page_count,
            "identity_before": identity_before,
            "identity_after": identity_after,
            "unchanged": identity_before == identity_after,
        },
        "selection": {
            "risk_map": {"path": risk_map_path.as_posix(), "sha256": sha256(risk_map_path)},
            "render_manifest": {"path": render_manifest_path.as_posix(), "sha256": sha256(render_manifest_path)},
            "extra_page_specification": args.extra_pages,
            "final_log_risk_page_count": len(risk_pages),
            "automatic_flag_page_count": len(sparse_pages),
            "extra_sample_page_count": len(extra_pages),
            "union_page_count": len(pages),
            "pages_one_based": pages,
        },
        "renderer": {
            "path": executable_path.as_posix(),
            "bytes": executable_path.stat().st_size,
            "sha256": sha256(executable_path),
            "version": command_version(str(executable_path)),
            "arguments": ["-png", "-r", str(args.dpi)],
            "dpi": args.dpi,
            "expected_dimensions_pixels": list(expected),
        },
        "page_rasters": {
            "directory": args.page_dir.resolve().as_posix(),
            "count": len(page_inventory),
            "canonical_inventory_sha256": canonical_sha256(page_inventory),
            "inventory": page_inventory,
        },
        "inspection_sheets": {
            "directory": args.sheet_dir.resolve().as_posix(),
            "layout": {"columns": 2, "rows": 2, "page_images_resized": False},
            "count": len(sheets),
            "canonical_inventory_sha256": canonical_sha256(sheets),
            "inventory": sheets,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Selected {len(pages)} physical pages across {len(sheets)} sheets", flush=True)
    print(f"Wrote {args.output.resolve()}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
