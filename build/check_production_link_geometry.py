"""Statically validate the selected production RTL link-geometry layer.

This checker binds the guarded four-mode probe and its complete visual review,
then verifies that production installs only the minimal native-atomic behavior.
It never launches TeX; a fresh complete-reader build remains mandatory.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import hashlib
import json
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
LOCALE = ROOT / "source/locale/fa-IR"
BODY = LOCALE / "standalone/body.tex"
PRODUCTION = LOCALE / "standalone/link-geometry.tex"
RUNTIME_FIXES = LOCALE / "standalone/runtime-fixes.tex"
DRIVER = LOCALE / "open-logic-standalone-fa-IR.tex"
NATIVE_QA = ROOT / "evidence/LINK_GEOMETRY_NATIVE_PROBE_QA.json"
VISUAL_QA = ROOT / "evidence/LINK_GEOMETRY_NATIVE_PROBE_VISUAL_QA.json"
PROBE_INTERVENTION = ROOT / "build/probes/link-geometry/link-geometry-intervention.tex"
EXPECTED_NATIVE_QA = "c1ea7eb51a2c8c49f08f9460613011ab83db8fbf78c66281f6dd4f39f8fd6099"
EXPECTED_VISUAL_QA = "93b7aed6fce2e3d23ef590cecac882c841c2a08fd379fa63c82b38e160cf50d4"
EXPECTED_PROBE_INTERVENTION = "81a17ac8e249619f8a466cd6545d60b5e6bab8c41eae1b3c60b2fbd8c8c35de0"
EXPECTED_BODY_INPUTS = [
    "standalone/runtime-fixes.tex",
    "standalone/link-geometry.tex",
    "standalone/runtime.tex",
    "standalone/generated-ledger.tex",
    "standalone/context.tex",
    "standalone/source-corrections.tex",
    "standalone/typography.tex",
    "standalone/bidi-layout.tex",
    "standalone/variants.tex",
]


class CheckError(RuntimeError):
    pass


def require(condition: object, message: str) -> None:
    if not condition:
        raise CheckError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record(path: Path) -> dict[str, object]:
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": path.stat().st_size,
        "sha256": sha(path),
    }


def load_json(path: Path) -> dict[str, object]:
    pairs_seen: list[str] = []

    def unique(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in pairs:
            require(key not in result, f"duplicate JSON key in {path}: {key}")
            result[key] = value
            pairs_seen.append(key)
        return result

    value = json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=unique)
    require(isinstance(value, dict), f"JSON root is not an object: {path}")
    return value


def active_tex(text: str) -> str:
    lines = []
    for raw in text.splitlines():
        escaped = False
        out = []
        for character in raw:
            if character == "%" and not escaped:
                break
            out.append(character)
            if character == "\\":
                escaped = not escaped
            else:
                escaped = False
        lines.append("".join(out))
    return "\n".join(lines)


def body_inputs(text: str) -> list[str]:
    return re.findall(r"(?m)^[ \t]*\\input[ \t]*\{([^{}]+)\}[ \t]*$", active_tex(text))


def check_layer(text: str) -> dict[str, object]:
    source = active_tex(text)
    required_once = [
        r"\def\OLStandaloneLinkGeometryInstalled{native-atomic-v1}",
        r"\let\OLSA@original@hyper@link\hyper@link",
        r"\let\OLSA@original@hyper@linkstart\hyper@linkstart",
        r"\let\OLSA@original@hyper@linkend\hyper@linkend",
        r"\def\OLSA@link@cite@type{cite}",
        r"\long\def\OLSA@link@nativebox#1{\leavevmode\hbox{#1}}",
        r"\long\def\hyper@link#1#2#3",
        r"\def\hyper@linkstart#1#2",
        r"\def\hyper@linkend",
        r"OL-STANDALONE-LINK-GEOMETRY|native-atomic-v1|toc-and-url-direction-unchanged",
    ]
    for token in required_once:
        require(source.count(token) == 1, f"production link token missing or duplicated: {token}")
    require(source.index(r"\let\OLSA@original@hyper@link\hyper@link") < source.index(r"\long\def\hyper@link#1#2#3"), "direct link is replaced before original is saved")
    require(source.index(r"\let\OLSA@original@hyper@linkstart\hyper@linkstart") < source.index(r"\def\hyper@linkstart#1#2"), "link-start is replaced before original is saved")
    require(source.index(r"\let\OLSA@original@hyper@linkend\hyper@linkend") < source.index(r"\def\hyper@linkend"), "link-end is replaced before original is saved")
    require(r"\ifx\OLSA@link@this@type\OLSA@link@cite@type" in source, "citation-only start/end selection is absent")
    require(r"\hbox\bgroup\OLSA@original@hyper@linkstart{#1}{#2}" in source, "citation link is not atomically boxed")
    require(r"\OLSA@link@nativebox{\OLSA@original@hyper@link{#1}{#2}{#3}}" in source, "direct link is not atomically boxed")
    for forbidden in (
        r"\bbl@textdir",
        r"\bbl@setdirs",
        r"\url@",
        r"\OLLinkProbeMode",
        r"\OLLinkGeometryInstall",
        "isolated",
        "raw-url-ltr",
    ):
        require(forbidden not in source, f"production layer contains rejected stronger behavior: {forbidden}")
    require(source.count(r"\PackageError{standalone-link-geometry}") == 2, "fail-closed load/precondition guards changed")
    return {
        "direct_hyper_links_atomic": True,
        "citation_start_end_pairs_atomic": True,
        "toc_start_end_pairs_unchanged": True,
        "raw_url_direction_unchanged": True,
        "explicit_direction_isolation_absent": True,
        "duplicate_load_and_missing_hyperref_fail_closed": True,
    }


def check_probe_evidence() -> dict[str, object]:
    require(sha(NATIVE_QA) == EXPECTED_NATIVE_QA, "native link-geometry QA identity changed")
    require(sha(VISUAL_QA) == EXPECTED_VISUAL_QA, "visual link-geometry QA identity changed")
    require(sha(PROBE_INTERVENTION) == EXPECTED_PROBE_INTERVENTION, "probe intervention identity changed")
    native = load_json(NATIVE_QA)
    visual = load_json(VISUAL_QA)
    require(native.get("schema") == "farsi-standalone-link-geometry-native-probe-qa-v1", "native QA schema changed")
    require(native.get("status") == "PASS_NATIVE_DIAGNOSTIC_PENDING_COMPLETE_VISUAL_INSPECTION_NOT_FULL_READER", "native QA status changed")
    selected = native.get("selected_intervention")
    require(isinstance(selected, dict) and selected.get("probe_mode") == 1 and selected.get("name") == "NATIVE-ATOMIC", "native QA no longer selects mode 1")
    checks = native.get("checks")
    require(isinstance(checks, dict), "native QA checks missing")
    for key in (
        "all_link_targets_and_page_statistics_exact",
        "native_atomic_equals_isolated_atomic_geometry",
        "native_atomic_is_minimal_successful_mode",
        "raw_url_ltr_mode_rejected",
    ):
        require(checks.get(key) is True, f"native QA check is not true: {key}")
    trace = native.get("drawing_trace")
    require(isinstance(trace, dict), "native QA drawing trace missing")
    require(trace.get("pages") == 10 and trace.get("links") == 265, "native QA trace cardinality changed")
    page2 = trace.get("per_page", {}).get("2")
    page4 = trace.get("per_page", {}).get("4")
    page8 = trace.get("per_page", {}).get("8")
    require(isinstance(page2, dict) and page2.get("outside_page") == 4 and page2.get("full_text_width") == 4, "baseline failure witness changed")
    require(isinstance(page4, dict) and page4.get("outside_page") == 0 and page4.get("full_text_width") == 0, "mode 1 success witness changed")
    require(isinstance(page8, dict) and page8.get("zero_enclosed_glyph_groups") == 2, "mode 3 regression witness changed")

    require(visual.get("schema") == "farsi-standalone-link-geometry-native-probe-visual-qa-v1", "visual QA schema changed")
    require(visual.get("status") == "PASS_COMPLETE_VISUAL_INSPECTION_NATIVE_DIAGNOSTIC_NOT_FULL_READER", "visual QA status changed")
    receipt = visual.get("semantic_qa_receipt")
    require(isinstance(receipt, dict) and receipt == record(NATIVE_QA), "visual QA is not bound to native semantic QA")
    rendered = visual.get("rendered_pages")
    require(isinstance(rendered, list) and [row.get("page_one_based") for row in rendered if isinstance(row, dict)] == list(range(1, 11)), "visual QA page coverage changed")
    for row in rendered:
        require(isinstance(row, dict) and set(row) == {"page_one_based", "path", "bytes", "sha256"}, "visual page record fields changed")
        path = ROOT / str(row["path"])
        require(path.is_file() and record(path) == {"path": row["path"], "bytes": row["bytes"], "sha256": row["sha256"]}, f"visual page identity changed: {row.get('page_one_based')}")
    visual_checks = visual.get("checks")
    require(isinstance(visual_checks, dict) and visual_checks.get("all_pages_rendered_and_inspected") is True, "visual QA is incomplete")
    require(visual_checks.get("complete_reader_qualified") is False, "diagnostic visual QA overclaims full-reader qualification")
    selected_visual = visual.get("inspection", {}).get("selected_mode")
    require(isinstance(selected_visual, dict) and selected_visual.get("mode") == 1, "visual QA no longer selects mode 1")
    return {
        "native_qa": record(NATIVE_QA),
        "visual_qa": record(VISUAL_QA),
        "probe_intervention": record(PROBE_INTERVENTION),
        "diagnostic_pages_inspected": 10,
        "diagnostic_links_audited": 265,
        "selected_probe_mode": 1,
    }


def validate() -> dict[str, object]:
    for path in (BODY, PRODUCTION, RUNTIME_FIXES, DRIVER, NATIVE_QA, VISUAL_QA, PROBE_INTERVENTION):
        require(path.is_file(), f"required file missing: {path}")
    evidence = check_probe_evidence()
    layer = check_layer(PRODUCTION.read_text(encoding="utf-8"))
    inputs = body_inputs(BODY.read_text(encoding="utf-8"))
    require(inputs == EXPECTED_BODY_INPUTS, f"standalone body input topology changed: {inputs!r}")
    body = active_tex(BODY.read_text(encoding="utf-8"))
    positions = [body.index(rf"\input{{{name}}}") for name in EXPECTED_BODY_INPUTS]
    require(positions == sorted(positions), "standalone body input order changed")
    require(positions[1] < body.index(r"\OLSAStart"), "link layer is not installed before reader content")
    require(BODY.read_text(encoding="utf-8").count(r"\input{standalone/link-geometry.tex}") == 1, "production layer load count changed")
    require(DRIVER.read_text(encoding="utf-8").count(r"\input{standalone/body.tex}") == 1, "driver body activation count changed")
    require("OL-STANDALONE-BANG-FALLBACK|guarded" in RUNTIME_FIXES.read_text(encoding="utf-8"), "proven runtime-fix marker is absent")

    # Mutation tests exercise the semantic assertions, not only file hashes.
    mutations = [
        PRODUCTION.read_text(encoding="utf-8").replace(r"\hbox{#1}", "#1", 1),
        PRODUCTION.read_text(encoding="utf-8").replace(r"\OLSA@link@cite@type{cite}", r"\OLSA@link@cite@type{link}", 1),
        PRODUCTION.read_text(encoding="utf-8") + "\n\\def\\url@#1{#1}\n",
        PRODUCTION.read_text(encoding="utf-8").replace("native-atomic-v1", "isolated", 1),
    ]
    for mutation in mutations:
        try:
            check_layer(mutation)
        except CheckError:
            pass
        else:
            raise CheckError("production link-geometry mutation was accepted")

    return {
        "schema": "farsi-standalone-production-link-geometry-static-qa-v1",
        "status": "PASS_STATIC_SELECTED_NATIVE_ATOMIC_READY_FOR_FULL_READER_BUILD",
        "selection_evidence": evidence,
        "production_layer": {**record(PRODUCTION), **layer},
        "activation": {
            "body": record(BODY),
            "runtime_fixes": record(RUNTIME_FIXES),
            "driver": record(DRIVER),
            "body_inputs": inputs,
            "installed_before_olsa_start": True,
            "link_layer_load_count": 1,
        },
        "negative_controls": [
            "direct_link_atomic_box_removal_rejected",
            "citation_type_change_rejected",
            "raw_url_override_rejected",
            "direction_isolation_rejected",
        ],
        "full_reader_qa_passed": False,
        "next_required_gate": "Fresh guarded full-reader build, semantic/link audit, complete page rendering and visual inspection, then deterministic replay.",
        "files": [record(path) for path in (Path(__file__), BODY, PRODUCTION, RUNTIME_FIXES, DRIVER, NATIVE_QA, VISUAL_QA)],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-evidence", type=Path)
    args = parser.parse_args()
    try:
        result = validate()
        if args.write_evidence is not None:
            output = args.write_evidence.resolve()
            evidence_root = (ROOT / "evidence").resolve()
            require(output.parent == evidence_root and output.suffix == ".json", "evidence output must be an explicit JSON file directly under evidence/")
            output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, ensure_ascii=True, sort_keys=True))
    except (CheckError, AssertionError, KeyError, TypeError, ValueError) as exc:
        message = str(exc).encode("ascii", "backslashreplace").decode("ascii")
        print(f"FAIL: {message}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
