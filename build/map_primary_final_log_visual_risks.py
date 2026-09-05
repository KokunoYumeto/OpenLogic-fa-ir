#!/usr/bin/env python3
"""Map final TeX-log warnings to conservative physical-PDF page candidates."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from bisect import bisect_left
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def line_number(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


def warning_block(text: str, start: int) -> str:
    end = text.find("\n\n", start)
    if end < 0:
        end = min(len(text), start + 1200)
    return " ".join(text[start:end].replace("\r", "").split())


def logical_enter_events(text: str) -> list[dict]:
    # TeX wraps even marker tokens (for example, ``canoni\ncal`` and
    # ``foo\n.tex``), so bind the event at the first whitespace-tolerant .tex|.
    pattern = re.compile(
        r"OL-STANDALONE-ENTER\|(OLP-\d+)\|(.{1,500}?\.\s*t\s*e\s*x)\|",
        re.DOTALL,
    )
    rows = []
    for match in pattern.finditer(text):
        source = re.sub(r"\s+", "", match.group(2))
        tail = re.sub(r"\s+", "", text[match.end() : match.end() + 100])
        tail_match = re.match(r"([^|]+)\|([^|]+)\|(\d+)", tail)
        rows.append(
            {
                "position": match.start(),
                "unit_id": match.group(1),
                "source_path": source,
                "namespace": tail_match.group(1) if tail_match else None,
                "context": tail_match.group(2) if tail_match else None,
                "occurrence": int(tail_match.group(3)) if tail_match else None,
            }
        )
    return rows


def enclosing_unit(enters: list[dict], position: int) -> dict | None:
    candidates = [event for event in enters if event["position"] < position]
    return candidates[-1] if candidates else None


def build_label_map(reader: PdfReader) -> dict[str, list[int]]:
    labels: dict[str, list[int]] = {}
    for physical, label in enumerate(reader.page_labels, start=1):
        labels.setdefault(str(label), []).append(physical)
    return labels


def marker_context(markers: list[tuple[int, str]], marker_positions: list[int], position: int, label_map: dict[str, list[int]]) -> dict:
    index = bisect_left(marker_positions, position)
    previous = markers[index - 1] if index > 0 else None
    following = markers[index] if index < len(markers) else None

    def expand(marker: tuple[int, str] | None) -> dict | None:
        if marker is None:
            return None
        return {
            "log_position": marker[0],
            "printed_label": marker[1],
            "physical_page_candidates": label_map.get(marker[1], []),
        }

    conservative_pages: set[int] = set()
    for marker in (previous, following):
        if marker is not None:
            conservative_pages.update(label_map.get(marker[1], []))
    primary_page = None
    if following is not None:
        candidates = label_map.get(following[1], [])
        if len(candidates) == 1:
            primary_page = candidates[0]
    return {
        "previous_shipout": expand(previous),
        "following_shipout": expand(following),
        "primary_physical_page": primary_page,
        "conservative_physical_pages": sorted(conservative_pages),
        "mapping_rule": "The warning is mapped primarily to the next shipout marker; both adjacent shipout pages are retained for conservative high-resolution review.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", required=True, type=Path)
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    log = args.log.resolve()
    pdf = args.pdf.resolve()
    text = log.read_text(encoding="utf-8", errors="replace")
    reader = PdfReader(str(pdf))
    label_map = build_label_map(reader)
    enters = logical_enter_events(text)
    marker_matches = list(re.finditer(r"(?<![A-Za-z0-9])\[(\d+)\]", text))
    markers = [(match.start(), match.group(1)) for match in marker_matches]
    marker_positions = [position for position, _ in markers]

    overfull_pattern = re.compile(r"Overfull \\hbox \(([0-9.]+)pt too wide\)")
    underfull_pattern = re.compile(r"Underfull \\hbox")
    font_pattern = re.compile(r"LaTeX Font Warning:")
    proof_pattern = re.compile(r"Package prooftrees Warning:")
    missing_character_pattern = re.compile(r"Missing character:")

    overfull_all = list(overfull_pattern.finditer(text))
    underfull_all = list(underfull_pattern.finditer(text))
    font_all = list(font_pattern.finditer(text))
    proof_all = list(proof_pattern.finditer(text))
    missing_all = list(missing_character_pattern.finditer(text))

    large_overfull = []
    for ordinal, match in enumerate(overfull_all, start=1):
        width = float(match.group(1))
        if width < 10.0:
            continue
        position = match.start()
        unit = enclosing_unit(enters, position)
        large_overfull.append(
            {
                "id": f"OVERFULL-GE10-{len(large_overfull) + 1:02d}",
                "ordinal_among_all_overfull": ordinal,
                "log_line": line_number(text, position),
                "width_points": width,
                "message": warning_block(text, position),
                "unit": {key: value for key, value in (unit or {}).items() if key != "position"} if unit else None,
                "page_mapping": marker_context(markers, marker_positions, position, label_map),
            }
        )

    def mapped_warning_rows(matches: list[re.Match[str]], prefix: str) -> list[dict]:
        rows = []
        for ordinal, match in enumerate(matches, start=1):
            position = match.start()
            unit = enclosing_unit(enters, position)
            rows.append(
                {
                    "id": f"{prefix}-{ordinal:02d}",
                    "log_line": line_number(text, position),
                    "message": warning_block(text, position),
                    "unit": {key: value for key, value in (unit or {}).items() if key != "position"} if unit else None,
                    "page_mapping": marker_context(markers, marker_positions, position, label_map),
                }
            )
        return rows

    font_rows = mapped_warning_rows(font_all, "FONT")
    proof_rows = mapped_warning_rows(proof_all, "PROOFTREES")
    missing_rows = mapped_warning_rows(missing_all, "MISSING-CHARACTER")

    high_resolution_pages: set[int] = set()
    for row in large_overfull + font_rows + proof_rows + missing_rows:
        high_resolution_pages.update(row["page_mapping"]["conservative_physical_pages"])

    result = {
        "schema": "farsi-standard-primary-final-log-visual-risk-map-v1",
        "created_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "status": "MAP_COMPLETE_PENDING_HIGH_RESOLUTION_VISUAL_ADJUDICATION",
        "final_primary_log": {
            "path": log.as_posix(),
            "bytes": log.stat().st_size,
            "sha256": sha256(log),
        },
        "bound_pdf": {
            "path": pdf.as_posix(),
            "bytes": pdf.stat().st_size,
            "sha256": sha256(pdf),
            "physical_pages": len(reader.pages),
            "page_label_observation": "Physical page 1 and 2 both label as 1; from physical page 3 onward, the printed decimal label is physical page minus one.",
        },
        "counts": {
            "overfull_hbox_all": len(overfull_all),
            "underfull_hbox_all": len(underfull_all),
            "overfull_hbox_ge_10pt": len(large_overfull),
            "latex_font_warnings": len(font_all),
            "prooftrees_conflicting_justification_warnings": len(proof_all),
            "missing_character_warnings": len(missing_all),
        },
        "overfull_hbox_ge_10pt": large_overfull,
        "font_warnings": font_rows,
        "prooftrees_warnings": proof_rows,
        "missing_character_warnings": missing_rows,
        "high_resolution_review_pages_one_based": sorted(high_resolution_pages),
        "mapping_limit": "TeX warnings occur before the implicated box is necessarily shipped. The next shipout is the primary mapping and both adjacent shipouts are retained to avoid false precision.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["counts"], sort_keys=True))
    print("high_resolution_pages=" + ",".join(str(page) for page in result["high_resolution_review_pages_one_based"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
