"""Fail-closed static and trace checks for the standalone BiDi/layout overlay.

This checker never invokes TeX. It pins every immutable source carrier and the
shared configuration, validates the additive implementation and its setup
composition, and deterministically replays both bootstrap and final traces with
adversarial mutations.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
from typing import Iterable


HERE = Path(__file__).resolve().parent
STANDALONE = HERE.parent
ROOT = HERE.parents[4]
EVIDENCE = ROOT / "evidence/STANDALONE_BIDI_LAYOUT_QA.json"

SOURCE_0371 = ROOT / (
    "source/locale/fa-IR/content/lambda-calculus/church-rosser/"
    "parallel-beta-eta-reduction.tex"
)
SURNAME_SOURCES = {
    "OLP-0394": ROOT
    / "source/locale/fa-IR/content/many-valued-logic/three-valued-logics/lukasiewicz.tex",
    "OLP-0396": ROOT
    / "source/locale/fa-IR/content/many-valued-logic/three-valued-logics/goedel.tex",
    "OLP-0397": ROOT
    / "source/locale/fa-IR/content/many-valued-logic/three-valued-logics/multiple-designation.tex",
    "OLP-0400": ROOT
    / "source/locale/fa-IR/content/many-valued-logic/infinite-valued-logics/lukasiewicz.tex",
    "OLP-0404": ROOT
    / "source/locale/fa-IR/content/many-valued-logic/sequent-calculus/rules-and-proofs.tex",
    "OLP-0406": ROOT
    / "source/locale/fa-IR/content/many-valued-logic/sequent-calculus/propositional-rules.tex",
}
SURNAME_SOURCE_COUNTS = {
    "OLP-0394": 11,
    "OLP-0396": 3,
    "OLP-0397": 1,
    "OLP-0400": 5,
    "OLP-0404": 1,
    "OLP-0406": 4,
}
SURNAME_RENDER_COUNTS = {
    "OLP-0394": 12,
    "OLP-0396": 3,
    "OLP-0397": 1,
    "OLP-0400": 6,
    "OLP-0404": 1,
    "OLP-0406": 4,
}
SURNAME_DEFERRED_COUNTS = {
    "OLP-0394": 1,
    "OLP-0396": 0,
    "OLP-0397": 0,
    "OLP-0400": 0,
    "OLP-0404": 0,
    "OLP-0406": 0,
}
HEADING_UNITS = ("OLP-0394", "OLP-0400")
HEADING_COMMANDS = {"OLP-0394": "first", "OLP-0400": "second"}
SETUP_NAMES = {
    "OLP-0371": "church_rosser",
    "OLP-0394": "lukasiewicz_finite",
    "OLP-0396": "goedel",
    "OLP-0397": "multiple_designation",
    "OLP-0400": "lukasiewicz_infinite",
    "OLP-0404": "sequent_rules",
    "OLP-0406": "propositional_rules",
    "OLP-0429": "normal_logics",
}
SOURCE_0429 = ROOT / (
    "source/locale/fa-IR/content/normal-modal-logic/axioms-systems/normal-logics.tex"
)
MASTER_CONFIG = ROOT / "source/open-logic-config.sty"
LOCALE_CONFIG = ROOT / "source/locale/fa-IR/open-logic-config.sty"
OPEN_LOGIC_STYLE = ROOT / "source/sty/open-logic.sty"
DEFER_STYLE = ROOT / "source/sty/open-logic-defer.sty"
MODULE = STANDALONE / "bidi-layout.tex"
BODY = STANDALONE / "body.tex"
RUNTIME = STANDALONE / "runtime.tex"
LEDGER = STANDALONE / "generated-ledger.tex"
CHECKER = Path(__file__).resolve()

PINNED = {
    SOURCE_0371: (
        4301,
        "9e04a817c2d0b41e1ed2464a25a1e87ce46eed6aff7c82bb4c29957e33e61663",
    ),
    SURNAME_SOURCES["OLP-0394"]: (
        12507,
        "06a61a20946f0aa52833b28b64bc06088a3da5dc1056c1bb2229226dd7176191",
    ),
    SURNAME_SOURCES["OLP-0396"]: (
        4848,
        "b10f79be19a3ea0f576acc9ffb40d9e1842d15b8883e1ed1c315b451bd63207b",
    ),
    SURNAME_SOURCES["OLP-0397"]: (
        10705,
        "03cd087819cf1b43bc73467df7e0646674bde8c01d99b72ead20a112d43ceba0",
    ),
    SURNAME_SOURCES["OLP-0400"]: (
        3552,
        "8b470101e82cf7d03f8940ddbcdbd5df16cce2b353f4c0c5b88139524b0cd0aa",
    ),
    SURNAME_SOURCES["OLP-0404"]: (
        4192,
        "1d88521f5dd3a4126c7cf48b53ebc7656d1970a5393bbcbf19d44a1c16efbee0",
    ),
    SURNAME_SOURCES["OLP-0406"]: (
        8376,
        "b557c5a5d70ab08804e51ea39bdf696e9652f077c69cb153afc6d53d26fe3257",
    ),
    SOURCE_0429: (
        6082,
        "6bb32bc7ecc9e8ddf99ad94a4e63541c691328522f9695efcd94e0592e013395",
    ),
    MASTER_CONFIG: (
        52113,
        "ab19be71b50b415738603290317b504d9fa6b82850fe640d585c62db1540ced3",
    ),
    LOCALE_CONFIG: (
        6879,
        "c8df8c39abbd1ab36dbac380490b72e9b3c565bbd1ec3d1f1be88bdc300abd0b",
    ),
    OPEN_LOGIC_STYLE: (
        11069,
        "556675a5ddfc00999dae90da0272ca0e33004866823aec6efb33ffe0a410dcbf",
    ),
    DEFER_STYLE: (
        5083,
        "5fec681f627ac0b840ed02958a9edabe90962a4f66c2972b94a7a704daad81f6",
    ),
}

# Twenty-two contracts always run. Two TOC replay contracts are registered at
# Start only after an exact read-only inventory of the preexisting TOC.
BASE_RULES = [
    ("OLP-0371", "setup", 1),
    ("OLP-0371", "align-ltr-before", 1),
    ("OLP-0371", "align-ltr-after", 1),
    ("OLP-0371", "second-proof-emergency-stretch", 1),
    ("OLP-0394", "setup", 1),
    ("OLP-0394", "lukasiewicz-name-source-ltr", 11),
    ("OLP-0396", "setup", 1),
    ("OLP-0396", "lukasiewicz-name-source-ltr", 3),
    ("OLP-0397", "setup", 1),
    ("OLP-0397", "lukasiewicz-name-source-ltr", 1),
    ("OLP-0400", "setup", 1),
    ("OLP-0400", "lukasiewicz-name-source-ltr", 5),
    ("OLP-0404", "setup", 1),
    ("OLP-0404", "lukasiewicz-name-source-ltr", 1),
    ("OLP-0406", "setup", 1),
    ("OLP-0406", "lukasiewicz-name-source-ltr", 4),
    ("OLP-0429", "setup", 1),
    ("OLP-0429", "native-display-semicolon", 1),
    ("OLP-0429", "tag-ltr", 2),
    ("OLP-0429", "dual-ltr", 2),
    ("OLP-0429", "rk-ltr", 2),
    ("OLP-0429", "first-proof-left-qed", 1),
]
TOC_RULES = [
    ("OLP-0394", "lukasiewicz-name-toc-ltr", 1),
    ("OLP-0400", "lukasiewicz-name-toc-ltr", 1),
]
FINAL_RULES = BASE_RULES + TOC_RULES
BASE_COUNTS = {(unit, event): count for unit, event, count in BASE_RULES}
FINAL_COUNTS = {(unit, event): count for unit, event, count in FINAL_RULES}
BASE_EVENTS = sum(BASE_COUNTS.values())
FINAL_EVENTS = sum(FINAL_COUNTS.values())


def counted_rows(unit: str, event: str, count: int) -> list[tuple[str, str, str]]:
    return [(unit, event, str(index)) for index in range(1, count + 1)]


# Final multi-pass execution order. TOC markers are read under OLP-0001 before
# target dispatch. Within OLP-0429, tagform@ records the second tag before its
# nested local Dual expands.
BASE_TRACE = [
    ("OLP-0371", "setup", "1"),
    ("OLP-0371", "align-ltr-before", "1"),
    ("OLP-0371", "align-ltr-after", "1"),
    ("OLP-0371", "second-proof-emergency-stretch", "1"),
]
for _unit in SURNAME_SOURCES:
    BASE_TRACE.append((_unit, "setup", "1"))
    BASE_TRACE.extend(
        counted_rows(
            _unit,
            "lukasiewicz-name-source-ltr",
            SURNAME_SOURCE_COUNTS[_unit] - SURNAME_DEFERRED_COUNTS[_unit],
        )
    )
    # The sole deferred OLP-0394 problem is read after the remaining chapter-52
    # units, including the later OLP-0396 and OLP-0397 surname targets.
    if _unit == "OLP-0397":
        BASE_TRACE.append(("OLP-0394", "lukasiewicz-name-source-ltr", "11"))
BASE_TRACE.extend(
    [
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
)
FINAL_TRACE = [
    ("OLP-0394", "lukasiewicz-name-toc-ltr", "1"),
    ("OLP-0400", "lukasiewicz-name-toc-ltr", "1"),
    *BASE_TRACE,
]
assert len(BASE_RULES) == 22 and BASE_EVENTS == len(BASE_TRACE) == 44
assert len(FINAL_RULES) == 24 and FINAL_EVENTS == len(FINAL_TRACE) == 46


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def exactly(text: str, needle: str, count: int = 1) -> None:
    actual = text.count(needle)
    assert actual == count, f"expected {count} occurrence(s) of {needle!r}, got {actual}"


def check_pins() -> None:
    for path, (size, sha256) in PINNED.items():
        data = path.read_bytes()
        assert len(data) == size, f"pinned size changed: {rel(path)}"
        assert digest(data) == sha256, f"pinned SHA-256 changed: {rel(path)}"


def check_source_shape(
    source_0371: str,
    surname_sources: dict[str, str],
    source_0429: str,
) -> None:
    exactly(source_0371, r"\begin{align}")
    exactly(source_0371, r"\end{align}")
    exactly(source_0371, r"\begin{align*}", 0)
    assert source_0371.index(r"\begin{align}") < source_0371.index(r"\end{align}")
    proof_bodies = re.findall(
        r"\\begin\{proof\}(.*?)\\end\{proof\}", source_0371, re.S
    )
    assert len(proof_bodies) == 4, "OLP-0371 proof ordinals changed"
    target_marker = r"\olref[pb]{lem:comp}"
    assert [target_marker in body for body in proof_bodies] == [
        False,
        True,
        False,
        False,
    ], "OLP-0371 overflow paragraph is no longer confined to proof 2"
    exactly(source_0371, r"\emergencystretch", 0)

    assert set(surname_sources) == set(SURNAME_SOURCE_COUNTS)
    for unit, expected in SURNAME_SOURCE_COUNTS.items():
        source = surname_sources[unit]
        exactly(source, r"\L ukasiewicz", expected)
        assert len(re.findall(r"\\L(?![A-Za-z@])", source)) == expected, (
            f"{unit} has a bare or non-name \\L occurrence"
        )
        exactly(source, "Łukasiewicz", 0)
        exactly(
            source,
            r"\olsection{منطق \L ukasiewicz}",
            1 if unit in HEADING_UNITS else 0,
        )
        problem_bodies = re.findall(
            r"\\begin\{prob\}(.*?)\\end\{prob\}", source, re.S
        )
        deferred = sum(body.count(r"\L ukasiewicz") for body in problem_bodies)
        assert deferred == SURNAME_DEFERRED_COUNTS[unit], (
            f"{unit} deferred surname topology changed"
        )
        if unit == "OLP-0394":
            assert len(problem_bodies) == 5
    assert sum(text.count(r"\L ukasiewicz") for text in surname_sources.values()) == 25

    exactly(source_0429, "\\]؛")
    exactly(source_0429, r"\tag{\Ax{K}}")
    exactly(source_0429, r"\tag{\Dual}")
    exactly(source_0429, r"\Dual", 2)
    exactly(source_0429, r"\RK", 2)
    exactly(source_0429, r"\begin{align*}", 2)
    exactly(source_0429, r"\end{align*}", 2)
    exactly(source_0429, r"\begin{proof}", 2)
    exactly(source_0429, r"\end{proof}", 2)
    proof_tail = re.findall(r"\\end\{align\*\}\s*\\end\{proof\}", source_0429)
    assert len(proof_tail) == 1, "first display-ended proof trigger is not unique"
    ordered = [
        source_0429.index("\\]؛"),
        source_0429.index(r"\Dual"),
        source_0429.index(r"\tag{\Ax{K}}"),
        source_0429.index(r"\tag{\Dual}"),
        source_0429.index(r"\RK"),
        source_0429.index(r"\begin{proof}"),
    ]
    assert ordered == sorted(ordered), "OLP-0429 trigger order changed"


def check_configs(master: str, locale: str, style: str, defer: str) -> None:
    exactly(master, r"\DeclareDocumentMacro \RK {\textsc{rk}}")
    exactly(master, r"\DeclareDocumentMacro \Dual {\textsc{dual}}")
    exactly(master, r"\DeclareDocumentMacro {\LogLuk} {\Log{\textbf{\L}}}")
    exactly(locale, r"\providecommand*{\olFaLTR}[1]")
    assert r"\foreignlanguage{english}{\babelsublr{#1}}" in locale
    exactly(style, r"\RequirePackage[thmmarks,amsmath,amsthm,hyperref]{ntheorem}")
    exactly(defer, r"\renewenvironment{probdeferred}[1]{\begin{probd}}{\end{probd}}")
    exactly(defer, r"\string\renewcommand*\string\theolpart{\theolpart}")
    exactly(defer, r"\string\renewcommand*\string\theolchapter{\theolchapter}")
    exactly(defer, r"\string\renewcommand*\string\theolsection{\theolsection}")
    exactly(defer, r"\Readsolutionfile{\jobname}", 2)


def check_ledger(ledger: str) -> None:
    for unit in ["OLP-0371", *SURNAME_SOURCES, "OLP-0429"]:
        exactly(ledger, rf"\OLSADeclareUnit{{{unit}}}")
        exactly(ledger, f"{unit}/FOL")
        exactly(ledger, f"{unit}/PL", 0)


def parse_rule_contract(module: str) -> list[tuple[str, str, int]]:
    return [
        (unit, event, int(count))
        for unit, event, count in re.findall(
            r"\\OLSABidiLayoutExpect\s*\{(OLP-\d{4})\}\s*\{([^{}]+)\}\s*\{(\d+)\}",
            module,
        )
    ]


def protected_macro_body(module: str, name: str) -> str:
    match = re.search(
        rf"\\cs_new_protected:Npn \\{re.escape(name)}(?:\s+[^\n]+)?\s*\n? \{{(.*?)\n \}}",
        module,
        re.S,
    )
    assert match, f"missing protected macro: {name}"
    return match.group(1)


def check_module(module: str) -> None:
    digit_bearing_control_words = sorted(
        set(re.findall(r"\\[A-Za-z@:_]*\d+[A-Za-z0-9@:_]*", module))
    )
    assert not digit_bearing_control_words, (
        "TeX control-word spellings must not contain digits; TeX terminates "
        f"the name before them: {digit_bearing_control_words}"
    )
    for identifier in (
        r"\l_olsa_bidi_layout_toc_first_int",
        r"\l_olsa_bidi_layout_toc_second_int",
    ):
        exactly(module, identifier, 3)

    # Dynamic TOC registrations occur textually before the unconditional block.
    assert parse_rule_contract(module) == TOC_RULES + BASE_RULES
    assert len(re.findall(r"\\OLSABidiLayoutExpect(?![A-Za-z@:_])", module)) == 25
    target_units = ["OLP-0371", *SURNAME_SOURCES, "OLP-0429"]
    setup_calls = re.findall(r"\\OLSADeclareSetup\s*\{(OLP-\d{4})\}", module)
    assert setup_calls == target_units, "target setup calls changed"
    assert len(re.findall(r"\\OLSADeclareSetup(?![A-Za-z@:_])", module)) == 8
    for unit, setup_name in SETUP_NAMES.items():
        exactly(
            module,
            rf"\OLSADeclareSetup{{{unit}}}{{\olsa_bidi_layout_setup_{setup_name}:}}",
        )

    for token in (
        r"\NewCommandCopy \olsa_bidi_layout_original_display_end: \]",
        r"\NewCommandCopy \olsa_bidi_layout_original_proof: \proof",
        r"\NewCommandCopy \olsa_bidi_layout_original_olsection: \olsection",
        r"\NewCommandCopy \olsa_bidi_layout_original_l: \L",
        r"\peek_meaning_remove:NTF ؛",
        r"\text{؛}\olsa_bidi_layout_original_display_end:",
        r"\AddToHookNext{env/align/before}{\OLSAAlignLTRBefore}",
        r"\AddToHookNext{env/align/after}{\OLSAAlignLTRAfter}",
        r"\begingroup\bbl@setdirs\z@\OLSABidiLayoutRecord{align-ltr-before}",
        r"\OLSABidiLayoutRecord{align-ltr-after}\endgroup",
        r"\ifmeasuring@\else\OLSABidiLayoutRecord{#1}\fi",
        r"\maketag@@@{\olFaLTR{(\ignorespaces#1\unskip\@@italiccorr)}}",
        r"{\olFaLTR{\textsc{dual}}}",
        r"{\olFaLTR{\textsc{rk}}}\peek_catcode:NTF a {\space}{}",
        r"\AddToHookNext{env/proof/begin}{\OLSABidiLayoutFirstProofLeftQED}",
        r"\OLSABidiLayoutRecord{first-proof-left-qed}\tagsleft@true",
    ):
        exactly(module, token)

    display_end = protected_macro_body(module, "olsa_bidi_layout_display_end:")
    exactly(display_end, r"\OLSABidiLayoutRecord{native-display-semicolon}")
    exactly(display_end, r"{\olsa_bidi_layout_original_display_end:}")
    dual = protected_macro_body(module, "olsa_bidi_layout_dual:")
    exactly(dual, r"\OLSABidiLayoutRecordUnlessMeasuring{dual-ltr}")
    rk = protected_macro_body(module, "olsa_bidi_layout_rk:")
    exactly(rk, r"\OLSABidiLayoutRecord{rk-ltr}")
    exactly(rk, r"{\olFaLTR{\textsc{rk}}}\peek_catcode:NTF a {\space}{}")

    proof = protected_macro_body(module, "olsa_bidi_layout_proof_target:")
    proof_tokens = (
        r"\int_gincr:N \g_olsa_bidi_layout_proof_target_int",
        r"\int_compare:nNnT {\g_olsa_bidi_layout_proof_target_int}={2}",
        r"\OLSABidiLayoutRecord{second-proof-emergency-stretch}",
        r"\emergencystretch=16pt\relax",
        r"\olsa_bidi_layout_original_proof:",
    )
    for token in proof_tokens:
        exactly(proof, token)
    assert [proof.index(token) for token in proof_tokens] == sorted(
        proof.index(token) for token in proof_tokens
    ), "OLP-0371 proof wrapper operation order changed"

    helper = re.search(
        r"\\cs_new:Npn \\olsa_bidi_layout_lukasiewicz: ukasiewicz\s*\{(.*?)\n \}",
        module,
        re.S,
    )
    assert helper, "complete-name helper must be unprotected and exactly delimited"
    exactly(helper.group(1), r"\OLSABidiLayoutRecord{lukasiewicz-name-source-ltr}")
    exactly(helper.group(1), r"\OLSABidiLayoutLukasiewiczName")
    assert "olFaLTR" not in helper.group(1), "helper must delegate one whole renderer"

    dispatcher = protected_macro_body(module, "olsa_bidi_layout_lukasiewicz_or_original:")
    for token in (
        r"\peek_meaning:NTF u",
        r"{\olsa_bidi_layout_lukasiewicz:}",
        r"{\olsa_bidi_layout_original_l:}",
    ):
        exactly(dispatcher, token)
    assert dispatcher.index(r"\peek_meaning:NTF u") < dispatcher.index(
        r"{\olsa_bidi_layout_lukasiewicz:}"
    ) < dispatcher.index(r"{\olsa_bidi_layout_original_l:}")

    deferred_helper = re.search(
        r"\\cs_new:Npn \\olsa_bidi_layout_lukasiewicz_deferred: ukasiewicz\s*\{(.*?)\n \}",
        module,
        re.S,
    )
    assert deferred_helper, "deferred complete-name helper must be exactly delimited"
    exactly(deferred_helper.group(1), r"\olsa_bidi_layout_record:nn{OLP-0394}{lukasiewicz-name-source-ltr}")
    exactly(deferred_helper.group(1), r"\OLSABidiLayoutLukasiewiczName")
    deferred_dispatcher = protected_macro_body(
        module, "olsa_bidi_layout_lukasiewicz_deferred_or_original:"
    )
    for token in (
        r"\peek_meaning:NTF u",
        r"{\olsa_bidi_layout_lukasiewicz_deferred:}",
        r"{\olsa_bidi_layout_original_l:}",
    ):
        exactly(deferred_dispatcher, token)
    deferred_setup = protected_macro_body(module, "olsa_bidi_layout_deferred_problem_setup:")
    for token in (
        r"\tl_set:Nx \l_olsa_bidi_layout_deferred_namespace_tl",
        r"{\theolpart :\theolchapter :\theolsection}",
        r"\tl_if_eq:VnT \l_olsa_bidi_layout_deferred_namespace_tl {mvl:thr:luk}",
        r"{\cs_set_eq:NN \L \olsa_bidi_layout_lukasiewicz_deferred_or_original:}",
    ):
        exactly(deferred_setup, token)
    exactly(module, r"\AddToHook{env/probd/begin}{\olsa_bidi_layout_deferred_problem_setup:}")

    renderer = re.search(
        r"\\NewDocumentCommand \\OLSABidiLayoutLukasiewiczName \{\}\s*\{(.*?)\}",
        module,
        re.S,
    )
    assert renderer
    assert renderer.group(1).strip() == r"\olFaLTR{Łukasiewicz"
    assert "Record" not in renderer.group(1)
    exactly(
        module,
        "\\pdfstringdefDisableCommands{%\n"
        "  \\def\\OLSABidiLayoutLukasiewiczName{Łukasiewicz}}",
    )

    section = protected_macro_body(module, "olsa_bidi_layout_lukasiewicz_section:nnn")
    for token in (
        r"\IfNoValueTF{#2}",
        r"\tl_if_eq:nnTF {#3}{منطق~\L ukasiewicz}",
        r"\olsa_bidi_layout_record:nn{#1}{lukasiewicz-name-source-ltr}",
        "[منطق~\\OLSABidiLayoutLukasiewiczName]",
        "{منطق~\\OLSABidiLayoutLukasiewiczName}",
        r"\addtocontents{toc}{\protect\OLSABidiLayoutTOCReplay{#1}}",
    ):
        exactly(section, token)
    exactly(section, r"\olsa_bidi_layout_original_olsection:")
    assert section.index(r"\olsa_bidi_layout_record:nn") < section.index(
        r"\olsa_bidi_layout_original_olsection:"
    ) < section.index(r"\addtocontents{toc}")
    assert "[منطق \\OLSABidiLayoutLukasiewiczName]" not in section
    assert r"\olsa_bidi_layout_original_olsection:{#3}" not in section
    for unit in HEADING_UNITS:
        command = HEADING_COMMANDS[unit]
        exactly(module, rf"\NewDocumentCommand \olsa_bidi_layout_section_{command}: {{o m}}")
        exactly(
            module,
            rf"{{\olsa_bidi_layout_lukasiewicz_section:nnn{{{unit}}}{{#1}}{{#2}}}}",
        )

    scanner = protected_macro_body(module, "olsa_bidi_layout_register_toc_contract:")
    for token in (
        r"\file_if_exist:nTF {\jobname.toc}",
        r"\file_get:nnN {\jobname.toc} {\cctab_select:N \c_str_cctab} \l_olsa_bidi_layout_toc_tl",
        r"{OLSABidiLayoutTOCReplay\s*\{OLP-0394\}}",
        r"{OLSABidiLayoutTOCReplay\s*\{OLP-0400\}}",
        r"{OLSABidiLayoutTOCReplay\s*\{OLP-0394\}.*OLSABidiLayoutTOCReplay\s*\{OLP-0400\}}",
        r"\OLSABidiLayoutExpect{OLP-0394}{lukasiewicz-name-toc-ltr}{1}",
        r"\OLSABidiLayoutExpect{OLP-0400}{lukasiewicz-name-toc-ltr}{1}",
        "Reversed~Lukasiewicz~TOC~markers",
        "Malformed~Lukasiewicz~TOC~marker~inventory",
    ):
        assert token in scanner, f"TOC scanner lost {token!r}"
    exactly(scanner, r"\regex_count:nVN {OLSABidiLayoutTOCReplay}")
    exactly(scanner, r"\int_compare:nNnTF {\l_olsa_bidi_layout_toc_total_int}={0}")
    exactly(scanner, r"\int_compare:nNnTF {\l_olsa_bidi_layout_toc_total_int}={2}")

    marker = re.search(
        r"\\NewDocumentCommand \\OLSABidiLayoutTOCReplay \{m\}\s*\{(.*?)\n \}",
        module,
        re.S,
    )
    assert marker
    for unit in HEADING_UNITS:
        exactly(
            marker.group(1),
            rf"\olsa_bidi_layout_record:nn{{{unit}}}{{lukasiewicz-name-toc-ltr}}",
        )
    assert "Unexpected~Lukasiewicz~TOC~marker" in marker.group(1)
    assert "olFaLTR" not in marker.group(1), "marker must render no visible content"

    start = re.search(
        r"\\NewDocumentCommand \\OLSABidiLayoutStart \{\}\s*\{(.*?)\n \}",
        module,
        re.S,
    )
    assert start
    for token in (
        r"\olsa_bidi_layout_register_toc_contract:",
        r"\bool_gset_true:N \g_olsa_bidi_layout_started_bool",
        r"\iow_open:Nn \g_olsa_bidi_layout_iow",
    ):
        exactly(start.group(1), token)
    assert [start.group(1).index(token) for token in (
        r"\olsa_bidi_layout_register_toc_contract:",
        r"\bool_gset_true:N \g_olsa_bidi_layout_started_bool",
        r"\iow_open:Nn \g_olsa_bidi_layout_iow",
    )] == sorted(start.group(1).index(token) for token in (
        r"\olsa_bidi_layout_register_toc_contract:",
        r"\bool_gset_true:N \g_olsa_bidi_layout_started_bool",
        r"\iow_open:Nn \g_olsa_bidi_layout_iow",
    ))

    setup_0371 = protected_macro_body(module, "olsa_bidi_layout_setup_church_rosser:")
    for token in (
        r"\OLSABidiLayoutRecord{setup}",
        r"\int_gzero:N \g_olsa_bidi_layout_proof_target_int",
        r"\cs_set_eq:NN \proof \olsa_bidi_layout_proof_target:",
        r"\AddToHookNext{env/align/before}{\OLSAAlignLTRBefore}",
        r"\AddToHookNext{env/align/after}{\OLSAAlignLTRAfter}",
    ):
        exactly(setup_0371, token)

    for unit in SURNAME_SOURCES:
        setup = protected_macro_body(module, f"olsa_bidi_layout_setup_{SETUP_NAMES[unit]}:")
        exactly(setup, r"\OLSABidiLayoutRecord{setup}")
        exactly(setup, r"\cs_set_eq:NN \L \olsa_bidi_layout_lukasiewicz_or_original:")
        heading_binding = (
            rf"\cs_set_eq:NN \olsection "
            rf"\olsa_bidi_layout_section_{HEADING_COMMANDS.get(unit, 'absent')}:"
        )
        exactly(setup, heading_binding, 1 if unit in HEADING_UNITS else 0)

    setup_0429 = protected_macro_body(module, "olsa_bidi_layout_setup_normal_logics:")
    for token in (
        r"\OLSABidiLayoutRecord{setup}",
        r"\cs_set_eq:NN \] \olsa_bidi_layout_display_end:",
        r"\OLSABidiLayoutInstallTagForm",
        r"\cs_set_eq:NN \Dual \olsa_bidi_layout_dual:",
        r"\cs_set_eq:NN \RK \olsa_bidi_layout_rk:",
        r"\AddToHookNext{env/proof/begin}{\OLSABidiLayoutFirstProofLeftQED}",
    ):
        exactly(setup_0429, token)

    for token in (
        "parallel-beta-eta-reduction.tex",
        "goedel.tex",
        "multiple-designation.tex",
        "rules-and-proofs.tex",
        "propositional-rules.tex",
        "normal-logics.tex",
        r"\input{source/locale/fa-IR/content",
        r"\subfile{source/locale/fa-IR/content",
        r"\RenewDocumentCommand \olFaLTR",
    ):
        assert token not in module, f"forbidden source/config coupling: {token}"


def setup_registration_counts(module_override: str | None = None) -> Counter[str]:
    counts: Counter[str] = Counter()
    for path in STANDALONE.glob("*.tex"):
        text = module_override if module_override is not None and path == MODULE else read(path)
        counts.update(re.findall(r"\\OLSADeclareSetup\s*\{(OLP-\d{4})\}", text))
    return counts


def check_integration(body: str, runtime: str, module_override: str | None = None) -> None:
    include = r"\input{standalone/bidi-layout.tex}"
    exactly(body, include)
    assert (
        body.index(r"\input{standalone/runtime.tex}")
        < body.index(r"\input{standalone/typography.tex}")
        < body.index(include)
        < body.index(r"\InputIfFileExists{standalone-errata.tex}")
        < body.index(r"\OLSAStart")
        < body.index(r"\tableofcontents*")
    ), "BiDi module must load once before trace start and TOC replay"

    exactly(runtime, r"\cs_if_exist:cTF {olsa_setup_#1:}")
    exactly(runtime, r"Duplicate~setup~for~#1")
    exactly(runtime, r"\cs_generate_variant:Nn \prop_get:NnNTF {NVN}")
    exactly(runtime, r"\cs_generate_variant:Nn \prop_if_in:NnTF {NV}")
    exactly(runtime, r"\cs_if_exist:NT \OLSABidiLayoutStart {\OLSABidiLayoutStart}")
    exactly(runtime, r"\cs_if_exist:NT \OLSABidiLayoutVerify {\OLSABidiLayoutVerify}")
    declaration = re.search(
        r"\\NewDocumentCommand \\OLSADeclareSetup \{m \+m\}\s*\{(.*?)\n \}",
        runtime,
        re.S,
    )
    assert declaration
    assert declaration.group(1).index(r"\cs_if_exist:cTF") < declaration.group(1).index(
        r"\cs_gset:cpn"
    )

    counts = setup_registration_counts(module_override)
    targets = ["OLP-0371", *SURNAME_SOURCES, "OLP-0429"]
    assert {unit: counts[unit] for unit in targets} == {unit: 1 for unit in targets}
    assert not {unit: count for unit, count in counts.items() if count != 1}


def classify_toc_fixture(text: str) -> str:
    """Mirror the TeX Start-time marker inventory without executing TeX."""
    total = text.count("OLSABidiLayoutTOCReplay")
    match_0394 = list(
        re.finditer(r"OLSABidiLayoutTOCReplay\s*\{OLP-0394\}", text)
    )
    match_0400 = list(
        re.finditer(r"OLSABidiLayoutTOCReplay\s*\{OLP-0400\}", text)
    )
    if total == 0:
        return "bootstrap-22-rules-44-events"
    assert total == 2, "partial, duplicate, unknown or malformed TOC inventory"
    assert len(match_0394) == len(match_0400) == 1
    assert match_0394[0].start() < match_0400[0].start(), "reversed TOC markers"
    return "final-24-rules-46-events"


def check_final_toc_semantics(text: str) -> None:
    """Validate the converged TOC's serialized whole-name and marker bytes."""
    assert classify_toc_fixture(text) == "final-24-rules-46-events"
    renderer = r"\OLSABidiLayoutLukasiewiczName"
    marker_0394 = r"\OLSABidiLayoutTOCReplay"
    renderer_positions = [match.start() for match in re.finditer(re.escape(renderer), text)]
    marker_positions = [
        re.search(r"\\OLSABidiLayoutTOCReplay\s*\{OLP-0394\}", text),
        re.search(r"\\OLSABidiLayoutTOCReplay\s*\{OLP-0400\}", text),
    ]
    assert len(renderer_positions) == 2, "TOC must serialize two robust whole-name renderers"
    assert all(marker_positions)
    assert (
        renderer_positions[0]
        < marker_positions[0].start()
        < renderer_positions[1]
        < marker_positions[1].start()
    ), "TOC renderer/marker adjacency order changed"
    forbidden = (
        r"\L ukasiewicz",
        r"\OLPolishUpperL ukasiewicz",
        r"\olsa_bidi_layout_lukasiewicz:",
        r"\olsa_bidi_layout_lukasiewicz_or_original:",
        r"\olsa_bidi_layout_lukasiewicz_deferred:",
        r"\olsa_bidi_layout_lukasiewicz_deferred_or_original:",
        r"\olsa_bidi_layout_deferred_problem_setup:",
        r"\olsa_bidi_layout_original_l:",
        r"\olFaLTR{Łukasiewicz}",
        r"\OLSABidiLayoutRecord",
    )
    for token in forbidden:
        assert token not in text, f"unsafe TOC serialization: {token}"


def parse_trace_text(
    text: str, *, allow_bootstrap: bool = False
) -> list[tuple[str, str, str]]:
    lines = text.splitlines()
    assert lines and lines[0] == "source_id|event|occurrence", "wrong trace header"
    rows: list[tuple[str, str, str]] = []
    for line in lines[1:]:
        parts = line.split("|")
        assert len(parts) == 3, f"malformed trace row: {line!r}"
        rows.append((parts[0], parts[1], parts[2]))
    allowed = [FINAL_TRACE, BASE_TRACE] if allow_bootstrap else [FINAL_TRACE]
    assert rows in allowed, "trace event order/count/source contract changed"
    expected = FINAL_COUNTS if rows == FINAL_TRACE else BASE_COUNTS
    assert Counter((unit, event) for unit, event, _ in rows) == Counter(expected)
    return rows


def check_trace_log(text: str, *, allow_bootstrap: bool = False) -> None:
    rows = re.findall(
        r"^OL-STANDALONE-BIDI-LAYOUT\|(OLP-\d{4})\|([^|\r\n]+)\|(\d+)$",
        text,
        re.M,
    )
    allowed = [FINAL_TRACE, BASE_TRACE] if allow_bootstrap else [FINAL_TRACE]
    assert rows in allowed, "log trace order/count/source contract changed"
    coverage = re.findall(
        r"^OL-STANDALONE-BIDI-LAYOUT-COVERAGE\|(\d+)\|(\d+)$", text, re.M
    )
    expected = ("24", "46") if rows == FINAL_TRACE else ("22", "44")
    assert coverage == [expected]


def expect_reject(callable_obj, *args, **kwargs) -> None:
    try:
        callable_obj(*args, **kwargs)
    except AssertionError:
        return
    raise AssertionError("negative control was accepted")


def run_negative_controls(
    source_0371: str,
    surname_sources: dict[str, str],
    source_0429: str,
    module: str,
    body: str,
    runtime: str,
) -> list[str]:
    controls: list[tuple[str, object, tuple[object, ...]]] = []

    def sources_with(unit: str, replacement: str) -> dict[str, str]:
        result = dict(surname_sources)
        result[unit] = replacement
        return result

    controls.extend(
        [
            (
                "0371-second-align",
                check_source_shape,
                (source_0371 + "\n\\begin{align}x\\end{align}\n", surname_sources, source_0429),
            ),
            (
                "0371-starred-align",
                check_source_shape,
                (source_0371.replace(r"\begin{align}", r"\begin{align*}", 1), surname_sources, source_0429),
            ),
            (
                "0371-proof-inserted-before-target",
                check_source_shape,
                (source_0371.replace(r"\begin{proof}", "\\begin{proof}x\\end{proof}\n\\begin{proof}", 1), surname_sources, source_0429),
            ),
            (
                "0371-target-marker-moved",
                check_source_shape,
                (source_0371.replace(r"\olref[pb]{lem:comp}", r"\olref{lem:comp}", 1), surname_sources, source_0429),
            ),
            (
                "0371-source-emergency-stretch",
                check_source_shape,
                (source_0371 + "\n\\emergencystretch=16pt\n", surname_sources, source_0429),
            ),
        ]
    )
    for unit, source in surname_sources.items():
        controls.extend(
            [
                (
                    f"{unit.lower()}-missing-name",
                    check_source_shape,
                    (source_0371, sources_with(unit, source.replace(r"\L ukasiewicz", "Lukasiewicz", 1)), source_0429),
                ),
                (
                    f"{unit.lower()}-extra-name",
                    check_source_shape,
                    (source_0371, sources_with(unit, source + "\n\\L ukasiewicz\n"), source_0429),
                ),
                (
                    f"{unit.lower()}-bare-l-control",
                    check_source_shape,
                    (source_0371, sources_with(unit, source + "\n\\L test\n"), source_0429),
                ),
            ]
        )
    for unit in HEADING_UNITS:
        source = surname_sources[unit]
        controls.append(
            (
                f"{unit.lower()}-heading-changed",
                check_source_shape,
                (
                    source_0371,
                    sources_with(unit, source.replace(r"\olsection{منطق \L ukasiewicz}", r"\olsection[منطق]{منطق \L ukasiewicz}", 1)),
                    source_0429,
                ),
            )
        )
    controls.extend(
        [
            (
                "0429-missing-native-semicolon",
                check_source_shape,
                (source_0371, surname_sources, source_0429.replace("\\]؛", r"\]", 1)),
            ),
            (
                "0429-reordered-tags",
                check_source_shape,
                (
                    source_0371,
                    surname_sources,
                    source_0429.replace(r"\tag{\Ax{K}}", "TAG-A", 1)
                    .replace(r"\tag{\Dual}", r"\tag{\Ax{K}}", 1)
                    .replace("TAG-A", r"\tag{\Dual}", 1),
                ),
            ),
            ("0429-extra-dual", check_source_shape, (source_0371, surname_sources, source_0429 + "\n\\Dual\n")),
            ("0429-extra-rk", check_source_shape, (source_0371, surname_sources, source_0429 + "\n\\RK\n")),
            (
                "0429-second-display-ended-proof",
                check_source_shape,
                (source_0371, surname_sources, source_0429.replace("  با داشتن~$!A_1$", "  \\begin{align*}x=x\\end{align*}\n  با داشتن~$!A_1$", 1)),
            ),
        ]
    )

    module_mutations = [
        ("duplicate-event-registration", module + "\n\\OLSABidiLayoutExpect{OLP-0371}{setup}{1}\n"),
        ("proof-local-counter", module.replace(r"\int_gincr:N \g_olsa_bidi_layout_proof_target_int", r"\int_incr:N \g_olsa_bidi_layout_proof_target_int", 1)),
        ("proof-wrong-ordinal", module.replace(r"\int_compare:nNnT {\g_olsa_bidi_layout_proof_target_int}={2}", r"\int_compare:nNnT {\g_olsa_bidi_layout_proof_target_int}={3}", 1)),
        ("proof-missing-stretch", module.replace(r"\emergencystretch=16pt\relax", "", 1)),
        ("proof-original-before-stretch", module.replace("    \\emergencystretch=16pt\\relax\n   }\n  \\olsa_bidi_layout_original_proof:", "   }\n  \\olsa_bidi_layout_original_proof:\n  \\emergencystretch=16pt\\relax", 1)),
        ("proof-missing-original", module.replace("  \\olsa_bidi_layout_original_proof:\n }", " }", 1)),
        ("proof-missing-reset", module.replace(r"\int_gzero:N \g_olsa_bidi_layout_proof_target_int", "", 1)),
        ("proof-missing-binding", module.replace(r"\cs_set_eq:NN \proof \olsa_bidi_layout_proof_target:", "", 1)),
        ("surname-helper-protected", module.replace(r"\cs_new:Npn \olsa_bidi_layout_lukasiewicz:", r"\cs_new_protected:Npn \olsa_bidi_layout_lukasiewicz:", 1)),
        ("surname-delimiter-changed", module.replace(r"\olsa_bidi_layout_lukasiewicz: ukasiewicz", r"\olsa_bidi_layout_lukasiewicz: ukasiewic", 1)),
        ("surname-original-l-copy-removed", module.replace(r"\NewCommandCopy \olsa_bidi_layout_original_l: \L", "", 1)),
        ("surname-dispatch-peek-changed", module.replace(r"\peek_meaning:NTF u", r"\peek_meaning:NTF v", 1)),
        ("surname-dispatch-fallback-removed", module.replace(r"{\olsa_bidi_layout_original_l:}", "{}", 1)),
        ("surname-direct-binding-restored", module.replace(r"\cs_set_eq:NN \L \olsa_bidi_layout_lukasiewicz_or_original:", r"\cs_set_eq:NN \L \olsa_bidi_layout_lukasiewicz:", 1)),
        ("surname-deferred-record-removed", module.replace(r"\olsa_bidi_layout_record:nn{OLP-0394}{lukasiewicz-name-source-ltr}", "", 1)),
        ("surname-deferred-namespace-changed", module.replace("{mvl:thr:luk}", "{mvl:thr:kle}", 1)),
        ("surname-deferred-hook-removed", module.replace(r"\AddToHook{env/probd/begin}{\olsa_bidi_layout_deferred_problem_setup:}", "", 1)),
        ("surname-deferred-fallback-removed", module.replace(r"{\olsa_bidi_layout_lukasiewicz_deferred:}", "{}", 1)),
        ("surname-missing-source-record", module.replace(r"\OLSABidiLayoutRecord{lukasiewicz-name-source-ltr}", "", 1)),
        ("surname-split-renderer", module.replace(r"{\olFaLTR{Łukasiewicz}}", r"{\olFaLTR{Ł}ukasiewicz}", 1)),
        ("surname-heading-literal-space", module.replace(r"{#3}{منطق~\L ukasiewicz}", r"{#3}{منطق \L ukasiewicz}", 1)),
        ("surname-heading-output-literal-space", module.replace("[منطق~\\OLSABidiLayoutLukasiewiczName]", "[منطق \\OLSABidiLayoutLukasiewiczName]", 1)),
        ("surname-heading-record-removed", module.replace(r"\olsa_bidi_layout_record:nn{#1}{lukasiewicz-name-source-ltr}", "", 1)),
        ("surname-heading-marker-removed", module.replace(r"\addtocontents{toc}{\protect\OLSABidiLayoutTOCReplay{#1}}", "", 1)),
        ("surname-pdf-string-map-removed", module.replace(r"\def\OLSABidiLayoutLukasiewiczName{Łukasiewicz}", "", 1)),
        ("surname-olsection-copy-removed", module.replace(r"\NewCommandCopy \olsa_bidi_layout_original_olsection: \olsection", "", 1)),
        ("toc-scan-removed", module.replace(r"\file_if_exist:nTF {\jobname.toc}", r"\tl_clear:N", 1)),
        ("toc-total-count-removed", module.replace(r"\regex_count:nVN {OLSABidiLayoutTOCReplay}", r"\use_none:nn", 1)),
        ("toc-order-check-reversed", module.replace(r"{OLSABidiLayoutTOCReplay\s*\{OLP-0394\}.*OLSABidiLayoutTOCReplay\s*\{OLP-0400\}}", r"{OLSABidiLayoutTOCReplay\s*\{OLP-0400\}.*OLSABidiLayoutTOCReplay\s*\{OLP-0394\}}", 1)),
        ("toc-dynamic-0394-registration-removed", module.replace(r"\OLSABidiLayoutExpect{OLP-0394}{lukasiewicz-name-toc-ltr}{1}", "", 1)),
        ("toc-marker-0394-record-removed", module.replace(r"\olsa_bidi_layout_record:nn{OLP-0394}{lukasiewicz-name-toc-ltr}", "", 1)),
        ("toc-scan-after-trace-start", module.replace("    \\olsa_bidi_layout_register_toc_contract:\n    \\bool_gset_true:N \\g_olsa_bidi_layout_started_bool", "    \\bool_gset_true:N \\g_olsa_bidi_layout_started_bool\n    \\olsa_bidi_layout_register_toc_contract:", 1)),
        ("missing-rk-successor-peek", module.replace(r"\peek_catcode:NTF a {\space}{}", "", 1)),
        ("missing-rk-runtime-record", module.replace(r"\OLSABidiLayoutRecord{rk-ltr}", "", 1)),
        ("missing-native-semicolon-record", module.replace(r"\OLSABidiLayoutRecord{native-display-semicolon}", "", 1)),
        ("missing-display-false-delegation", module.replace(r"{\olsa_bidi_layout_original_display_end:}", "{}", 1)),
        ("missing-full-tag-parentheses", module.replace(r"\olFaLTR{(\ignorespaces#1\unskip\@@italiccorr)}", r"(\olFaLTR{#1})", 1)),
    ]
    for name, mutation in module_mutations:
        assert mutation != module, f"negative mutation did not change module: {name}"
        controls.append((name, check_module, (mutation,)))
    controls.extend(
        [
            ("duplicate-target-setup", check_integration, (body, runtime, module + "\n\\OLSADeclareSetup{OLP-0429}{}\n")),
            ("spaced-duplicate-target-setup", check_integration, (body, runtime, module + "\n\\OLSADeclareSetup {OLP-0429}{}\n")),
            ("missing-body-include", check_integration, (body.replace(r"\input{standalone/bidi-layout.tex}", "", 1), runtime, None)),
            ("runtime-collision-guard-removed", check_integration, (body, runtime.replace(r"\cs_if_exist:cTF {olsa_setup_#1:}", r"\use_none:n", 1), None)),
            ("runtime-required-variant-removed", check_integration, (body, runtime.replace(r"\cs_generate_variant:Nn \prop_get:NnNTF {NVN}", "", 1), None)),
        ]
    )
    for name, func, args in controls:
        try:
            expect_reject(func, *args)
        except AssertionError as error:
            raise AssertionError(f"negative control accepted: {name}") from error

    empty_toc = "\\contentsline {section}{legacy}{1}{}%\n"
    final_toc = (
        "\\contentsline {section}{منطق \\OLSABidiLayoutLukasiewiczName}{1}{}%\n"
        "\\OLSABidiLayoutTOCReplay {OLP-0394}\n"
        "\\contentsline {section}{منطق \\OLSABidiLayoutLukasiewiczName}{2}{}%\n"
        "\\OLSABidiLayoutTOCReplay{OLP-0400}\n"
    )
    assert classify_toc_fixture(empty_toc) == "bootstrap-22-rules-44-events"
    assert classify_toc_fixture(final_toc) == "final-24-rules-46-events"
    check_final_toc_semantics(final_toc)
    toc_mutations = [
        ("toc-only-0394", r"\OLSABidiLayoutTOCReplay{OLP-0394}"),
        ("toc-only-0400", r"\OLSABidiLayoutTOCReplay{OLP-0400}"),
        ("toc-duplicate-0394", r"\OLSABidiLayoutTOCReplay{OLP-0394}\OLSABidiLayoutTOCReplay{OLP-0394}"),
        ("toc-reversed", r"\OLSABidiLayoutTOCReplay{OLP-0400}\OLSABidiLayoutTOCReplay{OLP-0394}"),
        ("toc-unknown-id", r"\OLSABidiLayoutTOCReplay{OLP-0394}\OLSABidiLayoutTOCReplay{OLP-9999}"),
        ("toc-malformed-id", r"\OLSABidiLayoutTOCReplay{OLP-0394}\OLSABidiLayoutTOCReplay OLP-0400"),
        ("toc-extra-marker", final_toc + r"\OLSABidiLayoutTOCReplay{OLP-0400}"),
    ]
    for name, mutation in toc_mutations:
        try:
            expect_reject(classify_toc_fixture, mutation)
        except AssertionError as error:
            raise AssertionError(f"TOC negative accepted: {name}") from error
    toc_semantic_mutations = [
        (
            "toc-missing-whole-name-renderer",
            final_toc.replace(r"\OLSABidiLayoutLukasiewiczName", "Lukasiewicz", 1),
        ),
        (
            "toc-raw-source-name",
            final_toc.replace(r"\OLSABidiLayoutLukasiewiczName", r"\L ukasiewicz", 1),
        ),
        (
            "toc-legacy-glyph-only-name",
            final_toc.replace(
                r"\OLSABidiLayoutLukasiewiczName",
                r"\OLPolishUpperL ukasiewicz",
                1,
            ),
        ),
        (
            "toc-expanded-ltr-payload",
            final_toc.replace(
                r"\OLSABidiLayoutLukasiewiczName", r"\olFaLTR{Łukasiewicz}", 1
            ),
        ),
        (
            "toc-private-helper-leak",
            final_toc.replace(
                r"\OLSABidiLayoutLukasiewiczName",
                r"\olsa_bidi_layout_lukasiewicz:",
                1,
            ),
        ),
        (
            "toc-record-command-leak",
            final_toc.replace(
                r"\OLSABidiLayoutLukasiewiczName",
                r"\OLSABidiLayoutRecord{name}\OLSABidiLayoutLukasiewiczName",
                1,
            ),
        ),
        (
            "toc-renderers-before-both-markers",
            final_toc.replace(
                "\\OLSABidiLayoutTOCReplay {OLP-0394}\n",
                "",
                1,
            ).replace(
                "\\OLSABidiLayoutTOCReplay{OLP-0400}\n",
                "\\OLSABidiLayoutTOCReplay {OLP-0394}\n"
                "\\OLSABidiLayoutTOCReplay{OLP-0400}\n",
                1,
            ),
        ),
    ]
    for name, mutation in toc_semantic_mutations:
        try:
            expect_reject(check_final_toc_semantics, mutation)
        except AssertionError as error:
            raise AssertionError(f"TOC semantic negative accepted: {name}") from error

    final_text = "source_id|event|occurrence\n" + "\n".join(
        "|".join(row) for row in FINAL_TRACE
    ) + "\n"
    base_text = "source_id|event|occurrence\n" + "\n".join(
        "|".join(row) for row in BASE_TRACE
    ) + "\n"
    parse_trace_text(final_text)
    parse_trace_text(base_text, allow_bootstrap=True)
    trace_mutations = [
        ("trace-missing-row", final_text.replace("OLP-0429|rk-ltr|2\n", "", 1)),
        ("trace-duplicate-row", final_text + "OLP-0429|rk-ltr|2\n"),
        ("trace-wrong-source", final_text.replace("OLP-0429|dual-ltr|1", "OLP-0371|dual-ltr|1", 1)),
        ("trace-wrong-occurrence", final_text.replace("OLP-0394|lukasiewicz-name-source-ltr|11", "OLP-0394|lukasiewicz-name-source-ltr|12", 1)),
        ("trace-wrong-order", final_text.replace("OLP-0396|setup|1\nOLP-0396|lukasiewicz-name-source-ltr|1", "OLP-0396|lukasiewicz-name-source-ltr|1\nOLP-0396|setup|1", 1)),
        ("trace-unknown-event", final_text.replace("OLP-0429|rk-ltr|1", "OLP-0429|unknown|1", 1)),
        ("trace-wrong-header", final_text.replace("source_id|event|occurrence", "source|event|count", 1)),
        ("trace-one-toc-marker", final_text.replace("OLP-0394|lukasiewicz-name-toc-ltr|1\n", "", 1)),
        ("trace-duplicate-toc-marker", final_text.replace("OLP-0400|lukasiewicz-name-toc-ltr|1\n", "OLP-0400|lukasiewicz-name-toc-ltr|1\nOLP-0400|lukasiewicz-name-toc-ltr|2\n", 1)),
        ("trace-reversed-toc-markers", final_text.replace("OLP-0394|lukasiewicz-name-toc-ltr|1\nOLP-0400|lukasiewicz-name-toc-ltr|1", "OLP-0400|lukasiewicz-name-toc-ltr|1\nOLP-0394|lukasiewicz-name-toc-ltr|1", 1)),
    ]
    for name, mutation in trace_mutations:
        try:
            expect_reject(parse_trace_text, mutation, allow_bootstrap=True)
        except AssertionError as error:
            raise AssertionError(f"trace negative accepted: {name}") from error

    final_log = "\n".join(
        f"OL-STANDALONE-BIDI-LAYOUT|{'|'.join(row)}" for row in FINAL_TRACE
    ) + "\nOL-STANDALONE-BIDI-LAYOUT-COVERAGE|24|46\n"
    base_log = "\n".join(
        f"OL-STANDALONE-BIDI-LAYOUT|{'|'.join(row)}" for row in BASE_TRACE
    ) + "\nOL-STANDALONE-BIDI-LAYOUT-COVERAGE|22|44\n"
    check_trace_log(final_log)
    check_trace_log(base_log, allow_bootstrap=True)
    expect_reject(
        check_trace_log,
        final_log.replace(
            "OL-STANDALONE-BIDI-LAYOUT|OLP-0371|setup|1",
            "PREFIX-OL-STANDALONE-BIDI-LAYOUT|OLP-0371|setup|1-SUFFIX",
            1,
        ),
        allow_bootstrap=True,
    )
    expect_reject(
        check_trace_log,
        base_log.replace("COVERAGE|22|44", "COVERAGE|24|46"),
        allow_bootstrap=True,
    )
    return (
        [name for name, _, _ in controls]
        + [name for name, _ in toc_mutations]
        + [name for name, _ in toc_semantic_mutations]
        + [name for name, _ in trace_mutations]
        + ["log-markers-require-whole-lines", "bootstrap-log-requires-22-by-44"]
    )


def file_record(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": rel(path), "bytes": len(data), "sha256": digest(data)}


def make_evidence(negative_controls: Iterable[str]) -> dict[str, object]:
    source_0371 = read(SOURCE_0371)
    source_0429 = read(SOURCE_0429)
    setup_counts = setup_registration_counts()
    source_contracts: dict[str, object] = {
        "OLP-0371": {
            **file_record(SOURCE_0371),
            "sole_align": source_0371.count(r"\begin{align}"),
            "proof_environments": source_0371.count(r"\begin{proof}"),
            "emergency_stretch_target_proof_ordinal": 2,
            "emergency_stretch": "16pt",
        }
    }
    for unit, path in SURNAME_SOURCES.items():
        source_contracts[unit] = {
            **file_record(path),
            "lukasiewicz_source_occurrences": SURNAME_SOURCE_COUNTS[unit],
            "lukasiewicz_immediate_occurrences": (
                SURNAME_SOURCE_COUNTS[unit] - SURNAME_DEFERRED_COUNTS[unit]
            ),
            "lukasiewicz_deferred_problem_occurrences": SURNAME_DEFERRED_COUNTS[unit],
            "lukasiewicz_rendered_occurrences": SURNAME_RENDER_COUNTS[unit],
            "toc_replays": 1 if unit in HEADING_UNITS else 0,
        }
    source_contracts["OLP-0429"] = {
        **file_record(SOURCE_0429),
        "native_display_semicolon": source_0429.count("\\]؛"),
        "explicit_tag_order": ["K", "Dual"],
        "explicit_tags": 2,
        "dual_uses": source_0429.count(r"\Dual"),
        "rk_uses": source_0429.count(r"\RK"),
        "align_star_environments": source_0429.count(r"\begin{align*}"),
        "proof_environments": source_0429.count(r"\begin{proof}"),
        "display_ended_proofs": len(
            re.findall(r"\\end\{align\*\}\s*\\end\{proof\}", source_0429)
        ),
    }
    targets = ["OLP-0371", *SURNAME_SOURCES, "OLP-0429"]
    return {
        "schema": "farsi-standalone-bidi-layout/4",
        "audit_date": "2026-09-05",
        "result": "PASS_STATIC_TEX_NOT_RUN",
        "scope": targets,
        "source_contracts": source_contracts,
        "unchanged_configuration": [
            file_record(MASTER_CONFIG),
            file_record(LOCALE_CONFIG),
            file_record(OPEN_LOGIC_STYLE),
            file_record(DEFER_STYLE),
        ],
        "dispatch_contract": {
            "ledger": file_record(LEDGER),
            "contexts": {unit: ["FOL"] for unit in targets},
            "occurrences_per_target": 1,
        },
        "implementation": [
            file_record(MODULE),
            file_record(BODY),
            file_record(RUNTIME),
            file_record(CHECKER),
        ],
        "setup_contract": {
            "global_duplicate_registration_rejected": True,
            "registrations": {unit: setup_counts[unit] for unit in targets},
            "OLP-0371_composed_setup_count": 1,
            "OLP-0429_composed_setup_count": 1,
            "surname_unit_setup_count": 6,
        },
        "runtime_contract": {
            "sidecar": "<jobname>.olbidilayout",
            "header": "source_id|event|occurrence",
            "bootstrap": {
                "rules": 22,
                "events": 44,
                "condition": "preexisting TOC contains zero replay-marker names",
                "coverage": "OL-STANDALONE-BIDI-LAYOUT-COVERAGE|22|44",
                "trace_order": ["|".join(row) for row in BASE_TRACE],
            },
            "required_final": {
                "rules": 24,
                "events": 46,
                "condition": "preexisting TOC contains exactly OLP-0394 then OLP-0400 marker",
                "coverage": "OL-STANDALONE-BIDI-LAYOUT-COVERAGE|24|46",
                "trace_order": ["|".join(row) for row in FINAL_TRACE],
            },
            "final_rules": [
                {"source_id": unit, "event": event, "count": count}
                for unit, event, count in FINAL_RULES
            ],
            "toc_inventory_policy": "zero markers bootstrap; otherwise exactly one each in 0394-to-0400 order; partial/duplicate/unknown/malformed/reversed rejected",
            "final_toc_semantics": "exactly two public whole-name renderers interleaved before their 0394/0400 markers; raw, legacy, expanded, private and recording tokens rejected",
        },
        "negative_controls": list(negative_controls),
        "claims": [
            "all eight frozen target sources and shared configurations retain pinned bytes",
            "the additive module loads once before trace start and TOC replay; every target has one setup",
            "OLP-0371 composes one-shot align direction and proof-2-only 16pt emergency stretch in one setup",
            "all 25 frozen Lukasiewicz spellings become complete local LTR names; two heading names serialize robust corrected tokens for 27 visible renderings",
            "the surname dispatcher preserves every non-surname Polish-letter use, including the shared LogLuk mathematical symbol",
            "the one surname in an answers.sty-deferred OLP-0394 problem is rebound by its saved semantic namespace and counted against its originating unit",
            "source name events and the two ordered TOC replay events are independently counted",
            "the Start-time TOC inventory distinguishes 22/44 bootstrap from mandatory 24/46 final replay",
            "OLP-0429 composes display, tag, abbreviation spacing and first-proof direction in one setup",
            "synthetic TOC, bootstrap trace and final trace replay plus every listed mutation control pass",
        ],
        "limitations": [
            "TeX was not launched by this checker or implementation task",
            "static checks do not establish macro expansion, rendered direction, QED placement, pagination or visual acceptance",
            "the next owner-managed mutex-guarded build must validate a final 24-rule/46-event sidecar and log, inspect the serialized TOC and rerender all affected pages",
        ],
    }


def encode_evidence(payload: dict[str, object]) -> bytes:
    return (
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace-file", type=Path)
    parser.add_argument("--trace-log", type=Path)
    parser.add_argument("--toc-file", type=Path)
    parser.add_argument("--allow-bootstrap", action="store_true")
    parser.add_argument("--write-evidence", action="store_true")
    args = parser.parse_args()

    check_pins()
    source_0371 = read(SOURCE_0371)
    surname_sources = {unit: read(path) for unit, path in SURNAME_SOURCES.items()}
    source_0429 = read(SOURCE_0429)
    module = read(MODULE)
    body = read(BODY)
    runtime = read(RUNTIME)
    check_source_shape(source_0371, surname_sources, source_0429)
    check_configs(
        read(MASTER_CONFIG), read(LOCALE_CONFIG), read(OPEN_LOGIC_STYLE), read(DEFER_STYLE)
    )
    check_ledger(read(LEDGER))
    check_module(module)
    check_integration(body, runtime)
    negative_controls = run_negative_controls(
        source_0371, surname_sources, source_0429, module, body, runtime
    )

    if args.trace_file:
        parse_trace_text(
            args.trace_file.read_text(encoding="utf-8"),
            allow_bootstrap=args.allow_bootstrap,
        )
    if args.trace_log:
        check_trace_log(
            args.trace_log.read_text(encoding="utf-8", errors="replace"),
            allow_bootstrap=args.allow_bootstrap,
        )
    if args.toc_file:
        check_final_toc_semantics(
            args.toc_file.read_text(encoding="utf-8", errors="strict")
        )

    payload = make_evidence(negative_controls)
    encoded_a = encode_evidence(payload)
    encoded_b = encode_evidence(make_evidence(negative_controls))
    assert encoded_a == encoded_b, "evidence serialization is not deterministic"
    if args.write_evidence:
        EVIDENCE.write_bytes(encoded_a)

    print(
        "PASS: 8 pinned source units; 25 source/27 rendered Lukasiewicz names; "
        "1 composed OLP-0371 setup; 1 composed OLP-0429 setup; "
        f"22/44 bootstrap and 24/46 final runtime contracts; "
        f"{len(negative_controls)} negative controls; TeX not run"
    )


if __name__ == "__main__":
    main()
