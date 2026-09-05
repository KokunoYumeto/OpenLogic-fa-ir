"""Generate a guarded five-page standard-Farsi numeral diagnostic.

This script never launches TeX. It refuses to replace a differing reviewed
probe or fixture receipt unless the caller supplies its exact current SHA-256.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
LOCALE = ROOT / "source/locale/fa-IR"
DRIVER = LOCALE / "open-logic-standalone-fa-IR.tex"
TARGET = LOCALE / "standalone-probe-farsi-numerals.tex"
RECEIPT = ROOT / "evidence/FARSI_NUMERAL_PROBE_FIXTURE.json"
DOCUMENT_BOUNDARY = br"\begin{document}"
HISTORICAL_FULL_DRIVER_IDENTITY = (
    13343,
    "f983e663c874fcee8b2065e15ffca1b3ab7c08174fa5ec970b7e96366e2c05d2",
)
ACCEPTED_PREAMBLE_IDENTITY = (
    8212,
    "c6e31f3488f61233b446d848d80c0cc04d319d99d6c77c1fa28addfc4907ce47",
)
ACCEPTED_PROBE_IDENTITY = (
    10294,
    "f3eaa675755cb3b217faf308a3db73d3a5f2b6606dbde6e5a4fef184a906d7af",
)
ACCEPTED_NATIVE_QA = ROOT / "evidence/FARSI_NUMERAL_NATIVE_PROBE_QA_V3.json"
ACCEPTED_NATIVE_QA_IDENTITY = (
    2969,
    "33af6d3b6313ae087a3659f5e40f6fb1490c5ee03c70c9aa23e9f50732433948",
)
ACCEPTED_VISUAL_QA = ROOT / "evidence/FARSI_NUMERAL_NATIVE_PROBE_VISUAL_QA_V3.json"
ACCEPTED_VISUAL_QA_IDENTITY = (
    4887,
    "19eb63a23459794b43e60a8fa84ab042338784d2750969e7a64795c792fc14e1",
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


def require_replace_authority(path: Path, supplied: str | None) -> None:
    if not path.exists():
        return
    actual = sha(path.read_bytes())
    if actual != (supplied or "").lower():
        raise SystemExit(
            f"Refusing to replace differing {path.name}; provide its reviewed "
            f"SHA-256 explicitly: {actual}"
        )


def generate() -> tuple[bytes, bytes, dict]:
    driver_data = DRIVER.read_bytes()
    preamble_through_boundary = driver_preamble_through_boundary(driver_data)
    require_identity(
        "Driver preamble through document boundary",
        preamble_through_boundary,
        ACCEPTED_PREAMBLE_IDENTITY,
    )
    preamble = preamble_through_boundary[:-len(DOCUMENT_BOUNDARY)]
    preamble_text = preamble.decode("utf-8", errors="strict")
    assert preamble_text.count(
        r"\babelprovide[import=fa,main,onchar=ids fonts,mapdigits]{persian}"
    ) == 1
    assert "maparabic" not in preamble_text

    body = r'''
\begin{document}
\pagestyle{empty}

% Page 1: the only digits are an ASCII source sequence in Persian context.
\thispagestyle{empty}
\noindent\foreignlanguage{english}{\textbf{PERSIAN-TEXT-CONTROL:}}
0246813579
\clearpage

% Page 2: structural numbers, one numbered formula, and no numeric prose.
\setcounter{page}{212}
\setcounter{chapter}{12}
\setcounter{section}{33}
\section{بخش آزمایشی}\label{olsa:numeral-probe-section}
\setcounter{thm}{7}
\begin{thm}\label{olsa:numeral-probe-theorem}
این قضیه فقط رفتار شمارهٔ نمایشی را می‌سنجد.
\end{thm}
\setcounter{equation}{55}
\begin{equation}\label{olsa:numeral-probe-equation}
7=3+4
\end{equation}
\newwrite\OLFaNumeralTrace
\immediate\openout\OLFaNumeralTrace=\jobname.olnumbers
\immediate\write\OLFaNumeralTrace{schema=farsi-numeral-probe-v2}
\immediate\write\OLFaNumeralTrace{raw-page=\number\value{page}}
\immediate\write\OLFaNumeralTrace{raw-chapter=\number\value{chapter}}
\immediate\write\OLFaNumeralTrace{raw-section=\thesection}
\immediate\write\OLFaNumeralTrace{raw-theorem=\thethm}
\immediate\write\OLFaNumeralTrace{raw-equation=\number\value{equation}}
\immediate\write\OLFaNumeralTrace{raw-equation-display=\theequation}
\immediate\write\OLFaNumeralTrace{raw-anchor=\theHsection}
\immediate\closeout\OLFaNumeralTrace
\clearpage

% Page 3: every digit is deliberately ASCII. The URL is not wrapped in an
% English language environment, matching ordinary production \url usage.
\thispagestyle{empty}
\noindent\foreignlanguage{english}{\textbf{ENGLISH-CONTROL: 0123456789}}
\par
\foreignlanguage{english}{\textbf{DOI-CONTROL:}
\babelsublr{10.5281/zenodo.21921852}}
\par
\foreignlanguage{english}{\textbf{BARE-URL-CONTROL:}}
\url{https://example.org/v3/item/456}
\clearpage

% Page 4: the only digits are in a conventional LTR formula.
\thispagestyle{empty}
\noindent\foreignlanguage{english}{\textbf{MATH-CONTROL:}}
\[
6=1+2+3
\]
\clearpage

% Page 5: the only digits are the visible folio, in the footer band.
\setcounter{page}{789}
\thispagestyle{plain}
\noindent آزمون
\end{document}
'''

    target_data = preamble + body.encode("utf-8")
    require_identity("Generated numeral probe TeX", target_data, ACCEPTED_PROBE_IDENTITY)
    require_identity("Accepted native QA", ACCEPTED_NATIVE_QA.read_bytes(), ACCEPTED_NATIVE_QA_IDENTITY)
    require_identity("Accepted complete visual QA", ACCEPTED_VISUAL_QA.read_bytes(), ACCEPTED_VISUAL_QA_IDENTITY)
    receipt = {
        "schema": "farsi-numeral-probe-fixture-v3",
        "status": "FIXTURE_GENERATED_NOT_NATIVE_VALIDATED",
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
        "output": {
            "path": TARGET.relative_to(ROOT).as_posix(),
            "sha256": sha(target_data),
            "bytes": len(target_data),
            "pages_expected": 5,
        },
        "expected_raw_sidecar": {
            "schema": "farsi-numeral-probe-v2",
            "raw-page": "212",
            "raw-chapter": "12",
            "raw-section": "12.34",
            "raw-theorem": "12.8",
            "raw-equation": "56",
            "raw-equation-display": "12.56",
            "raw-anchor": "12.34",
        },
        "expected_aux": {
            "section_number": "12.34",
            "section_page": "212",
            "section_destination_prefix": "section",
            "theorem_number": "12.8",
            "theorem_page": "212",
            "theorem_destination_prefix": "thm",
            "equation_number": "12.56",
            "equation_page": "212",
            "equation_destination_prefix": "equation",
        },
        "expected_pdf_pages": {
            "1": {
                "persian_digits_exact": "۰۲۴۶۸۱۳۵۷۹",
                "ascii_digits_exact": "",
            },
            "2": {
                "persian_digits_multiset": "۱۲۳۴۱۲۸۱۲۵۶",
                "ascii_digits_multiset": "734",
                "equation_ltr_ascii": "7=3+4",
                "persian_equation_tag": "۱۲.۵۶",
            },
            "3": {
                "persian_digits_exact": "",
                "ascii_digits_multiset": "0123456789" + "10528121921852" + "3456",
                "doi": "10.5281/zenodo.21921852",
                "bare_url": "https://example.org/v3/item/456",
            },
            "4": {
                "persian_digits_exact": "",
                "ascii_digits_exact": "6123",
                "math_ltr_ascii": "6=1+2+3",
            },
            "5": {
                "persian_digits_exact": "۷۸۹",
                "ascii_digits_exact": "",
                "footer_band_minimum_fraction": 0.85,
            },
        },
        "expected_uri": "https://example.org/v3/item/456",
        "native_acceptance": [
            "one guarded LuaLaTeX diagnostic pass exits zero",
            "olnumbers sidecar and AUX retain exact ASCII counter/anchor identities",
            "per-page glyph codepoint multisets prove Persian prose, structure, equation tag, and folio contexts",
            "English, DOI, and bare URL controls retain ASCII digits and the URI annotation target is exact",
            "math digits stay ASCII and formula digit centers increase left-to-right",
            "the footer-only Persian folio lies entirely in the footer band",
            "all five rendered pages receive complete visual inspection",
        ],
        "tex_run": False,
        "not_full_reader": True,
    }
    receipt_data = (
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")
    return target_data, receipt_data, receipt


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
