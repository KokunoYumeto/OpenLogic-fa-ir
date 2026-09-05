"""Validate exact native output from the guarded five-page numeral probe."""
from __future__ import annotations

from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
import re

import fitz


ROOT = Path(__file__).resolve().parents[1]
RUNS = (ROOT / "tmp/pdfs/standalone").resolve()
JOB = "standalone-probe-farsi-numerals"
FIXTURE = ROOT / "evidence/FARSI_NUMERAL_PROBE_FIXTURE.json"
DRIVER = ROOT / "source/locale/fa-IR/open-logic-standalone-fa-IR.tex"
PROBE = ROOT / "source/locale/fa-IR/standalone-probe-farsi-numerals.tex"
ACCEPTED_NATIVE_QA = ROOT / "evidence/FARSI_NUMERAL_NATIVE_PROBE_QA_V3.json"
ACCEPTED_VISUAL_QA = ROOT / "evidence/FARSI_NUMERAL_NATIVE_PROBE_VISUAL_QA_V3.json"
DOCUMENT_BOUNDARY = br"\begin{document}"
FIXTURE_IDENTITY = (3971, "b0fd8ba2ef295278890abe2bc7e3d1a31246762f0993515ab297cb95707950a0")
PREAMBLE_IDENTITY = (8212, "c6e31f3488f61233b446d848d80c0cc04d319d99d6c77c1fa28addfc4907ce47")
PROBE_IDENTITY = (10294, "f3eaa675755cb3b217faf308a3db73d3a5f2b6606dbde6e5a4fef184a906d7af")
HISTORICAL_FULL_DRIVER_IDENTITY = (13343, "f983e663c874fcee8b2065e15ffca1b3ab7c08174fa5ec970b7e96366e2c05d2")
ACCEPTED_NATIVE_QA_IDENTITY = (2969, "33af6d3b6313ae087a3659f5e40f6fb1490c5ee03c70c9aa23e9f50732433948")
ACCEPTED_VISUAL_QA_IDENTITY = (4887, "19eb63a23459794b43e60a8fa84ab042338784d2750969e7a64795c792fc14e1")
PERSIAN_DIGITS = set("۰۱۲۳۴۵۶۷۸۹")
ARABIC_INDIC_DIGITS = set("٠١٢٣٤٥٦٧٨٩")
ASCII_DIGITS = set("0123456789")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def preamble_through_boundary(data: bytes) -> bytes:
    boundary_at = data.find(DOCUMENT_BOUNDARY)
    assert boundary_at >= 0
    boundary_end = boundary_at + len(DOCUMENT_BOUNDARY)
    return data[:boundary_end]


def assert_file_record(record: dict, path: Path, identity: tuple[int, str]) -> None:
    assert set(record) == {"path", "bytes", "sha256"}
    assert record["path"] == path.relative_to(ROOT).as_posix()
    assert (record["bytes"], record["sha256"]) == identity
    assert (path.stat().st_size, sha(path)) == identity


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def parse_sidecar(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if "=" not in raw:
            raise AssertionError(f"sidecar line {number} has no equals sign: {raw!r}")
        key, value = raw.split("=", 1)
        if not key or key in result:
            raise AssertionError(f"invalid/duplicate sidecar key at line {number}: {key!r}")
        result[key] = value
    return result


def glyphs(page: fitz.Page) -> list[tuple[str, tuple[float, float, float, float]]]:
    result: list[tuple[str, tuple[float, float, float, float]]] = []
    raw = page.get_text("rawdict")
    for block in raw.get("blocks", []):
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                for char in span.get("chars", []):
                    result.append((char["c"], tuple(char["bbox"])))
    return result


def only(chars, alphabet: set[str]) -> list[tuple[str, tuple[float, float, float, float]]]:
    return [(char, bbox) for char, bbox in chars if char in alphabet]


def exact_counter(actual, expected: str, label: str) -> None:
    assert Counter(char for char, _ in actual) == Counter(expected), (
        label,
        Counter(char for char, _ in actual),
        Counter(expected),
    )


def label_line(aux_text: str, name: str) -> str:
    return next(
        line for line in aux_text.splitlines()
        if line.startswith(r"\newlabel{" + name + "}")
    )


def assert_aux_label(line: str, number: str, page: str, prefix: str) -> None:
    assert f"{{{{{number}}}{{" in line, line
    assert re.search(r"\{\\babelsublr\s+\{" + re.escape(page) + r"\}\}", line), line
    assert re.search(
        r"\{" + re.escape(prefix) + r"(?:\*|\.)[^{}]+\}\{\}\}$",
        line,
    ), line


parser = argparse.ArgumentParser()
parser.add_argument("--receipt", type=Path, required=True)
parser.add_argument("--write-evidence", type=Path)
args = parser.parse_args()

receipt_path = args.receipt.resolve()
assert receipt_path.name == "BUILD_RECEIPT.json"
assert is_relative_to(receipt_path, RUNS), (receipt_path, RUNS)
run_root = receipt_path.parent
receipt = json.loads(receipt_path.read_text(encoding="utf-8-sig"))
fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

assert (FIXTURE.stat().st_size, sha(FIXTURE)) == FIXTURE_IDENTITY
assert fixture["schema"] == "farsi-numeral-probe-fixture-v3"
assert fixture["status"] == "FIXTURE_GENERATED_NOT_NATIVE_VALIDATED"
driver_preamble = preamble_through_boundary(DRIVER.read_bytes())
assert set(fixture["driver_preamble"]) == {
    "path", "boundary", "boundary_inclusive", "bytes", "sha256",
}
assert fixture["driver_preamble"] == {
    "path": DRIVER.relative_to(ROOT).as_posix(),
    "boundary": DOCUMENT_BOUNDARY.decode("ascii"),
    "boundary_inclusive": True,
    "bytes": PREAMBLE_IDENTITY[0],
    "sha256": PREAMBLE_IDENTITY[1],
}
assert (len(driver_preamble), sha_bytes(driver_preamble)) == PREAMBLE_IDENTITY
continuity = fixture["historical_evidence_continuity"]
assert set(continuity) == {
    "status", "historical_full_driver_locator_only",
    "historical_driver_preamble", "accepted_probe_tex",
    "accepted_native_qa", "accepted_complete_visual_qa",
    "preamble_bytes_unchanged", "probe_tex_bytes_unchanged",
    "post_boundary_driver_changes_out_of_scope",
}
assert continuity["status"] == "PASS_PREAMBLE_AND_PROBE_TEX_BYTES_UNCHANGED"
assert continuity["historical_full_driver_locator_only"] == {
    "path": DRIVER.relative_to(ROOT).as_posix(),
    "bytes": HISTORICAL_FULL_DRIVER_IDENTITY[0],
    "sha256": HISTORICAL_FULL_DRIVER_IDENTITY[1],
}
assert continuity["historical_driver_preamble"] == {
    "boundary": DOCUMENT_BOUNDARY.decode("ascii"),
    "boundary_inclusive": True,
    "bytes": PREAMBLE_IDENTITY[0],
    "sha256": PREAMBLE_IDENTITY[1],
}
assert_file_record(continuity["accepted_probe_tex"], PROBE, PROBE_IDENTITY)
assert_file_record(continuity["accepted_native_qa"], ACCEPTED_NATIVE_QA, ACCEPTED_NATIVE_QA_IDENTITY)
assert_file_record(continuity["accepted_complete_visual_qa"], ACCEPTED_VISUAL_QA, ACCEPTED_VISUAL_QA_IDENTITY)
assert continuity["preamble_bytes_unchanged"] is True
assert continuity["probe_tex_bytes_unchanged"] is True
assert continuity["post_boundary_driver_changes_out_of_scope"] is True
assert fixture["output"]["path"] == PROBE.relative_to(ROOT).as_posix()
assert fixture["output"]["bytes"] == PROBE_IDENTITY[0]
assert fixture["output"]["sha256"] == PROBE_IDENTITY[1] == sha(PROBE)

assert receipt["mode"] == "Diagnostic"
assert Path(receipt["driver"]).name == f"{JOB}.tex"
assert receipt["status"] == "DIAGNOSTIC_ONLY_NOT_ACCEPTED"
assert receipt["accepted_build"] is False
assert receipt["publication_or_visual_qa_passed"] is False
assert receipt["mutex"]["acquired"] is True
assert receipt["mutex"]["released_after_confirmed_tree_exit"] is True
assert len(receipt["builds"]) == 1
build = receipt["builds"][0]
assert build["name"] == "primary"
assert len(build["passes"]) == 1
diagnostics = build["passes"][0]["diagnostics"]
assert diagnostics["fatal"] == []
assert diagnostics["duplicate"] == []

primary = Path(build["directory"]).resolve()
assert primary.parent == run_root
pdf = Path(build["pdf"]["path"]).resolve()
assert pdf.parent == primary and pdf.name == f"{JOB}.pdf"
aux = primary / f"{JOB}.aux"
log = primary / f"{JOB}.log"
sidecar_path = primary / f"{JOB}.olnumbers"
for required in (pdf, aux, log, sidecar_path):
    assert required.is_file(), required

sidecar = parse_sidecar(sidecar_path)
assert sidecar == fixture["expected_raw_sidecar"], (sidecar, fixture["expected_raw_sidecar"])
assert all(not (set(value) & (PERSIAN_DIGITS | ARABIC_INDIC_DIGITS)) for value in sidecar.values())

aux_text = aux.read_text(encoding="utf-8", errors="strict")
for suffix in ("aux", "toc", "out", "thm", "olnumbers"):
    path = primary / f"{JOB}.{suffix}"
    if path.is_file():
        text = path.read_text(encoding="utf-8", errors="strict")
        assert not (set(text) & (PERSIAN_DIGITS | ARABIC_INDIC_DIGITS)), path

expected_aux = fixture["expected_aux"]
section_label = label_line(aux_text, "olsa:numeral-probe-section")
theorem_label = label_line(aux_text, "olsa:numeral-probe-theorem")
equation_label = label_line(aux_text, "olsa:numeral-probe-equation")
assert_aux_label(
    section_label,
    expected_aux["section_number"],
    expected_aux["section_page"],
    expected_aux["section_destination_prefix"],
)
assert_aux_label(
    theorem_label,
    expected_aux["theorem_number"],
    expected_aux["theorem_page"],
    expected_aux["theorem_destination_prefix"],
)
assert_aux_label(
    equation_label,
    expected_aux["equation_number"],
    expected_aux["equation_page"],
    expected_aux["equation_destination_prefix"],
)
section_cref = label_line(aux_text, "olsa:numeral-probe-section@cref")
theorem_cref = label_line(aux_text, "olsa:numeral-probe-theorem@cref")
assert "[section][34][12]12.34" in section_cref, section_cref
assert "[thm][8][12]12.8" in theorem_cref, theorem_cref

document = fitz.open(pdf)
assert document.page_count == fixture["output"]["pages_expected"] == 5
page_glyphs = [glyphs(page) for page in document]
for index, chars in enumerate(page_glyphs, 1):
    assert not only(chars, ARABIC_INDIC_DIGITS), f"page {index} has U+0660--U+0669"

expected_pages = fixture["expected_pdf_pages"]
# Page 1: Persian prose mapping only.
exact_counter(only(page_glyphs[0], PERSIAN_DIGITS), expected_pages["1"]["persian_digits_exact"], "page1 Persian")
exact_counter(only(page_glyphs[0], ASCII_DIGITS), expected_pages["1"]["ascii_digits_exact"], "page1 ASCII")

# Page 2: localized section/theorem/equation tag; ASCII equation body.
exact_counter(only(page_glyphs[1], PERSIAN_DIGITS), expected_pages["2"]["persian_digits_multiset"], "page2 Persian")
page2_ascii = only(page_glyphs[1], ASCII_DIGITS)
exact_counter(page2_ascii, expected_pages["2"]["ascii_digits_multiset"], "page2 ASCII")
assert "".join(char for char, _ in sorted(page2_ascii, key=lambda item: item[1][0])) == "734"

# Page 3: English/DOI and a bare production-style URL remain ASCII.
exact_counter(only(page_glyphs[2], PERSIAN_DIGITS), expected_pages["3"]["persian_digits_exact"], "page3 Persian")
exact_counter(only(page_glyphs[2], ASCII_DIGITS), expected_pages["3"]["ascii_digits_multiset"], "page3 ASCII")
page3_text = document[2].get_text("text")
assert expected_pages["3"]["doi"] in page3_text
assert expected_pages["3"]["bare_url"] in page3_text
uris = [link.get("uri") for link in document[2].get_links() if link.get("uri")]
assert uris == [fixture["expected_uri"]], uris

# Page 4: formula digits are unchanged and advance left-to-right.
exact_counter(only(page_glyphs[3], PERSIAN_DIGITS), expected_pages["4"]["persian_digits_exact"], "page4 Persian")
page4_ascii = only(page_glyphs[3], ASCII_DIGITS)
exact_counter(page4_ascii, expected_pages["4"]["ascii_digits_exact"], "page4 ASCII")
page4_sorted = sorted(page4_ascii, key=lambda item: item[1][0])
assert "".join(char for char, _ in page4_sorted) == "6123"
assert all(page4_sorted[i][1][2] <= page4_sorted[i + 1][1][0] for i in range(3))

# Page 5: footer-only localized folio.
page5_persian = only(page_glyphs[4], PERSIAN_DIGITS)
exact_counter(page5_persian, expected_pages["5"]["persian_digits_exact"], "page5 Persian")
exact_counter(only(page_glyphs[4], ASCII_DIGITS), expected_pages["5"]["ascii_digits_exact"], "page5 ASCII")
footer_minimum = document[4].rect.height * expected_pages["5"]["footer_band_minimum_fraction"]
assert all(bbox[1] >= footer_minimum for _, bbox in page5_persian), page5_persian

log_text = log.read_text(encoding="utf-8", errors="replace")
for forbidden in (
    "Missing character:",
    "destination with the same identifier",
    "multiply defined",
    "Fatal error",
    "Emergency stop",
):
    assert forbidden not in log_text, forbidden

evidence = {
    "schema": "farsi-numeral-native-probe-qa-v2",
    "status": "PASS_NATIVE_PROBE_PENDING_COMPLETE_VISUAL_INSPECTION_NOT_FULL_READER",
    "run_root": run_root.as_posix(),
    "build_receipt": {"path": receipt_path.as_posix(), "sha256": sha(receipt_path)},
    "pdf": {
        "path": pdf.as_posix(),
        "sha256": sha(pdf),
        "bytes": pdf.stat().st_size,
        "pages": document.page_count,
    },
    "sidecar": {"path": sidecar_path.as_posix(), "sha256": sha(sidecar_path), "values": sidecar},
    "aux": {
        "path": aux.as_posix(),
        "sha256": sha(aux),
        "section_label": section_label,
        "theorem_label": theorem_label,
        "equation_label": equation_label,
        "contains_localized_digit_codepoints": False,
    },
    "checks": {
        "five_context_isolated_pages": True,
        "persian_text_and_structure_and_equation_tag": True,
        "ascii_english_doi_and_bare_url": True,
        "uri_annotation_exact": True,
        "ascii_counter_aux_anchor_payloads": True,
        "ltr_ascii_math_digit_geometry": True,
        "footer_only_persian_folio_geometry": True,
        "fatal_missing_glyph_duplicate_destination_diagnostics_absent": True,
    },
    "pymupdf_version": fitz.VersionBind,
    "limitations": [
        "Glyph and annotation checks do not by themselves prove whole-page visual quality.",
        "All five rendered pages require direct inspection before changing status.",
        "This diagnostic does not qualify the full 722-unit reader.",
    ],
}
document.close()

if args.write_evidence:
    output = args.write_evidence.resolve()
    assert is_relative_to(output, ROOT.resolve()), output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(evidence, ensure_ascii=True))
