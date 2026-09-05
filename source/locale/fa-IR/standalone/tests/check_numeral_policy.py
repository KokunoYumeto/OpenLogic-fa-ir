"""Static checks for the generated standard-Farsi numeral profile."""
from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parents[5]
LOCALE = ROOT / "source/locale/fa-IR"
DRIVER = LOCALE / "open-logic-standalone-fa-IR.tex"
GENERATOR = ROOT / "build/make_standalone_driver.py"
PROBE = LOCALE / "standalone-probe-farsi-numerals.tex"
FIXTURE = ROOT / "evidence/FARSI_NUMERAL_PROBE_FIXTURE.json"
DOCUMENT_BOUNDARY = br"\begin{document}"
PREAMBLE_IDENTITY = (8212, "c6e31f3488f61233b446d848d80c0cc04d319d99d6c77c1fa28addfc4907ce47")
PROBE_IDENTITY = (10294, "f3eaa675755cb3b217faf308a3db73d3a5f2b6606dbde6e5a4fef184a906d7af")
HISTORICAL_FULL_DRIVER_IDENTITY = (13343, "f983e663c874fcee8b2065e15ffca1b3ab7c08174fa5ec970b7e96366e2c05d2")
ACCEPTED_NATIVE_QA = ROOT / "evidence/FARSI_NUMERAL_NATIVE_PROBE_QA_V3.json"
ACCEPTED_NATIVE_QA_IDENTITY = (2969, "33af6d3b6313ae087a3659f5e40f6fb1490c5ee03c70c9aa23e9f50732433948")
ACCEPTED_VISUAL_QA = ROOT / "evidence/FARSI_NUMERAL_NATIVE_PROBE_VISUAL_QA_V3.json"
ACCEPTED_VISUAL_QA_IDENTITY = (4887, "19eb63a23459794b43e60a8fa84ab042338784d2750969e7a64795c792fc14e1")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def preamble_through_boundary(data: bytes) -> bytes:
    boundary_at = data.find(DOCUMENT_BOUNDARY)
    assert boundary_at >= 0
    end = boundary_at + len(DOCUMENT_BOUNDARY)
    return data[:end]


def assert_file_record(record: dict, path: Path, identity: tuple[int, str]) -> None:
    data = path.read_bytes()
    assert set(record) == {"path", "bytes", "sha256"}
    assert record["path"] == path.relative_to(ROOT).as_posix()
    assert (record["bytes"], record["sha256"]) == identity
    assert (len(data), digest(data)) == identity


driver_bytes = DRIVER.read_bytes()
driver = driver_bytes.decode("utf-8", errors="strict")
generator = GENERATOR.read_text(encoding="utf-8")
probe = PROBE.read_text(encoding="utf-8")
fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

map_line = r"\babelprovide[import=fa,main,onchar=ids fonts,mapdigits]{persian}"
assert driver.count(map_line) == 1
assert "maparabic" not in driver
assert r"\number\value{chapter}.\number\value{#1}" in driver
assert r"\foreignlanguage{english}{\babelsublr{10.5281/zenodo.21921852}}" in driver
assert "babel_persian = r'\\babelprovide[import=fa,main,onchar=ids fonts]{persian}'" in generator
assert "r'\\babelprovide[import=fa,main,onchar=ids fonts,mapdigits]{persian}'" in generator
assert r"{\foreignlanguage{english}{CC BY 4.0}}" in driver
assert "native_probe_required': True" in generator

for marker in (
    "PERSIAN-TEXT-CONTROL",
    "ENGLISH-CONTROL",
    "DOI-CONTROL",
    "URL-CONTROL",
    "BARE-URL-CONTROL",
    "MATH-CONTROL",
    r"\foreignlanguage{english}{\textbf{MATH-CONTROL:}}",
    r"\url{https://example.org/v3/item/456}",
    r"\begin{equation}\label{olsa:numeral-probe-equation}",
    r"raw-page=\number\value{page}",
    r"raw-chapter=\number\value{chapter}",
    r"raw-section=\thesection",
    r"raw-theorem=\thethm",
):
    assert marker in probe, marker

assert fixture["status"] == "FIXTURE_GENERATED_NOT_NATIVE_VALIDATED"
assert fixture["schema"] == "farsi-numeral-probe-fixture-v3"
assert set(fixture["driver_preamble"]) == {
    "path", "boundary", "boundary_inclusive", "bytes", "sha256",
}
current_preamble = preamble_through_boundary(driver_bytes)
assert fixture["driver_preamble"] == {
    "path": DRIVER.relative_to(ROOT).as_posix(),
    "boundary": DOCUMENT_BOUNDARY.decode("ascii"),
    "boundary_inclusive": True,
    "bytes": PREAMBLE_IDENTITY[0],
    "sha256": PREAMBLE_IDENTITY[1],
}
assert (len(current_preamble), digest(current_preamble)) == PREAMBLE_IDENTITY
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
assert fixture["output"]["sha256"] == digest(PROBE.read_bytes()) == PROBE_IDENTITY[1]
assert fixture["output"]["bytes"] == PROBE_IDENTITY[0]
assert fixture["output"]["pages_expected"] == 5
assert fixture["expected_raw_sidecar"]["raw-section"] == "12.34"
assert fixture["expected_raw_sidecar"]["raw-anchor"] == "12.34"
assert fixture["expected_aux"]["section_destination_prefix"] == "section"
assert fixture["expected_aux"]["theorem_destination_prefix"] == "thm"
assert fixture["expected_aux"]["equation_destination_prefix"] == "equation"
assert fixture["expected_pdf_pages"]["1"]["persian_digits_exact"] == "۰۲۴۶۸۱۳۵۷۹"
assert fixture["expected_pdf_pages"]["2"]["persian_equation_tag"] == "۱۲.۵۶"
assert fixture["expected_pdf_pages"]["3"]["bare_url"].endswith("/456")
assert fixture["expected_pdf_pages"]["4"]["math_ltr_ascii"] == "6=1+2+3"
assert fixture["expected_pdf_pages"]["5"]["persian_digits_exact"] == "۷۸۹"

print(
    "PASS: one mapdigits profile; ASCII counter/anchor expansion retained; "
    "English/DOI/URL and LTR-math controls present; exact boundary-inclusive "
    "preamble and accepted probe identities bound."
)
