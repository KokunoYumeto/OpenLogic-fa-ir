"""Fail-closed link-geometry QA for the accepted Standard-Farsi full reader.

This validator never launches TeX and never mutates a PDF.  It recomputes the
drawing-level trace produced by ``diagnose_standalone_link_geometry.py``, binds
the accepted deterministic primary/replay bytes, checks every link annotation
and destination, and compares compact distribution fingerprints for the whole
1,201-page reader.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from copy import deepcopy
from pathlib import Path
from urllib.parse import urlsplit
import argparse
import json
import math
import re
import sys

import fitz

from check_production_link_geometry import CheckError, validate as validate_production_layer
from diagnose_standalone_link_geometry import audit
from probe_postbuild_common import (
    PYMUPDF_VERSION,
    ROOT,
    ValidationError,
    as_list,
    as_mapping,
    clear_snapshot_cache,
    expect_validation_error,
    file_size,
    load_json,
    relative_repo_path,
    require,
    same_path,
    self_test_common_primitives,
    sha256_bytes,
    sha256_file,
    write_json,
)


EXPECTED_INPUT = ROOT / (
    "tmp/pdfs/standalone/20260905T121245261Z-975f45c04bc2418e95d68965829b251c/"
    "primary/open-logic-standalone-fa-IR.pdf"
)
EXPECTED_TRACE = EXPECTED_INPUT.parent / "FULL_READER_LINK_GEOMETRY_TRACE.json"
EXPECTED_RECEIPT = EXPECTED_INPUT.parent.parent / "BUILD_RECEIPT.json"
EXPECTED_REPLAY = EXPECTED_INPUT.parent.parent / "replay/open-logic-standalone-fa-IR.pdf"
DIAGNOSTIC = ROOT / "build/diagnose_standalone_link_geometry.py"
PRODUCTION_LAYER = ROOT / "source/locale/fa-IR/standalone/link-geometry.tex"
PRODUCTION_STATIC_QA = ROOT / "evidence/LINK_GEOMETRY_PRODUCTION_STATIC_QA.json"

EXPECTED_PDF = {
    "bytes": 9_285_597,
    "sha256": "6b7a24d6b39474fd76ea08496c97783bcf5a4c46f10d8f500ed0414a5dd38a08",
}
EXPECTED_RECEIPT_IDENTITY = {
    "bytes": 1_240_927,
    "sha256": "4c2dac46ca76c029a49841db1336fd036da7c35aa154366a46d52597da046d0e",
}
BUILD_DISPOSITION = {
    "status": "DETERMINISTIC_BUILD_ACCEPTED_PENDING_VISUAL_AND_PUBLICATION_QA",
    "reason": "This guarded build incorporates the source-safe OLP-0298 reflow and passed byte-identical primary/replay acceptance.",
    "required_next_action": "Complete whole-reader rendered-page visual QA and publication-byte verification.",
}

FULL_WIDTH_PAGE_RATIO = 0.75
COORDINATE_TOLERANCE = 0.001
WIDTH_BUCKET_EDGES = (12.0, 24.0, 48.0, 96.0, 192.0, 384.0, 459.0)
HEIGHT_BUCKET_EDGES = (10.0, 12.0, 14.0, 16.0, 18.0, 24.0, 36.0)
QUANTILES = (0.0, 0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99, 1.0)

EXPECTED_DISTRIBUTION = {
    "pages": 1201,
    "links": 3233,
    "page_geometry": [
        {"rect": [0.0, 0.0, 612.0, 792.0], "rotation": 0, "pages": 1201},
    ],
    "source_pages": {
        "with_links": 553,
        "first_with_links": 1,
        "last_with_links": 1201,
        "maximum_links_on_one_page": 34,
        "pages_with_maximum": [9, 209, 386],
    },
    "page_link_count_histogram": {
        "0": 648,
        "1": 139,
        "2": 92,
        "3": 59,
        "4": 52,
        "5": 34,
        "6": 22,
        "7": 28,
        "8": 17,
        "9": 23,
        "10": 14,
        "11": 6,
        "12": 7,
        "13": 7,
        "14": 11,
        "15": 5,
        "17": 1,
        "18": 1,
        "19": 2,
        "20": 2,
        "22": 1,
        "23": 1,
        "26": 1,
        "28": 1,
        "29": 1,
        "30": 2,
        "31": 9,
        "32": 4,
        "33": 8,
        "34": 3,
    },
    "page_link_sequence_sha256": "5275185fe73691ac2feccb6bbcd6d3cfc7323dea3d945a02c476a1f1a80c4298",
    "link_kinds": {"external_uri": 76, "internal_named": 3157},
    "target_classes": {"citation": 377, "external_uri": 76, "internal_reference": 2780},
    "annotation_actions": {"/GoTo": 3157, "/URI": 76},
    "annotation_colours": {"0/1/0": 377, "0/1/1": 76, "1/0/0": 2780},
    "anchor_profile": {
        "citation": {"1/1/1": 377},
        "external_uri": {"0/0/1": 29, "1/0/1": 3, "1/1/1": 41, "1/1/4": 1, "1/1/7": 2},
        "internal_reference": {
            "1/1/1": 2642,
            "1/1/10": 1,
            "1/1/2": 1,
            "1/1/4": 124,
            "1/1/5": 3,
            "1/1/7": 9,
        },
    },
    "width_buckets_points": {
        "citation": {"le_12": 2, "le_24": 47, "le_48": 273, "le_96": 48, "le_192": 7},
        "external_uri": {"le_12": 1, "le_48": 4, "le_96": 11, "le_192": 20, "le_384": 32, "le_459": 8},
        "internal_reference": {
            "le_12": 64,
            "le_24": 237,
            "le_48": 703,
            "le_96": 1270,
            "le_192": 477,
            "le_384": 29,
        },
    },
    "height_buckets_points": {
        "citation": {"le_10": 229, "le_12": 92, "le_14": 53, "le_16": 1, "le_18": 2},
        "external_uri": {"le_10": 2, "le_12": 7, "le_14": 19, "le_16": 24, "le_18": 24},
        "internal_reference": {"le_10": 225, "le_12": 866, "le_14": 467, "le_16": 1057, "le_18": 138, "le_24": 27},
    },
    "targets": {
        "unique_all": 1909,
        "unique_internal": 1866,
        "unique_external": 43,
        "kind_target_inventory_sha256": "be23ddd0213ee611634146bd6ee841d96e9223c1129d82db6aa141285028ea61",
    },
    "destinations": {
        "internal_links": 3157,
        "unique_named_destinations": 1866,
        "target_pages": 880,
        "first_target_page_one_based": 2,
        "last_target_page_one_based": 1201,
        "resolved_inverted_y_coordinate": 3157,
    },
    "geometry_extrema_points": {
        "minimum_width": 6.698,
        "maximum_width": 453.89801,
        "minimum_height": 7.008,
        "maximum_height": 21.349,
    },
}


def record(path: Path) -> dict[str, object]:
    return {
        "path": relative_repo_path(path),
        "bytes": file_size(path),
        "sha256": sha256_file(path),
    }


def finite_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def rounded_box(value: object) -> list[float]:
    return [round(float(item), 5) for item in value]


def contains_rect(page_rect: list[float], rect: list[float]) -> bool:
    return (
        rect[0] >= page_rect[0] - COORDINATE_TOLERANCE
        and rect[1] >= page_rect[1] - COORDINATE_TOLERANCE
        and rect[2] <= page_rect[2] + COORDINATE_TOLERANCE
        and rect[3] <= page_rect[3] + COORDINATE_TOLERANCE
    )


def contains_point(page_rect: list[float], point: list[float]) -> bool:
    return (
        page_rect[0] - COORDINATE_TOLERANCE <= point[0] <= page_rect[2] + COORDINATE_TOLERANCE
        and page_rect[1] - COORDINATE_TOLERANCE <= point[1] <= page_rect[3] + COORDINATE_TOLERANCE
    )


def target_class(row: dict[str, object]) -> str:
    if row["kind"] == fitz.LINK_URI:
        return "external_uri"
    return "citation" if str(row["nameddest"]).startswith("cite.") else "internal_reference"


def colour_key(value: object) -> str:
    colour = as_list(value, "annotation colour")
    require(len(colour) == 3, "annotation colour must have three channels")
    require(all(finite_number(item) and float(item) in (0.0, 1.0) for item in colour), "unexpected annotation colour")
    return "/".join(str(int(float(item))) for item in colour)


def bucket(value: float, edges: tuple[float, ...]) -> str:
    for edge in edges:
        if value <= edge:
            return f"le_{edge:g}"
    return f"gt_{edges[-1]:g}"


def quantile_profile(values: list[float]) -> dict[str, float]:
    ordered = sorted(values)
    require(bool(ordered), "quantile profile requires observations")
    return {
        f"{quantile:g}": round(ordered[round((len(ordered) - 1) * quantile)], 5)
        for quantile in QUANTILES
    }


def collect_model(pdf_path: Path, trace: dict[str, object]) -> dict[str, object]:
    document = fitz.open(pdf_path)
    try:
        pages = [
            {
                "page_one_based": page.number + 1,
                "rect": rounded_box(page.rect),
                "rotation": page.rotation,
            }
            for page in document
        ]
        trace_links = as_list(trace.get("links"), "trace links")
        traced_by_xref: dict[int, dict[str, object]] = {}
        for index, value in enumerate(trace_links):
            traced = dict(as_mapping(value, f"trace link {index}"))
            xref = traced.get("xref")
            require(isinstance(xref, int) and not isinstance(xref, bool) and xref > 0, "invalid trace xref")
            require(xref not in traced_by_xref, f"duplicate trace xref: {xref}")
            traced_by_xref[xref] = traced

        links: list[dict[str, object]] = []
        raw_xrefs: set[int] = set()
        low_level_link_xrefs: list[dict[str, int]] = []
        for page in document:
            for annotation_xref, annotation_type, _annotation_id in page.annot_xrefs():
                if annotation_type == fitz.PDF_ANNOT_LINK:
                    low_level_link_xrefs.append(
                        {"source_page_one_based": page.number + 1, "xref": annotation_xref}
                    )
            for raw in page.get_links():
                xref = raw.get("xref")
                require(isinstance(xref, int) and not isinstance(xref, bool) and xref > 0, "invalid raw link xref")
                require(xref not in raw_xrefs, f"duplicate raw link xref: {xref}")
                raw_xrefs.add(xref)
                require(xref in traced_by_xref, f"raw link xref absent from drawing trace: {xref}")
                traced = traced_by_xref[xref]
                kind = raw.get("kind")
                named = raw.get("nameddest")
                uri = raw.get("uri")
                destination_page = raw.get("page") if kind in (fitz.LINK_GOTO, fitz.LINK_NAMED) else None
                destination_point = raw.get("to") if kind in (fitz.LINK_GOTO, fitz.LINK_NAMED) else None
                resolved = None
                if kind == fitz.LINK_NAMED and isinstance(named, str):
                    resolved = list(document.resolve_link("#" + named))
                links.append(
                    {
                        "source_page_one_based": page.number + 1,
                        "xref": xref,
                        "trace_rect": list(traced.get("rect", [])),
                        "raw_rect": rounded_box(raw["from"]),
                        "trace_width": traced.get("width"),
                        "trace_target": traced.get("target"),
                        "trace_colour": traced.get("color"),
                        "left_count": len(as_list(traced.get("left"), "left glyph anchors")),
                        "right_count": len(as_list(traced.get("right"), "right glyph anchors")),
                        "enclosed_count": len(as_list(traced.get("enclosed"), "enclosed glyph groups")),
                        "band_count": len(as_list(traced.get("band"), "same-band glyph groups")),
                        "trace_outside": traced.get("outside"),
                        "kind": kind,
                        "nameddest": named,
                        "uri": uri,
                        "destination_page_zero_based": destination_page,
                        "destination_point": (
                            [float(destination_point.x), float(destination_point.y)]
                            if destination_point is not None
                            else None
                        ),
                        "resolved_destination": resolved,
                        "annotation_subtype": document.xref_get_key(xref, "Subtype")[1],
                        "annotation_action": document.xref_get_key(xref, "A/S")[1],
                    }
                )
        require(raw_xrefs == set(traced_by_xref), "drawing trace/raw annotation xref inventories differ")
        return {
            "pages": pages,
            "links": links,
            "low_level_link_xrefs": low_level_link_xrefs,
        }
    finally:
        document.close()


def validate_geometry_safety(model: dict[str, object]) -> dict[str, object]:
    pages = as_list(model.get("pages"), "model pages")
    links = as_list(model.get("links"), "model links")
    low_level_values = as_list(model.get("low_level_link_xrefs"), "low-level link annotations")
    require(bool(pages), "PDF has no pages")
    page_rects: list[list[float]] = []
    page_geometry = Counter()
    for index, value in enumerate(pages, start=1):
        page = as_mapping(value, f"page {index}")
        require(page.get("page_one_based") == index, "page sequence changed")
        rect = as_list(page.get("rect"), "page rectangle")
        require(len(rect) == 4 and all(finite_number(item) for item in rect), "invalid page rectangle")
        page_rect = [float(item) for item in rect]
        require(page_rect[2] > page_rect[0] and page_rect[3] > page_rect[1], "non-positive page geometry")
        rotation = page.get("rotation")
        require(isinstance(rotation, int) and not isinstance(rotation, bool), "invalid page rotation")
        page_rects.append(page_rect)
        page_geometry[(tuple(page_rect), rotation)] += 1

    xrefs: set[int] = set()
    by_page = Counter()
    kinds = Counter()
    classes = Counter()
    actions = Counter()
    colours = Counter()
    anchors: dict[str, Counter[str]] = defaultdict(Counter)
    widths: dict[str, list[float]] = defaultdict(list)
    heights: dict[str, list[float]] = defaultdict(list)
    width_buckets: dict[str, Counter[str]] = defaultdict(Counter)
    height_buckets: dict[str, Counter[str]] = defaultdict(Counter)
    target_counts: Counter[tuple[str, str]] = Counter()
    destination_pages = Counter()
    inverted_resolution_count = 0
    both_edges = 0
    width_ratios: list[float] = []

    for index, value in enumerate(links):
        row = dict(as_mapping(value, f"link {index}"))
        source_page = row.get("source_page_one_based")
        require(isinstance(source_page, int) and not isinstance(source_page, bool), "invalid source page")
        require(1 <= source_page <= len(pages), "link source page is outside the PDF")
        page_rect = page_rects[source_page - 1]
        xref = row.get("xref")
        require(isinstance(xref, int) and not isinstance(xref, bool) and xref > 0, "invalid link xref")
        require(xref not in xrefs, f"duplicate link xref: {xref}")
        xrefs.add(xref)

        trace_rect = as_list(row.get("trace_rect"), "trace rectangle")
        raw_rect = as_list(row.get("raw_rect"), "raw rectangle")
        require(len(trace_rect) == len(raw_rect) == 4, "link rectangle must have four coordinates")
        require(all(finite_number(item) for item in trace_rect + raw_rect), "non-finite link rectangle")
        trace_rect = [float(item) for item in trace_rect]
        raw_rect = [float(item) for item in raw_rect]
        require(trace_rect == raw_rect, "drawing trace/raw link rectangle divergence")
        width = raw_rect[2] - raw_rect[0]
        height = raw_rect[3] - raw_rect[1]
        require(width > 0 and height > 0, "zero-area or inverted link rectangle")
        # The diagnostic rounds each coordinate and the independently measured
        # width to five decimals, so one final decimal of subtraction drift is
        # possible when the rounded rectangle is reconstructed.
        require(abs(float(row.get("trace_width")) - round(width, 5)) <= 2e-5, "trace width disagrees with rectangle")
        require(contains_rect(page_rect, raw_rect), "link rectangle escapes its source page")
        require(row.get("trace_outside") is False, "drawing trace marks link rectangle outside page")
        page_width = page_rect[2] - page_rect[0]
        require(width < FULL_WIDTH_PAGE_RATIO * page_width, "full-width link rectangle rejected")
        width_ratios.append(width / page_width)

        enclosed_count = row.get("enclosed_count")
        band_count = row.get("band_count")
        left_count = row.get("left_count")
        right_count = row.get("right_count")
        require(all(isinstance(item, int) and not isinstance(item, bool) and item >= 0 for item in (enclosed_count, band_count, left_count, right_count)), "invalid glyph-anchor count")
        require(enclosed_count >= 1, "link rectangle encloses no matching drawn glyph group")
        require(band_count >= enclosed_count, "enclosed glyph count exceeds same-band count")

        require(row.get("annotation_subtype") == "/Link", "annotation subtype is not /Link")
        kind = row.get("kind")
        require(kind in (fitz.LINK_URI, fitz.LINK_NAMED), f"unexpected link kind: {kind!r}")
        klass = target_class(row)
        expected_colour = {
            "citation": "0/1/0",
            "external_uri": "0/1/1",
            "internal_reference": "1/0/0",
        }[klass]
        observed_colour = colour_key(row.get("trace_colour"))
        require(observed_colour == expected_colour, "link target class/annotation colour mismatch")

        if kind == fitz.LINK_NAMED:
            require(row.get("annotation_action") == "/GoTo", "internal link action is not /GoTo")
            named = row.get("nameddest")
            require(isinstance(named, str) and named, "internal link has no named destination")
            require(row.get("uri") in (None, ""), "internal link unexpectedly has a URI")
            require(row.get("trace_target") == named, "trace/raw named destination mismatch")
            require(left_count >= 1 and right_count >= 1, "internal/citation link is not anchored at both drawn edges")
            destination_page = row.get("destination_page_zero_based")
            require(isinstance(destination_page, int) and not isinstance(destination_page, bool), "invalid destination page")
            require(0 <= destination_page < len(pages), "destination page is outside the PDF")
            point = as_list(row.get("destination_point"), "destination point")
            require(len(point) == 2 and all(finite_number(item) for item in point), "invalid destination point")
            point = [float(item) for item in point]
            target_page_rect = page_rects[destination_page]
            require(contains_point(target_page_rect, point), "destination point is outside its target page")
            resolved = as_list(row.get("resolved_destination"), "resolved named destination")
            require(len(resolved) == 3 and all(finite_number(item) for item in resolved), "named destination did not resolve")
            require(int(resolved[0]) == destination_page and float(resolved[0]) == destination_page, "resolved destination page mismatch")
            require(abs(float(resolved[1]) - point[0]) <= COORDINATE_TOLERANCE, "resolved destination x-coordinate mismatch")
            inverted_y = target_page_rect[3] - float(resolved[2])
            require(abs(inverted_y - point[1]) <= COORDINATE_TOLERANCE, "resolved destination y-coordinate mismatch")
            inverted_resolution_count += 1
            destination_pages[destination_page + 1] += 1
            target_counts[("internal_named", named)] += 1
        else:
            require(row.get("annotation_action") == "/URI", "external link action is not /URI")
            require(row.get("nameddest") in (None, ""), "external link unexpectedly has a named destination")
            require(row.get("destination_page_zero_based") is None, "external URI unexpectedly has a PDF destination page")
            require(row.get("destination_point") is None, "external URI unexpectedly has a PDF destination point")
            require(row.get("resolved_destination") is None, "external URI unexpectedly has a resolved PDF destination")
            uri = row.get("uri")
            require(isinstance(uri, str) and uri, "external link has no URI")
            require(row.get("trace_target") == uri, "trace/raw URI mismatch")
            require(not re.search(r"[\x00-\x20\x7f]", uri), "external URI contains whitespace/control characters")
            parsed = urlsplit(uri)
            require(parsed.scheme.lower() in {"http", "https"} and bool(parsed.netloc), "external URI is malformed or uses an unexpected scheme")
            target_counts[("external_uri", uri)] += 1

        if left_count >= 1 and right_count >= 1:
            both_edges += 1
        by_page[source_page] += 1
        kinds["external_uri" if kind == fitz.LINK_URI else "internal_named"] += 1
        classes[klass] += 1
        actions[str(row.get("annotation_action"))] += 1
        colours[observed_colour] += 1
        anchors[klass][f"{left_count}/{right_count}/{enclosed_count}"] += 1
        widths[klass].append(width)
        heights[klass].append(height)
        width_buckets[klass][bucket(width, WIDTH_BUCKET_EDGES)] += 1
        height_buckets[klass][bucket(height, HEIGHT_BUCKET_EDGES)] += 1

    require(len(xrefs) == len(links), "link xref inventory is not unique")
    low_level_pairs: list[tuple[int, int]] = []
    for index, value in enumerate(low_level_values):
        row = as_mapping(value, f"low-level link annotation {index}")
        page = row.get("source_page_one_based")
        xref = row.get("xref")
        require(isinstance(page, int) and not isinstance(page, bool) and 1 <= page <= len(pages), "invalid low-level link source page")
        require(isinstance(xref, int) and not isinstance(xref, bool) and xref > 0, "invalid low-level link xref")
        low_level_pairs.append((page, xref))
    raw_pairs = [
        (int(as_mapping(value, "link")["source_page_one_based"]), int(as_mapping(value, "link")["xref"]))
        for value in links
    ]
    require(len(low_level_pairs) == len(set(low_level_pairs)), "duplicate low-level /Link annotation xref")
    require(set(low_level_pairs) == set(raw_pairs), "Page.get_links omitted or invented a low-level /Link annotation")
    source_counts = [by_page.get(page, 0) for page in range(1, len(pages) + 1)]
    pages_with_links = [page for page, count in enumerate(source_counts, start=1) if count]
    maximum_links = max(source_counts, default=0)
    target_payload = json.dumps(
        sorted((kind, target, count) for (kind, target), count in target_counts.items()),
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    page_payload = json.dumps(source_counts, separators=(",", ":")).encode("ascii")
    internal_targets = {target for (kind, target) in target_counts if kind == "internal_named"}
    external_targets = {target for (kind, target) in target_counts if kind == "external_uri"}
    all_widths = [value for values in widths.values() for value in values]
    all_heights = [value for values in heights.values() for value in values]

    distribution = {
        "pages": len(pages),
        "links": len(links),
        "page_geometry": [
            {"rect": list(rect), "rotation": rotation, "pages": count}
            for (rect, rotation), count in sorted(page_geometry.items())
        ],
        "source_pages": {
            "with_links": len(pages_with_links),
            "first_with_links": pages_with_links[0] if pages_with_links else None,
            "last_with_links": pages_with_links[-1] if pages_with_links else None,
            "maximum_links_on_one_page": maximum_links,
            "pages_with_maximum": [page for page, count in enumerate(source_counts, start=1) if count == maximum_links],
        },
        "page_link_count_histogram": {str(count): pages for count, pages in sorted(Counter(source_counts).items())},
        "page_link_sequence_sha256": sha256_bytes(page_payload),
        "link_kinds": dict(sorted(kinds.items())),
        "target_classes": dict(sorted(classes.items())),
        "annotation_actions": dict(sorted(actions.items())),
        "annotation_colours": dict(sorted(colours.items())),
        "anchor_profile": {klass: dict(sorted(counts.items())) for klass, counts in sorted(anchors.items())},
        "width_buckets_points": {klass: dict(sorted(counts.items())) for klass, counts in sorted(width_buckets.items())},
        "height_buckets_points": {klass: dict(sorted(counts.items())) for klass, counts in sorted(height_buckets.items())},
        "targets": {
            "unique_all": len(target_counts),
            "unique_internal": len(internal_targets),
            "unique_external": len(external_targets),
            "kind_target_inventory_sha256": sha256_bytes(target_payload),
        },
        "destinations": {
            "internal_links": sum(destination_pages.values()),
            "unique_named_destinations": len(internal_targets),
            "target_pages": len(destination_pages),
            "first_target_page_one_based": min(destination_pages, default=None),
            "last_target_page_one_based": max(destination_pages, default=None),
            "resolved_inverted_y_coordinate": inverted_resolution_count,
        },
        "geometry_extrema_points": {
            "minimum_width": round(min(all_widths), 5),
            "maximum_width": round(max(all_widths), 5),
            "minimum_height": round(min(all_heights), 5),
            "maximum_height": round(max(all_heights), 5),
        },
    }
    safety = {
        "all_pages_inspected": len(pages),
        "all_annotations_inspected": len(links),
        "unique_link_xrefs": len(xrefs),
        "low_level_pdf_link_annotations": len(low_level_pairs),
        "outside_page_rectangles": 0,
        "non_finite_rectangles": 0,
        "zero_or_negative_area_rectangles": 0,
        "full_width_rectangles": 0,
        "full_width_rejection_ratio": FULL_WIDTH_PAGE_RATIO,
        "full_width_threshold_points_for_612_point_page": 612.0 * FULL_WIDTH_PAGE_RATIO,
        "maximum_observed_width_to_page_ratio": round(max(width_ratios), 8),
        "zero_enclosed_glyph_groups": 0,
        "bad_internal_destinations": 0,
        "malformed_external_uris": 0,
        "unexpected_annotation_kinds_or_actions": 0,
        "trace_raw_geometry_or_target_divergences": 0,
        "both_drawn_edges_anchored": both_edges,
        "both_drawn_edges_anchored_ratio": round(both_edges / len(links), 8),
    }
    quantiles = {
        "width_points": {klass: quantile_profile(values) for klass, values in sorted(widths.items())},
        "height_points": {klass: quantile_profile(values) for klass, values in sorted(heights.items())},
    }
    return {"distribution": distribution, "safety": safety, "quantiles": quantiles}


def validate_expected_distribution(distribution: object) -> None:
    observed = as_mapping(distribution, "full-reader link distribution")
    require(dict(observed) == EXPECTED_DISTRIBUTION, "accepted full-reader link distribution changed")


def validate_receipt_and_replay(input_path: Path) -> dict[str, object]:
    require(same_path(input_path, EXPECTED_INPUT), "input is not the accepted Standard-Farsi primary PDF")
    require(record(input_path) == {"path": relative_repo_path(input_path), **EXPECTED_PDF}, "accepted primary PDF identity changed")
    require(record(EXPECTED_RECEIPT) == {"path": relative_repo_path(EXPECTED_RECEIPT), **EXPECTED_RECEIPT_IDENTITY}, "accepted build receipt identity changed")
    receipt = as_mapping(load_json(EXPECTED_RECEIPT), "accepted Full build receipt")
    require(receipt.get("schema") == "interlanguage-standalone-tex-build-v1", "build receipt schema changed")
    require(receipt.get("mode") == "Full", "accepted build is not Full mode")
    require(receipt.get("status") == "BUILD_AND_REPLAY_PASS_NOT_PUBLICATION_QA", "accepted build status changed")
    require(receipt.get("accepted_build") is True, "build receipt is not accepted")
    mutex = as_mapping(receipt.get("mutex"), "build mutex receipt")
    require(mutex.get("name") == r"Global\InterlanguageTeXSlotV1", "build mutex name changed")
    require(mutex.get("acquired") is True and mutex.get("released_after_confirmed_tree_exit") is True, "build mutex lifecycle is incomplete")
    builds = as_list(receipt.get("builds"), "deterministic builds")
    require(len(builds) == 2, "Full build must contain primary and replay")
    expected_paths = {"primary": EXPECTED_INPUT, "replay": EXPECTED_REPLAY}
    for value in builds:
        build = as_mapping(value, "build")
        name = build.get("name")
        require(name in expected_paths, "unexpected deterministic build name")
        require(build.get("accepted") is True, f"deterministic build is not accepted: {name}")
        pdf = as_mapping(build.get("pdf"), f"{name} PDF receipt")
        expected_path = expected_paths[str(name)]
        require(same_path(str(pdf.get("path")), expected_path), f"{name} PDF path changed")
        require(pdf.get("bytes") == EXPECTED_PDF["bytes"], f"{name} PDF byte count changed")
        require(str(pdf.get("sha256", "")).lower() == EXPECTED_PDF["sha256"], f"{name} PDF hash changed")
    require(record(EXPECTED_REPLAY) == {"path": relative_repo_path(EXPECTED_REPLAY), **EXPECTED_PDF}, "replay PDF bytes differ from accepted primary")
    return {
        "receipt": record(EXPECTED_RECEIPT),
        "accepted_build": True,
        "primary": record(EXPECTED_INPUT),
        "replay": record(EXPECTED_REPLAY),
        "primary_equals_replay": True,
        "mutex_acquired_and_released_after_confirmed_tree_exit": True,
    }


def synthetic_model() -> dict[str, object]:
    pages = [
        {"page_one_based": 1, "rect": [0.0, 0.0, 100.0, 100.0], "rotation": 0},
        {"page_one_based": 2, "rect": [0.0, 0.0, 100.0, 100.0], "rotation": 0},
    ]
    common = {
        "source_page_one_based": 1,
        "trace_rect": [10.0, 10.0, 30.0, 20.0],
        "raw_rect": [10.0, 10.0, 30.0, 20.0],
        "trace_width": 20.0,
        "left_count": 1,
        "right_count": 1,
        "enclosed_count": 1,
        "band_count": 1,
        "trace_outside": False,
        "kind": fitz.LINK_NAMED,
        "uri": None,
        "destination_page_zero_based": 1,
        "destination_point": [20.0, 80.0],
        "resolved_destination": [1, 20.0, 20.0],
        "annotation_subtype": "/Link",
        "annotation_action": "/GoTo",
    }
    internal = {**common, "xref": 10, "trace_target": "section*.1", "trace_colour": [1.0, 0.0, 0.0], "nameddest": "section*.1"}
    citation = {**common, "xref": 11, "trace_rect": [35.0, 10.0, 55.0, 20.0], "raw_rect": [35.0, 10.0, 55.0, 20.0], "trace_target": "cite.Sample", "trace_colour": [0.0, 1.0, 0.0], "nameddest": "cite.Sample"}
    uri = {
        **common,
        "source_page_one_based": 2,
        "xref": 12,
        "trace_rect": [10.0, 30.0, 40.0, 40.0],
        "raw_rect": [10.0, 30.0, 40.0, 40.0],
        "trace_width": 30.0,
        "trace_target": "https://example.org/a",
        "trace_colour": [0.0, 1.0, 1.0],
        "kind": fitz.LINK_URI,
        "nameddest": None,
        "uri": "https://example.org/a",
        "destination_page_zero_based": None,
        "destination_point": None,
        "resolved_destination": None,
        "annotation_action": "/URI",
    }
    return {
        "pages": pages,
        "links": [internal, citation, uri],
        "low_level_link_xrefs": [
            {"source_page_one_based": 1, "xref": 10},
            {"source_page_one_based": 1, "xref": 11},
            {"source_page_one_based": 2, "xref": 12},
        ],
    }


def self_test() -> dict[str, object]:
    baseline = synthetic_model()
    validate_geometry_safety(baseline)
    controls: list[tuple[str, object]] = []

    def mutation(name: str, link_index: int, field: str, value: object) -> None:
        candidate = deepcopy(baseline)
        candidate["links"][link_index][field] = value
        controls.append((name, candidate))

    mutation("outside_page_rectangle", 0, "raw_rect", [-1.0, 10.0, 30.0, 20.0])
    mutation("zero_width_rectangle", 0, "raw_rect", [10.0, 10.0, 10.0, 20.0])
    mutation("zero_height_rectangle", 0, "raw_rect", [10.0, 10.0, 30.0, 10.0])
    mutation("full_width_rectangle", 0, "raw_rect", [10.0, 10.0, 85.0, 20.0])
    mutation("non_finite_rectangle", 0, "raw_rect", [10.0, 10.0, math.nan, 20.0])
    mutation("zero_enclosed_glyphs", 0, "enclosed_count", 0)
    mutation("internal_missing_left_anchor", 0, "left_count", 0)
    mutation("wrong_annotation_colour", 0, "trace_colour", [0.0, 1.0, 1.0])
    mutation("trace_target_mismatch", 0, "trace_target", "section*.other")
    mutation("unexpected_link_kind", 0, "kind", fitz.LINK_LAUNCH)
    mutation("destination_page_outside_pdf", 0, "destination_page_zero_based", 2)
    mutation("destination_point_outside_page", 0, "destination_point", [120.0, 80.0])
    mutation("resolved_destination_page_mismatch", 0, "resolved_destination", [0, 20.0, 20.0])
    mutation("resolved_destination_x_mismatch", 0, "resolved_destination", [1, 21.0, 20.0])
    mutation("resolved_destination_y_mismatch", 0, "resolved_destination", [1, 20.0, 21.0])
    mutation("missing_named_destination", 0, "nameddest", "")
    mutation("malformed_external_uri", 2, "uri", "javascript:alert(1)")
    mutation("whitespace_external_uri", 2, "uri", "https://example.org/bad path")
    mutation("wrong_annotation_subtype", 0, "annotation_subtype", "/Widget")
    mutation("wrong_annotation_action", 0, "annotation_action", "/URI")
    mutation("duplicate_xref", 1, "xref", 10)
    mutation("trace_width_mismatch", 0, "trace_width", 19.0)
    mutation("band_smaller_than_enclosed", 0, "band_count", 0)
    mutation("trace_reports_outside", 0, "trace_outside", True)

    omitted_low_level = deepcopy(baseline)
    omitted_low_level["low_level_link_xrefs"] = omitted_low_level["low_level_link_xrefs"][:-1]
    controls.append(("low_level_link_omission", omitted_low_level))

    # These mutations alter paired trace/raw fields so they reach the intended
    # area/full-width assertions instead of failing first on trace divergence.
    for name in ("outside_page_rectangle", "zero_width_rectangle", "zero_height_rectangle", "full_width_rectangle", "non_finite_rectangle"):
        candidate = next(value for label, value in controls if label == name)
        candidate["links"][0]["trace_rect"] = deepcopy(candidate["links"][0]["raw_rect"])
        if name not in {"non_finite_rectangle"}:
            rect = candidate["links"][0]["raw_rect"]
            candidate["links"][0]["trace_width"] = rect[2] - rect[0]
    for name in ("malformed_external_uri", "whitespace_external_uri"):
        candidate = next(value for label, value in controls if label == name)
        candidate["links"][2]["trace_target"] = candidate["links"][2]["uri"]

    for _name, candidate in controls:
        expect_validation_error(validate_geometry_safety, candidate)

    profile_controls = []
    for path, replacement in (
        (("links",), 3232),
        (("page_link_sequence_sha256",), "0" * 64),
        (("annotation_colours", "1/0/0"), 2779),
        (("width_buckets_points", "external_uri", "le_459"), 7),
        (("targets", "kind_target_inventory_sha256"), "f" * 64),
    ):
        candidate = deepcopy(EXPECTED_DISTRIBUTION)
        cursor = candidate
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = replacement
        profile_controls.append(candidate)
    validate_expected_distribution(deepcopy(EXPECTED_DISTRIBUTION))
    for candidate in profile_controls:
        expect_validation_error(validate_expected_distribution, candidate)

    common_controls = self_test_common_primitives()
    return {
        "schema": "farsi-full-reader-link-geometry-self-test-v1",
        "status": "PASS",
        "positive_synthetic_models": 1,
        "geometry_negative_controls": [name for name, _candidate in controls],
        "distribution_negative_controls": len(profile_controls),
        "common_primitive_negative_controls": common_controls,
        "total_negative_controls": len(controls) + len(profile_controls) + common_controls,
    }


def validate(input_path: Path, trace_path: Path) -> dict[str, object]:
    clear_snapshot_cache()
    input_path = input_path.resolve()
    trace_path = trace_path.resolve()
    require(same_path(trace_path, EXPECTED_TRACE), "trace is not the accepted full-reader trace path")
    build_binding = validate_receipt_and_replay(input_path)
    preserved_trace = as_mapping(load_json(trace_path), "preserved full-reader drawing trace")
    # JSON normalization matches the on-disk trace representation (notably
    # tuple colours become arrays) before exact semantic comparison.
    recomputed_trace = json.loads(json.dumps(audit(input_path), ensure_ascii=False))
    require(dict(preserved_trace) == recomputed_trace, "preserved full-reader drawing trace differs from recomputation")
    require(preserved_trace.get("input") == str(input_path), "trace input path changed")
    require(str(preserved_trace.get("sha256", "")).lower() == EXPECTED_PDF["sha256"], "trace PDF hash changed")
    require(preserved_trace.get("pages") == EXPECTED_DISTRIBUTION["pages"], "trace page count changed")

    model = collect_model(input_path, dict(preserved_trace))
    result = validate_geometry_safety(model)
    validate_expected_distribution(result["distribution"])

    require(fitz.__version__ == PYMUPDF_VERSION, "PyMuPDF version changed")
    production = validate_production_layer()
    require(production.get("status") == "PASS_STATIC_SELECTED_NATIVE_ATOMIC_READY_FOR_FULL_READER_BUILD", "production link layer is not the selected native-atomic mode")
    selection = as_mapping(production.get("selection_evidence"), "production selection evidence")
    require(selection.get("selected_probe_mode") == 1, "production link layer no longer selects probe mode 1")

    tests = self_test()
    return {
        "schema": "farsi-standalone-full-reader-link-geometry-qa-v1",
        "status": "PASS_ALL_3233_LINKS_ON_ALL_1201_PAGES_PENDING_VISUAL_AND_PUBLICATION_QA",
        "scope": "Accepted deterministic Standard-Farsi build; drawing-level link annotations and resolved destinations only.",
        "build_disposition": BUILD_DISPOSITION,
        "pdf": record(input_path),
        "deterministic_build_binding": build_binding,
        "drawing_trace": record(trace_path),
        "dependencies": [
            record(DIAGNOSTIC),
            record(Path(__file__)),
            record(PRODUCTION_LAYER),
            record(PRODUCTION_STATIC_QA),
        ],
        "runtime": {"pymupdf_version": fitz.__version__},
        "selected_intervention": {
            "probe_mode": 1,
            "name": "NATIVE-ATOMIC",
            "production_layer": record(PRODUCTION_LAYER),
            "static_selection_qa": record(PRODUCTION_STATIC_QA),
        },
        "annotation_audit": result,
        "mutation_self_test": tests,
        "checks": {
            "preserved_trace_equals_fresh_recomputation": True,
            "all_pdf_pages_enumerated": True,
            "all_link_annotation_xrefs_unique_and_enumerated": True,
            "low_level_pdf_link_inventory_equals_page_get_links_inventory": True,
            "all_rectangles_finite_positive_inside_page_and_below_full_width_threshold": True,
            "every_link_encloses_matching_drawn_glyphs": True,
            "all_internal_and_citation_links_anchor_both_drawn_edges": True,
            "all_internal_named_destinations_resolve_inside_target_pages": True,
            "all_external_uris_are_well_formed_http_or_https": True,
            "page_kind_colour_anchor_size_and_target_distributions_match_accepted_reader": True,
            "accepted_primary_and_replay_pdf_bytes_identical": True,
        },
        "limitations": [
            "Drawing-level annotation QA does not replace complete rendered-page visual inspection.",
            "External URI syntax is checked, but network reachability is outside this PDF-geometry gate.",
            "The incorporated OLP-0298 reflow still requires confirmation in complete rendered-page visual inspection.",
            "This receipt does not establish release packaging or anonymous public-byte identity.",
            "This receipt does not claim final full-reader visual QA or publication readiness.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path)
    parser.add_argument("--trace", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_test:
            require(args.input is None and args.trace is None and args.output is None, "--self-test cannot be combined with input/trace/output")
            result = self_test()
        else:
            require(args.input is not None, "--input is required")
            require(args.trace is not None, "--trace is required")
            require(args.output is not None, "--output is required and has no default")
            result = validate(args.input, args.trace)
            write_json(args.output, result)
        print(json.dumps(result, ensure_ascii=True, sort_keys=True))
    except (ValidationError, CheckError, AssertionError, KeyError, TypeError, ValueError) as exc:
        message = str(exc).encode("ascii", "backslashreplace").decode("ascii")
        print(f"FAIL: {message}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
