#!/usr/bin/env python3
"""Repair the Persian screen PDFs' RTL-inflated hyperlink rectangles.

This is deliberately fail-closed and byte-gated.  It changes only the third
number (x1) of explicitly identified /Link /Rect arrays.  The replacement x1
is the right edge of a uniquely selected hyperlink-coloured text span plus a
one-point annotation tolerance.  Ambiguous wrapped citations are resolved by
an exact page/xref/text-colour/bbox assertion recorded below.

The script refuses unknown inputs, pre-existing outputs, unexpected link
counts, unexpected source rectangles, ambiguous glyph spans, and any output
whose page content, link targets, boxes, outline, metadata, or non-rectangle
annotation fields differ from the raw input.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import fitz
from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, FloatObject, IndirectObject


PAGE_WIDTH = 960.0
RIGHT_TOLERANCE_PT = 1.0
HYPERLINK_COLOURS = {0x00FF00, 0xFF0000, 0x00AEEF}


# Exact manual assertions for the fifteen wrapped/bidirectional cases where
# the annotation's preserved x0 starts on adjacent black/grey text rather than
# on its coloured target run.  Bboxes use PyMuPDF's top-left coordinate system.
MANUAL_MAIN: dict[tuple[int, int], dict[str, Any]] = {
    (314, 6815): {"text": " 12.28", "colour": 0xFF0000, "bbox": [770.596, 145.175, 809.099, 163.768]},
    (315, 6837): {"text": " 12.18", "colour": 0xFF0000, "bbox": [813.635, 427.541, 852.138, 446.134]},
    (323, 6966): {"text": "2021", "colour": 0x00FF00, "bbox": [444.907, 494.156, 464.378, 507.068]},
    (579, 9576): {"text": " 22.32", "colour": 0xFF0000, "bbox": [770.596, 450.559, 809.099, 469.152]},
    (584, 9660): {"text": " 22.21", "colour": 0xFF0000, "bbox": [813.635, 315.843, 852.138, 334.436]},
    (1466, 19539): {"text": "1915", "colour": 0x00FF00, "bbox": [824.100, 272.924, 852.138, 291.517]},
    (1478, 19731): {"text": "2003", "colour": 0x00FF00, "bbox": [824.100, 182.291, 852.138, 200.884]},
    (1513, 20000): {"text": "2013", "colour": 0x00FF00, "bbox": [824.100, 100.253, 852.138, 118.846]},
    (1513, 20005): {"text": "2013", "colour": 0x00FF00, "bbox": [726.806, 125.678, 754.844, 144.271]},
    (1513, 20008): {"text": "2019", "colour": 0x00FF00, "bbox": [522.729, 125.678, 550.767, 144.271]},
    (1513, 20010): {"text": "2018", "colour": 0x00FF00, "bbox": [685.217, 151.103, 713.255, 169.696]},
    (1513, 20022): {"text": "2004", "colour": 0x00FF00, "bbox": [817.092, 227.377, 845.130, 245.970]},
    (1533, 20206): {"text": "2014", "colour": 0x00FF00, "bbox": [662.722, 136.560, 690.760, 155.153]},
    (1542, 20400): {"text": "1905", "colour": 0x00FF00, "bbox": [421.655, 365.383, 449.693, 383.976]},
    (1568, 20647): {"text": "1953", "colour": 0x00FF00, "bbox": [806.885, 323.435, 834.923, 342.028]},
}


CONFIG: dict[str, dict[str, Any]] = {
    "open-logic-complete-fa-IR-screen.raw-before-link-repair.pdf": {
        "sha256": "71FBF902707E833FA6D707DFB2C3D39D9FC134DF33538CA5AE3529F07F530E2E",
        "pages": 1578,
        "links": 2983,
        "overflow": 137,
        "automatic": 122,
        "manual": MANUAL_MAIN,
    },
    "open-logic-closure-supplement-fa-IR-screen.raw-before-link-repair.pdf": {
        "sha256": "47ABE97A267E94D3759BD42E89E844A9EE01B44E5E1E72D04A5EC00D9341093B",
        "pages": 222,
        "links": 137,
        "overflow": 9,
        "automatic": 9,
        "manual": {},
    },
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def nearly(a: float, b: float, tolerance: float = 0.01) -> bool:
    return math.isclose(float(a), float(b), rel_tol=0.0, abs_tol=tolerance)


def bbox_list(rect: fitz.Rect) -> list[float]:
    return [round(float(value), 6) for value in rect]


def vertical_overlap_ratio(a: fitz.Rect, b: fitz.Rect) -> float:
    overlap = max(0.0, min(a.y1, b.y1) - max(a.y0, b.y0))
    return overlap / max(0.001, min(a.height, b.height))


def page_spans(page: fitz.Page) -> list[dict[str, Any]]:
    spans: list[dict[str, Any]] = []
    for block in page.get_text("dict").get("blocks", []):
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                spans.append(
                    {
                        "rect": fitz.Rect(span["bbox"]),
                        "colour": int(span.get("color", 0)),
                        "text": str(span.get("text", "")),
                        "font": str(span.get("font", "")),
                        "size": float(span.get("size", 0.0)),
                    }
                )
    return spans


def select_span(
    page_number: int,
    link: dict[str, Any],
    spans: list[dict[str, Any]],
    manual: dict[tuple[int, int], dict[str, Any]],
) -> tuple[dict[str, Any], str]:
    rect = fitz.Rect(link["from"])
    xref = int(link["xref"])
    key = (page_number, xref)
    anchored = [
        span
        for span in spans
        if span["colour"] in HYPERLINK_COLOURS
        and vertical_overlap_ratio(rect, span["rect"]) >= 0.45
        and 0.30 <= span["rect"].x0 - rect.x0 <= 1.70
    ]

    if key in manual:
        if anchored:
            raise RuntimeError(f"Manual case unexpectedly gained an automatic anchor: {key}")
        expected = manual[key]
        matches = []
        for span in spans:
            if span["text"] != expected["text"] or span["colour"] != expected["colour"]:
                continue
            if all(nearly(actual, wanted, 0.015) for actual, wanted in zip(span["rect"], expected["bbox"])):
                matches.append(span)
        if len(matches) != 1:
            raise RuntimeError(f"Manual glyph assertion {key} matched {len(matches)} spans")
        if vertical_overlap_ratio(rect, matches[0]["rect"]) < 0.45:
            raise RuntimeError(f"Manual glyph assertion {key} is outside the annotation band")
        return matches[0], "manual-explicit-complementary-run"

    if len(anchored) != 1:
        raise RuntimeError(f"Automatic glyph assertion {key} matched {len(anchored)} spans")
    return anchored[0], "automatic-unique-hyperlink-colour-x0-anchor"


def canonical(value: Any) -> Any:
    """Canonicalize the small, non-cyclic values used in link annotations."""
    if isinstance(value, IndirectObject):
        return {"indirect": [value.idnum, value.generation]}
    if isinstance(value, dict):
        return {str(key): canonical(val) for key, val in sorted(value.items(), key=lambda item: str(item[0]))}
    if isinstance(value, (list, tuple, ArrayObject)):
        return [canonical(item) for item in value]
    if isinstance(value, bytes):
        return {"bytes_hex": value.hex()}
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    try:
        return float(value)
    except (TypeError, ValueError):
        return str(value)


def without_object_xrefs(value: Any) -> Any:
    """Remove serialization-local object numbers from semantic outline data."""
    if isinstance(value, dict):
        return {
            key: without_object_xrefs(item)
            for key, item in value.items()
            if str(key) != "xref"
        }
    if isinstance(value, (list, tuple)):
        return [without_object_xrefs(item) for item in value]
    return value


def link_records(reader: PdfReader) -> list[list[dict[str, Any]]]:
    result: list[list[dict[str, Any]]] = []
    for page in reader.pages:
        page_records = []
        for reference in page.get("/Annots", []):
            annotation = reference.get_object()
            if str(annotation.get("/Subtype")) != "/Link":
                continue
            rect = [float(value) for value in annotation["/Rect"]]
            fields = {
                str(key): canonical(value)
                for key, value in annotation.items()
                if str(key) not in {"/Rect", "/P"}
            }
            page_records.append({"rect": rect, "fields": fields})
        result.append(page_records)
    return result


def content_hashes(reader: PdfReader) -> list[str]:
    hashes = []
    for page in reader.pages:
        contents = page.get_contents()
        data = b"" if contents is None else contents.get_data()
        hashes.append(hashlib.sha256(data).hexdigest().upper())
    return hashes


def page_geometry(reader: PdfReader) -> list[dict[str, Any]]:
    return [
        {
            "mediabox": [float(value) for value in page.mediabox],
            "cropbox": [float(value) for value in page.cropbox],
            "rotation": int(page.get("/Rotate", 0)),
        }
        for page in reader.pages
    ]


def fitz_semantics(path: Path) -> dict[str, Any]:
    document = fitz.open(path)
    try:
        links = []
        overflow = []
        for page_index, page in enumerate(document):
            page_links = []
            for link in page.get_links():
                rect = fitz.Rect(link["from"])
                semantic = {
                    "kind": link.get("kind"),
                    "page": link.get("page"),
                    "to": None if link.get("to") is None else [round(float(v), 5) for v in link["to"]],
                    "uri": link.get("uri"),
                    "file": link.get("file"),
                    "nameddest": link.get("nameddest"),
                }
                page_links.append(semantic)
                if rect.x0 < 0 or rect.y0 < 0 or rect.x1 > page.rect.width or rect.y1 > page.rect.height:
                    overflow.append({"page": page_index + 1, "rect": bbox_list(rect), **semantic})
            links.append(page_links)
        return {
            "pages": document.page_count,
            "links": links,
            "link_count": sum(len(page_links) for page_links in links),
            "overflow": overflow,
            "toc": canonical(without_object_xrefs(document.get_toc(simple=False))),
            "metadata": canonical(document.metadata),
        }
    finally:
        document.close()


def build_mapping(input_path: Path, config: dict[str, Any]) -> list[dict[str, Any]]:
    document = fitz.open(input_path)
    try:
        if document.page_count != config["pages"]:
            raise RuntimeError(f"Unexpected page count: {document.page_count}")
        mapping = []
        total_links = 0
        automatic = 0
        manual_count = 0
        seen_manual: set[tuple[int, int]] = set()
        for page_index, page in enumerate(document):
            spans = page_spans(page)
            for link in page.get_links():
                total_links += 1
                rect = fitz.Rect(link["from"])
                if rect.x0 >= 0 and rect.y0 >= 0 and rect.x1 <= page.rect.width and rect.y1 <= page.rect.height:
                    continue
                if rect.x0 < 0 or rect.y0 < 0 or rect.y1 > page.rect.height:
                    raise RuntimeError(
                        f"Unsupported non-x1 overflow at page {page_index + 1}, xref {link.get('xref')}: {bbox_list(rect)}"
                    )
                span, mode = select_span(page_index + 1, link, spans, config["manual"])
                key = (page_index + 1, int(link["xref"]))
                if mode.startswith("manual"):
                    manual_count += 1
                    seen_manual.add(key)
                else:
                    automatic += 1
                new_x1 = float(span["rect"].x1) + RIGHT_TOLERANCE_PT
                if not rect.x0 < new_x1 <= PAGE_WIDTH:
                    raise RuntimeError(f"Invalid inferred x1 {new_x1} for {key}")
                mapping.append(
                    {
                        "page": page_index + 1,
                        "xref": int(link["xref"]),
                        "target": link.get("nameddest") or link.get("file") or link.get("uri"),
                        "selection": mode,
                        "glyph": {
                            "text_unicode_escape": span["text"].encode("unicode_escape").decode("ascii"),
                            "colour_rgb24": f"{span['colour']:06X}",
                            "font": span["font"],
                            "size_pt": round(span["size"], 6),
                            "bbox_top_left_pt": bbox_list(span["rect"]),
                        },
                        "old_rect_top_left_pt": bbox_list(rect),
                        "new_x1_pt": round(new_x1, 6),
                    }
                )
        if total_links != config["links"]:
            raise RuntimeError(f"Unexpected link count: {total_links}")
        if len(mapping) != config["overflow"]:
            raise RuntimeError(f"Unexpected overflow count: {len(mapping)}")
        if automatic != config["automatic"] or manual_count != len(config["manual"]):
            raise RuntimeError(f"Unexpected selection counts: automatic={automatic}, manual={manual_count}")
        if seen_manual != set(config["manual"]):
            raise RuntimeError(f"Unseen manual mappings: {set(config['manual']) - seen_manual}")
        return mapping
    finally:
        document.close()


def apply_mapping(input_path: Path, output_path: Path, mapping: list[dict[str, Any]]) -> None:
    reader = PdfReader(input_path)
    by_xref = {item["xref"]: item for item in mapping}
    changed = set()
    for page_number, page in enumerate(reader.pages, 1):
        for reference in page.get("/Annots", []):
            if reference.idnum not in by_xref:
                continue
            item = by_xref[reference.idnum]
            if item["page"] != page_number:
                raise RuntimeError(f"xref/page mismatch for {reference.idnum}")
            annotation = reference.get_object()
            if str(annotation.get("/Subtype")) != "/Link":
                raise RuntimeError(f"xref {reference.idnum} is not a /Link annotation")
            rect = annotation["/Rect"]
            old_top = item["old_rect_top_left_pt"]
            expected_pdf = [old_top[0], 540.0 - old_top[3], old_top[2], 540.0 - old_top[1]]
            if not all(nearly(actual, expected, 0.015) for actual, expected in zip(rect, expected_pdf)):
                raise RuntimeError(f"Raw /Rect mismatch for xref {reference.idnum}: {list(rect)}")
            rect[2] = FloatObject(item["new_x1_pt"])
            changed.add(reference.idnum)
    if changed != set(by_xref):
        raise RuntimeError(f"Missing annotation xrefs: {set(by_xref) - changed}")
    writer = PdfWriter()
    writer.pdf_header = reader.pdf_header
    writer.clone_document_from_reader(reader)
    with output_path.open("wb") as handle:
        writer.write(handle)


def verify_equivalence(input_path: Path, output_path: Path, mapping: list[dict[str, Any]]) -> dict[str, Any]:
    raw_reader = PdfReader(input_path)
    final_reader = PdfReader(output_path)
    if len(raw_reader.pages) != len(final_reader.pages):
        raise RuntimeError("Page count changed")
    raw_content = content_hashes(raw_reader)
    final_content = content_hashes(final_reader)
    if raw_content != final_content:
        changed_pages = [i + 1 for i, pair in enumerate(zip(raw_content, final_content)) if pair[0] != pair[1]]
        raise RuntimeError(f"Decoded page content changed on pages {changed_pages[:20]}")
    if page_geometry(raw_reader) != page_geometry(final_reader):
        raise RuntimeError("Page geometry changed")
    if canonical(raw_reader.metadata) != canonical(final_reader.metadata):
        raise RuntimeError("PDF metadata changed")

    raw_links = link_records(raw_reader)
    final_links = link_records(final_reader)
    if [len(page) for page in raw_links] != [len(page) for page in final_links]:
        raise RuntimeError("Per-page link annotation counts changed")
    expected = {(item["page"], item["xref"]): item for item in mapping}
    changed = []
    raw_xrefs = []
    for page in raw_reader.pages:
        raw_xrefs.append([
            reference.idnum
            for reference in page.get("/Annots", [])
            if str(reference.get_object().get("/Subtype")) == "/Link"
        ])
    for page_index, (raw_page, final_page) in enumerate(zip(raw_links, final_links), 1):
        for annotation_index, (raw, final) in enumerate(zip(raw_page, final_page)):
            if raw["fields"] != final["fields"]:
                raise RuntimeError(f"Non-rectangle annotation field changed at page {page_index}, index {annotation_index}")
            old_rect = raw["rect"]
            new_rect = final["rect"]
            xref = raw_xrefs[page_index - 1][annotation_index]
            item = expected.get((page_index, xref))
            if item is None:
                if any(not nearly(a, b, 0.0001) for a, b in zip(old_rect, new_rect)):
                    raise RuntimeError(f"Unapproved rectangle change at page {page_index}, xref {xref}")
                continue
            if any(not nearly(old_rect[i], new_rect[i], 0.0001) for i in (0, 1, 3)):
                raise RuntimeError(f"x0/y rectangle coordinate changed at page {page_index}, xref {xref}")
            if not nearly(new_rect[2], item["new_x1_pt"], 0.0001):
                raise RuntimeError(f"Incorrect x1 at page {page_index}, xref {xref}")
            changed.append({"page": page_index, "xref": xref, "old_x1": old_rect[2], "new_x1": new_rect[2]})
    if len(changed) != len(mapping):
        raise RuntimeError(f"Expected {len(mapping)} approved changes, observed {len(changed)}")

    raw_fitz = fitz_semantics(input_path)
    final_fitz = fitz_semantics(output_path)
    if raw_fitz["pages"] != final_fitz["pages"] or raw_fitz["link_count"] != final_fitz["link_count"]:
        raise RuntimeError("PyMuPDF page/link count changed")
    if raw_fitz["links"] != final_fitz["links"]:
        raise RuntimeError("Link actions or destinations changed")
    if raw_fitz["toc"] != final_fitz["toc"]:
        raise RuntimeError("Outline changed")
    if raw_fitz["metadata"] != final_fitz["metadata"]:
        raise RuntimeError("PyMuPDF metadata changed")
    if final_fitz["overflow"]:
        raise RuntimeError(f"Final PDF still has {len(final_fitz['overflow'])} overflowing links")
    return {
        "decoded_page_content_sha256_equal": True,
        "page_geometry_equal": True,
        "metadata_equal": True,
        "outline_equal": True,
        "per_page_link_counts_equal": True,
        "link_actions_and_destinations_equal": True,
        "non_rect_annotation_fields_equal": True,
        "changed_rectangles": len(changed),
        "final_link_overflow_count": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--evidence", required=True, type=Path)
    args = parser.parse_args()

    input_path = args.input.resolve()
    output_path = args.output.resolve()
    evidence_path = args.evidence.resolve()
    if not input_path.is_file():
        raise SystemExit(f"Input does not exist: {input_path}")
    if output_path.exists() or evidence_path.exists():
        raise SystemExit("Refusing to overwrite an existing output or evidence file")
    config = CONFIG.get(input_path.name)
    if config is None:
        raise SystemExit(f"Unsupported input basename: {input_path.name}")
    input_hash = sha256(input_path)
    if input_hash != config["sha256"]:
        raise SystemExit(f"Input SHA-256 mismatch: {input_hash}")

    mapping = build_mapping(input_path, config)
    apply_mapping(input_path, output_path, mapping)
    verification = verify_equivalence(input_path, output_path, mapping)
    evidence = {
        "schema": "fa-IR-rtl-link-rect-repair-v1",
        "input_basename": input_path.name,
        "input_bytes": input_path.stat().st_size,
        "input_sha256": input_hash,
        "output_bytes": output_path.stat().st_size,
        "output_sha256": sha256(output_path),
        "algorithm": {
            "only_mutation": "/Link /Rect third coordinate (x1)",
            "right_tolerance_pt": RIGHT_TOLERANCE_PT,
            "automatic_rule": "unique hyperlink-colour span in y band with span.x0 - Rect.x0 in [0.30, 1.70] pt",
            "manual_rule": "exact asserted complementary hyperlink-colour span for wrapped/paired bidi cases",
            "fail_closed": True,
        },
        "counts": {
            "pages": config["pages"],
            "all_links": config["links"],
            "repaired": len(mapping),
            "automatic": config["automatic"],
            "manual": len(config["manual"]),
        },
        "verification": verification,
        "mapping": mapping,
    }
    evidence_path.write_text(json.dumps(evidence, ensure_ascii=True, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({key: evidence[key] for key in ("input_basename", "input_sha256", "output_bytes", "output_sha256", "counts", "verification")}, indent=2))


if __name__ == "__main__":
    main()
