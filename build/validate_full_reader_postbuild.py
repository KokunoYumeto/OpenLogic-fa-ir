"""Fail-closed postbuild acceptance checks for the complete Standard-Farsi reader.

This validator never launches TeX and never edits translated source.  It binds
one completed Full-mode guarded transaction to its captured source inventory,
both converged output directories, the independently reconstructed 722-unit
integration ledger, runtime sidecars, final logs, and the byte-identical PDF.

A PASS here establishes deterministic build/readback acceptance only.  It does
not establish rendered-page visual QA, link-annotation geometry QA, release
packaging, publication, or public-byte readback.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import math
import os
import re
import stat
import sys

import make_standalone_ledger
from probe_postbuild_common import (
    ENTRYPOINT,
    HELPER,
    LOCALE,
    MEMORY_LIMIT,
    MUTEX_NAME,
    PYMUPDF_VERSION,
    RECEIPT_SCHEMA,
    ROOT,
    RUNS,
    SOURCE,
    ValidationError,
    _validate_inventory,
    as_list,
    as_mapping,
    clear_snapshot_cache,
    expect_validation_error,
    file_snapshot,
    is_json_integer,
    load_json,
    parse_log_diagnostics,
    read_file_bytes,
    read_file_text,
    recorder_manifest,
    relative_repo_path,
    require,
    require_exact_keys,
    require_recorder_inputs,
    same_path,
    sha256_bytes,
    sha256_file,
    under,
    validate_output_path,
    validate_receipt_path,
    validate_repo_recorder_input_freshness,
    write_json,
)


JOB = "open-logic-standalone-fa-IR"
DEFAULT_OUTPUT = ROOT / "evidence/STANDALONE_FULL_READER_POSTBUILD_QA.json"
DRIVER = LOCALE / f"{JOB}.tex"
INTEGRATION_LEDGER = ROOT / "evidence/STANDALONE_INTEGRATION_LEDGER.json"
GENERATED_LEDGER = LOCALE / "standalone/generated-ledger.tex"
DERIVED_SOURCE_MANIFEST = LOCALE / "standalone/generated-source-corrections/MANIFEST.json"
LEDGER_GENERATOR = ROOT / "build/make_standalone_ledger.py"
DERIVED_SOURCE_GENERATOR = ROOT / "build/generate_source_correction_overlays.py"
SOURCE_CORRECTION_CHECKER = ROOT / "build/check_functions_source_corrections.py"

PINNED_DRIVER_SHA256 = "918eedfd83099a4ae65caaf7f65113e771460c420bda3b8fc9fe93d5d748dea7"
PINNED_ENTRYPOINT_SHA256 = "2f9de87404e90a3de625c6d25a89e7014ef26c4153a3c251ef592b8c4fcb4320"
PINNED_HELPER_SHA256 = "d072db671c4dde29d2bf53d97719df2ffcd3446795e1c2fb4f54fb4078b26117"
PINNED_LEDGER_GENERATOR_SHA256 = "e62ef89de245ff6671e548e6492f429658a3716caf2d314c24cdb9e5aa4746a5"
PINNED_INTEGRATION_LEDGER_SHA256 = "0a6cc8b2799117a3216e25ebe84ecd3c0cd3a665ddd9d55d7e7bad2bdda21dea"
PINNED_GENERATED_LEDGER_SHA256 = "ca05c3dedf9ec23a32be75c6556e7cdd94fcbe326b5bb3ec3023cdcb5ab1140e"
PINNED_DERIVED_SOURCE_GENERATOR_SHA256 = "142f98e3f89b615e7cb308692a18688ebbbcbd40da569844b92bee851938c2bd"
PINNED_SOURCE_CORRECTION_CHECKER_SHA256 = "08cc941074e016624e891e85349d88741cddd177ca8443fb786639d859569dac"
EXPECTED_DERIVED_PREFLIGHT_OUTPUT = (
    "PASS: 18 derived source files; 24 exact correction events; frozen sources untouched"
)
EXPECTED_C0_CONTROL_COUNTS = {
    "U+0000": 4,
    "U+0001": 4,
    "U+0006": 8,
    "U+0007": 8,
    "U+000C": 24,
    "U+000E": 2,
    "U+0012": 1,
    "U+0013": 1,
    "U+001A": 1,
    "U+001B": 2,
}
EXPECTED_C0_CONTROL_FONTS = ["CMEX10", "MSBM10"]

EXPECTED_ENVIRONMENT = {
    "SOURCE_DATE_EPOCH": "1783874174",
    "FORCE_SOURCE_DATE": "1",
    "TZ": "UTC",
    "max_print_line": "1000",
    "openin_any": "a",
    "openout_any": "p",
    "shell_escape": "0",
}
EXPECTED_LAYOUT_MARKERS = [
    "OL-R2-TEXTWIDTH=468.0pt",
    "OL-R2-TEXTHEIGHT=650.0pt",
    "OL-R2-FONTSIZE=14.4pt",
    "OL-R2-BASELINESKIP=18.37505pt",
    "OL-R2-ODDSIDEMARGIN=0.8773pt",
    "OL-R2-EVENSIDEMARGIN=0.8773pt",
    "OL-R2-UPPERMARGIN=72.485pt",
]
EXPECTED_RUNTIME_MARKERS = {
    "bang": "OL-STANDALONE-BANG-FALLBACK|guarded",
    "link_geometry_selection": (
        "OL-STANDALONE-LINK-GEOMETRY|native-atomic-v1|"
        "toc-and-url-direction-unchanged"
    ),
    "unit_coverage": "OL-STANDALONE-COVERAGE|722|774",
    "source_correction_coverage": (
        "OL-STANDALONE-SOURCE-CORRECTION-COVERAGE|39|39"
    ),
    "typography_coverage": "OL-STANDALONE-TYPOGRAPHY-COVERAGE|18|18",
    "bidi_layout_coverage": "OL-STANDALONE-BIDI-LAYOUT-COVERAGE|24|46",
}

EXPECTED_CORRECTION_TRACE = [
    ("OLP-0021", "ex", "OLFUN-002", "1"),
    ("OLP-0021", "ex", "OLFUN-003", "1"),
    ("OLP-0023", "explain", "OLFUN-004", "1"),
    ("OLP-0023", "explain", "OLFUN-005", "1"),
    ("OLP-0024", "prop", "OLFUN-001-THEOREM", "1"),
    ("OLP-0024", "proof", "OLFUN-001-PROOF", "1"),
    ("OLP-0029", "ex", "OLSIZ-001", "1"),
    ("OLP-0032", "explain", "OLSIZ-003", "1"),
    ("OLP-0034", "proof", "OLSIZ-004", "1"),
    ("OLP-0034", "explain", "OLSIZ-005", "1"),
    ("OLP-0035", "proof", "OLSIZ-006", "1"),
    ("OLP-0036", "proof", "OLSIZ-007", "1"),
    ("OLP-0039", "proof", "OLSIZ-008+009", "1"),
    ("OLP-0040", "proof", "OLSIZ-010", "1"),
    ("OLP-0031", "prob", "OLSIZ-002", "1"),
    ("OLP-0091", "document-text", "OLVIS-0091", "1"),
    ("OLP-0164", "document-text", "OLVIS-0164", "1"),
    ("OLP-0165", "document-text", "OLVIS-0165", "1"),
    ("OLP-0091", "document-text", "OLVIS-0091", "2"),
    ("OLP-0133", "document-text", "OLVIS-0133-OVERFLOW", "1"),
    ("OLP-0133", "document-text", "OLVIS-0133-COMMA", "1"),
    ("OLP-0179", "document-text", "OLEMPH-001", "1"),
    ("OLP-0179", "document-text", "OLEMPH-002", "1"),
    ("OLP-0179", "document-text", "OLEMPH-003", "1"),
    ("OLP-0180", "document-text", "OLEMPH-004", "1"),
    ("OLP-0180", "document-text", "OLEMPH-005", "1"),
    ("OLP-0180", "document-text", "OLEMPH-006", "1"),
    ("OLP-0180", "document-text", "OLEMPH-007", "1"),
    ("OLP-0193", "document-text", "OLVIS-0193", "1"),
    ("OLP-0220", "document-text", "OLVIS-0220", "1"),
    ("OLP-0273", "document-text", "OLVIS-0273", "1"),
    ("OLP-0286", "document-text", "OLVIS-0286", "1"),
    ("OLP-0362", "document-text", "OLVIS-0362", "1"),
    ("OLP-0379", "document-text", "OLVIS-0379", "1"),
    ("OLP-0391", "document-text", "OLVIS-0391", "1"),
    ("OLP-0526", "document-text", "OLVIS-0526", "1"),
    ("OLP-0527", "document-text", "OLVIS-0527", "1"),
    ("OLP-0569", "document-text", "OLVIS-0569", "1"),
    ("OLP-0570", "document-text", "OLVIS-0570", "1"),
    ("OLP-0599", "document-text", "OLVIS-0599", "1"),
]
EXPECTED_TYPOGRAPHY_TRACE = [
    ("OLP-0163", "valuation-tuple", "1"),
    ("OLP-0711", "sequent-height-two-premises", "1"),
    ("OLP-0702", "sequent-depth-binary-case", "1"),
    ("OLP-0701", "invertibility-b-context-sequent", "1"),
    ("OLP-0701", "invertibility-b-context-sequent", "2"),
    ("OLP-0668", "height-two-premises", "1"),
    ("OLP-0668", "height-three-premises", "1"),
    ("OLP-0290", "representability-equivalence", "1"),
    ("OLP-0291", "q-provability-m", "1"),
    ("OLP-0291", "q-provability-l", "1"),
    ("OLP-0291", "q-provability-m", "2"),
    ("OLP-0291", "encoded-formula", "1"),
    ("OLP-0295", "composition-g-formula", "1"),
    ("OLP-0298", "relation-formula", "1"),
    ("OLP-0298", "relation-formula", "2"),
    ("OLP-0298", "relation-formula", "3"),
    ("OLP-0298", "relation-characteristic-positive", "1"),
    ("OLP-0325", "second-order-term-set", "1"),
    ("OLP-0369", "substitution-before-expansion", "1"),
    ("OLP-0369", "substitution-after-expansion", "1"),
    ("OLP-0556", "ordinal-type-beta", "1"),
    ("OLP-0588", "union-injection-map", "1"),
]
EXPECTED_BIDI_LAYOUT_TRACE = [
    ("OLP-0394", "lukasiewicz-name-toc-ltr", "1"),
    ("OLP-0400", "lukasiewicz-name-toc-ltr", "1"),
    ("OLP-0371", "setup", "1"),
    ("OLP-0371", "align-ltr-before", "1"),
    ("OLP-0371", "align-ltr-after", "1"),
    ("OLP-0371", "second-proof-emergency-stretch", "1"),
    ("OLP-0394", "setup", "1"),
    ("OLP-0394", "lukasiewicz-name-source-ltr", "1"),
    ("OLP-0394", "lukasiewicz-name-source-ltr", "2"),
    ("OLP-0394", "lukasiewicz-name-source-ltr", "3"),
    ("OLP-0394", "lukasiewicz-name-source-ltr", "4"),
    ("OLP-0394", "lukasiewicz-name-source-ltr", "5"),
    ("OLP-0394", "lukasiewicz-name-source-ltr", "6"),
    ("OLP-0394", "lukasiewicz-name-source-ltr", "7"),
    ("OLP-0394", "lukasiewicz-name-source-ltr", "8"),
    ("OLP-0394", "lukasiewicz-name-source-ltr", "9"),
    ("OLP-0394", "lukasiewicz-name-source-ltr", "10"),
    ("OLP-0396", "setup", "1"),
    ("OLP-0396", "lukasiewicz-name-source-ltr", "1"),
    ("OLP-0396", "lukasiewicz-name-source-ltr", "2"),
    ("OLP-0396", "lukasiewicz-name-source-ltr", "3"),
    ("OLP-0397", "setup", "1"),
    ("OLP-0397", "lukasiewicz-name-source-ltr", "1"),
    ("OLP-0394", "lukasiewicz-name-source-ltr", "11"),
    ("OLP-0400", "setup", "1"),
    ("OLP-0400", "lukasiewicz-name-source-ltr", "1"),
    ("OLP-0400", "lukasiewicz-name-source-ltr", "2"),
    ("OLP-0400", "lukasiewicz-name-source-ltr", "3"),
    ("OLP-0400", "lukasiewicz-name-source-ltr", "4"),
    ("OLP-0400", "lukasiewicz-name-source-ltr", "5"),
    ("OLP-0404", "setup", "1"),
    ("OLP-0404", "lukasiewicz-name-source-ltr", "1"),
    ("OLP-0406", "setup", "1"),
    ("OLP-0406", "lukasiewicz-name-source-ltr", "1"),
    ("OLP-0406", "lukasiewicz-name-source-ltr", "2"),
    ("OLP-0406", "lukasiewicz-name-source-ltr", "3"),
    ("OLP-0406", "lukasiewicz-name-source-ltr", "4"),
    ("OLP-0429", "setup", "1"),
    ("OLP-0429", "native-display-semicolon", "1"),
    ("OLP-0429", "dual-ltr", "1"),
    ("OLP-0429", "tag-ltr", "1"),
    ("OLP-0429", "tag-ltr", "2"),
    ("OLP-0429", "dual-ltr", "2"),
    ("OLP-0429", "rk-ltr", "1"),
    ("OLP-0429", "rk-ltr", "2"),
    ("OLP-0429", "first-proof-left-qed", "1"),
]
EXPECTED_BIDI_LAYOUT_BOOTSTRAP_TRACE = EXPECTED_BIDI_LAYOUT_TRACE[2:]
EXPECTED_BIDI_LAYOUT_BOOTSTRAP_COVERAGE = (
    "OL-STANDALONE-BIDI-LAYOUT-COVERAGE|22|44"
)
EXPECTED_METADATA = {
    "format": "PDF 1.5",
    "title": "متن منطق باز",
    "author": "Open Logic Project",
    "subject": "خوانشگر یکپارچهٔ فارسی معیار؛ منطق صوری، فرامنطق و مبانی منطق ریاضی",
    "keywords": "منطق صوری؛ فرامنطق؛ نظریهٔ مجموعه‌ها؛ نظریهٔ برهان؛ محاسبه‌پذیری؛ تمامیت؛ ناتمامیت",
    "creator": "LaTeX with hyperref",
    "producer": "LuaTeX-1.25.7",
    "creationDate": "D:20260712163614Z",
    "modDate": "D:20260712163614Z",
    "trapped": "",
    "encryption": None,
}
EXPECTED_WORKER_LABELS = [
    "primary-latex-01",
    "primary-bibtex-01",
    "primary-latex-02",
    "primary-bibtex-02",
    "primary-latex-03",
    "primary-latex-04",
    "replay-latex-01",
    "replay-bibtex-01",
    "replay-latex-02",
    "replay-bibtex-02",
    "replay-latex-03",
    "replay-latex-04",
]
POSTBUILD_ONLY_FILES = {
    "primary": ["FULL_READER_LINK_GEOMETRY_TRACE.json"],
    "replay": [],
}
STABLE_REPLAY_SUFFIXES = [
    "aux", "bbl", "toc", "out", "thm", "prb", "pcr",
    "olunits", "olcorrections", "oltypography", "olbidilayout", "pdf",
]


def _utc(value: object, label: str) -> datetime:
    require(isinstance(value, str) and value, f"{label} must be a timestamp")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValidationError(f"{label} is not ISO-8601: {value!r}") from exc
    require(parsed.tzinfo is not None, f"{label} lacks a timezone")
    require(parsed.utcoffset() == timezone.utc.utcoffset(parsed), f"{label} is not UTC")
    return parsed


def _finite(value: object) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def inventory_signature(rows: Sequence[tuple[str, int, str]]) -> str:
    text = "\n".join(f"{path}\t{size}\t{digest}" for path, size, digest in rows)
    return sha256_bytes(text.encode("utf-8"))


def validate_captured_output_inventory(
    raw_inventory: object,
    directory: Path,
    *,
    postbuild_only_files: Sequence[str],
) -> dict[str, tuple[int, str]]:
    """Validate receipted build bytes while isolating named later QA artifacts."""

    rows = as_list(raw_inventory, "build output inventory")
    require(rows, "build output inventory is empty")
    normalized: list[tuple[str, int, str]] = []
    for index, raw in enumerate(rows):
        row = as_mapping(raw, f"build output inventory row {index}")
        require_exact_keys(row, {"path", "bytes", "sha256"}, f"build output inventory row {index}")
        name, size, digest = row["path"], row["bytes"], row["sha256"]
        require(
            isinstance(name, str)
            and name
            and name == Path(name).name
            and not Path(name).is_absolute()
            and "/" not in name
            and "\\" not in name
            and ":" not in name,
            "unsafe build output inventory path",
        )
        require(is_json_integer(size) and size >= 0, "invalid build output byte count")
        require(isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest), "invalid build output hash")
        normalized.append((name, size, digest))
    names = [row[0] for row in normalized]
    require(names == sorted(names, key=str.casefold), "build output inventory is not sorted")
    require(len({name.casefold() for name in names}) == len(names), "duplicate build output inventory path")

    current_entries = [entry for entry in directory.iterdir() if entry.is_file()]
    require(len(current_entries) <= 200 + len(postbuild_only_files), "output directory exceeds bounded inventory")
    current_names = sorted((entry.name for entry in current_entries), key=str.casefold)
    expected_names = sorted(names + list(postbuild_only_files), key=str.casefold)
    require(
        current_names == expected_names,
        "current output set differs from receipted bytes plus the explicit postbuild-only boundary",
    )
    for extra_name in postbuild_only_files:
        extra = directory / extra_name
        require(extra.is_file() and not extra.is_symlink(), f"postbuild-only artifact is missing or linked: {extra_name}")
        require(extra_name not in names, f"postbuild-only artifact unexpectedly appears in build receipt: {extra_name}")

    result: dict[str, tuple[int, str]] = {}
    for name, size, digest in normalized:
        path = directory / name
        require(path.is_file() and not path.is_symlink(), f"receipted build output missing or linked: {name}")
        snapshot = file_snapshot(path)
        require(snapshot.size == size, f"build output byte count changed: {name}")
        require(snapshot.sha256 == digest, f"build output hash changed: {name}")
        result[name] = (size, digest)
    return result


def current_source_inventory() -> list[tuple[str, int, str]]:
    """Re-enumerate only repo/source with the producer's explicit bounds."""

    pending = [SOURCE.resolve()]
    rows: list[tuple[str, int, str]] = []
    directories = 0
    total_bytes = 0
    while pending:
        directory = pending.pop(0)
        directories += 1
        require(directories <= 5_000, "current source tree exceeds directory bound")
        directory_stat = directory.lstat()
        require(
            not (
                getattr(directory_stat, "st_file_attributes", 0)
                & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
            ),
            f"current source inventory refuses a reparse point: {directory}",
        )
        for entry in directory.iterdir():
            entry_stat = entry.lstat()
            require(
                not entry.is_symlink()
                and not (
                    getattr(entry_stat, "st_file_attributes", 0)
                    & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
                ),
                f"current source inventory refuses a link/reparse point: {entry}",
            )
            if entry.is_dir():
                pending.append(entry)
                continue
            require(entry.is_file(), f"unexpected non-file source entry: {entry}")
            snapshot = file_snapshot(entry)
            total_bytes += snapshot.size
            require(len(rows) < 5_000, "current source tree exceeds file bound")
            require(total_bytes <= 536_870_912, "current source tree exceeds byte bound")
            relative = entry.resolve().relative_to(SOURCE.resolve()).as_posix()
            rows.append((relative, snapshot.size, snapshot.sha256))
    rows.sort(key=lambda row: row[0].casefold())
    require(
        len({row[0].casefold() for row in rows}) == len(rows),
        "current source inventory contains case-fold duplicate paths",
    )
    return rows


def validate_ledger(inventory_rows: list[tuple[str, int, str]]) -> tuple[dict[str, object], list[str]]:
    require(
        sha256_file(LEDGER_GENERATOR) == PINNED_LEDGER_GENERATOR_SHA256,
        "integration-ledger generator identity changed",
    )
    require(
        sha256_file(INTEGRATION_LEDGER) == PINNED_INTEGRATION_LEDGER_SHA256,
        "integration-ledger evidence identity changed",
    )
    require(
        sha256_file(GENERATED_LEDGER) == PINNED_GENERATED_LEDGER_SHA256,
        "generated TeX ledger identity changed",
    )
    try:
        products = make_standalone_ledger.generate()
    except Exception as exc:
        raise ValidationError(f"independent ledger reconstruction failed: {exc}") from exc
    require(
        read_file_bytes(INTEGRATION_LEDGER) == products[INTEGRATION_LEDGER],
        "integration-ledger JSON differs from independent reconstruction",
    )
    require(
        read_file_bytes(GENERATED_LEDGER) == products[GENERATED_LEDGER],
        "generated TeX ledger differs from independent reconstruction",
    )
    ledger = dict(as_mapping(load_json(INTEGRATION_LEDGER), "integration ledger"))
    require_exact_keys(
        ledger,
        {
            "schema", "status", "closure_manifest_sha256", "source_targets",
            "primary_graph_targets", "retained_targets",
            "integrated_proof_theory_targets", "variant_wrappers",
            "injections_before", "injections_after",
            "variant_canonical_anchor_targets", "expected_order",
            "expected_unique_body_paths", "expected_context_body_occurrences",
            "default_tags", "primary_lexical_duplicate_requests",
            "integrated_lexical_duplicate_requests", "suppressed_variant_imports",
            "label_remaps", "rows", "reference_aliases", "validation",
            "runtime_gate", "uncertainties",
        },
        "integration ledger",
    )
    require(ledger["schema"] == "farsi-standalone-integration-ledger/1", "wrong integration-ledger schema")
    require(ledger["status"] == "PASS_STATIC_PLACEMENT_NOT_TEX_VALIDATED", "wrong integration-ledger status")
    require(ledger["source_targets"] == 722, "integration ledger does not name 722 units")
    require(ledger["primary_graph_targets"] == 642, "primary graph target count changed")
    require(ledger["retained_targets"] == 80, "retained target count changed")
    require(ledger["expected_unique_body_paths"] == 722, "unique body-path count changed")
    require(ledger["expected_context_body_occurrences"] == 774, "context occurrence count changed")
    validation = as_mapping(ledger["validation"], "integration validation")
    require(
        dict(validation)
        == {
            "all_target_hashes_match": True,
            "all_import_edges_resolve": True,
            "every_source_context_placed_once": True,
            "all_722_unique_source_units_placed": True,
            "unique_namespaced_label_targets": True,
            "tex_run": False,
        },
        "integration-ledger validation claims changed",
    )

    rows_raw = as_list(ledger["rows"], "integration rows")
    require(len(rows_raw) == 722, "integration ledger row count is not 722")
    rows = [as_mapping(row, f"integration row {index}") for index, row in enumerate(rows_raw)]
    ids = [row.get("id") for row in rows]
    paths = [row.get("source_path") for row in rows]
    require(ids == [f"OLP-{index:04d}" for index in range(1, 723)], "unit id inventory is incomplete or reordered")
    require(len(set(paths)) == 722, "unit source paths are not unique")
    require(sum(int(row.get("expected_body_occurrences", 0)) for row in rows) == 774, "row occurrence total changed")
    require(sum(row.get("expected_body_occurrences") == 2 for row in rows) == 52, "repeated-context unit count changed")

    expected_order_raw = as_list(ledger["expected_order"], "expected unit order")
    require(
        len(expected_order_raw) == 774
        and len(set(expected_order_raw)) == 774
        and all(isinstance(value, str) for value in expected_order_raw),
        "expected unit order is not 774 unique context keys",
    )
    inventory = {path: (size, digest) for path, size, digest in inventory_rows}
    expected_unit_lines = ["id|source_path|namespace|FOL_context|occurrence"]
    by_id = {str(row["id"]): row for row in rows}
    for row in rows:
        source_path = row.get("source_path")
        source_bytes = row.get("source_bytes")
        source_hash = row.get("source_sha256")
        require(isinstance(source_path, str) and source_path, "invalid ledger source path")
        inventory_path = f"locale/fa-IR/{source_path}"
        require(
            inventory.get(inventory_path) == (source_bytes, source_hash),
            f"ledger source identity is absent or changed in build inventory: {row.get('id')}",
        )
    for key in expected_order_raw:
        identifier, separator, context = str(key).partition("/")
        require(separator == "/" and context in {"FOL", "PL"}, f"invalid context key: {key!r}")
        require(identifier in by_id, f"unknown unit in expected order: {identifier}")
        row = by_id[identifier]
        expected_unit_lines.append(
            "|".join(
                [identifier, str(row["source_path"]), str(row["namespace"]), context, "1"]
            )
        )
    try:
        ledger_self_test = make_standalone_ledger.self_test(ledger)
    except Exception as exc:
        raise ValidationError(f"ledger self-test failed: {exc}") from exc
    require(ledger_self_test["negative_trace_tests"] == 4, "ledger mutation controls changed")
    return ledger, expected_unit_lines


def parse_pipe_trace(
    text: str,
    *,
    header: str,
    expected: Sequence[tuple[str, ...]],
    columns: int,
    label: str,
) -> list[tuple[str, ...]]:
    lines = text.lstrip("\ufeff").splitlines()
    require(lines and lines[0] == header, f"{label} header changed")
    require(all(lines[1:]), f"{label} contains a blank row")
    rows = [tuple(line.split("|")) for line in lines[1:]]
    require(all(len(row) == columns for row in rows), f"{label} column count changed")
    require(rows == list(expected), f"{label} events or order changed")
    require(len(rows) == len(set(rows)), f"{label} contains duplicate events")
    return rows


def validate_runtime_event_trace(
    lines: Sequence[str],
    *,
    marker: str,
    expected: Sequence[tuple[str, ...]],
    label: str,
) -> list[str]:
    prefix = marker + "|"
    expected_markers = [prefix + "|".join(row) for row in expected]
    actual = [line for line in lines if line.startswith(prefix)]
    require(actual == expected_markers, f"{label} log markers changed")
    return actual


def validate_overlay_pass_log(
    log_text: str, *, expects_toc_replay: bool, label: str,
) -> dict[str, object]:
    lines = log_text.splitlines()
    correction_trace = [
        (unit, finding, occurrence)
        for unit, _environment, finding, occurrence in EXPECTED_CORRECTION_TRACE
    ]
    corrections = validate_runtime_event_trace(
        lines,
        marker="OL-STANDALONE-SOURCE-CORRECTION",
        expected=correction_trace,
        label=f"{label} source-correction",
    )
    typography = validate_runtime_event_trace(
        lines,
        marker="OL-STANDALONE-TYPOGRAPHY",
        expected=EXPECTED_TYPOGRAPHY_TRACE,
        label=f"{label} typography",
    )
    expected_bidi = (
        EXPECTED_BIDI_LAYOUT_TRACE
        if expects_toc_replay
        else EXPECTED_BIDI_LAYOUT_BOOTSTRAP_TRACE
    )
    bidi = validate_runtime_event_trace(
        lines,
        marker="OL-STANDALONE-BIDI-LAYOUT",
        expected=expected_bidi,
        label=f"{label} bidi-layout",
    )
    require_exact_single_marker(
        lines,
        EXPECTED_RUNTIME_MARKERS["source_correction_coverage"],
        f"{label} source-correction coverage",
    )
    require_exact_single_marker(
        lines,
        EXPECTED_RUNTIME_MARKERS["typography_coverage"],
        f"{label} typography coverage",
    )
    bidi_coverage = (
        EXPECTED_RUNTIME_MARKERS["bidi_layout_coverage"]
        if expects_toc_replay
        else EXPECTED_BIDI_LAYOUT_BOOTSTRAP_COVERAGE
    )
    require_exact_single_marker(lines, bidi_coverage, f"{label} bidi-layout coverage")
    return {
        "source_correction_events": len(corrections),
        "typography_events": len(typography),
        "bidi_layout_rules": len({(row[0], row[1]) for row in expected_bidi}),
        "bidi_layout_events": len(bidi),
        "toc_replay_events": 2 if expects_toc_replay else 0,
    }


def validate_unit_trace(text: str, expected_lines: Sequence[str]) -> list[tuple[str, ...]]:
    lines = text.lstrip("\ufeff").splitlines()
    require(lines == list(expected_lines), "olunits events, order, or boundary fields changed")
    rows = [tuple(line.split("|")) for line in lines[1:]]
    require(all(len(row) == 5 for row in rows), "olunits column count changed")
    require(len(rows) == 774, "olunits context occurrence count changed")
    require(len({row[0] for row in rows}) == 722, "olunits unique unit count changed")
    return rows


def expected_boundary_events(ledger: Mapping[str, object]) -> list[tuple[str, str, str]]:
    rows = [as_mapping(value, "integration row") for value in as_list(ledger["rows"], "integration rows")]
    occurrences: dict[str, Mapping[str, object]] = {}
    for row in rows:
        for raw in as_list(row.get("expected_context_occurrences"), "row context occurrences"):
            occurrence = as_mapping(raw, "context occurrence")
            key = occurrence.get("key")
            require(isinstance(key, str) and key not in occurrences, "duplicate or invalid occurrence key")
            occurrences[key] = occurrence

    result: list[tuple[str, str, str]] = []
    stack: list[tuple[str, str]] = []
    for raw_key in as_list(ledger["expected_order"], "expected order"):
        key = str(raw_key)
        require(key in occurrences, f"expected occurrence lacks placement data: {key}")
        occurrence = occurrences[key]
        identifier = str(occurrence.get("id"))
        context = str(occurrence.get("context"))
        parent = occurrence.get("parent")
        via = str(occurrence.get("via"))
        if via in {"insert_before", "insert_after"}:
            target_key = f"{parent}/{context}"
            require(target_key in occurrences, f"injection target occurrence is missing: {target_key}")
            parent = occurrences[target_key].get("parent")
        if parent is None:
            while stack:
                closed_id, closed_context = stack.pop()
                result.append(("EXIT", closed_id, closed_context))
        else:
            while stack and stack[-1][0] != parent:
                closed_id, closed_context = stack.pop()
                result.append(("EXIT", closed_id, closed_context))
            require(stack and stack[-1][0] == parent, f"placement parent is absent at {key}: {parent}")
        result.append(("ENTER", identifier, context))
        stack.append((identifier, context))
    while stack:
        closed_id, closed_context = stack.pop()
        result.append(("EXIT", closed_id, closed_context))
    require(len(result) == 1_548, "expected entry/exit boundary event count changed")
    return result


def _tex_wrapped_line(value: str) -> str:
    """Model the accepted LuaTeX log's 79-column terminal wrapping."""

    return "\n".join(value[offset : offset + 79] for offset in range(0, len(value), 79))


def require_exact_single_marker(lines: Sequence[str], marker: str, label: str) -> None:
    family = marker.partition("|")[0] + "|"
    require(
        [line for line in lines if line.startswith(family)] == [marker],
        f"{label} marker missing, duplicated, or malformed",
    )


def validate_runtime_log(
    log_text: str,
    *,
    unit_rows: Sequence[tuple[str, ...]],
    expected_boundaries: Sequence[tuple[str, str, str]],
    ledger: Mapping[str, object],
) -> dict[str, object]:
    lines = log_text.splitlines()
    layout_lines = [line for line in lines if line.startswith("OL-R2-")]
    require(layout_lines == EXPECTED_LAYOUT_MARKERS, "full-reader layout markers changed")
    for label, marker in EXPECTED_RUNTIME_MARKERS.items():
        require_exact_single_marker(lines, marker, label)
    require(not any("OL-STANDALONE-SKIP" in line for line in lines), "runtime contains a skipped-unit marker")
    first_enter_offset = log_text.find("OL-STANDALONE-ENTER|")
    last_exit_offset = log_text.rfind("OL-STANDALONE-EXIT|")
    require(
        0 <= log_text.find(EXPECTED_RUNTIME_MARKERS["bang"]) < first_enter_offset
        and 0 <= log_text.find(EXPECTED_RUNTIME_MARKERS["link_geometry_selection"]) < first_enter_offset,
        "runtime setup markers are not before source execution",
    )
    terminal_offsets = [
        log_text.find(EXPECTED_RUNTIME_MARKERS[key])
        for key in (
            "bidi_layout_coverage",
            "source_correction_coverage",
            "typography_coverage",
            "unit_coverage",
        )
    ]
    require(
        last_exit_offset >= 0
        and terminal_offsets == sorted(terminal_offsets)
        and all(offset > last_exit_offset for offset in terminal_offsets),
        "runtime coverage markers are missing, reordered, or precede the final source EXIT",
    )

    enter_positions = [
        match.start()
        for match in re.finditer(r"(?m)^OL-STANDALONE-ENTER\|", log_text)
    ]
    require(len(enter_positions) == len(unit_rows), "runtime ENTER count differs from olunits")
    for index, (position, row) in enumerate(zip(enter_positions, unit_rows, strict=True), 1):
        marker = "OL-STANDALONE-ENTER|" + "|".join(row)
        rendered = _tex_wrapped_line(marker)
        require(
            log_text.startswith(rendered + "\n", position),
            f"runtime ENTER marker {index} differs from the exact olunits row",
        )

    actual_boundaries: list[tuple[str, str, str]] = []
    enter_index = 0
    boundary_pattern = re.compile(
        r"(?m)^OL-STANDALONE-(ENTER|EXIT)\|(OLP-\d{4})(?:\|(FOL|PL))?"
    )
    for match in boundary_pattern.finditer(log_text):
        kind, identifier, context = match.groups()
        if kind == "ENTER":
            require(enter_index < len(unit_rows), "extra runtime ENTER marker")
            context = unit_rows[enter_index][3]
            enter_index += 1
        require(context in {"FOL", "PL"}, "runtime boundary lacks a valid context")
        actual_boundaries.append((kind, identifier, str(context)))
    require(
        actual_boundaries == list(expected_boundaries),
        "runtime source entry/exit nesting boundaries differ from the integration model",
    )
    boundary_depth = 0
    maximum_boundary_depth = 0
    for kind, _identifier, _context in actual_boundaries:
        boundary_depth += 1 if kind == "ENTER" else -1
        require(boundary_depth >= 0, "runtime boundary stack underflow")
        maximum_boundary_depth = max(maximum_boundary_depth, boundary_depth)
    require(boundary_depth == 0, "runtime boundary stack does not close")
    require(maximum_boundary_depth == 5, "runtime maximum nesting depth changed")

    correction_trace = [
        (unit, finding, occurrence)
        for unit, _environment, finding, occurrence in EXPECTED_CORRECTION_TRACE
    ]
    actual_corrections = validate_runtime_event_trace(
        lines,
        marker="OL-STANDALONE-SOURCE-CORRECTION",
        expected=correction_trace,
        label="source-correction",
    )
    actual_typography = validate_runtime_event_trace(
        lines,
        marker="OL-STANDALONE-TYPOGRAPHY",
        expected=EXPECTED_TYPOGRAPHY_TRACE,
        label="typography",
    )
    actual_bidi_layout = validate_runtime_event_trace(
        lines,
        marker="OL-STANDALONE-BIDI-LAYOUT",
        expected=EXPECTED_BIDI_LAYOUT_TRACE,
        label="bidi-layout",
    )

    suppressed = [
        as_mapping(row, "suppressed variant import")
        for row in as_list(ledger["suppressed_variant_imports"], "suppressed variant imports")
    ]
    expected_suppressed = [
        f"OL-STANDALONE-SUPPRESSED-VARIANT-EDGE|{row.get('from')}|{row.get('target')}"
        for row in suppressed
    ]
    actual_suppressed = [
        line for line in lines if line.startswith("OL-STANDALONE-SUPPRESSED-VARIANT-EDGE|")
    ]
    require(actual_suppressed == expected_suppressed, "suppressed-variant runtime markers changed")

    known_prefixes = (
        "OL-STANDALONE-ENTER|",
        "OL-STANDALONE-EXIT|",
        "OL-STANDALONE-SUPPRESSED-VARIANT-EDGE|",
        "OL-STANDALONE-SOURCE-CORRECTION|",
        "OL-STANDALONE-SOURCE-CORRECTION-COVERAGE|",
        "OL-STANDALONE-TYPOGRAPHY|",
        "OL-STANDALONE-TYPOGRAPHY-COVERAGE|",
        "OL-STANDALONE-BIDI-LAYOUT|",
        "OL-STANDALONE-BIDI-LAYOUT-COVERAGE|",
        "OL-STANDALONE-BANG-FALLBACK|",
        "OL-STANDALONE-LINK-GEOMETRY|",
        "OL-STANDALONE-COVERAGE|",
    )
    unknown = [
        line
        for line in lines
        if line.startswith("OL-STANDALONE-")
        and not line.startswith(known_prefixes)
    ]
    require(not unknown, f"unknown standalone runtime marker family: {unknown[:3]!r}")
    return {
        "layout_markers": EXPECTED_LAYOUT_MARKERS,
        "runtime_markers": EXPECTED_RUNTIME_MARKERS,
        "enter_events": len(unit_rows),
        "exit_events": sum(event[0] == "EXIT" for event in actual_boundaries),
        "exact_boundary_events": len(actual_boundaries),
        "maximum_boundary_depth": maximum_boundary_depth,
        "suppressed_variant_edges": len(actual_suppressed),
        "source_correction_rules": len({row[1] for row in correction_trace}),
        "source_correction_events": len(actual_corrections),
        "typography_rules": len({row[1] for row in EXPECTED_TYPOGRAPHY_TRACE}),
        "typography_events": len(actual_typography),
        "bidi_layout_rules": len({(row[0], row[1]) for row in EXPECTED_BIDI_LAYOUT_TRACE}),
        "bidi_layout_events": len(actual_bidi_layout),
    }


def validate_final_diagnostics(diagnostics: Mapping[str, object], label: str) -> None:
    require(
        set(diagnostics)
        == {"fatal", "duplicate", "unresolved", "bibliography_warning", "rerun"},
        f"{label} diagnostic categories changed",
    )
    require(all(diagnostics[key] == [] for key in diagnostics), f"{label} diagnostics are not all zero")


def warning_inventory(log_text: str, label: str) -> dict[str, object]:
    """Inventory residual warnings without treating their count as adjudication."""

    counts = {
        "formal_tex_warning_starts": len(
            re.findall(
                r"(?m)^(?:LaTeX(?: Font)?|Package [^\r\n]+|Class [^\r\n]+) Warning:",
                log_text,
            )
        ),
        "plain_latex_warning_starts": len(re.findall(r"(?m)^LaTeX Warning:", log_text)),
        "latex_font_warning_starts": len(re.findall(r"(?m)^LaTeX Font Warning:", log_text)),
        "package_warning_starts": len(re.findall(r"(?m)^Package [^\r\n]+ Warning:", log_text)),
        "class_warning_starts": len(re.findall(r"(?m)^Class [^\r\n]+ Warning:", log_text)),
        "overfull_hbox": len(re.findall(r"(?m)^Overfull \\hbox", log_text)),
        "overfull_vbox": len(re.findall(r"(?m)^Overfull \\vbox", log_text)),
        "underfull_hbox": len(re.findall(r"(?m)^Underfull \\hbox", log_text)),
        "underfull_vbox": len(re.findall(r"(?m)^Underfull \\vbox", log_text)),
    }
    return {
        "counts": counts,
        "bound_to_final_log": True,
        "semantic_or_visual_adjudication_passed": False,
        "note": (
            "Counts are an exact inventory, not a finding that warnings or box "
            "diagnostics are harmless; complete rendered-page QA remains separate."
        ),
    }


def validate_tex_output_summary(
    log_text: str, *, pdf_bytes: int, label: str,
) -> dict[str, int]:
    matches = re.findall(
        rf"(?m)^Output written on {re.escape(JOB)}\.pdf \((\d+) pages?, (\d+) bytes\)\.$",
        log_text,
    )
    require(len(matches) == 1, f"{label} final log lacks one exact PDF output summary")
    pages, reported_bytes = (int(value) for value in matches[0])
    require(pages > 1_000, f"{label} reported page count is implausibly small")
    require(reported_bytes == pdf_bytes, f"{label} final log PDF byte count changed")
    return {"pages": pages, "bytes": reported_bytes}


def validate_build(
    build_raw: object,
    *,
    name: str,
    run_root: Path,
    inventory: Mapping[str, object],
    limits: Mapping[str, object],
) -> dict[str, object]:
    build = as_mapping(build_raw, f"{name} build")
    require_exact_keys(
        build,
        {
            "name", "directory", "accepted", "effective_deterministic_environment",
            "passes", "pdf", "fls", "output_inventory",
        },
        f"{name} build",
    )
    require(build.get("name") == name, f"{name} build name changed")
    directory = (run_root / name).resolve()
    require(same_path(str(build.get("directory", "")), directory), f"{name} directory mismatch")
    require(directory.is_dir() and not directory.is_symlink(), f"{name} directory is missing or linked")
    require(build.get("accepted") is True, f"{name} build is not converged/accepted")
    environment = as_mapping(
        build.get("effective_deterministic_environment"),
        f"{name} effective environment",
    )
    expected_environment = {
        **EXPECTED_ENVIRONMENT,
        "TEXINPUTS": f"{directory};{LOCALE};",
        "BIBINPUTS": f"{LOCALE};{SOURCE / 'bib'};",
        "BSTINPUTS": f"{LOCALE};{SOURCE / 'bib'};",
        "TEXMFOUTPUT": str(directory),
        "TEXMF_OUTPUT_DIRECTORY": str(directory),
    }
    require(dict(environment) == expected_environment, f"{name} effective environment changed")

    output_inventory = validate_captured_output_inventory(
        build.get("output_inventory"),
        directory,
        postbuild_only_files=POSTBUILD_ONLY_FILES[name],
    )
    passes = as_list(build.get("passes"), f"{name} passes")
    require(len(passes) == 4, f"{name} must contain the accepted four-pass convergence trace")
    pass_summaries: list[dict[str, object]] = []
    final_log: Path | None = None
    final_log_text = ""
    for number, raw_pass in enumerate(passes, 1):
        pass_record = as_mapping(raw_pass, f"{name} pass {number}")
        require_exact_keys(
            pass_record,
            {"pass", "log", "log_sha256", "diagnostics"},
            f"{name} pass {number}",
        )
        require(pass_record.get("pass") == number, f"{name} pass numbering changed")
        log = (directory / f"{name}-latex-{number:02d}.tex.log").resolve()
        require(same_path(str(pass_record.get("log", "")), log), f"{name} pass log path mismatch")
        log_snapshot = file_snapshot(log)
        require(
            log_snapshot.sha256 == str(pass_record.get("log_sha256", "")).lower(),
            f"{name} pass log hash mismatch",
        )
        try:
            log_text = log_snapshot.data.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ValidationError(f"{name} pass log is not strict UTF-8") from exc
        actual = parse_log_diagnostics(log_text)
        reported = as_mapping(pass_record.get("diagnostics"), f"{name} pass diagnostics")
        require(dict(reported) == actual, f"{name} pass diagnostics differ from preserved log")
        require(not actual["fatal"], f"{name} pass {number} has fatal diagnostics")
        require(not actual["duplicate"], f"{name} pass {number} has duplicate diagnostics")
        require(not actual["bibliography_warning"], f"{name} pass {number} has bibliography warnings")
        overlay_runtime = validate_overlay_pass_log(
            log_text,
            expects_toc_replay=number > 1,
            label=f"{name} pass {number}",
        )
        pass_summaries.append(
            {
                "diagnostics": {key: len(value) for key, value in actual.items()},
                "overlay_runtime": overlay_runtime,
            }
        )
        final_log = log
        final_log_text = log_text
    require(final_log is not None, f"{name} final log is unavailable")
    validate_final_diagnostics(
        as_mapping(passes[-1]["diagnostics"], f"{name} final diagnostics"),
        f"{name} final pass",
    )
    canonical_log = directory / f"{JOB}.log"
    require(
        read_file_bytes(canonical_log) == read_file_bytes(final_log),
        f"{name} canonical log differs from the accepted final-pass snapshot",
    )

    pdf = directory / f"{JOB}.pdf"
    pdf_record = as_mapping(build.get("pdf"), f"{name} PDF record")
    require_exact_keys(pdf_record, {"path", "bytes", "sha256"}, f"{name} PDF record")
    require(same_path(str(pdf_record.get("path", "")), pdf), f"{name} PDF path mismatch")
    pdf_snapshot = file_snapshot(pdf)
    require(pdf_snapshot.data[:5] == b"%PDF-", f"{name} output lacks a PDF header")
    require(pdf_record.get("bytes") == pdf_snapshot.size, f"{name} PDF byte count mismatch")
    require(str(pdf_record.get("sha256", "")).lower() == pdf_snapshot.sha256, f"{name} PDF hash mismatch")
    require(
        output_inventory.get(pdf.name) == (pdf_snapshot.size, pdf_snapshot.sha256),
        f"{name} PDF is not bound by output inventory",
    )

    fls = directory / f"{JOB}.fls"
    fls_record = as_mapping(build.get("fls"), f"{name} recorder record")
    require_exact_keys(fls_record, {"path", "sha256"}, f"{name} recorder record")
    require(same_path(str(fls_record.get("path", "")), fls), f"{name} recorder path mismatch")
    require(str(fls_record.get("sha256", "")).lower() == sha256_file(fls), f"{name} recorder hash mismatch")
    manifest = recorder_manifest(fls)
    validate_repo_recorder_input_freshness(set(manifest.inputs), inventory["rows"])
    source_inputs = {path for path in manifest.inputs if under(path, SOURCE)}
    require(800 <= len(manifest.inputs) <= 2_000, f"{name} recorder input count is outside the bounded full-reader range")
    require(722 <= len(source_inputs) <= inventory["files"], f"{name} recorder source-input count is implausible")
    internal_outputs = {path for path in manifest.outputs if under(path, directory)}
    external_outputs = sorted(
        (path for path in manifest.outputs if not under(path, directory)),
        key=lambda value: str(value).casefold(),
    )
    expected_internal_output_names = {
        f"{JOB}.{suffix}"
        for suffix in (
            "aux", "log", "olbidilayout", "olcorrections", "oltypography",
            "olunits", "out", "pcr", "pdf", "prb", "thm", "toc",
        )
    }
    require(
        {path.name for path in internal_outputs} == expected_internal_output_names,
        f"{name} recorder internal-output set changed",
    )
    require(len(external_outputs) == 1, f"{name} recorder external-output boundary changed")
    external = external_outputs[0]
    external_parts = [part.casefold() for part in external.parts]
    require(
        external.name.casefold() == "m_t_x_t_e_s_t.tmp"
        and external_parts[-4:-1] == ["appdata", "local", "miktex"],
        f"{name} recorder named an unexpected external output",
    )
    required_source_inputs = [
        DRIVER,
        LOCALE / "standalone/body.tex",
        LOCALE / "standalone/runtime-fixes.tex",
        LOCALE / "standalone/link-geometry.tex",
        LOCALE / "standalone/runtime.tex",
        GENERATED_LEDGER,
        LOCALE / "standalone/source-corrections.tex",
        LOCALE / "standalone/typography.tex",
        LOCALE / "standalone/bidi-layout.tex",
    ]
    require_recorder_inputs(set(manifest.inputs), required_source_inputs)
    output_summary = validate_tex_output_summary(
        final_log_text,
        pdf_bytes=pdf_snapshot.size,
        label=name,
    )

    return {
        "name": name,
        "directory": directory,
        "passes": len(passes),
        "pass_diagnostic_counts": pass_summaries,
        "final_log": final_log,
        "final_log_sha256": sha256_file(final_log),
        "final_log_text": final_log_text,
        "residual_warnings": warning_inventory(final_log_text, f"{name} final log"),
        "pdf": pdf,
        "pdf_bytes": pdf_snapshot.size,
        "pdf_sha256": pdf_snapshot.sha256,
        "output_summary": output_summary,
        "fls": fls,
        "fls_sha256": sha256_file(fls),
        "recorder_inputs": set(manifest.inputs),
        "recorder_outputs": set(manifest.outputs),
        "recorder_source_inputs": source_inputs,
        "recorder_summary": {
            "unique_inputs": len(manifest.inputs),
            "repo_source_inputs": len(source_inputs),
            "unique_outputs": len(manifest.outputs),
            "run_directory_outputs": len(internal_outputs),
            "external_outputs": [
                {
                    "basename": external.name,
                    "sanitized_location_class": "user-local/MiKTeX",
                    "receipted_build_artifact": False,
                }
            ],
        },
        "output_inventory": output_inventory,
        "postbuild_only_files_excluded_from_build_acceptance": POSTBUILD_ONLY_FILES[name],
    }


def require_bound_runtime_output(build: Mapping[str, object], path: Path) -> dict[str, object]:
    resolved = path.resolve()
    require(resolved in build["recorder_outputs"], f"runtime sidecar absent from recorder OUTPUT: {path.name}")
    snapshot = file_snapshot(resolved)
    require(
        build["output_inventory"].get(path.name) == (snapshot.size, snapshot.sha256),
        f"runtime sidecar absent or changed in output inventory: {path.name}",
    )
    return {
        "path": relative_repo_path(resolved),
        "bytes": snapshot.size,
        "sha256": snapshot.sha256,
    }


def normalized_recorder_paths(paths: set[Path], build_directory: Path) -> set[str]:
    normalized: set[str] = set()
    for path in paths:
        if under(path, build_directory):
            value = "<build-output>/" + path.resolve().relative_to(build_directory.resolve()).as_posix()
        else:
            value = os.path.normcase(str(path.resolve()))
        normalized.add(value)
    return normalized


def validate_lukasiewicz_toc(text: str) -> dict[str, object]:
    """Require the two public whole-surname renderers and replay markers."""

    text = text.lstrip("\ufeff")
    marker_token = r"\OLSABidiLayoutTOCReplay"
    public_name_token = r"\OLSABidiLayoutLukasiewiczName"
    marker_pattern = re.compile(
        re.escape(marker_token) + r"\s*\{\s*(OLP-\d{4})\s*\}"
    )
    public_pattern = re.compile(re.escape(public_name_token) + r"(?![A-Za-z@])")
    marker_matches = list(marker_pattern.finditer(text))
    public_matches = list(public_pattern.finditer(text))
    require(
        text.count(marker_token) == len(marker_matches) == 2,
        "TOC replay markers are missing, duplicated, or malformed",
    )
    require(
        [match.group(1) for match in marker_matches] == ["OLP-0394", "OLP-0400"],
        "TOC replay marker identities or order changed",
    )
    require(
        text.count(public_name_token) == len(public_matches) == 2,
        "TOC public whole-surname renderer count changed",
    )
    require(
        public_matches[0].start() < marker_matches[0].start()
        < public_matches[1].start() < marker_matches[1].start(),
        "TOC whole-surname renderers and replay markers are not interleaved in source order",
    )
    forbidden = {
        "raw_source_surname": r"\L ukasiewicz",
        "legacy_glyph_renderer": r"\OLPolishUpperL",
        "expanded_ltr_payload": r"\olFaLTR",
        "literal_expanded_surname": "Łukasiewicz",
        "private_helper": r"\olsa_bidi_layout_",
        "recording_command": r"\OLSABidiLayoutRecord",
    }
    leaked = [label for label, token in forbidden.items() if token in text]
    require(not leaked, f"TOC contains non-public or expanded surname machinery: {leaked!r}")
    return {
        "public_whole_surname_renderers": 2,
        "replay_markers": ["OLP-0394", "OLP-0400"],
        "renderer_marker_order": "renderer-0394,marker-0394,renderer-0400,marker-0400",
        "raw_legacy_expanded_private_or_recording_tokens": 0,
    }


def validate_sidecars(
    build: Mapping[str, object],
    *,
    ledger: Mapping[str, object],
    expected_unit_lines: Sequence[str],
    expected_boundaries: Sequence[tuple[str, str, str]],
) -> dict[str, object]:
    directory = Path(build["directory"])
    units = directory / f"{JOB}.olunits"
    corrections = directory / f"{JOB}.olcorrections"
    typography = directory / f"{JOB}.oltypography"
    bidi_layout = directory / f"{JOB}.olbidilayout"
    toc = directory / f"{JOB}.toc"
    unit_rows = validate_unit_trace(read_file_text(units), expected_unit_lines)
    correction_rows = parse_pipe_trace(
        read_file_text(corrections),
        header="source_id|environment|finding_id|occurrence",
        expected=EXPECTED_CORRECTION_TRACE,
        columns=4,
        label="olcorrections",
    )
    typography_rows = parse_pipe_trace(
        read_file_text(typography),
        header="source_id|rule|occurrence",
        expected=EXPECTED_TYPOGRAPHY_TRACE,
        columns=3,
        label="oltypography",
    )
    bidi_layout_rows = parse_pipe_trace(
        read_file_text(bidi_layout),
        header="source_id|event|occurrence",
        expected=EXPECTED_BIDI_LAYOUT_TRACE,
        columns=3,
        label="olbidilayout",
    )
    toc_semantics = validate_lukasiewicz_toc(read_file_text(toc))
    runtime = validate_runtime_log(
        str(build["final_log_text"]),
        unit_rows=unit_rows,
        expected_boundaries=expected_boundaries,
        ledger=ledger,
    )
    return {
        "units": {
            **require_bound_runtime_output(build, units),
            "unique_source_units": len({row[0] for row in unit_rows}),
            "ordered_context_occurrences": len(unit_rows),
        },
        "source_corrections": {
            **require_bound_runtime_output(build, corrections),
            "rules": len({row[2] for row in correction_rows}),
            "events": len(correction_rows),
        },
        "typography": {
            **require_bound_runtime_output(build, typography),
            "rules": len({row[1] for row in typography_rows}),
            "events": len(typography_rows),
        },
        "bidi_layout": {
            **require_bound_runtime_output(build, bidi_layout),
            "rules": len({(row[0], row[1]) for row in bidi_layout_rows}),
            "events": len(bidi_layout_rows),
        },
        "toc_lukasiewicz": {
            **require_bound_runtime_output(build, toc),
            **toc_semantics,
        },
        "runtime_log": runtime,
    }


def require_equal_pdf_identity(
    left: tuple[int, str], right: tuple[int, str],
) -> None:
    require(left == right, "primary and replay PDF byte/hash identities differ")


def require_equal_stable_artifact(left: bytes, right: bytes, suffix: str) -> None:
    require(left == right, f"primary/replay {suffix} bytes differ")


def validate_pdf(
    primary: Path,
    replay: Path,
    *,
    log_reported_pages: int,
    expected_sha256: str | None,
    expected_bytes: int | None,
    expected_pages: int | None,
) -> dict[str, object]:
    primary_snapshot = file_snapshot(primary)
    replay_snapshot = file_snapshot(replay)
    require_equal_pdf_identity(
        (primary_snapshot.size, primary_snapshot.sha256),
        (replay_snapshot.size, replay_snapshot.sha256),
    )
    require(primary_snapshot.data == replay_snapshot.data, "primary/replay PDFs are not byte-identical")
    if expected_bytes is not None:
        require(primary_snapshot.size == expected_bytes, "accepted PDF byte count differs from the caller pin")
    if expected_sha256 is not None:
        require(primary_snapshot.sha256 == expected_sha256, "accepted PDF hash differs from the caller pin")
    try:
        import fitz
    except ImportError as exc:
        raise ValidationError("PyMuPDF is required for full-reader extraction QA") from exc
    require(
        getattr(fitz, "VersionBind", None) == PYMUPDF_VERSION,
        f"unreviewed PyMuPDF version: {getattr(fitz, 'VersionBind', None)!r}",
    )
    try:
        document = fitz.open(stream=primary_snapshot.data, filetype="pdf")
    except Exception as exc:
        raise ValidationError(f"cannot parse accepted PDF: {exc}") from exc
    try:
        require(document.is_pdf, "accepted artifact is not a PDF")
        require(not document.is_encrypted, "accepted PDF is encrypted")
        require(document.page_count == log_reported_pages, "PDF page count differs from both final-log summaries")
        if expected_pages is not None:
            require(document.page_count == expected_pages, "accepted PDF page count differs from the caller pin")
        metadata = dict(document.metadata)
        require(metadata == EXPECTED_METADATA, "accepted PDF metadata changed or is incomplete")
        total_characters = 0
        arabic_script_characters = 0
        minimum_page_characters: int | None = None
        maximum_page_characters = 0
        replacement_pages: list[int] = []
        empty_pages: list[int] = []
        c0_counts: dict[str, int] = {}
        c0_pages: dict[str, set[int]] = {}
        c0_fonts: set[str] = set()
        for index, page in enumerate(document, 1):
            rectangle = tuple(float(value) for value in page.rect)
            require(
                rectangle == (0.0, 0.0, 612.0, 792.0) and page.rotation == 0,
                f"PDF page {index} is not unrotated US Letter geometry",
            )
            text = page.get_text("text")
            if not text.strip():
                empty_pages.append(index)
            if "\ufffd" in text:
                replacement_pages.append(index)
            page_c0 = {
                character
                for character in text
                if ord(character) < 32 and character not in "\t\n\r"
            }
            for character in text:
                if character not in page_c0:
                    continue
                codepoint = f"U+{ord(character):04X}"
                c0_counts[codepoint] = c0_counts.get(codepoint, 0) + 1
                c0_pages.setdefault(codepoint, set()).add(index)
            if page_c0:
                page_dictionary = page.get_text("dict", flags=fitz.TEXTFLAGS_TEXT)
                for block in page_dictionary.get("blocks", []):
                    for line in block.get("lines", []):
                        for span in line.get("spans", []):
                            if any(character in page_c0 for character in span.get("text", "")):
                                font = span.get("font")
                                require(isinstance(font, str) and font, f"C0 span on page {index} lacks a font")
                                c0_fonts.add(font)
            length = len(text)
            total_characters += length
            arabic_script_characters += sum(
                "\u0600" <= character <= "\u06ff" or "\u0750" <= character <= "\u077f"
                for character in text
            )
            minimum_page_characters = (
                length if minimum_page_characters is None else min(minimum_page_characters, length)
            )
            maximum_page_characters = max(maximum_page_characters, length)
        require(not empty_pages, f"PDF text extraction is empty on pages: {empty_pages[:20]}")
        require(not replacement_pages, f"PDF text extraction contains replacement glyphs on pages: {replacement_pages[:20]}")
        require(total_characters > 1_000_000, "full-reader extracted text volume is implausibly small")
        require(arabic_script_characters > 100_000, "full-reader Persian-script extraction is implausibly small")
        normalized_c0_pages = {key: sorted(value) for key, value in sorted(c0_pages.items())}
        require(c0_counts == EXPECTED_C0_CONTROL_COUNTS, "accepted PDF C0 extraction inventory changed")
        require(sorted(c0_fonts) == EXPECTED_C0_CONTROL_FONTS, "accepted PDF C0 extraction fonts changed")
        return {
            "parser": {"name": "PyMuPDF", "version": PYMUPDF_VERSION},
            "pages": document.page_count,
            "page_geometry_points": [0.0, 0.0, 612.0, 792.0],
            "rotated_pages": 0,
            "encrypted": False,
            "metadata": metadata,
            "text_extraction": {
                "pages_attempted": document.page_count,
                "pages_with_nonempty_text": document.page_count,
                "empty_pages": 0,
                "replacement_character_pages": 0,
                "total_extracted_characters": total_characters,
                "arabic_script_characters": arabic_script_characters,
                "minimum_page_characters": minimum_page_characters,
                "maximum_page_characters": maximum_page_characters,
                "c0_control_characters": {
                    "status": "KNOWN_MATH_FONT_TOUNICODE_LIMITATION_NOT_CLEAN_SEARCHABLE_TEXT",
                    "counts": c0_counts,
                    "pages_by_codepoint": normalized_c0_pages,
                    "affected_pages": sorted({page for pages in c0_pages.values() for page in pages}),
                    "total_occurrences": sum(c0_counts.values()),
                    "fonts": sorted(c0_fonts),
                    "clean_text_extraction_passed": False,
                    "tagged_pdf_accessibility_or_math_copy_paste_passed": False,
                },
            },
        }
    finally:
        document.close()


def validate_events(
    receipt: Mapping[str, object],
    *,
    builds: Mapping[str, Mapping[str, object]],
    inventory: Mapping[str, object],
    started: datetime,
    finished: datetime,
) -> dict[str, object]:
    events = as_list(receipt.get("events"), "receipt events")
    require(len(events) == 39, "accepted transaction event count changed")
    parsed_events = [as_mapping(event, f"event {index}") for index, event in enumerate(events)]
    for index, event in enumerate(parsed_events):
        require_exact_keys(event, {"utc", "kind", "details"}, f"event {index}")
    event_times = [_utc(event["utc"], f"event {index} utc") for index, event in enumerate(parsed_events)]
    require(event_times == sorted(event_times), "receipt event timestamps are not monotonic")
    require(started <= event_times[0] <= event_times[-1] <= finished, "event times escape receipt interval")

    first = parsed_events[0]
    require(first["kind"] == "mutex_acquired", "first event is not mutex acquisition")
    first_details = as_mapping(first["details"], "mutex-acquired details")
    require_exact_keys(first_details, {"abandoned_recovery"}, "mutex-acquired details")
    require(
        first_details["abandoned_recovery"] == receipt["mutex"]["abandoned_recovery"],
        "mutex acquisition event differs from receipt",
    )

    labels: list[str] = []
    latex_records = {
        f"{name}-latex-{number:02d}": as_mapping(raw_pass, "pass record")
        for name, build in builds.items()
        for number, raw_pass in enumerate(as_list(receipt["builds"][0 if name == "primary" else 1]["passes"], "passes"), 1)
    }
    executable_records = [
        as_mapping(value, "executable identity")
        for value in as_list(receipt["executable_identities"], "executable identities")
    ]
    executables = {Path(str(row["path"])).name.casefold(): row for row in executable_records}
    index = 1
    peaks: list[int] = []
    while index < len(parsed_events) and parsed_events[index]["kind"] == "worker_start":
        require(index + 2 < len(parsed_events), "worker event triplet is truncated")
        start_event, exit_event, check_event = parsed_events[index : index + 3]
        require(exit_event["kind"] == "worker_tree_exit", "worker start is not followed by tree exit")
        start_details = as_mapping(start_event["details"], "worker-start details")
        exit_details = as_mapping(exit_event["details"], "worker-exit details")
        require_exact_keys(start_details, {"label", "executable", "arguments", "timeout_seconds"}, "worker-start details")
        require_exact_keys(exit_details, {"label", "result"}, "worker-exit details")
        label = start_details.get("label")
        require(isinstance(label, str), "worker label is missing")
        require(exit_details.get("label") == label, "worker start/exit labels differ")
        labels.append(label)
        timeout = start_details.get("timeout_seconds")
        require(is_json_integer(timeout) and 0 < timeout <= receipt["limits"]["per_worker_seconds"], "worker timeout invalid")
        result = as_mapping(exit_details.get("result"), "worker result")
        require_exact_keys(result, {"ProcessId", "ExitCode", "ElapsedSeconds", "PeakJobCommitBytes"}, "worker result")
        require(is_json_integer(result["ProcessId"]) and result["ProcessId"] > 0, "worker PID invalid")
        require(result["ExitCode"] == 0 and is_json_integer(result["ExitCode"]), "worker did not exit zero")
        require(_finite(result["ElapsedSeconds"]) and 0 <= result["ElapsedSeconds"] <= timeout, "worker elapsed time invalid")
        peak = result["PeakJobCommitBytes"]
        require(is_json_integer(peak) and 0 < peak <= MEMORY_LIMIT, "worker peak memory invalid")
        peaks.append(peak)

        if "-latex-" in label:
            require(check_event["kind"] == "immediate_log_check", "LuaLaTeX worker lacks immediate log check")
            check_details = as_mapping(check_event["details"], "LuaLaTeX log-check details")
            require_exact_keys(check_details, {"label", "diagnostics"}, "LuaLaTeX log-check details")
            require(check_details["label"] == label, "LuaLaTeX check label changed")
            require(label in latex_records, f"unexpected LuaLaTeX worker label: {label}")
            require(check_details["diagnostics"] == latex_records[label]["diagnostics"], "event/pass diagnostics differ")
            build_name = label.split("-", 1)[0]
            directory = Path(builds[build_name]["directory"])
            expected_arguments = [
                "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error",
                "-file-line-error", "-recorder", "-synctex=0", f"-jobname={JOB}",
                f"-output-directory={directory}", f"{JOB}.tex",
            ]
            require(start_details["arguments"] == expected_arguments, "LuaLaTeX argument vector changed")
            require(
                same_path(str(start_details["executable"]), str(executables["lualatex.exe"]["path"])),
                "LuaLaTeX executable differs from bound identity",
            )
        else:
            require("-bibtex-" in label, f"unknown worker type: {label}")
            require(check_event["kind"] == "immediate_bibliography_check", "BibTeX worker lacks immediate log check")
            check_details = as_mapping(check_event["details"], "BibTeX check details")
            require_exact_keys(check_details, {"label", "log", "diagnostics"}, "BibTeX check details")
            require(check_details["label"] == label, "BibTeX check label changed")
            build_name = label.split("-", 1)[0]
            directory = Path(builds[build_name]["directory"])
            bib_log = directory / f"{label}.blg"
            require(same_path(str(check_details["log"]), bib_log), "BibTeX log path changed")
            actual = parse_log_diagnostics(read_file_text(bib_log))
            require(check_details["diagnostics"] == actual, "BibTeX event diagnostics differ from log")
            validate_final_diagnostics(actual, label)
            require(start_details["arguments"] == [str(directory / JOB)], "BibTeX argument vector changed")
            require(
                same_path(str(start_details["executable"]), str(executables["bibtex.exe"]["path"])),
                "BibTeX executable differs from bound identity",
            )
        index += 3

    require(labels == EXPECTED_WORKER_LABELS, "worker sequence differs from accepted transaction")
    require(
        [event["kind"] for event in parsed_events[index:]]
        == ["deterministic_replay_match", "source_and_infrastructure_unchanged"],
        "accepted transaction terminal event sequence changed",
    )
    replay_event = as_mapping(parsed_events[index]["details"], "deterministic replay details")
    primary_pdf = receipt["builds"][0]["pdf"]
    require(dict(replay_event) == dict(primary_pdf), "replay-match event differs from primary PDF identity")
    source_event = as_mapping(parsed_events[index + 1]["details"], "source identity event")
    require_exact_keys(source_event, {"source_signature"}, "source identity event")
    require(source_event["source_signature"] == inventory["signature"], "post-build source signature event changed")
    require(max(peaks) == receipt["observed_peak_job_commit_bytes"], "receipt peak differs from worker peaks")
    return {
        "events": len(events),
        "worker_trees": len(labels),
        "worker_sequence": labels,
        "terminal_events": ["deterministic_replay_match", "source_and_infrastructure_unchanged"],
        "peak_job_commit_bytes": max(peaks),
    }


def validate_receipt(
    receipt_path: Path, *, expected_source_signature: str | None,
) -> dict[str, object]:
    receipt_path = validate_receipt_path(receipt_path)
    receipt = as_mapping(load_json(receipt_path), "Full build receipt")
    require_exact_keys(
        receipt,
        {
            "schema", "mode", "started_utc", "status", "accepted_build",
            "publication_or_visual_qa_passed", "run_root", "driver",
            "driver_sha256", "helper_sha256", "entrypoint_sha256",
            "derived_source_generator_sha256", "source_correction_checker_sha256",
            "preflight_executable_identity", "derived_source_preflight",
            "executable_identities", "limits", "deterministic_environment",
            "mutex", "events", "builds", "observed_peak_job_commit_bytes",
            "source_inventory", "finished_utc", "elapsed_guarded_seconds",
        },
        "successful Full receipt",
    )
    require(receipt["schema"] == RECEIPT_SCHEMA, "wrong build receipt schema")
    require(receipt["mode"] == "Full", "receipt is not a Full build")
    require(receipt["status"] == "BUILD_AND_REPLAY_PASS_NOT_PUBLICATION_QA", "Full build status is not accepted")
    require(receipt["accepted_build"] is True, "Full build is not accepted")
    require(receipt["publication_or_visual_qa_passed"] is False, "build receipt improperly claims visual/publication QA")
    run_root = receipt_path.parent.resolve()
    require(same_path(str(receipt["run_root"]), run_root), "receipt run root mismatch")
    require(same_path(str(receipt["driver"]), DRIVER), "receipt names the wrong driver")
    require(sha256_file(DRIVER) == PINNED_DRIVER_SHA256, "current driver identity changed")
    require(receipt["driver_sha256"] == PINNED_DRIVER_SHA256, "receipt driver identity changed")
    require(sha256_file(ENTRYPOINT) == PINNED_ENTRYPOINT_SHA256, "current guarded entrypoint identity changed")
    require(receipt["entrypoint_sha256"] == PINNED_ENTRYPOINT_SHA256, "receipt entrypoint identity changed")
    require(sha256_file(HELPER) == PINNED_HELPER_SHA256, "current process guard identity changed")
    require(receipt["helper_sha256"] == PINNED_HELPER_SHA256, "receipt process guard identity changed")
    require(
        sha256_file(DERIVED_SOURCE_GENERATOR) == PINNED_DERIVED_SOURCE_GENERATOR_SHA256,
        "current derived-source generator identity changed",
    )
    require(
        receipt["derived_source_generator_sha256"] == PINNED_DERIVED_SOURCE_GENERATOR_SHA256,
        "receipt derived-source generator identity changed",
    )
    require(SOURCE_CORRECTION_CHECKER.is_file(), "source-correction checker is missing")
    current_correction_checker_sha256 = sha256_file(SOURCE_CORRECTION_CHECKER)
    require(
        current_correction_checker_sha256 == PINNED_SOURCE_CORRECTION_CHECKER_SHA256,
        "current source-correction checker identity changed",
    )
    require(
        receipt["source_correction_checker_sha256"] == PINNED_SOURCE_CORRECTION_CHECKER_SHA256,
        "receipt source-correction checker identity changed",
    )

    preflight_executable = as_mapping(
        receipt["preflight_executable_identity"], "preflight executable identity",
    )
    require_exact_keys(preflight_executable, {"path", "sha256"}, "preflight executable identity")
    preflight_path = Path(str(preflight_executable["path"])).resolve()
    require(
        preflight_path.name.casefold() in {"python.exe", "python3.exe"}
        and preflight_path.is_file(),
        "derived-source preflight executable is missing or is not Python",
    )
    require(
        sha256_file(preflight_path) == preflight_executable["sha256"],
        "derived-source preflight Python identity changed",
    )
    derived_preflight = as_mapping(receipt["derived_source_preflight"], "derived-source preflight")
    require_exact_keys(
        derived_preflight,
        {"status", "output", "generator", "generator_sha256", "source_correction_checker_sha256"},
        "derived-source preflight",
    )
    require(derived_preflight["status"] == "PASS", "derived-source preflight did not pass")
    require(
        derived_preflight["output"] == EXPECTED_DERIVED_PREFLIGHT_OUTPUT,
        "derived-source preflight inventory changed",
    )
    require(
        same_path(str(derived_preflight["generator"]), DERIVED_SOURCE_GENERATOR),
        "derived-source preflight names the wrong generator",
    )
    require(
        derived_preflight["generator_sha256"] == PINNED_DERIVED_SOURCE_GENERATOR_SHA256,
        "derived-source preflight generator identity changed",
    )
    require(
        derived_preflight["source_correction_checker_sha256"] == current_correction_checker_sha256,
        "derived-source preflight checker identity differs from the transaction",
    )

    started = _utc(receipt["started_utc"], "started_utc")
    finished = _utc(receipt["finished_utc"], "finished_utc")
    require(finished >= started, "receipt finish precedes start")
    elapsed = receipt["elapsed_guarded_seconds"]
    require(_finite(elapsed) and elapsed > 0, "guarded elapsed time is invalid")

    mutex = as_mapping(receipt["mutex"], "mutex")
    require_exact_keys(mutex, {"name", "acquired", "abandoned_recovery", "released_after_confirmed_tree_exit"}, "mutex")
    require(mutex["name"] == MUTEX_NAME, "wrong machine-wide TeX mutex")
    require(mutex["acquired"] is True, "TeX mutex was not acquired")
    require(mutex["abandoned_recovery"] is False, "accepted run unexpectedly recovered an abandoned mutex")
    require(mutex["released_after_confirmed_tree_exit"] is True, "mutex release lacks confirmed worker-tree exit")

    limits = as_mapping(receipt["limits"], "limits")
    require_exact_keys(
        limits,
        {
            "mutex_acquisition_seconds", "per_worker_seconds", "complete_session_seconds",
            "maximum_latex_passes_per_build", "maximum_bibtex_passes_per_build",
            "job_commit_memory_bytes", "active_processes_in_owned_tree",
            "cleanup_deadline_seconds", "unconfirmed_exit_policy", "memory_semantics",
        },
        "limits",
    )
    require(limits["job_commit_memory_bytes"] == MEMORY_LIMIT, "wrong 2 GiB worker-tree cap")
    require(limits["maximum_latex_passes_per_build"] == 6, "LuaLaTeX pass cap changed")
    require(limits["maximum_bibtex_passes_per_build"] == 2, "BibTeX pass cap changed")
    require(limits["active_processes_in_owned_tree"] == 16, "owned process cap changed")
    require(limits["cleanup_deadline_seconds"] == 60, "cleanup deadline changed")
    require(
        limits["unconfirmed_exit_policy"]
        == "Retain host/job/mutex and observe same handles with 5-to-30-second backoff; never timeout-release",
        "unconfirmed-exit policy changed",
    )
    require(
        limits["memory_semantics"]
        == "Windows Job Object aggregate committed memory; NOT working set or GPU memory",
        "memory semantics changed",
    )
    require(elapsed <= limits["complete_session_seconds"], "accepted run exceeded session time cap")
    require(dict(as_mapping(receipt["deterministic_environment"], "deterministic environment")) == EXPECTED_ENVIRONMENT, "deterministic environment changed")

    executables = as_list(receipt["executable_identities"], "executable identities")
    require(len(executables) == 2, "Full build must bind LuaLaTeX and BibTeX")
    expected_names = ["lualatex.exe", "bibtex.exe"]
    for raw, expected_name in zip(executables, expected_names, strict=True):
        record = as_mapping(raw, f"{expected_name} identity")
        require_exact_keys(record, {"path", "sha256"}, f"{expected_name} identity")
        executable = Path(str(record["path"])).resolve()
        require(executable.name.casefold() == expected_name, f"unexpected executable: {executable.name}")
        require(executable.is_file(), f"bound executable is missing: {expected_name}")
        require(sha256_file(executable) == record["sha256"], f"bound executable hash changed: {expected_name}")

    inventory = _validate_inventory(receipt, run_root)
    require(722 <= inventory["files"] <= 1_000, "captured source inventory is outside the bounded reader range")
    if expected_source_signature is not None:
        require(
            inventory["signature"] == expected_source_signature,
            "captured source signature differs from the caller pin",
        )
    current_inventory = current_source_inventory()
    require(current_inventory == inventory["rows"], "current complete source tree differs from build-start inventory")
    require(inventory_signature(current_inventory) == inventory["signature"], "current source signature differs from receipt")

    builds_raw = as_list(receipt["builds"], "builds")
    require(len(builds_raw) == 2, "Full receipt must contain primary and replay builds")
    primary = validate_build(builds_raw[0], name="primary", run_root=run_root, inventory=inventory, limits=limits)
    replay = validate_build(builds_raw[1], name="replay", run_root=run_root, inventory=inventory, limits=limits)
    require(
        primary["output_summary"] == replay["output_summary"],
        "primary/replay final-log PDF summaries differ",
    )
    require(
        primary["residual_warnings"]["counts"] == replay["residual_warnings"]["counts"],
        "primary/replay residual warning inventories differ",
    )
    build_map = {"primary": primary, "replay": replay}
    events = validate_events(
        receipt,
        builds=build_map,
        inventory=inventory,
        started=started,
        finished=finished,
    )
    return {
        "receipt": receipt,
        "receipt_path": receipt_path,
        "receipt_sha256": sha256_file(receipt_path),
        "run_root": run_root,
        "inventory": inventory,
        "current_inventory": current_inventory,
        "builds": build_map,
        "events": events,
        "elapsed_guarded_seconds": elapsed,
        "peak_job_commit_bytes": receipt["observed_peak_job_commit_bytes"],
    }


def run_mutation_controls(
    *,
    expected_unit_lines: Sequence[str],
    expected_boundaries: Sequence[tuple[str, str, str]],
    inventory_rows: Sequence[tuple[str, int, str]],
) -> list[str]:
    controls: list[str] = []
    valid_units = "\n".join(expected_unit_lines) + "\n"
    expect_validation_error(validate_unit_trace, "\n".join(expected_unit_lines[:-1]) + "\n", expected_unit_lines)
    controls.append("missing_unit_occurrence_rejected")
    swapped = list(expected_unit_lines)
    swapped[1], swapped[2] = swapped[2], swapped[1]
    expect_validation_error(validate_unit_trace, "\n".join(swapped) + "\n", expected_unit_lines)
    controls.append("reordered_unit_occurrences_rejected")
    validate_unit_trace(valid_units, expected_unit_lines)

    mutated_boundaries = list(expected_boundaries)
    kind, _identifier, context = mutated_boundaries[-1]
    mutated_boundaries[-1] = (kind, "OLP-0001", context)
    expect_validation_error(
        lambda actual, expected: require(actual == expected, "boundary mismatch"),
        mutated_boundaries,
        expected_boundaries,
    )
    controls.append("mismatched_final_boundary_rejected")

    correction_text = "source_id|environment|finding_id|occurrence\n" + "\n".join(
        "|".join(row) for row in EXPECTED_CORRECTION_TRACE
    ) + "\n"
    expect_validation_error(
        parse_pipe_trace,
        correction_text + "|".join(EXPECTED_CORRECTION_TRACE[-1]) + "\n",
        header="source_id|environment|finding_id|occurrence",
        expected=EXPECTED_CORRECTION_TRACE,
        columns=4,
        label="mutated corrections",
    )
    controls.append("duplicate_correction_event_rejected")

    typography_text = "source_id|rule|occurrence\n" + "\n".join(
        "|".join(row) for row in EXPECTED_TYPOGRAPHY_TRACE
    ) + "\n"
    expect_validation_error(
        parse_pipe_trace,
        typography_text.replace("|2\n", "|3\n", 1),
        header="source_id|rule|occurrence",
        expected=EXPECTED_TYPOGRAPHY_TRACE,
        columns=3,
        label="mutated typography",
    )
    controls.append("wrong_typography_occurrence_rejected")

    bidi_text = "source_id|event|occurrence\n" + "\n".join(
        "|".join(row) for row in EXPECTED_BIDI_LAYOUT_TRACE
    ) + "\n"
    expect_validation_error(
        parse_pipe_trace,
        bidi_text.replace("source_id|event|occurrence", "source|event|count", 1),
        header="source_id|event|occurrence",
        expected=EXPECTED_BIDI_LAYOUT_TRACE,
        columns=3,
        label="mutated bidi layout",
    )
    controls.append("wrong_bidi_layout_header_rejected")

    bidi_log_lines = [
        "OL-STANDALONE-BIDI-LAYOUT|" + "|".join(row)
        for row in EXPECTED_BIDI_LAYOUT_TRACE
    ]
    bidi_log_lines[0], bidi_log_lines[1] = bidi_log_lines[1], bidi_log_lines[0]
    expect_validation_error(
        validate_runtime_event_trace,
        bidi_log_lines,
        marker="OL-STANDALONE-BIDI-LAYOUT",
        expected=EXPECTED_BIDI_LAYOUT_TRACE,
        label="mutated bidi layout",
    )
    controls.append("reordered_bidi_layout_log_events_rejected")

    bidi_coverage = EXPECTED_RUNTIME_MARKERS["bidi_layout_coverage"]
    expect_validation_error(
        require_exact_single_marker,
        [bidi_coverage, bidi_coverage],
        bidi_coverage,
        "mutated bidi-layout coverage",
    )
    controls.append("duplicate_bidi_layout_coverage_marker_rejected")

    expect_validation_error(
        require_exact_single_marker,
        [bidi_coverage, bidi_coverage + "0"],
        bidi_coverage,
        "mutated bidi-layout coverage",
    )
    controls.append("bidi_layout_coverage_prefix_collision_rejected")

    coverage_stem, separator, coverage_events = bidi_coverage.rpartition("|")
    require(separator == "|" and coverage_events.isdigit(), "invalid bidi-layout coverage contract")
    expect_validation_error(
        require_exact_single_marker,
        [coverage_stem + "|" + str(int(coverage_events) - 1)],
        bidi_coverage,
        "mutated bidi-layout coverage",
    )
    controls.append("wrong_bidi_layout_coverage_count_rejected")

    correction_log_rows = [
        "OL-STANDALONE-SOURCE-CORRECTION|" + "|".join((row[0], row[2], row[3]))
        for row in EXPECTED_CORRECTION_TRACE
    ]
    typography_log_rows = [
        "OL-STANDALONE-TYPOGRAPHY|" + "|".join(row)
        for row in EXPECTED_TYPOGRAPHY_TRACE
    ]
    bootstrap_bidi_log_rows = [
        "OL-STANDALONE-BIDI-LAYOUT|" + "|".join(row)
        for row in EXPECTED_BIDI_LAYOUT_BOOTSTRAP_TRACE
    ]
    valid_bootstrap_overlay_log = "\n".join(
        correction_log_rows
        + typography_log_rows
        + bootstrap_bidi_log_rows
        + [
            EXPECTED_RUNTIME_MARKERS["source_correction_coverage"],
            EXPECTED_RUNTIME_MARKERS["typography_coverage"],
            EXPECTED_BIDI_LAYOUT_BOOTSTRAP_COVERAGE,
            "",
        ]
    )
    validate_overlay_pass_log(
        valid_bootstrap_overlay_log,
        expects_toc_replay=False,
        label="synthetic bootstrap",
    )
    valid_final_overlay_log = "\n".join(
        correction_log_rows
        + typography_log_rows
        + [
            "OL-STANDALONE-BIDI-LAYOUT|" + "|".join(row)
            for row in EXPECTED_BIDI_LAYOUT_TRACE
        ]
        + [
            EXPECTED_RUNTIME_MARKERS["source_correction_coverage"],
            EXPECTED_RUNTIME_MARKERS["typography_coverage"],
            EXPECTED_RUNTIME_MARKERS["bidi_layout_coverage"],
            "",
        ]
    )
    validate_overlay_pass_log(
        valid_final_overlay_log,
        expects_toc_replay=True,
        label="synthetic final",
    )
    expect_validation_error(
        validate_overlay_pass_log,
        valid_bootstrap_overlay_log,
        expects_toc_replay=True,
        label="bootstrap presented as final",
    )
    controls.append("bootstrap_bidi_trace_rejected_as_final")

    valid_toc = "\n".join(
        [
            r"\contentsline {section}{منطق~\OLSABidiLayoutLukasiewiczName}{1}{section.1}%",
            r"\OLSABidiLayoutTOCReplay{OLP-0394}",
            r"\contentsline {section}{منطق~\OLSABidiLayoutLukasiewiczName}{2}{section.2}%",
            r"\OLSABidiLayoutTOCReplay{OLP-0400}",
            "",
        ]
    )
    validate_lukasiewicz_toc(valid_toc)
    toc_mutations = [
        (
            "missing_toc_whole_surname_renderer_rejected",
            valid_toc.replace(r"\OLSABidiLayoutLukasiewiczName", "", 1),
        ),
        (
            "missing_toc_replay_marker_rejected",
            valid_toc.replace(r"\OLSABidiLayoutTOCReplay{OLP-0400}" + "\n", "", 1),
        ),
        (
            "duplicate_toc_replay_marker_rejected",
            valid_toc + r"\OLSABidiLayoutTOCReplay{OLP-0400}" + "\n",
        ),
        (
            "reversed_toc_replay_markers_rejected",
            valid_toc.replace("OLP-0394", "OLP-TEMP", 1)
            .replace("OLP-0400", "OLP-0394", 1)
            .replace("OLP-TEMP", "OLP-0400", 1),
        ),
        (
            "toc_renderers_before_both_markers_rejected",
            "\n".join(
                [
                    r"\contentsline {section}{منطق~\OLSABidiLayoutLukasiewiczName}{1}{section.1}%",
                    r"\contentsline {section}{منطق~\OLSABidiLayoutLukasiewiczName}{2}{section.2}%",
                    r"\OLSABidiLayoutTOCReplay{OLP-0394}",
                    r"\OLSABidiLayoutTOCReplay{OLP-0400}",
                    "",
                ]
            ),
        ),
        (
            "unknown_toc_replay_marker_rejected",
            valid_toc.replace("OLP-0400", "OLP-9999", 1),
        ),
        (
            "raw_toc_source_surname_rejected",
            valid_toc.replace(r"\OLSABidiLayoutLukasiewiczName", r"\L ukasiewicz", 1),
        ),
        (
            "legacy_toc_glyph_renderer_rejected",
            valid_toc.replace(
                r"\OLSABidiLayoutLukasiewiczName", r"\OLPolishUpperL ukasiewicz", 1,
            ),
        ),
        (
            "expanded_toc_ltr_payload_rejected",
            valid_toc.replace(
                r"\OLSABidiLayoutLukasiewiczName", r"\olFaLTR{Łukasiewicz}", 1,
            ),
        ),
        (
            "private_toc_helper_rejected",
            valid_toc + r"\olsa_bidi_layout_private:" + "\n",
        ),
        (
            "toc_recording_command_rejected",
            valid_toc + r"\OLSABidiLayoutRecord{setup}" + "\n",
        ),
    ]
    for control, mutated_toc in toc_mutations:
        expect_validation_error(validate_lukasiewicz_toc, mutated_toc)
        controls.append(control)

    marker_lines = [EXPECTED_RUNTIME_MARKERS["bang"], EXPECTED_RUNTIME_MARKERS["bang"]]
    expect_validation_error(
        require_exact_single_marker,
        marker_lines,
        EXPECTED_RUNTIME_MARKERS["bang"],
        "mutated runtime",
    )
    controls.append("duplicate_runtime_marker_rejected")

    diagnostics = {key: [] for key in ("fatal", "duplicate", "unresolved", "bibliography_warning", "rerun")}
    diagnostics["unresolved"] = [{"line": 1, "text": "Reference X undefined"}]
    expect_validation_error(validate_final_diagnostics, diagnostics, "mutated final pass")
    controls.append("nonzero_final_diagnostics_rejected")

    expect_validation_error(require_equal_pdf_identity, (10, "a" * 64), (10, "b" * 64))
    controls.append("primary_replay_pdf_hash_mismatch_rejected")

    expect_validation_error(
        require_equal_stable_artifact,
        b"source_id|event|occurrence\nOLP-0371|setup|1\n",
        b"source_id|event|occurrence\nOLP-0371|setup|2\n",
        "olbidilayout",
    )
    controls.append("bidi_layout_replay_mismatch_rejected")

    changed_inventory = list(inventory_rows)
    first_path, first_size, first_hash = changed_inventory[0]
    changed_inventory[0] = (first_path, first_size + 1, first_hash)
    expect_validation_error(
        lambda rows, expected: require(inventory_signature(rows) == expected, "inventory signature mismatch"),
        changed_inventory,
        inventory_signature(inventory_rows),
    )
    controls.append("source_inventory_mutation_rejected")

    metadata = dict(EXPECTED_METADATA)
    metadata.pop("title")
    expect_validation_error(
        lambda actual: require(actual == EXPECTED_METADATA, "metadata mismatch"),
        metadata,
    )
    controls.append("missing_pdf_metadata_rejected")
    require(len(controls) == 28, "mutation-control inventory changed")
    return controls


def sha256_argument(value: str) -> str:
    normalized = value.lower()
    if re.fullmatch(r"[0-9a-f]{64}", normalized) is None:
        raise argparse.ArgumentTypeError("expected exactly 64 hexadecimal SHA-256 characters")
    return normalized


def positive_integer_argument(value: str) -> int:
    try:
        parsed = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("expected a positive integer") from exc
    if parsed <= 0:
        raise argparse.ArgumentTypeError("expected a positive integer")
    return parsed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--receipt",
        type=Path,
        required=True,
        help="accepted Full BUILD_RECEIPT.json beneath tmp/pdfs/standalone",
    )
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--expected-pdf-sha256", type=sha256_argument)
    parser.add_argument("--expected-pdf-bytes", type=positive_integer_argument)
    parser.add_argument("--expected-page-count", type=positive_integer_argument)
    parser.add_argument("--expected-source-signature", type=sha256_argument)
    args = parser.parse_args()
    clear_snapshot_cache()
    try:
        common = validate_receipt(
            args.receipt,
            expected_source_signature=args.expected_source_signature,
        )
        ledger, expected_unit_lines = validate_ledger(common["inventory"]["rows"])
        expected_boundaries = expected_boundary_events(ledger)
        expected_unit_rows = [tuple(line.split("|")) for line in expected_unit_lines[1:]]
        context_counts = {
            "FOL": sum(row[3] == "FOL" for row in expected_unit_rows),
            "PL": sum(row[3] == "PL" for row in expected_unit_rows),
        }
        namespace_counts = {
            namespace: sum(row[2] == namespace for row in expected_unit_rows)
            for namespace in sorted({row[2] for row in expected_unit_rows})
        }
        require(context_counts == {"FOL": 720, "PL": 54}, "FOL/PL occurrence counts changed")
        require(
            namespace_counts
            == {
                "canonical": 769,
                "retained:OLP-0643": 1,
                "variant:OLP-0646": 1,
                "variant:OLP-0719": 1,
                "variant:OLP-0720": 1,
                "variant:OLP-0722": 1,
            },
            "runtime namespace inventory changed",
        )

        sidecars = {
            name: validate_sidecars(
                build,
                ledger=ledger,
                expected_unit_lines=expected_unit_lines,
                expected_boundaries=expected_boundaries,
            )
            for name, build in common["builds"].items()
        }
        stable_replay_artifacts: dict[str, dict[str, object]] = {}
        for suffix in STABLE_REPLAY_SUFFIXES:
            primary_path = Path(common["builds"]["primary"]["directory"]) / f"{JOB}.{suffix}"
            replay_path = Path(common["builds"]["replay"]["directory"]) / f"{JOB}.{suffix}"
            require_equal_stable_artifact(
                read_file_bytes(primary_path), read_file_bytes(replay_path), suffix,
            )
            snapshot = file_snapshot(primary_path)
            stable_replay_artifacts[suffix] = {
                "bytes": snapshot.size,
                "sha256": snapshot.sha256,
            }

        require(
            normalized_recorder_paths(
                common["builds"]["primary"]["recorder_inputs"],
                Path(common["builds"]["primary"]["directory"]),
            )
            == normalized_recorder_paths(
                common["builds"]["replay"]["recorder_inputs"],
                Path(common["builds"]["replay"]["directory"]),
            ),
            "primary/replay normalized recorder INPUT sets differ",
        )

        # Eighteen frozen localized units are deliberately replaced at TeX input
        # time by hash-bound, generator-produced physical overlays.  Requiring
        # the frozen path itself in the recorder for those units is impossible:
        # the recorder correctly records the derived file that TeX actually
        # consumed.  Validate the complete source->derived map and both byte
        # identities, then substitute only those exact recorder targets.
        derived_manifest = as_mapping(load_json(DERIVED_SOURCE_MANIFEST), "derived-source manifest")
        derived_rows = as_list(derived_manifest.get("files"), "derived-source manifest files")
        require(len(derived_rows) == 18, "derived-source manifest must contain exactly 18 files")
        derived_by_source: dict[str, Path] = {}
        for raw_row in derived_rows:
            row = as_mapping(raw_row, "derived-source manifest row")
            source_rel = str(row.get("source_path"))
            derived_rel = str(row.get("derived_path"))
            require(source_rel not in derived_by_source, f"duplicate derived-source mapping: {source_rel}")
            source_path = ROOT / source_rel
            derived_path = ROOT / derived_rel
            require(source_path.is_file(), f"derived-source frozen input missing: {source_rel}")
            require(derived_path.is_file(), f"derived-source physical input missing: {derived_rel}")
            require(sha256_file(source_path) == row.get("source_sha256"), f"derived-source frozen hash changed: {source_rel}")
            require(sha256_file(derived_path) == row.get("derived_sha256"), f"derived-source physical hash changed: {derived_rel}")
            derived_by_source[source_rel] = derived_path

        source_targets = []
        for ledger_row in ledger["rows"]:
            source_path = LOCALE / str(ledger_row["source_path"])
            source_rel = relative_repo_path(source_path)
            source_targets.append(derived_by_source.get(source_rel, source_path))
        require(len(source_targets) == 722, "recorder target projection must retain all 722 units")
        require(len(set(path.resolve() for path in source_targets)) == 722, "recorder target projection contains duplicates")
        for name, build in common["builds"].items():
            require_recorder_inputs(build["recorder_inputs"], source_targets)
            for runtime_name in (
                "olunits", "olcorrections", "oltypography", "olbidilayout", "pdf",
            ):
                output = Path(build["directory"]) / f"{JOB}.{runtime_name}"
                require(output.resolve() in build["recorder_outputs"], f"{name} recorder lacks OUTPUT {output.name}")

        pdf = validate_pdf(
            common["builds"]["primary"]["pdf"],
            common["builds"]["replay"]["pdf"],
            log_reported_pages=common["builds"]["primary"]["output_summary"]["pages"],
            expected_sha256=args.expected_pdf_sha256,
            expected_bytes=args.expected_pdf_bytes,
            expected_pages=args.expected_page_count,
        )
        controls = run_mutation_controls(
            expected_unit_lines=expected_unit_lines,
            expected_boundaries=expected_boundaries,
            inventory_rows=common["inventory"]["rows"],
        )
        output = validate_output_path(args.output)
        evidence: dict[str, object] = {
            "schema": "farsi-standalone-full-reader-postbuild-qa-v2",
            "status": "PASS_BUILD_AND_REPLAY_NOT_VISUAL_OR_PUBLICATION_QA",
            "scope": {
                "build_acceptance_passed": True,
                "current_full_reader_candidate_accepted": True,
                "source_and_runtime_trace_acceptance_passed": True,
                "pdf_parse_and_nonempty_text_extraction_available": True,
                "clean_searchable_text_extraction_passed": False,
                "tagged_pdf_accessibility_passed": False,
                "math_copy_paste_fidelity_passed": False,
                "rendered_page_visual_qa_passed": False,
                "link_annotation_geometry_qa_passed": False,
                "publication_packaging_qa_passed": False,
                "public_byte_readback_passed": False,
                "tex_run_by_this_validator": False,
                "source_edits_by_this_validator": False,
            },
            "guarded_run": {
                "receipt": {
                    "path": relative_repo_path(common["receipt_path"]),
                    "bytes": file_snapshot(common["receipt_path"]).size,
                    "sha256": common["receipt_sha256"],
                },
                "mode": "Full",
                "status": "BUILD_AND_REPLAY_PASS_NOT_PUBLICATION_QA",
                "accepted_build": True,
                "publication_or_visual_qa_passed": False,
                "elapsed_guarded_seconds": common["elapsed_guarded_seconds"],
                "peak_job_commit_bytes": common["peak_job_commit_bytes"],
                "mutex": MUTEX_NAME,
                "mutex_released_after_confirmed_tree_exit": True,
                "events": common["events"],
            },
            "source_inventory": {
                key: common["inventory"][key]
                for key in ("path", "sha256", "files", "signature")
            },
            "source_inventory_current_complete_match": True,
            "optional_caller_pins": {
                "source_signature": args.expected_source_signature,
                "pdf_sha256": args.expected_pdf_sha256,
                "pdf_bytes": args.expected_pdf_bytes,
                "page_count": args.expected_page_count,
                "transaction_and_replay_binding_enforced_independently": True,
            },
            "integration": {
                "ledger": {
                    "path": relative_repo_path(INTEGRATION_LEDGER),
                    "bytes": file_snapshot(INTEGRATION_LEDGER).size,
                    "sha256": sha256_file(INTEGRATION_LEDGER),
                    "independently_reconstructed_exactly": True,
                },
                "generated_tex_ledger": {
                    "path": relative_repo_path(GENERATED_LEDGER),
                    "bytes": file_snapshot(GENERATED_LEDGER).size,
                    "sha256": sha256_file(GENERATED_LEDGER),
                    "independently_reconstructed_exactly": True,
                },
                "unique_source_units": 722,
                "primary_graph_units": 642,
                "retained_units": 80,
                "ordered_context_occurrences": 774,
                "context_occurrences": context_counts,
                "namespace_occurrences": namespace_counts,
                "repeated_context_units": 52,
                "entry_exit_boundary_events": len(expected_boundaries),
                "all_unit_source_bytes_match_build_inventory": True,
                "all_unit_sources_present_in_both_recorders": True,
            },
            "builds": {
                name: {
                    "passes": build["passes"],
                    "postbuild_only_files_excluded_from_build_acceptance": build[
                        "postbuild_only_files_excluded_from_build_acceptance"
                    ],
                    "pass_diagnostic_counts": build["pass_diagnostic_counts"],
                    "final_diagnostics_all_zero": True,
                    "residual_warnings": build["residual_warnings"],
                    "final_log_pdf_summary": build["output_summary"],
                    "final_log": {
                        "path": relative_repo_path(build["final_log"]),
                        "sha256": build["final_log_sha256"],
                    },
                    "recorder": {
                        "path": relative_repo_path(build["fls"]),
                        "sha256": build["fls_sha256"],
                        **build["recorder_summary"],
                    },
                    "pdf": {
                        "path": relative_repo_path(build["pdf"]),
                        "bytes": build["pdf_bytes"],
                        "sha256": build["pdf_sha256"],
                    },
                    "sidecars": sidecars[name],
                }
                for name, build in common["builds"].items()
            },
            "deterministic_replay": {
                "pdf_byte_identical": True,
                "pdf_bytes": common["builds"]["primary"]["pdf_bytes"],
                "pdf_sha256": common["builds"]["primary"]["pdf_sha256"],
                "stable_artifacts_byte_identical": stable_replay_artifacts,
                "normalized_recorder_input_sets_identical": True,
            },
            "pdf_parse_and_extraction": pdf,
            "mutation_controls": {
                "status": "PASS",
                "validator_controls": controls,
                "validator_negative_controls": len(controls),
                "ledger_negative_controls": 4,
                "total_negative_controls": len(controls) + 4,
            },
            "remaining_gates": [
                "complete rendered inspection of every accepted PDF page",
                "independent full-PDF link-annotation geometry and destination QA",
                "remediate the recorded Type-1 math-font C0/ToUnicode extraction defect or carry an explicit non-accessible-text limitation",
                "release-package inventory and license/provenance QA",
                "publication followed by anonymous byte/hash readback",
            ],
        }
        write_json(output, evidence)
        print(
            json.dumps(
                {
                    "status": evidence["status"],
                    "units": 722,
                    "context_occurrences": 774,
                    "boundary_events": len(expected_boundaries),
                    "source_correction_rules": len({row[2] for row in EXPECTED_CORRECTION_TRACE}),
                    "source_correction_events": len(EXPECTED_CORRECTION_TRACE),
                    "typography_rules": len({row[1] for row in EXPECTED_TYPOGRAPHY_TRACE}),
                    "typography_events": len(EXPECTED_TYPOGRAPHY_TRACE),
                    "bidi_layout_rules": len(
                        {(row[0], row[1]) for row in EXPECTED_BIDI_LAYOUT_TRACE}
                    ),
                    "bidi_layout_events": len(EXPECTED_BIDI_LAYOUT_TRACE),
                    "pages": pdf["pages"],
                    "pdf_sha256": common["builds"]["primary"]["pdf_sha256"],
                    "negative_controls": len(controls) + 4,
                    "output": relative_repo_path(output),
                },
                ensure_ascii=False,
            )
        )
    except (ValidationError, KeyError, IndexError, TypeError, ValueError, AssertionError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
