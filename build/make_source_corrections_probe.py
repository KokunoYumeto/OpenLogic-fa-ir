"""Generate the guarded combined OLFUN/OLSIZ source-correction probe.

This generator never launches TeX. It derives the diagnostic from the live
standalone preamble and refuses to replace differing reviewed artifacts unless
their exact current SHA-256 values are supplied.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
LOCALE = ROOT / "source/locale/fa-IR"
DRIVER = LOCALE / "open-logic-standalone-fa-IR.tex"
TARGET = LOCALE / "standalone-probe-source-corrections.tex"
RECEIPT = ROOT / "evidence/SOURCE_CORRECTIONS_PROBE_FIXTURE.json"
OVERLAY = LOCALE / "standalone/source-corrections.tex"
ERRATA = LOCALE / "standalone-errata.tex"
RUNTIME = LOCALE / "standalone/runtime.tex"
DOCUMENT_BOUNDARY = br"\begin{document}"

# These identities come from the accepted 2026-09-04 native diagnostic and
# complete 29-page visual inspection.  The old full driver changed later only
# after \begin{document}; the exact preamble and generated probe TeX did not.
HISTORICAL_FULL_DRIVER_IDENTITY = (
    13343,
    "F983E663C874FCEE8B2065E15FFCA1B3AB7C08174FA5EC970B7E96366E2C05D2",
)
ACCEPTED_PREAMBLE_IDENTITY = (
    8212,
    "C6E31F3488F61233B446D848D80C0CC04D319D99D6C77C1FA28ADDFC4907CE47",
)
ACCEPTED_PROBE_IDENTITY = (
    11387,
    "C5AFAFE6D39DF524E60FB34749022275C8B022F59B76ECFC2E86821D922388DD",
)
ACCEPTED_NATIVE_QA = ROOT / "evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_QA.json"
ACCEPTED_NATIVE_QA_IDENTITY = (
    54438,
    "6AFCAADC1C1997EF4A537B9ABA469C470F8CAF82322C36FCA729DADEC4D3D1CE",
)
ACCEPTED_VISUAL_QA = ROOT / "evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_VISUAL_QA.json"
ACCEPTED_VISUAL_QA_IDENTITY = (
    8048,
    "3A1F7E00DDCCBF4AE10FAAB58D86E019CA8AC129BFBDB96646A1295146A7800D",
)

UNITS = [
    ("OLP-0021", "content/sets-functions-relations/functions/function-basics.tex"),
    ("OLP-0023", "content/sets-functions-relations/functions/functions-relations.tex"),
    ("OLP-0024", "content/sets-functions-relations/functions/inverses.tex"),
    ("OLP-0029", "content/sets-functions-relations/size-of-sets/enumerability.tex"),
    ("OLP-0031", "content/sets-functions-relations/size-of-sets/pairing.tex"),
    ("OLP-0032", "content/sets-functions-relations/size-of-sets/pairing-alt.tex"),
    ("OLP-0034", "content/sets-functions-relations/size-of-sets/reduction.tex"),
    ("OLP-0035", "content/sets-functions-relations/size-of-sets/equinumerous-sets.tex"),
    ("OLP-0036", "content/sets-functions-relations/size-of-sets/comparing-size.tex"),
    ("OLP-0039", "content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex"),
    ("OLP-0040", "content/sets-functions-relations/size-of-sets/reduction-alt.tex"),
]

PHYSICAL_RULES = [
    "OLFUN-002",
    "OLFUN-003",
    "OLFUN-004",
    "OLFUN-005",
    "OLFUN-001-THEOREM",
    "OLFUN-001-PROOF",
    "OLSIZ-001",
    "OLSIZ-002",
    "OLSIZ-003",
    "OLSIZ-004",
    "OLSIZ-005",
    "OLSIZ-006",
    "OLSIZ-007",
    "OLSIZ-008+009",
    "OLSIZ-010",
]

CITATION_KEYS = ["Frege1884", "Cantor1892"]
CITATION_SEED = r'''
% Resolve the two citations present in the exact affected source units without
% invoking BibTeX or reading a bibliography database in this one-pass probe.
% The source units still write their own exact \citation rows to the AUX file.
\AtBeginDocument{%
  \bibcite{Frege1884}{{1}{1884}{{Frege}}{{}}}%
  \bibcite{Cantor1892}{{2}{1892}{{Cantor}}{{}}}%
}
'''

CONDITIONAL_REFERENCE_KEYS = [
    "sfr:rel:ref:sec",
    "sfr:rel:ops:sec",
    "sfr:siz:nen:sec",
]
CONDITIONAL_REFERENCE_SEED = r'''
% The complete reader defines these cross-unit labels.  Seed only their
% in-memory r@ records so this isolated one-pass probe exercises the same
% conditional prose branches; do not write synthetic labels to the AUX file.
\makeatletter
\AtBeginDocument{%
  \@namedef{r@sfr:rel:ref:sec}{{0}{0}{}{}{}}%
  \@namedef{r@sfr:rel:ops:sec}{{0}{0}{}{}{}}%
  \@namedef{r@sfr:siz:nen:sec}{{0}{0}{}{}{}}%
}
\makeatother
'''


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def file_record(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": len(data),
        "sha256": sha(data),
    }


def require_identity(label: str, data: bytes, expected: tuple[int, str]) -> None:
    expected_bytes, expected_sha256 = expected
    actual = (len(data), sha(data))
    if actual != (expected_bytes, expected_sha256):
        raise SystemExit(
            f"{label} identity changed: bytes={actual[0]} sha256={actual[1]}"
        )


def driver_preamble_through_boundary(data: bytes) -> bytes:
    boundary_at = data.find(DOCUMENT_BOUNDARY)
    if boundary_at < 0:
        raise SystemExit(
            "Standalone driver has no literal "
            f"{DOCUMENT_BOUNDARY.decode('ascii')} boundary"
        )
    boundary_end = boundary_at + len(DOCUMENT_BOUNDARY)
    return data[:boundary_end]


def generate() -> tuple[bytes, bytes, dict[str, object]]:
    driver_data = DRIVER.read_bytes()
    preamble_through_boundary = driver_preamble_through_boundary(driver_data)
    require_identity(
        "Driver preamble through document boundary",
        preamble_through_boundary,
        ACCEPTED_PREAMBLE_IDENTITY,
    )
    preamble = preamble_through_boundary[:-len(DOCUMENT_BOUNDARY)]

    runtime_text = RUNTIME.read_text(encoding="utf-8")
    assert r"\NewDocumentCommand \OLSAInstallDeferredSourceContext" in runtime_text
    assert r"\OLSAInstallDeferredSourceContext" in runtime_text
    overlay_text = OVERLAY.read_text(encoding="utf-8")
    for rule in PHYSICAL_RULES:
        assert f"{{{rule}}}" in overlay_text, rule
    # One command definition plus fifteen declarations.
    assert overlay_text.count(r"\OLSADeclareSourceCorrection") == 16
    assert r"\olsa_source_correction_install_probdeferred:" in overlay_text

    calls = "\n".join(
        f"\\OLSACorrectionProbeUnit{{{unit}}}%\n {{{relative}}}"
        for unit, relative in UNITS
    )
    body = r'''
\begin{document}
\input{standalone/runtime.tex}
\input{standalone/source-corrections.tex}
\InputIfFileExists{standalone-errata.tex}{}{}
\OLSASourceCorrectionsStart
\OLSAInstallDeferredSourceContext

\chapter*{آزمونِ تصحیح‌های ممیزیِ منبع}
\noindent این سند فقط آزمونِ تشخیصیِ لایهٔ تصحیح است و خوانشگرِ نهایی نیست.
شناسه‌های ممیزی: \foreignlanguage{english}{\texttt{OLFUN-20260904 / OLSIZ-20260904}}.

\ExplSyntaxOn
\NewDocumentCommand \OLSACorrectionProbeUnit {m m}
 {
  \clearpage
  \group_begin:
  \cs_set:Npn \OLStandaloneCurrentID {#1}
  \cs_set:Npn \OLStandaloneCurrentPath {#2}
  \OLSASetReferenceContext{#1}
  \cs_if_exist:cT {olsa_setup_#1:}{\use:c {olsa_setup_#1:}}
  \olsa_original_subfile:n {#2}
  \cs_if_exist:cT {olsa_after_#1:}{\use:c{olsa_after_#1:}}
  \group_end:
 }
\ExplSyntaxOff

''' + calls + r'''

% OLP-0031 is an answers.sty problem. Its exact source identity was written
% beside the deferred body; close and read that stream before coverage checks.
\clearpage
% Do not start a new chapter here: problemsperchapter would reopen and truncate
% the answers stream before this explicit readback.
\section*{آزمونِ مسئلهٔ معوق}
\printproblems

\OLSASourceCorrectionsVerify
\end{document}
'''
    target_data = (
        preamble
        + CITATION_SEED.encode("utf-8")
        + CONDITIONAL_REFERENCE_SEED.encode("utf-8")
        + body.encode("utf-8")
    )
    require_identity("Generated source-corrections probe TeX", target_data, ACCEPTED_PROBE_IDENTITY)
    require_identity("Accepted native QA", ACCEPTED_NATIVE_QA.read_bytes(), ACCEPTED_NATIVE_QA_IDENTITY)
    require_identity("Accepted complete visual QA", ACCEPTED_VISUAL_QA.read_bytes(), ACCEPTED_VISUAL_QA_IDENTITY)
    source_records = [file_record(LOCALE / relative) for _, relative in UNITS]
    for row, (unit, _) in zip(source_records, UNITS, strict=True):
        row["unit_id"] = unit

    receipt: dict[str, object] = {
        "schema": "farsi-combined-source-corrections-probe-fixture-v5",
        "status": "FIXTURE_GENERATED_NOT_NATIVE_VALIDATED",
        "audit_ids": ["OLFUN-20260904", "OLSIZ-20260904"],
        "driver_preamble": {
            "path": DRIVER.relative_to(ROOT).as_posix(),
            "boundary": DOCUMENT_BOUNDARY.decode("ascii"),
            "boundary_inclusive": True,
            "bytes": len(preamble_through_boundary),
            "sha256": sha(preamble_through_boundary),
        },
        "historical_evidence_continuity": {
            "status": "PASS_PREAMBLE_AND_PROBE_TEX_BYTES_UNCHANGED",
            "historical_full_driver_locator_only": {
                "path": DRIVER.relative_to(ROOT).as_posix(),
                "bytes": HISTORICAL_FULL_DRIVER_IDENTITY[0],
                "sha256": HISTORICAL_FULL_DRIVER_IDENTITY[1],
            },
            "historical_driver_preamble": {
                "boundary": DOCUMENT_BOUNDARY.decode("ascii"),
                "boundary_inclusive": True,
                "bytes": ACCEPTED_PREAMBLE_IDENTITY[0],
                "sha256": ACCEPTED_PREAMBLE_IDENTITY[1],
            },
            "accepted_probe_tex": {
                "path": TARGET.relative_to(ROOT).as_posix(),
                "bytes": ACCEPTED_PROBE_IDENTITY[0],
                "sha256": ACCEPTED_PROBE_IDENTITY[1],
            },
            "accepted_native_qa": file_record(ACCEPTED_NATIVE_QA),
            "accepted_complete_visual_qa": file_record(ACCEPTED_VISUAL_QA),
            "preamble_bytes_unchanged": True,
            "probe_tex_bytes_unchanged": True,
            "post_boundary_driver_changes_out_of_scope": True,
        },
        "dependencies": {
            "runtime": file_record(RUNTIME),
            "overlay": file_record(OVERLAY),
            "errata": file_record(ERRATA),
        },
        "source_units": source_records,
        "physical_rules": PHYSICAL_RULES,
        "physical_rule_count": 15,
        "semantic_finding_count": 15,
        "rule_to_findings": {
            "OLFUN-001-THEOREM": ["OLFUN-001"],
            "OLFUN-001-PROOF": ["OLFUN-001"],
            "OLSIZ-008+009": ["OLSIZ-008", "OLSIZ-009"],
        },
        "output": {
            "path": TARGET.relative_to(ROOT).as_posix(),
            "sha256": sha(target_data),
            "bytes": len(target_data),
        },
        "expected_trace_events": 15,
        "deferred_problem_rule": "OLSIZ-002",
        "citation_keys": CITATION_KEYS,
        "citation_resolution": "preamble_bibcite_seed_no_external_bibliography_worker",
        "conditional_reference_keys": CONDITIONAL_REFERENCE_KEYS,
        "conditional_reference_resolution": "in_memory_r_at_seed_no_synthetic_aux_labels",
        "native_acceptance": [
            "one guarded LuaLaTeX diagnostic pass exits zero",
            "olcorrections sidecar and log contain exactly fifteen expected physical events",
            "all fifteen semantic findings are mapped without duplicate or missing audit identities",
            "the OLSIZ-002 problem correction and note execute only after its persisted source context is restored",
            "all corrected semantic deltas are bound to bounded page-local line windows rather than whole-document text search",
            "the exact Frege1884 and Cantor1892 source citations resolve from local one-pass seeds and write ordered AUX citation rows without external bibliography input",
            "all rendered probe pages receive complete visual inspection",
        ],
        "tex_run": False,
        "not_full_reader": True,
    }
    receipt_data = (
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")
    return target_data, receipt_data, receipt


def require_replace_authority(path: Path, supplied: str | None) -> None:
    if not path.exists():
        return
    actual = sha(path.read_bytes())
    if actual != (supplied or "").upper():
        raise SystemExit(
            f"Refusing to replace differing {path.name}; provide its reviewed "
            f"SHA-256 explicitly: {actual}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--replace-output-sha256")
    parser.add_argument("--replace-receipt-sha256")
    args = parser.parse_args()
    if args.check and (args.replace_output_sha256 or args.replace_receipt_sha256):
        raise SystemExit("--check and replacement authorities are mutually exclusive")

    target_data, receipt_data, receipt = generate()
    if args.check:
        if not TARGET.is_file() or TARGET.read_bytes() != target_data:
            raise SystemExit("Probe does not match generator")
        if not RECEIPT.is_file() or RECEIPT.read_bytes() != receipt_data:
            raise SystemExit("Fixture receipt does not match generator")
    else:
        if TARGET.exists() and TARGET.read_bytes() != target_data:
            require_replace_authority(TARGET, args.replace_output_sha256)
        if RECEIPT.exists() and RECEIPT.read_bytes() != receipt_data:
            require_replace_authority(RECEIPT, args.replace_receipt_sha256)
        TARGET.write_bytes(target_data)
        RECEIPT.write_bytes(receipt_data)

    print(json.dumps(receipt, ensure_ascii=True))


if __name__ == "__main__":
    main()
