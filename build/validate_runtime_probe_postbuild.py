"""Validate the guarded native Babel/OpenLogic bang-shorthand diagnostic.

The fixture contrasts the known pre-fix alignment behavior with the corrected
runtime and carries four exact historical bibliography entries.  This script
never launches TeX and cannot replace rendered full-page inspection.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import argparse
import hashlib
import json
import re
import sys
import unicodedata

from probe_postbuild_common import (
    LOCALE,
    ROOT,
    ValidationError,
    base_evidence,
    clear_snapshot_cache,
    compact_text,
    expect_validation_error,
    file_size,
    load_json,
    load_pdf_text,
    read_file_bytes,
    read_file_text,
    relative_repo_path,
    require,
    require_bound_output,
    require_recorder_inputs,
    self_test_common_primitives,
    sha256_bytes,
    sha256_file,
    validate_diagnostic_receipt,
    write_json,
)


JOB = "standalone-probe-runtime"
DRIVER = LOCALE / f"{JOB}.tex"
FIXTURE_MANIFEST = ROOT / "evidence/RUNTIME_PROBE_FIXTURE.json"
LIVE_DRIVER = LOCALE / "open-logic-standalone-fa-IR.tex"
RUNTIME_FIXES = LOCALE / "standalone/runtime-fixes.tex"
RUNTIME_FIXES_SHA256 = "93afda9b09955c3d13d445b0ed2449cc49f789bf56e76d5fc293e7521a5bd995"
HISTORIC_BBL = ROOT / (
    "tmp/pdfs/standalone/20260904T160648332Z-05caf6e0aaa8475abd7899c4ee8744e1/"
    "primary/open-logic-standalone-fa-IR.bbl"
)
HISTORIC_BBL_SHA256 = "9e546e03a82d6d0ec2712d385e935a99b6f8c1b9ce9680252ba67203d8689609"
EXPECTED_BIBLIOGRAPHY_KEYS = [
    "Boolos2000",
    "Hume1740",
    "Montague1961",
    "WhiteheadRussell1910",
]
EXPECTED_POST_FORMULA_GLYPHS = Counter(
    {"ϕ": 11, "ψ": 9, "χ": 9, "θ": 6, "γ": 2, "δ": 2, "α": 1, "β": 1, "A": 1, "B": 1}
)
FORMULA_GLYPH_ALPHABET = set(EXPECTED_POST_FORMULA_GLYPHS)
CONTROL_ALPHABET = FORMULA_GLYPH_ALPHABET | set("CDGH!")
REQUIRED_POST_PHRASES = [
    "آزمون پس از اصلاح",
    "فرمول‌های زیر آزمونِ رفتارِ نمادها هستند",
    # PyMuPDF 1.27.2.3 can omit the HEH in a HEH+HAMZA ABOVE cluster.
    # Keep the distinctive, extraction-stable remainder of this sentence.
    "تعجب در متن ! و فاکتوریل در ریاضی",
    "وجودِ یگانه",
    "در متنِ درونِ فرمول",
    "آزمون",
]
REQUIRED_BIBLIOGRAPHY_PHRASES = [
    "Must we believe in set theory?",
    "A Treatise of Human Nature",
    "Semantic closure and non-finite axiomatizability I",
    "Principia Mathematica",
]


def pymupdf_marked_base_omission_variant(text: str) -> str:
    """Model the reviewed Scheherazade ToUnicode extraction quirk.

    PyMuPDF 1.27.2.3 retains an Arabic combining mark but can omit the base
    glyph that carries it. Poppler and the rendered page retain that glyph.
    Admit only this deterministic expected-string variant; do not generally
    fuzzy-match Persian prose.
    """
    output: list[str] = []
    for character in unicodedata.normalize("NFC", text):
        if unicodedata.category(character).startswith("M"):
            if output and unicodedata.category(output[-1]).startswith("L"):
                output.pop()
        output.append(character)
    return "".join(output)


def require_runtime_phrases_in_blocks(
    blocks_by_page: list[list[str]], phrases: list[str], label: str,
) -> None:
    compact_blocks = [compact_text(block) for page in blocks_by_page for block in page]
    missing = []
    for phrase in phrases:
        candidates = {
            compact_text(phrase),
            compact_text(pymupdf_marked_base_omission_variant(phrase)),
        }
        if not any(candidate in block for candidate in candidates for block in compact_blocks):
            missing.append(phrase)
    require(not missing, f"{label} required PDF phrases missing within individual text blocks: {missing}")


def require_bibliography_phrases_in_blocks(
    blocks_by_page: list[list[str]], phrases: list[str], label: str,
) -> None:
    # Admit only an ASCII alphabetic word split by a visible end-of-line
    # hyphen. This is the exact TeX layout observed for Mathemat- / ica.
    compact_blocks = [compact_bibliography_block(block) for page in blocks_by_page for block in page]
    missing = [
        phrase
        for phrase in phrases
        if not any(compact_text(phrase) in block for block in compact_blocks)
    ]
    require(not missing, f"{label} required PDF phrases missing within individual text blocks: {missing}")


def compact_bibliography_block(block: str) -> str:
    return compact_text(re.sub(r"(?<=[A-Za-z])-\s*\n\s*(?=[A-Za-z])", "", block))
BIBLIOGRAPHY_ENTRY_TOKENS = [
    ("Boolos2000", ("Boolos", "George", "2000", "Must we believe in set theory?")),
    ("Hume1740", ("Hume", "David", "1739", "A Treatise of Human Nature")),
    ("Montague1961", ("Montague", "Richard", "1961", "Semantic closure and non-finite axiomatizability I")),
    ("WhiteheadRussell1910", ("Whitehead", "Alfred", "Bertrand", "Russell", "1910", "Principia Mathematica")),
]
EXPECTED_FORMULA_SLOT_FRAGMENTS = [
    "ϕ∧ψ→χ",
    "ϕ→ψ",
    "χ∧θ",
    "γ∨δ",
    "ϕ→(ψ∧χ)",
    "ϕ=ψ",
    "χ=θ",
    "γ∧δ",
    "A=B",
    "α=β",
]

FORMULA_FIXTURE = r'''
\olgreekformulas
\noindent فرمول‌های زیر آزمونِ رفتارِ نمادها هستند.
!!{formula} و !!a{formula} و !!^a{formula} و !!{element}.
نشانهٔ تعجب در متن ! و فاکتوریل در ریاضی $5\mathexclaim=120$ و $\fact{5}=120$.
وجودِ یگانه: $\lexists![x][P(x)]$.
\[
!A \land !B \lif !C
\]
\begin{align*}
!A \lif !B & \quad !C \land !D \\
!G \lor !H & \quad !A \lif (!B \land !C)
\end{align*}
\begin{multline*}
!A(x) \land !B(y) \land {}\\
!C(z) \land !D(w).
\end{multline*}
\begin{eqnarray*}
!A&=&!B\\
!C&=&!D
\end{eqnarray*}
\begin{gather*}
!G\land !H\\
!A_{g_{k-1}}(x)\lif !A^N
\end{gather*}
\[\begin{aligned}!A&=!B\\!C&=!D\end{aligned}\]
\[\begin{array}{cc}!A&!B\\!C&!D\end{array}\]
\begin{equation}!A\quad\text{در متنِ درونِ فرمول $!B$}\tag{آزمون $!C$}\end{equation}
\begin{tabular}{cc}
$!A$ & $!B$\\
$!C$ & $!D$
\end{tabular}
\par
\ollatinformulas
\begin{align*}!A&=!B\end{align*}
\olalphagreekformulas
\begin{align*}!A&=!B\end{align*}
\olgreekformulas
'''


def _mapping(value: object, label: str) -> dict[str, object]:
    require(isinstance(value, dict), f"{label} must be an object")
    return value


def bibliography_blocks(text: str) -> list[tuple[str, str]]:
    pattern = re.compile(
        r"(?ms)^\\bibitem\[(.*?)\]\{([^}]+)\}\r?\n"
        r"(.*?)(?=^\\bibitem\[|^\\end\{thebibliography\})"
    )
    return [
        (match.group(2), match.group(0).replace("\r\n", "\n"))
        for match in pattern.finditer(text)
    ]


def reconstructed_driver_bytes() -> bytes:
    # Match Path.read_text(newline=None) in make_runtime_probe.py exactly: its
    # universal-newline reader normalizes CRLF/CR inputs before assembly.
    live_source = read_file_text(LIVE_DRIVER).replace("\r\n", "\n").replace("\r", "\n")
    live_preamble, separator, _live_body = live_source.partition(r"\begin{document}")
    require(bool(separator), "live standalone driver has no document boundary")
    raw_bbl = read_file_text(HISTORIC_BBL).replace("\r\n", "\n").replace("\r", "\n")
    bbl_parts = re.split(r"(?=\\bibitem\[)", raw_bbl)
    selected_entries: list[str] = []
    for key in EXPECTED_BIBLIOGRAPHY_KEYS:
        hits = [part for part in bbl_parts[1:] if re.search(r"\]\{" + re.escape(key) + r"\}", part)]
        require(len(hits) == 1, f"historic BBL key is missing or duplicated: {key}")
        selected_entries.append(hits[0].split(r"\end{thebibliography}", 1)[0])
    sample = bbl_parts[0].replace("{131}", "{4}", 1) + "".join(selected_entries) + "\\end{thebibliography}\n"
    wrapper_start = r"\begingroup" + "\n" + r"\begin{otherlanguage}{english}"
    wrapper_end = r"\end{otherlanguage}" + "\n" + r"\endgroup"
    require(wrapper_start in live_source and wrapper_end in live_source, "live driver bibliography wrapper changed")
    bibliography_wrapper = live_source[
        live_source.index(wrapper_start) : live_source.index(wrapper_end) + len(wrapper_end)
    ]
    require(r"\bibliography{standalone-bibliography}" in bibliography_wrapper, "live driver bibliography command changed")
    bibliography_wrapper = bibliography_wrapper.replace(r"\bibliography{standalone-bibliography}", sample)
    return (
        live_preamble
        + r"\begin{document}"
        + "\n"
        + r"\section*{آزمون پیش از اصلاح}"
        + FORMULA_FIXTURE
        + r"\clearpage"
        + "\n"
        + r"\input{standalone/runtime-fixes.tex}"
        + "\n"
        + r"\section*{آزمون پس از اصلاح}"
        + FORMULA_FIXTURE
        + r"\clearpage"
        + "\n"
        + bibliography_wrapper
        + "\n"
        + r"\end{document}"
        + "\n"
    ).encode("utf-8")


def validate_fixture() -> tuple[dict[str, object], list[tuple[str, str]]]:
    fixture = _mapping(load_json(FIXTURE_MANIFEST), "runtime fixture manifest")
    require(fixture.get("schema") == "standalone-runtime-probe-fixture-v1", "runtime fixture schema mismatch")
    require(fixture.get("output") == DRIVER.relative_to(ROOT).as_posix(), "runtime fixture output path changed")
    require(fixture.get("sha256") == sha256_file(DRIVER), "runtime fixture output hash is stale")
    require(fixture.get("bytes") == file_size(DRIVER), "runtime fixture byte count is stale")
    require(fixture.get("bbl_sha256") == HISTORIC_BBL_SHA256, "runtime fixture BBL identity changed")
    require(fixture.get("bibliography_keys") == EXPECTED_BIBLIOGRAPHY_KEYS, "runtime fixture bibliography key order changed")
    require(fixture.get("tex_run") is False and fixture.get("not_full_reader") is True, "runtime fixture scope claims changed")
    require(sha256_file(RUNTIME_FIXES) == RUNTIME_FIXES_SHA256, "runtime-fixes identity changed")
    require(HISTORIC_BBL.is_file(), "historic pinned BBL is missing")
    require(sha256_file(HISTORIC_BBL) == HISTORIC_BBL_SHA256, "historic pinned BBL hash mismatch")

    expected_driver = reconstructed_driver_bytes()
    require(
        read_file_bytes(DRIVER) == expected_driver,
        "runtime fixture is stale or differs from the independently reconstructed live-driver probe",
    )
    require(
        fixture.get("driver_sha256") == sha256_file(LIVE_DRIVER),
        "runtime fixture manifest is stale relative to the live driver",
    )

    source = read_file_text(DRIVER)
    require(source.count(r"\section*{آزمون پیش از اصلاح}") == 1, "pre-fix control heading changed")
    require(source.count(r"\section*{آزمون پس از اصلاح}") == 1, "post-fix control heading changed")
    require(source.count(r"\input{standalone/runtime-fixes.tex}") == 1, "runtime fix must be loaded exactly once")
    require(
        source.index(r"\section*{آزمون پیش از اصلاح}")
        < source.index(r"\input{standalone/runtime-fixes.tex}")
        < source.index(r"\section*{آزمون پس از اصلاح}"),
        "runtime-fix load is not between the control sections",
    )
    require(source.count(r"\begin{thebibliography}{4}") == 1, "embedded bibliography width/count changed")
    require(not re.search(r"\\(?:bibliography|bibliographystyle|cite|nocite)\b", source), "runtime fixture gained external bibliography commands")

    embedded = bibliography_blocks(source)
    historic = dict(bibliography_blocks(read_file_text(HISTORIC_BBL)))
    require([key for key, _block in embedded] == EXPECTED_BIBLIOGRAPHY_KEYS, "embedded bibliography keys changed")
    for key, block in embedded:
        require(key in historic, f"pinned historic BBL lacks bibliography key: {key}")
        require(block == historic[key], f"embedded bibliography entry differs from pinned BBL: {key}")
    return fixture, embedded


def validate_log_marker(text: str) -> None:
    marker = "OL-STANDALONE-BANG-FALLBACK|guarded"
    marker_lines = [
        line for line in text.splitlines()
        if line.startswith("OL-STANDALONE-BANG-FALLBACK|")
    ]
    require(
        marker_lines == [marker],
        f"Babel bang fallback marker is missing, malformed, duplicated, or has siblings: {marker_lines!r}",
    )
    for forbidden in (
        "Expected Babel bang fallback missing",
        "Token formula undefined",
        "Token element undefined",
        "Undefined control sequence",
    ):
        require(forbidden not in text, f"forbidden runtime probe log diagnostic: {forbidden}")


def _page_index(pages: list[str], heading: str) -> int:
    needle = compact_text(heading)
    hits = [
        (index, compact_text(page).count(needle))
        for index, page in enumerate(pages)
        if needle in compact_text(page)
    ]
    require(
        sum(count for _index, count in hits) == 1,
        f"PDF heading must occur exactly once: {heading!r}; hits={hits}",
    )
    return hits[0][0]


def validate_pdf_pages(
    pages: list[str], blocks_by_page: list[list[str]],
    lines_by_page: list[list[dict[str, object]]],
) -> dict[str, object]:
    require(
        len(pages) == len(blocks_by_page) == len(lines_by_page),
        "PDF page/block/line extraction lengths disagree",
    )
    before_index = _page_index(pages, "آزمون پیش از اصلاح")
    after_index = _page_index(pages, "آزمون پس از اصلاح")
    bibliography_index = _page_index(pages, "کتاب‌نامه")
    require(before_index < after_index < bibliography_index, "runtime diagnostic section order changed")
    before_pages = pages[before_index:after_index]
    after_pages = pages[after_index:bibliography_index]
    bibliography_pages = pages[bibliography_index:]
    after_blocks = blocks_by_page[after_index:bibliography_index]
    bibliography_blocks_by_page = blocks_by_page[bibliography_index:]
    before_text = "\n".join(before_pages)
    after_text = "\n".join(after_pages)
    bibliography_text = "\n".join(bibliography_pages)

    require_runtime_phrases_in_blocks(after_blocks, REQUIRED_POST_PHRASES, "runtime post-fix section")
    after_compact = compact_text(after_text)
    require(after_compact.count("فرمول") >= 4, "localized formula token output is missing")
    require("عضو" in after_compact, "localized element token output is missing")
    lowered = after_text.casefold()
    for leaked in ("!!", "{formula}", "{element}"):
        require(leaked not in lowered, f"raw token shorthand leaked into post-fix PDF: {leaked}")
    for leaked in ("!A", "!B", "!C", "!D", "!G", "!H"):
        require(leaked not in after_compact, f"math shorthand leaked after fix: {leaked}")

    compact_after_blocks = [compact_text(block) for page in after_blocks for block in page]
    missing_formula_slots = [
        fragment
        for fragment in EXPECTED_FORMULA_SLOT_FRAGMENTS
        if not any(compact_text(fragment) in block for block in compact_after_blocks)
    ]
    require(
        not missing_formula_slots,
        f"post-fix formula symbols are not bound to their expected semantic slots: {missing_formula_slots}",
    )

    after_counts = Counter(character for character in after_text if character in FORMULA_GLYPH_ALPHABET)
    require(after_counts == EXPECTED_POST_FORMULA_GLYPHS, f"post-fix formula glyph counts changed: {after_counts!r}")
    require(after_text.count("!") == 4, "post-fix literal/factorial/unique-existence bang count changed")
    require(after_text.count("∃") == 1, "post-fix unique-existence quantifier count changed")

    before_counts = Counter(character for character in before_text if character in CONTROL_ALPHABET)
    after_control_counts = Counter(character for character in after_text if character in CONTROL_ALPHABET)
    require(before_counts != after_control_counts, "pre-fix control does not differ from guarded post-fix output")
    require(
        any(
            re.search(r"![\u200c\u200d\u200e\u200f\u2066-\u2069]*[ABCDGH]", block)
            for page in blocks_by_page[before_index:after_index]
            for block in page
        ),
        "pre-fix control lacks an adjacent extracted ![ABCDGH] shorthand-corruption witness",
    )

    require_bibliography_phrases_in_blocks(
        bibliography_blocks_by_page, REQUIRED_BIBLIOGRAPHY_PHRASES, "runtime bibliography",
    )
    entry_locations: dict[str, dict[str, int]] = {}
    for key, tokens in BIBLIOGRAPHY_ENTRY_TOKENS:
        hits: list[tuple[int, int]] = []
        for page_index, page_blocks in enumerate(blocks_by_page[bibliography_index:], start=bibliography_index):
            for block_index, block in enumerate(page_blocks):
                compact_block = compact_bibliography_block(block)
                if all(compact_text(token) in compact_block for token in tokens):
                    hits.append((page_index, block_index))
        require(len(hits) == 1, f"bibliography entry token set must identify exactly one block: {key}; hits={hits}")
        entry_locations[key] = {"page_one_based": hits[0][0] + 1, "block_zero_based": hits[0][1]}
    bibliography_lines = [
        line
        for page_lines in lines_by_page[bibliography_index:]
        for line in page_lines
        if re.search(r"[A-Za-z]", str(line.get("text", "")))
    ]
    require(bibliography_lines, "runtime bibliography has no extractable Latin-script lines")
    for line in bibliography_lines:
        direction = line.get("direction")
        require(
            isinstance(direction, list)
            and len(direction) == 2
            and abs(float(direction[0]) - 1.0) < 1e-6
            and abs(float(direction[1])) < 1e-6,
            f"bibliography Latin line is not laid out left-to-right: {line.get('text')!r}",
        )
    bibliography_entry_count = len(entry_locations)
    require(bibliography_entry_count == 4, "not exactly four expected bibliography author/year entries are extractable")
    require("??" not in after_text and "??" not in bibliography_text, "unresolved placeholder leaked into accepted probe regions")
    return {
        "pages": len(pages),
        "section_start_pages_one_based": {
            "pre_fix": before_index + 1,
            "post_fix": after_index + 1,
            "bibliography": bibliography_index + 1,
        },
        "post_fix_formula_glyph_counts": dict(sorted(after_counts.items())),
        "post_fix_bang_count": after_text.count("!"),
        "post_fix_exists_count": after_text.count("∃"),
        "pre_fix_control_differs": True,
        "formula_semantic_slot_fragments": len(EXPECTED_FORMULA_SLOT_FRAGMENTS),
        "bibliography_entries_detected": bibliography_entry_count,
        "bibliography_entry_block_locations": entry_locations,
        "bibliography_ltr_lines_checked": len(bibliography_lines),
    }


def validate_auxiliary(primary: Path, common: dict[str, object]) -> dict[str, object]:
    aux = primary / f"{JOB}.aux"
    aux_snapshot = require_bound_output(common, aux)
    text = read_file_text(aux)
    bibcite = re.findall(r"^\\bibcite\{([^}]+)\}", text, re.MULTILINE)
    require(bibcite == EXPECTED_BIBLIOGRAPHY_KEYS, f"runtime auxiliary bibliography keys changed: {bibcite!r}")
    require(not re.search(r"^\\(?:citation|bibdata|bibstyle)\{", text, re.MULTILINE), "runtime probe unexpectedly requested BibTeX")
    for suffix in ("bbl", "blg", "bcf"):
        require(not (primary / f"{JOB}.{suffix}").exists(), f"runtime probe produced external bibliography artifact: .{suffix}")
    return {
        "path": relative_repo_path(aux),
        "sha256": aux_snapshot.sha256,
        "bibcite_keys": bibcite,
        "bibtex_input_commands": 0,
    }


def validate(receipt_path: Path) -> dict[str, object]:
    clear_snapshot_cache()
    fixture, embedded_bibliography = validate_fixture()
    common = validate_diagnostic_receipt(
        receipt_path,
        job=JOB,
        driver=DRIVER,
        driver_sha256=str(fixture["sha256"]),
        allow_reference_warnings=False,
        allow_latex_rerun_warnings=True,
    )
    validate_log_marker(common["log_text"])

    inputs = common["recorder_inputs"]
    require_recorder_inputs(inputs, (DRIVER, RUNTIME_FIXES))
    forbidden_inputs = [path for path in inputs if path.suffix.casefold() in {".bib", ".bst", ".bbl", ".blg", ".bcf"}]
    require(not forbidden_inputs, "runtime probe read an external bibliography input")
    auxiliary = validate_auxiliary(common["primary"], common)

    pages, blocks_by_page, lines_by_page, fitz_version, page_geometry = load_pdf_text(common["pdf"])
    require(len(pages) >= 3, "runtime diagnostic has too few pages for two controls and bibliography")
    pdf_checks = validate_pdf_pages(pages, blocks_by_page, lines_by_page)
    pdf_text = "\n\f\n".join(pages)

    evidence = base_evidence(
        kind="babel-bang-runtime",
        common=common,
        fixture=DRIVER,
        fixture_manifest=FIXTURE_MANIFEST,
    )
    evidence.update(
        {
            "schema": "farsi-standalone-runtime-native-probe-qa-v1",
            "status": "PASS_NATIVE_DIAGNOSTIC_CONTRAST_PENDING_COMPLETE_VISUAL_INSPECTION_NOT_FULL_READER",
            "dependencies": [
                {
                    "path": relative_repo_path(path),
                    "bytes": file_size(path),
                    "sha256": sha256_file(path),
                }
                for path in (DRIVER, RUNTIME_FIXES, HISTORIC_BBL)
            ],
            "runtime_marker": "OL-STANDALONE-BANG-FALLBACK|guarded",
            "bibliography": {
                "source_bbl_sha256": HISTORIC_BBL_SHA256,
                "embedded_entry_keys": [key for key, _block in embedded_bibliography],
                "embedded_entry_sha256": {
                    key: hashlib.sha256(block.encode("utf-8")).hexdigest()
                    for key, block in embedded_bibliography
                },
                "pdf_entries_detected": pdf_checks["bibliography_entries_detected"],
                "external_bibtex_workers_or_inputs": 0,
            },
            "auxiliary": auxiliary,
            "pdf_text": {
                **pdf_checks,
                "extracted_text_sha256": sha256_bytes(pdf_text.encode("utf-8")),
                "pymupdf_version": fitz_version,
                "page_geometry": page_geometry,
            },
            "checks": {
                "guarded_fallback_marker_exactly_once": True,
                "pre_fix_control_exhibits_expected_corruption": True,
                "post_fix_formula_glyph_multiset_exact": True,
                "post_fix_raw_shorthand_absent": True,
                "localized_text_tokens_present": True,
                "embedded_bibliography_entries_match_pinned_bbl": True,
                "auxiliary_bibcite_key_order_exact": True,
                "external_bibtex_commands_workers_inputs_and_artifacts_absent": True,
                "guard_mutex_tree_exit_and_log_receipt_recomputed": True,
            },
            "limitations": [
                "The deliberately defective pre-fix section is a control, not acceptable reader content; only the post-fix section is required to have the exact corrected glyph multiset.",
                "PDF text extraction is not visual-layout evidence. Every diagnostic page still requires rendered full-page inspection.",
                "This diagnostic does not qualify the complete 722-unit reader.",
            ],
        }
    )
    return evidence


def self_test() -> dict[str, object]:
    valid_log = "OL-STANDALONE-BANG-FALLBACK|guarded\n"
    validate_log_marker(valid_log)
    expect_validation_error(validate_log_marker, valid_log + valid_log)
    expect_validation_error(
        validate_log_marker,
        valid_log + "OL-STANDALONE-BANG-FALLBACK|unguarded\n",
    )
    expect_validation_error(validate_log_marker, "")
    expect_validation_error(validate_log_marker, valid_log + "Undefined control sequence")

    post = "\n".join(REQUIRED_POST_PHRASES)
    semantic_formula = " ".join(EXPECTED_FORMULA_SLOT_FRAGMENTS)
    used_counts = Counter(character for character in semantic_formula if character in FORMULA_GLYPH_ALPHABET)
    require(
        all(used_counts[character] <= count for character, count in EXPECTED_POST_FORMULA_GLYPHS.items()),
        "self-test semantic formula overuses glyphs",
    )
    remainder = "".join(
        character * (count - used_counts[character])
        for character, count in EXPECTED_POST_FORMULA_GLYPHS.items()
    )
    post += "\n" + semantic_formula + remainder
    # One required prose phrase contains one literal bang; add the remaining
    # factorial and unique-existence control glyphs without joining them to A-H.
    post += "\n! ! ! ∃ عضو فرمول فرمول فرمول فرمول"
    before = "آزمون پیش از اصلاح\n!A !B !C !D !G !H\n" + post.replace("آزمون پس از اصلاح", "")
    bibliography = "کتاب‌نامه\n" + "\n".join(
        " ".join(tokens) for _key, tokens in BIBLIOGRAPHY_ENTRY_TOKENS
    )
    pages = [before, post, bibliography]
    synthetic_lines = [
        [{"text": page, "direction": [1.0, 0.0], "bbox": [1.0, 1.0, 2.0, 2.0]}]
        for page in pages
    ]
    result = validate_pdf_pages(pages, [[page] for page in pages], synthetic_lines)
    require(result["post_fix_formula_glyph_counts"] == dict(sorted(EXPECTED_POST_FORMULA_GLYPHS.items())), "self-test glyph receipt mismatch")

    extraction_variant = "\n".join(
        pymupdf_marked_base_omission_variant(phrase)
        for phrase in REQUIRED_POST_PHRASES
    )
    require_runtime_phrases_in_blocks(
        [[extraction_variant]], REQUIRED_POST_PHRASES, "runtime marked-base extraction self-test"
    )
    expect_validation_error(
        require_runtime_phrases_in_blocks,
        [[extraction_variant.replace("فاکتوریل", "", 1)]],
        REQUIRED_POST_PHRASES,
        "runtime marked-base extraction negative self-test",
    )
    split_bibliography = "Principia Mathemat-\nica\n" + "\n".join(
        phrase for phrase in REQUIRED_BIBLIOGRAPHY_PHRASES if phrase != "Principia Mathematica"
    )
    require_bibliography_phrases_in_blocks(
        [[split_bibliography]], REQUIRED_BIBLIOGRAPHY_PHRASES, "bibliography line-break self-test"
    )
    expect_validation_error(
        require_bibliography_phrases_in_blocks,
        [[split_bibliography.replace("Mathemat-\nica", "Mathemat-\nology")]],
        REQUIRED_BIBLIOGRAPHY_PHRASES,
        "bibliography line-break negative self-test",
    )

    bad_glyphs = list(pages)
    bad_glyphs[1] = bad_glyphs[1].replace("ϕ", "A", 1)
    expect_validation_error(validate_pdf_pages, bad_glyphs, [[page] for page in bad_glyphs], synthetic_lines)
    no_contrast = list(pages)
    no_contrast[0] = "آزمون پیش از اصلاح\n" + post.replace("آزمون پس از اصلاح", "")
    expect_validation_error(validate_pdf_pages, no_contrast, [[page] for page in no_contrast], synthetic_lines)
    raw_shorthand = list(pages)
    raw_shorthand[1] += "\n!A"
    expect_validation_error(validate_pdf_pages, raw_shorthand, [[page] for page in raw_shorthand], synthetic_lines)
    scattered_control = list(pages)
    scattered_control[0] = scattered_control[0].replace("!A !B !C !D !G !H", "! A ! B ! C ! D ! G ! H")
    expect_validation_error(
        validate_pdf_pages,
        scattered_control,
        [[page] for page in scattered_control],
        synthetic_lines,
    )
    swapped_slots = list(pages)
    swapped_slots[1] = swapped_slots[1].replace("ϕ∧ψ→χ", "ϕ∧χ→ψ", 1)
    expect_validation_error(
        validate_pdf_pages, swapped_slots, [[page] for page in swapped_slots], synthetic_lines,
    )

    sample_bib = (
        "\\begin{thebibliography}{1}\n"
        "\\bibitem[{A(2000)}]{A2000}\nEntry A.\n\n"
        "\\bibitem[{B(2001)}]{B2001}\nEntry B.\n"
        "\\end{thebibliography}\n"
    )
    require([key for key, _ in bibliography_blocks(sample_bib)] == ["A2000", "B2001"], "bibliography parser self-test failed")
    common_negative_controls = self_test_common_primitives()
    return {
        "schema": "farsi-runtime-postbuild-self-test-v1",
        "status": "PASS",
        "negative_controls": 11 + common_negative_controls,
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
