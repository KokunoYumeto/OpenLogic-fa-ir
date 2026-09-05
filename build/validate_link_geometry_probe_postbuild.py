"""Validate the guarded four-mode RTL link-geometry diagnostic.

The validator recomputes the drawing-level trace from the PDF, compares the
four intervention modes, and binds the minimal accepted intervention choice.
It never launches TeX and does not qualify the complete reader.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from copy import deepcopy
from pathlib import Path
import argparse
import json
import re
import sys

from diagnose_standalone_link_geometry import audit
from make_link_geometry_probe import generate
from probe_postbuild_common import (
    LOCALE,
    ROOT,
    ValidationError,
    as_list,
    as_mapping,
    base_evidence,
    clear_snapshot_cache,
    compact_text,
    expect_validation_error,
    file_size,
    load_json,
    load_pdf_text,
    read_file_bytes,
    relative_repo_path,
    require,
    require_recorder_inputs,
    self_test_common_primitives,
    sha256_bytes,
    sha256_file,
    validate_diagnostic_receipt,
    write_json,
)


JOB = "standalone-probe-bidi-links"
DRIVER = LOCALE / f"{JOB}.tex"
MANIFEST = ROOT / "evidence/LINK_GEOMETRY_PROBE_FIXTURE.json"
GENERATOR = ROOT / "build/make_link_geometry_probe.py"
FIXTURE = ROOT / "build/probes/link-geometry/link-geometry-fixture.tex"
INTERVENTION = ROOT / "build/probes/link-geometry/link-geometry-intervention.tex"
DIAGNOSTIC = ROOT / "build/diagnose_standalone_link_geometry.py"
TRACE_NAME = "LINK_GEOMETRY_TRACE.json"

EXPECTED_CASES = [
    {"mode": 0, "name": "BASELINE", "pages_one_based": [1, 2]},
    {"mode": 1, "name": "NATIVE-ATOMIC", "pages_one_based": [3, 4]},
    {"mode": 2, "name": "ISOLATED-ATOMIC", "pages_one_based": [5, 6]},
    {"mode": 3, "name": "ISOLATED-ATOMIC-RAW-URL-LTR", "pages_one_based": [7, 8]},
]
EXPECTED_PAGE_STATS = {
    1: (35, 0, 0, 0, 52.12100, {"1/0/0": 35}),
    2: (32, 4, 4, 1, 468.24400, {"0/1/0": 21, "0/1/1": 11}),
    3: (35, 0, 0, 0, 52.12100, {"1/0/0": 35}),
    4: (31, 0, 0, 1, 261.02097, {"0/1/0": 20, "0/1/1": 11}),
    5: (35, 0, 0, 0, 52.12100, {"1/0/0": 35}),
    6: (31, 0, 0, 1, 261.02097, {"0/1/0": 20, "0/1/1": 11}),
    7: (35, 0, 0, 0, 52.12100, {"1/0/0": 35}),
    8: (31, 0, 0, 2, 261.02097, {"0/1/0": 20, "0/1/1": 11}),
    9: (0, 0, 0, 0, 0.0, {}),
    10: (0, 0, 0, 0, 0.0, {}),
}
EXPECTED_TARGET_COUNTS = {
    "Hfootnote.1": 1,
    "Hfootnote.2": 1,
    "Hfootnote.3": 1,
    "Hfootnote.4": 1,
    "cite.Benacerraf1965": 16,
    "cite.Cantor1892": 16,
    "cite.Frege1884": 16,
    "cite.Hammack2013": 8,
    "cite.Magnus2021": 17,
    "cite.Solow2013": 8,
    "fixture.n10.19": 16,
    "fixture.n11.19": 24,
    "fixture.n12.26": 16,
    "fixture.n41.10": 16,
    "fixture.n41.13": 16,
    "fixture.n41.15": 16,
    "fixture.n41.17": 16,
    "fixture.n9.21": 16,
    "https://example.org/book-of-proof": 8,
    "https://example.org/explicit-ltr-title": 12,
    "https://example.org/logic/sets/relations/a-very-long-reference-name?edition=persian&mode=standalone": 16,
    "https://example.org/persian-title": 8,
}


def file_record(path: Path) -> dict[str, object]:
    return {
        "path": relative_repo_path(path),
        "bytes": file_size(path),
        "sha256": sha256_file(path),
    }


def require_record(record: object, path: Path, label: str) -> None:
    row = as_mapping(record, label)
    require(set(row) == {"path", "bytes", "sha256"}, f"{label} fields changed")
    require(dict(row) == file_record(path), f"{label} identity is stale")


def validate_fixture() -> dict[str, object]:
    manifest = as_mapping(load_json(MANIFEST), "link geometry fixture manifest")
    require(
        set(manifest)
        == {
            "schema", "status", "generator", "fixture", "intervention",
            "output", "case_order", "shared_pages_one_based", "tex_run",
            "not_full_reader",
        },
        "link geometry fixture manifest fields changed",
    )
    require(
        manifest.get("schema") == "farsi-standalone-link-geometry-probe-fixture-v1",
        "link geometry fixture schema changed",
    )
    require(
        manifest.get("status") == "GENERATED_DIAGNOSTIC_FIXTURE_NOT_FULL_READER",
        "link geometry fixture status changed",
    )
    require_record(manifest.get("generator"), GENERATOR, "generator")
    require_record(manifest.get("fixture"), FIXTURE, "fixture")
    require_record(manifest.get("intervention"), INTERVENTION, "intervention")
    require_record(manifest.get("output"), DRIVER, "output")
    require(manifest.get("case_order") == EXPECTED_CASES, "probe case order changed")
    require(
        manifest.get("shared_pages_one_based") == {"destinations": 9, "bibliography": 10},
        "shared page roles changed",
    )
    require(manifest.get("tex_run") is False, "fixture manifest may not claim a TeX run")
    require(manifest.get("not_full_reader") is True, "fixture manifest scope changed")
    require(read_file_bytes(DRIVER) == generate(), "probe differs from deterministic generator")
    source = read_file_bytes(DRIVER).decode("utf-8")
    for mode in range(4):
        require(
            source.count(rf"\OLLinkGeometryInstall{{{mode}}}") == 1,
            f"probe mode {mode} installation is missing or duplicated",
        )
    for case in EXPECTED_CASES:
        marker = rf"\typeout{{OL-LINK-GEOMETRY-CASE={case['name']}}}"
        require(source.count(marker) == 1, f"probe case marker changed: {case['name']}")
    return dict(manifest)


def validate_log_markers(text: str) -> dict[str, object]:
    modes = [
        int(match.group(1))
        for line in text.splitlines()
        if (match := re.fullmatch(r"OL-LINK-GEOMETRY-PROBE-MODE=([0-3])", line))
    ]
    cases = [
        match.group(1)
        for line in text.splitlines()
        if (match := re.fullmatch(r"OL-LINK-GEOMETRY-CASE=([A-Z0-9-]+)", line))
    ]
    # The intervention file first registers mode zero when it is loaded, then
    # the four generated groups install modes zero through three.
    require(modes == [0, 0, 1, 2, 3], f"link probe mode markers changed: {modes!r}")
    expected_cases = [case["name"] for case in EXPECTED_CASES]
    require(cases == expected_cases, f"link probe case markers changed: {cases!r}")
    return {"mode_markers": modes, "case_markers": cases}


def colour_key(value: object) -> str:
    colour = as_list(value, "link colour")
    require(len(colour) == 3, "link colour must have three channels")
    require(all(channel in (0, 1, 0.0, 1.0) for channel in colour), "unexpected link colour")
    return "/".join(str(int(channel)) for channel in colour)


def page_stats(links: list[dict[str, object]]) -> tuple[int, int, int, int, float, dict[str, int]]:
    widths = [float(link["width"]) for link in links]
    return (
        len(links),
        sum(link.get("outside") is True for link in links),
        sum(abs(float(link["width"]) - 468.244) < 0.02 for link in links),
        sum(not as_list(link.get("enclosed"), "enclosed glyph indices") for link in links),
        round(max(widths, default=0.0), 5),
        dict(sorted(Counter(colour_key(link.get("color")) for link in links).items())),
    )


def normalized_page_signature(links: list[dict[str, object]]) -> list[dict[str, object]]:
    fields = (
        "rect", "width", "color", "draw_colors", "target", "outside",
        "left", "right", "enclosed", "band",
    )
    result = []
    for link in links:
        row = {field: link[field] for field in fields}
        if re.fullmatch(r"Hfootnote\.\d+", str(row["target"])):
            row["target"] = "Hfootnote.N"
        result.append(row)
    return result


def validate_trace(trace: object) -> dict[str, object]:
    data = as_mapping(trace, "link geometry trace")
    require(set(data) == {"input", "sha256", "pages", "links", "glyph_groups", "counts"}, "trace fields changed")
    require(data.get("pages") == 10, "link geometry diagnostic must have exactly ten pages")
    links_raw = as_list(data.get("links"), "trace links")
    links: list[dict[str, object]] = []
    by_page: dict[int, list[dict[str, object]]] = defaultdict(list)
    for index, value in enumerate(links_raw):
        link = dict(as_mapping(value, f"trace link {index}"))
        require(isinstance(link.get("page"), int) and not isinstance(link.get("page"), bool), "invalid link page")
        require(1 <= link["page"] <= 10, "link page is outside the diagnostic")
        require(isinstance(link.get("width"), (int, float)) and not isinstance(link.get("width"), bool), "invalid link width")
        require(float(link["width"]) > 0, "non-positive link width")
        links.append(link)
        by_page[link["page"]].append(link)
    require(len(links) == 265, "total link count changed")
    observed_stats = {page: page_stats(by_page[page]) for page in range(1, 11)}
    require(observed_stats == EXPECTED_PAGE_STATS, f"per-page link geometry changed: {observed_stats!r}")
    target_counts = Counter(str(link.get("target")) for link in links)
    require(dict(target_counts) == EXPECTED_TARGET_COUNTS, f"link target inventory changed: {target_counts!r}")

    # Native atomic and explicit-direction isolation must be byte-for-byte
    # geometry-equivalent in this fixture after normalizing footnote numbers.
    require(
        normalized_page_signature(by_page[3]) == normalized_page_signature(by_page[5]),
        "mode 1 and mode 2 internal-reference geometry diverged",
    )
    require(
        normalized_page_signature(by_page[4]) == normalized_page_signature(by_page[6]),
        "mode 1 and mode 2 citation/external-link geometry diverged",
    )
    require(
        normalized_page_signature(by_page[5]) == normalized_page_signature(by_page[7]),
        "mode 3 unexpectedly changed internal-reference geometry",
    )
    require(
        normalized_page_signature(by_page[6]) != normalized_page_signature(by_page[8]),
        "raw-URL direction mode must retain its observed external-link difference",
    )
    require(
        observed_stats[2][1:3] == (4, 4)
        and observed_stats[4][1:3] == (0, 0),
        "mode 1 no longer removes baseline outside/full-width annotations",
    )
    require(
        observed_stats[8][3] > observed_stats[4][3],
        "raw-URL direction mode no longer has its observed extra empty-edge annotation",
    )
    return {
        "pages": 10,
        "links": len(links),
        "per_page": {
            str(page): {
                "links": values[0],
                "outside_page": values[1],
                "full_text_width": values[2],
                "zero_enclosed_glyph_groups": values[3],
                "maximum_width_points": values[4],
                "annotation_colours": values[5],
            }
            for page, values in observed_stats.items()
        },
        "target_counts": dict(sorted(target_counts.items())),
        "mode_1_equals_mode_2_geometry": True,
        "mode_1_removes_baseline_outside_and_full_width_annotations": True,
        "mode_3_adds_one_zero-enclosed_external-link_edge": True,
    }


def validate_pdf_roles(pages: list[str], lines_by_page: list[list[dict[str, object]]]) -> dict[str, object]:
    require(len(pages) == 10, "PDF page count changed")
    for page, mode in ((1, 0), (3, 1), (5, 2), (7, 3)):
        require(compact_text(f"MODE {mode}") in compact_text(pages[page - 1]), f"mode heading missing from page {page}")
        # PyMuPDF can omit the HEH carrying HAMZA ABOVE in ``هندسهٔ``.
        # Bind the two extraction-stable heading fragments on the same page.
        require(
            all(compact_text(fragment) in compact_text(pages[page - 1]) for fragment in ("آزمون", "پیوندها")),
            f"geometry heading missing from page {page}",
        )
    for page in (2, 4, 6, 8):
        require(
            compact_text("آزمون استنادها و پیوندهای برون‌متنی") in compact_text(pages[page - 1]),
            f"citation/link heading missing from page {page}",
        )
        for phrase in ("Cantor", "Frege", "Magnus", "example.org", "عنوان فارسی"):
            require(compact_text(phrase) in compact_text(pages[page - 1]), f"page {page} lacks fixture phrase {phrase}")
    require(compact_text("مقصدهای آزمون") in compact_text(pages[8]), "destination page role changed")
    require(compact_text("کتاب‌نامه") in compact_text(pages[9]), "bibliography page role changed")
    for author in ("Cantor", "Frege", "Benacerraf", "Magnus", "Solow", "Hammack"):
        require(compact_text(author) in compact_text(pages[9]), f"bibliography author missing: {author}")
    bibliography_latin_lines = [
        line
        for line in lines_by_page[9]
        if re.search(r"[A-Za-z]", str(line.get("text", "")))
    ]
    require(len(bibliography_latin_lines) == 6, "bibliography must contain six Latin fixture lines")
    for line in bibliography_latin_lines:
        direction = as_list(line.get("direction"), "bibliography line direction")
        require(
            len(direction) == 2
            and abs(float(direction[0]) - 1.0) < 1e-6
            and abs(float(direction[1])) < 1e-6,
            "bibliography line is not left-to-right",
        )
    return {"page_roles": [case["name"] for case in EXPECTED_CASES] + ["DESTINATIONS", "BIBLIOGRAPHY"], "bibliography_ltr_lines": 6}


def validate(receipt_path: Path) -> dict[str, object]:
    clear_snapshot_cache()
    manifest = validate_fixture()
    common = validate_diagnostic_receipt(
        receipt_path,
        job=JOB,
        driver=DRIVER,
        driver_sha256=str(as_mapping(manifest["output"], "output")["sha256"]),
        allow_reference_warnings=False,
        allow_latex_rerun_warnings=True,
        require_layout_markers=False,
    )
    log_markers = validate_log_markers(common["log_text"])
    require_recorder_inputs(common["recorder_inputs"], (DRIVER, INTERVENTION))
    trace_path = common["run_root"] / TRACE_NAME
    require(trace_path.is_file(), "drawing-level link trace is missing")
    preserved_trace = load_json(trace_path)
    recomputed_trace = json.loads(json.dumps(audit(common["pdf"]), ensure_ascii=False))
    require(preserved_trace == recomputed_trace, "preserved drawing-level trace differs from recomputation")
    trace_checks = validate_trace(recomputed_trace)

    pages, _blocks, lines, fitz_version, page_geometry = load_pdf_text(common["pdf"])
    page_roles = validate_pdf_roles(pages, lines)
    extracted_text = "\n\f\n".join(pages)

    evidence = base_evidence(
        kind="rtl-link-geometry",
        common=common,
        fixture=DRIVER,
        fixture_manifest=MANIFEST,
    )
    evidence.update(
        {
            "schema": "farsi-standalone-link-geometry-native-probe-qa-v1",
            "status": "PASS_NATIVE_DIAGNOSTIC_PENDING_COMPLETE_VISUAL_INSPECTION_NOT_FULL_READER",
            "dependencies": [file_record(path) for path in (GENERATOR, FIXTURE, INTERVENTION, DIAGNOSTIC)],
            "log_markers": log_markers,
            "drawing_trace": {**file_record(trace_path), **trace_checks},
            "pdf_text": {
                **page_roles,
                "extracted_text_sha256": sha256_bytes(extracted_text.encode("utf-8")),
                "pymupdf_version": fitz_version,
                "page_geometry": page_geometry,
            },
            "selected_intervention": {
                "probe_mode": 1,
                "name": "NATIVE-ATOMIC",
                "reason": "It removes all four outside/full-text-width baseline annotations and is geometry-equivalent to the stronger isolated mode; raw-URL direction adds an edge mismatch.",
                "production_scope": "Atomic native-direction content for direct hyper@link links and citation start/end pairs; TOC start/end pairs and raw URL direction remain unchanged.",
            },
            "checks": {
                "fixture_reconstructed_from_generator": True,
                "guard_mutex_tree_exit_and_log_receipt_recomputed": True,
                "drawing_trace_recomputed_byte_semantically": True,
                "all_link_targets_and_page_statistics_exact": True,
                "native_atomic_equals_isolated_atomic_geometry": True,
                "native_atomic_is_minimal_successful_mode": True,
                "raw_url_ltr_mode_rejected": True,
            },
            "limitations": [
                "This diagnostic compares one adversarial fixture; the selected production intervention still requires a fresh complete-reader build and link audit.",
                "PDF extraction and rectangle checks do not replace rendered full-page inspection.",
                "This diagnostic does not qualify the complete 722-unit reader.",
            ],
        }
    )
    return evidence


def self_test() -> dict[str, object]:
    valid_log = "\n".join(
        [
            "OL-LINK-GEOMETRY-PROBE-MODE=0",
            "OL-LINK-GEOMETRY-PROBE-MODE=0",
            "OL-LINK-GEOMETRY-CASE=BASELINE",
            "OL-LINK-GEOMETRY-PROBE-MODE=1",
            "OL-LINK-GEOMETRY-CASE=NATIVE-ATOMIC",
            "OL-LINK-GEOMETRY-PROBE-MODE=2",
            "OL-LINK-GEOMETRY-CASE=ISOLATED-ATOMIC",
            "OL-LINK-GEOMETRY-PROBE-MODE=3",
            "OL-LINK-GEOMETRY-CASE=ISOLATED-ATOMIC-RAW-URL-LTR",
        ]
    )
    validate_log_markers(valid_log)
    expect_validation_error(validate_log_markers, valid_log.replace("PROBE-MODE=3", "PROBE-MODE=2"))
    expect_validation_error(validate_log_markers, valid_log.replace("CASE=NATIVE-ATOMIC\n", ""))

    sample = {"target": "Hfootnote.7", "rect": [1, 2, 3, 4], "width": 2.0, "color": [1, 0, 0], "draw_colors": [[1, 0, 0]], "outside": False, "left": [], "right": [], "enclosed": [0], "band": [0]}
    other = deepcopy(sample)
    other["target"] = "Hfootnote.8"
    require(normalized_page_signature([sample]) == normalized_page_signature([other]), "footnote target normalization failed")
    other["width"] = 3.0
    require(normalized_page_signature([sample]) != normalized_page_signature([other]), "geometry signature ignored width mutation")
    require(page_stats([]) == (0, 0, 0, 0, 0.0, {}), "empty-page statistics changed")
    outside = deepcopy(sample)
    outside["outside"] = True
    outside["width"] = 468.244
    outside["enclosed"] = []
    require(page_stats([outside])[:5] == (1, 1, 1, 1, 468.244), "page statistics failed")
    expect_validation_error(colour_key, [0.5, 0, 0])
    common_controls = self_test_common_primitives()
    return {
        "schema": "farsi-link-geometry-postbuild-self-test-v1",
        "status": "PASS",
        "negative_controls": 4 + common_controls,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_test:
            require(args.receipt is None and args.output is None, "--self-test cannot be combined with receipt/output")
            result = self_test()
        else:
            require(args.receipt is not None, "--receipt is required")
            require(args.output is not None, "--output is required and has no default")
            result = validate(args.receipt)
            write_json(args.output, result)
        print(json.dumps(result, ensure_ascii=True, sort_keys=True))
    except ValidationError as exc:
        message = str(exc).encode("ascii", "backslashreplace").decode("ascii")
        print(f"FAIL: {message}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
