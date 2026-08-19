#!/usr/bin/env python3
"""Fail-closed A4 adapter for the pinned Persian RTL link-rectangle repair."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
SHARED_REPAIR = HERE / "repair_rtl_link_rects_fa.py"
SPEC = importlib.util.spec_from_file_location("fa_rtl_link_repair_shared", SHARED_REPAIR)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load shared repair implementation: {SHARED_REPAIR}")
repair = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(repair)


repair.PAGE_WIDTH = 595.276

MANUAL_MAIN = {
    (152, 6071): {"text": " 12.24", "colour": 0xFF0000, "bbox": [481.596, 181.402, 508.334, 194.314]},
    (152, 6099): {"text": " 12.28", "colour": 0xFF0000, "bbox": [481.596, 488.918, 508.334, 501.830]},
    (158, 6240): {"text": "2021", "colour": 0x00FF00, "bbox": [203.167, 776.994, 219.393, 787.754]},
    (279, 8237): {"text": " 22.28", "colour": 0xFF0000, "bbox": [481.596, 671.945, 508.334, 684.857]},
    (401, 10148): {"text": " 32.20", "colour": 0xFF0000, "bbox": [511.641, 528.190, 538.222, 541.102]},
    (762, 16719): {"text": "2013", "colour": 0x00FF00, "bbox": [518.751, 363.534, 538.222, 376.446]},
    (762, 16721): {"text": "2019", "colour": 0x00FF00, "bbox": [518.751, 380.869, 538.222, 393.781]},
    (762, 16724): {"text": "2013", "colour": 0x00FF00, "bbox": [383.213, 380.869, 402.684, 393.781]},
    (762, 16735): {"text": "2004", "colour": 0x00FF00, "bbox": [480.899, 450.209, 500.370, 463.121]},
    (774, 16888): {"text": "2014", "colour": 0x00FF00, "bbox": [391.563, 507.095, 411.034, 520.007]},
    (776, 16958): {"text": "1990", "colour": 0x00FF00, "bbox": [518.751, 309.795, 538.222, 322.707]},
    (777, 17000): {"text": "1994", "colour": 0x00FF00, "bbox": [518.751, 581.140, 538.222, 594.052]},
    (794, 17258): {"text": "1953", "colour": 0x00FF00, "bbox": [506.796, 207.121, 526.267, 220.033]},
}

repair.CONFIG = {
    "open-logic-complete-fa-IR-screen.raw-before-link-repair.pdf": {
        "sha256": "FBD13FA9EE4F77B0626E175D1D911E3FEDE4B2E17B8E72648D57FC3E61E6B78B",
        "pages": 798,
        "links": 2986,
        "overflow": 141,
        "automatic": 128,
        "manual": MANUAL_MAIN,
    },
    "open-logic-closure-supplement-fa-IR-screen.raw-before-link-repair.pdf": {
        "sha256": "AF01DA08D66B46CAD03BC4145BB2C6C0694B1C4B6659B974A96CA6885EA8ED7F",
        "pages": 113,
        "links": 137,
        "overflow": 9,
        "automatic": 9,
        "manual": {},
    },
}


def apply_mapping(input_path: Path, output_path: Path, mapping: list[dict]) -> None:
    """Apply only approved x1 replacements, using each A4 page's true height."""
    reader = repair.PdfReader(input_path)
    by_xref = {item["xref"]: item for item in mapping}
    changed = set()
    for page_number, page in enumerate(reader.pages, 1):
        page_height = float(page.mediabox.height)
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
            expected_pdf = [old_top[0], page_height - old_top[3], old_top[2], page_height - old_top[1]]
            if not all(repair.nearly(actual, expected, 0.015) for actual, expected in zip(rect, expected_pdf)):
                raise RuntimeError(f"Raw /Rect mismatch for xref {reference.idnum}: {list(rect)}")
            rect[2] = repair.FloatObject(item["new_x1_pt"])
            changed.add(reference.idnum)
    if changed != set(by_xref):
        raise RuntimeError(f"Missing annotation xrefs: {set(by_xref) - changed}")
    writer = repair.PdfWriter()
    writer.pdf_header = reader.pdf_header
    writer.clone_document_from_reader(reader)
    with output_path.open("wb") as handle:
        writer.write(handle)


repair.apply_mapping = apply_mapping
repair.main()
