"""Generate or verify frozen-source-derived document-text correction inputs.

The standalone source-correction layer must not capture an entire TeX document
as one macro argument: doing so tokenizes deferred/verbatim-style environments
before their native catcodes are installed.  This tool instead applies the
already hash-pinned, exact substitutions to derived physical inputs.  Frozen
localized sources remain untouched.  TeX reads the derived files normally and
therefore preserves native input/catcode semantics.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CHECKER_PATH = HERE / "check_functions_source_corrections.py"
SPEC = importlib.util.spec_from_file_location("source_correction_checker", CHECKER_PATH)
assert SPEC and SPEC.loader
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)

ROOT = HERE.parent
DERIVED_ROOT = CHECKER.FA / "standalone/generated-source-corrections"
DERIVED_CONTENT = DERIVED_ROOT / "content"
MANIFEST = DERIVED_ROOT / "MANIFEST.json"
SELF = Path(__file__).resolve()
UTF8_BOM = b"\xef\xbb\xbf"


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_file(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def trace_block(unit: str, rules: list[str]) -> str:
    rows = "".join(
        f"\\OLSASourceCorrectionRecordDocumentText{{{unit}}}{{{rule}}}\n"
        for rule in rules
    )
    return (
        "% Standalone derived-source correction trace; generated, do not edit.\n"
        + rows
    )


def expected_tree() -> tuple[dict[Path, bytes], dict[str, object]]:
    overlay_text = CHECKER.OVERLAY.read_text(encoding="utf-8")
    declarations = CHECKER.document_text_declarations(overlay_text)
    expected_headers = [
        (unit, rule)
        for unit, _environment, rule, _relative
        in CHECKER.DOCUMENT_TEXT_EXPECTED_DECLARATIONS
    ]
    assert [(row["unit"], row["rule"]) for row in declarations] == expected_headers

    by_source: dict[Path, list[dict[str, str]]] = defaultdict(list)
    for row in declarations:
        unit, environment, relative = CHECKER.DOCUMENT_TEXT_EXPECTED[row["rule"]]
        assert environment == "document-text" and row["unit"] == unit
        by_source[CHECKER.CONTENT_ROOT / relative].append(row)

    outputs: dict[Path, bytes] = {}
    records: list[dict[str, object]] = []
    seen_units: set[str] = set()
    for source in sorted(by_source, key=lambda item: item.as_posix()):
        rows = by_source[source]
        unit = rows[0]["unit"]
        assert unit not in seen_units and all(row["unit"] == unit for row in rows)
        seen_units.add(unit)

        relative = source.relative_to(CHECKER.CONTENT_ROOT)
        identity = CHECKER.DOCUMENT_TEXT_SOURCE_IDENTITIES[relative.as_posix()]
        source_bytes = source.read_bytes()
        assert len(source_bytes) == identity["bytes"]
        assert sha_bytes(source_bytes) == identity["sha256"]
        has_bom = source_bytes.startswith(UTF8_BOM)
        source_text = source_bytes[len(UTF8_BOM):].decode("utf-8") if has_bom else source_bytes.decode("utf-8")
        corrected = source_text
        rule_records: list[dict[str, str]] = []
        for row in rows:
            assert corrected.count(row["original"]) == 1, row["rule"]
            corrected = corrected.replace(row["original"], row["replacement"], 1)
            rule_records.append({
                "finding_id": row["rule"],
                "original_sha256": CHECKER.text_sha(row["original"]),
                "replacement_sha256": CHECKER.text_sha(row["replacement"]),
            })

        terminal = r"\end{document}"
        assert corrected.count(terminal) == 1, source
        corrected = corrected.replace(
            terminal,
            trace_block(unit, [row["rule"] for row in rows]) + terminal,
            1,
        )
        derived_bytes = (UTF8_BOM if has_bom else b"") + corrected.encode("utf-8")
        output = DERIVED_CONTENT / relative
        outputs[output] = derived_bytes
        records.append({
            "source_id": unit,
            "source_path": source.relative_to(ROOT).as_posix(),
            "source_bytes": len(source_bytes),
            "source_sha256": sha_bytes(source_bytes),
            "derived_path": output.relative_to(ROOT).as_posix(),
            "derived_bytes": len(derived_bytes),
            "derived_sha256": sha_bytes(derived_bytes),
            "utf8_bom_preserved": has_bom,
            "rules": rule_records,
        })

    manifest: dict[str, object] = {
        "schema": "farsi-standalone-derived-source-corrections/1.0.0",
        "policy": "Frozen localized sources are untouched; exact hash-pinned substitutions are materialized before TeX tokenization.",
        "overlay_path": CHECKER.OVERLAY.relative_to(ROOT).as_posix(),
        "overlay_sha256": sha_file(CHECKER.OVERLAY),
        "checker_path": CHECKER_PATH.relative_to(ROOT).as_posix(),
        "checker_sha256": sha_file(CHECKER_PATH),
        "generator_path": SELF.relative_to(ROOT).as_posix(),
        "generator_sha256": sha_file(SELF),
        "source_files": len(records),
        "physical_correction_events": sum(len(row["rules"]) for row in records),
        "files": records,
    }
    return outputs, manifest


def manifest_bytes(manifest: dict[str, object]) -> bytes:
    return (
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def write_atomic(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".next")
    temporary.write_bytes(data)
    temporary.replace(path)


def write_expected(outputs: dict[Path, bytes], manifest: dict[str, object]) -> None:
    for path, data in outputs.items():
        write_atomic(path, data)
    write_atomic(MANIFEST, manifest_bytes(manifest))


def check_expected(outputs: dict[Path, bytes], manifest: dict[str, object]) -> None:
    assert MANIFEST.is_file(), f"missing derived-source manifest: {MANIFEST}"
    assert MANIFEST.read_bytes() == manifest_bytes(manifest), "stale derived-source manifest"
    expected_paths = set(outputs) | {MANIFEST}
    actual_paths = {path for path in DERIVED_ROOT.rglob("*") if path.is_file()}
    assert actual_paths == expected_paths, {
        "missing": sorted(str(path) for path in expected_paths - actual_paths),
        "unexpected": sorted(str(path) for path in actual_paths - expected_paths),
    }
    for path, data in outputs.items():
        assert path.read_bytes() == data, f"stale derived source: {path}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="atomically materialize the exact derived files and manifest",
    )
    args = parser.parse_args()
    outputs, manifest = expected_tree()
    if args.write:
        write_expected(outputs, manifest)
    check_expected(outputs, manifest)
    print(
        "PASS: "
        f"{manifest['source_files']} derived source files; "
        f"{manifest['physical_correction_events']} exact correction events; "
        "frozen sources untouched"
    )


if __name__ == "__main__":
    main()
