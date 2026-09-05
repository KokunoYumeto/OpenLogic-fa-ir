"""Validate the guarded native combined OLFUN/OLSIZ corrections diagnostic.

The validator consumes an explicit BUILD_RECEIPT.json and writes evidence only
to an explicit repository evidence path.  It does not run TeX and cannot
qualify the complete reader or replace full-page visual inspection.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import json
import re
import subprocess
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
    reject_compact_phrases_in_pages,
    read_file_bytes,
    read_file_text,
    relative_repo_path,
    require,
    require_bound_output,
    require_compact_phrases_in_blocks,
    require_exact_keys,
    is_json_integer,
    require_recorder_inputs,
    self_test_common_primitives,
    sha256_bytes,
    sha256_file,
    validate_diagnostic_receipt,
    write_json,
)


JOB = "standalone-probe-source-corrections"
VALIDATOR = Path(__file__).resolve()
DRIVER = LOCALE / f"{JOB}.tex"
FIXTURE_MANIFEST = ROOT / "evidence/SOURCE_CORRECTIONS_PROBE_FIXTURE.json"
LIVE_DRIVER = LOCALE / "open-logic-standalone-fa-IR.tex"
RUNTIME = LOCALE / "standalone/runtime.tex"
GENERATOR = ROOT / "build/make_source_corrections_probe.py"
GENERATOR_SHA256 = "f6cfeb7c9e07f1ec545c98ca535c70a06ab6cf6dea14329f695529c1fd3488da"
RUNTIME_SHA256 = "2155dee2f9762c6f58c4898811fca07d8f42eee45210b73d3e9a9a47caff31e8"
DOCUMENT_BOUNDARY = br"\begin{document}"
HISTORICAL_FULL_DRIVER_IDENTITY = (13343, "f983e663c874fcee8b2065e15ffca1b3ab7c08174fa5ec970b7e96366e2c05d2")
LIVE_DRIVER_PREAMBLE_IDENTITY = (8212, "c6e31f3488f61233b446d848d80c0cc04d319d99d6c77c1fa28addfc4907ce47")
DRIVER_IDENTITY = (11387, "c5afafe6d39df524e60fb34749022275c8b022f59b76ecfc2e86821d922388dd")
FIXTURE_MANIFEST_SHA256 = "7bb9d8b2ad9db83df0c4c77fc07823dfd267dff5e23de1a8194028431aac3179"
OVERLAY_IDENTITY = (61699, "9f9875f14dbcf20f6482cdc40f2eff1787c6a084708eed154be521d6c600ac60")
ERRATA_IDENTITY = (13459, "77efdcb3fc8848406bda7f2f766491da23abb72e2c6971a71734bd6d93379d63")
ACCEPTED_NATIVE_QA_IDENTITY = (54438, "6afcaadc1c1997ef4a537b9aba469c470f8caf82322c36fca729dadec4d3d1ce")
ACCEPTED_VISUAL_QA_IDENTITY = (8048, "3a1f7e00ddccbf4ae10faab58d86e019ca8ac129bfbdb96646a1295146a7800d")
PDFTOTEXT_VERSION = "24.04.0"
PDFTOTEXT_SHA256 = "6f1f7d8db783bd2fac74043dca400a53f42d0a03c4e7f81b2c51ed436c13faeb"
POPPLER_DLL_NAME = "MiKTeX260500-poppler.dll"
POPPLER_DLL_SHA256 = "ff3ff8afc81f883e1d4d79bf8e18d56bcb6d8d1a2a9e80e0c9082290e42955d4"
MAX_SEMANTIC_WINDOW_LINES = 6

EXPECTED_UNITS = [
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

PROBE_PREFIX = r'''
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

'''

PROBE_SUFFIX = r'''

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

EXPECTED_DECLARATIONS = [
    ("OLP-0021", "ex", "OLFUN-002", "1"),
    ("OLP-0021", "ex", "OLFUN-003", "1"),
    ("OLP-0023", "explain", "OLFUN-004", "1"),
    ("OLP-0023", "explain", "OLFUN-005", "1"),
    ("OLP-0024", "prop", "OLFUN-001-THEOREM", "1"),
    ("OLP-0024", "proof", "OLFUN-001-PROOF", "1"),
    ("OLP-0029", "ex", "OLSIZ-001", "1"),
    ("OLP-0031", "prob", "OLSIZ-002", "1"),
    ("OLP-0032", "explain", "OLSIZ-003", "1"),
    ("OLP-0034", "proof", "OLSIZ-004", "1"),
    ("OLP-0034", "explain", "OLSIZ-005", "1"),
    ("OLP-0035", "proof", "OLSIZ-006", "1"),
    ("OLP-0036", "proof", "OLSIZ-007", "1"),
    ("OLP-0039", "proof", "OLSIZ-008+009", "1"),
    ("OLP-0040", "proof", "OLSIZ-010", "1"),
]
# The deferred OLSIZ-002 body is not rendered when OLP-0031 is read.  It is
# corrected only when the answers stream is read by \printproblems, after every
# ordinary unit.  Keep declaration order and observed execution order separate.
EXPECTED_TRACE = [
    *EXPECTED_DECLARATIONS[:7],
    *EXPECTED_DECLARATIONS[8:],
    EXPECTED_DECLARATIONS[7],
]
PHYSICAL_RULES = [row[2] for row in EXPECTED_DECLARATIONS]
SEMANTIC_AUDIT_IDS = [
    "OLFUN-001", "OLFUN-002", "OLFUN-003", "OLFUN-004", "OLFUN-005",
    "OLSIZ-001", "OLSIZ-002", "OLSIZ-003", "OLSIZ-004", "OLSIZ-005",
    "OLSIZ-006", "OLSIZ-007", "OLSIZ-008", "OLSIZ-009", "OLSIZ-010",
]
EXPECTED_LOG_MARKERS = [
    f"OL-STANDALONE-SOURCE-CORRECTION|{unit}|{finding}|{occurrence}"
    for unit, _environment, finding, occurrence in EXPECTED_TRACE
]
EXPECTED_LABELS = [
    "sfr:fun:bas:fig:function",
    "sfr:fun:bas:examplefunext",
    "sfr:fun:rel:prop:graph-function",
    "sfr:fun:rel:defn:funimage",
    "sfr:fun:inv:prop:bijection-inverse",
    "sfr:fun:inv:prop:left-right",
    "sfr:fun:inv:prop:inverse-unique",
    "sfr:siz:enm:defn:enumerable",
    "sfr:siz:enm:prop:enum-shift",
    "sfr:siz:enm:cor:enum-nat",
    "sfr:siz:enm:prop:enum-bij",
    "sfr:siz:enm:cor:enum-nat-bij",
    "sfr:siz:equ:comparisondef",
    "sfr:siz:equ:equinumerosityisequi",
    "sfr:siz:car:thm:cantor",
    "sfr:siz:nen-alt:thm:nonenum-bin-omega",
    "sfr:siz:nen-alt:thm:nonenum-pownat",
    "sfr:siz:red:prob:nat-nat",
    "sfr:siz:red-alt:prob:nat-nat",
]

REQUIRED_PDF_PHRASES = [
    "آزمونِ تصحیح‌های ممیزیِ منبع",
    "این سند فقط آزمونِ تشخیصیِ لایهٔ تصحیح است و خوانشگرِ نهایی نیست",
    "آزمونِ مسئلهٔ معوق",
    "تصحیح‌های این ویرایش: ریشهٔ اصلی و نامِ متغیر",
    "تصحیح‌های این ویرایش: گراف و تحدیدِ تابع",
    "تصحیحِ این ویرایش: شرطِ وارونِ چپ",
    "تصحیحِ این ویرایش: مقدارِ جاافتادهٔ جدول",
    "تصحیحِ این ویرایش: متمم نسبت به اعداد طبیعی",
    "تصحیحِ این ویرایش: خانوادهٔ سومِ زوج‌ها",
    "تصحیح‌های این ویرایش: نامِ دنباله و خروجیِ نامتناهی",
    "تصحیحِ این ویرایش: نامِ تابع در حالتِ مجموعهٔ تهی",
    "تصحیحِ این ویرایش: دامنهٔ سور در استدلال قطری",
    "تصحیحِ این ویرایش: ترتیبِ شاخص‌ها",
    "تصحیحِ این ویرایش: تغییرِ مکملِ بیت",
    "تصحیحِ این ویرایش: نامِ دنبالهٔ مشخصه",
]
REJECTED_PDF_PHRASES = [
    "بازگرداندن تنها ریشهٔ دوم مثبت آن را تابع‌وار کنیم",
    "با داشتن یک عدد طبیعی n، تابع",
    "گرافی دارد؛ یعنی رابطه‌ای روی",
    "دقیقاً همان‌اند که انتظار می‌رود",
    "می‌توانیم آن را به هر a",
    "متممِ یک زیرمجموعهٔ متناهی از",
]

SEMANTIC_NOTE_SPECS = [
    (("OLFUN-002", "OLFUN-003"), "تصحیح‌های این ویرایش: ریشهٔ اصلی و نامِ متغیر"),
    (("OLFUN-004", "OLFUN-005"), "تصحیح‌های این ویرایش: گراف و تحدیدِ تابع"),
    (("OLFUN-001",), "تصحیحِ این ویرایش: شرطِ وارونِ چپ"),
    (("OLSIZ-001",), "تصحیحِ این ویرایش: مقدارِ جاافتادهٔ جدول"),
    (("OLSIZ-002",), "تصحیحِ این ویرایش: متمم نسبت به اعداد طبیعی"),
    (("OLSIZ-003",), "تصحیحِ این ویرایش: خانوادهٔ سومِ زوج‌ها"),
    (("OLSIZ-004", "OLSIZ-005"), "تصحیح‌های این ویرایش: نامِ دنباله و خروجیِ نامتناهی"),
    (("OLSIZ-006",), "تصحیحِ این ویرایش: نامِ تابع در حالتِ مجموعهٔ تهی"),
    (("OLSIZ-007",), "تصحیحِ این ویرایش: دامنهٔ سور در استدلال قطری"),
    (("OLSIZ-008",), "تصحیحِ این ویرایش: ترتیبِ شاخص‌ها"),
    (("OLSIZ-009",), "تصحیحِ این ویرایش: تغییرِ مکملِ بیت"),
    (("OLSIZ-010",), "تصحیحِ این ویرایش: نامِ دنبالهٔ مشخصه"),
]

# Each tuple is (semantic finding, required page-local line-window token groups
# with exact match counts, rejected legacy line-window token groups).  Every
# group is bounded to at most MAX_SEMANTIC_WINDOW_LINES and can never cross a
# page boundary, so unrelated text cannot satisfy a semantic delta.
SEMANTIC_DELTA_SPECS = [
    (
        "OLFUN-002",
        [
            (("دو ریشهٔ دوم", "دومِ نامنفی"), 1),
            (("ریشهٔ اصلی", "تابع‌وار کنیم"), 1),
        ],
        [("دوم مثبت", "تابع‌وار کنیم")],
    ),
    (
        "OLFUN-003",
        [(("با داشتن یک عدد طبیعی x", "تابع g", "پیشینِ جانشینِ جانشینِ x", "x+1"), 1)],
        [("با داشتن یک عدد طبیعی n", "تابع g")],
    ),
    (
        "OLFUN-004",
        [(("هر تابع f : A → B گرافی دارد", "با f(x)=y تعریف می‌شود"), 1)],
        [("گرافی دارد؛ یعنی رابطه‌ای روی A", "B")],
    ),
    ("OLFUN-005", [(("تحدیدِ تابع فقط ورودی را محدود می‌کند", "نه هر دو مختصهٔ رابطه را"), 1)], [("دقیقاً همان‌اند که انتظار می‌رود",)]),
    (
        "OLFUN-001",
        [
            (("اگر A ناتهی باشد و f", "وارون چپی"), 1),
            (("فرض کنید A ناتهی باشد", "عنصری a ∈ A برگزینید"), 1),
            (("آن را به همان a نگاشت می‌کنیم", "g : B → A"), 1),
        ],
        [
            (("اگر f : A → B یک‌به‌یک باشد", "وارون چپی مانند g : B → A")),
            (("می‌توانیم آن را به هر a", "نگاشت کنیم")),
        ],
    ),
    ("OLSIZ-001", [(("0", "1", "-1", "2", "-2", "3", "-3"), 1)], []),
    ("OLSIZ-002", [(("متممِ آن نسبت به", "متناهی باشد"), 1)], [("متممِ یک زیرمجموعهٔ متناهی از",)]),
    ("OLSIZ-003", [(("زوج‌های", "2,m", "3,m", "همین شیوه"), 1)], [("زوج‌های", "2,m", "2,m و جز آن")]),
    ("OLSIZ-004", [(("f(Z)", "s(n)=1", "s(n)=0"), 1)], [("f(Z)", "sk(n)=1")]),
    ("OLSIZ-005", [(("h(n)=", "111", "n تا 0"), 1)], []),
    ("OLSIZ-006", [(("اما هیچ عضوی", "f(x)=y"), 1)], [("اما هیچ عضوی", "g(x)=y")]),
    (
        "OLSIZ-007",
        [(("x ∈ A را دلخواه بگیرید", "چون x دلخواه بود", "برای هر", "g(x)"), 1)],
        [("برای هر x", "overline", "g(x)")],
    ),
    (
        "OLSIZ-008",
        [(("هر برشماری از یک زیرمجموعه", "رقم mاُمِ رشتهٔ nاُمِ", "s"), 1)],
        [("رقم nاُمِ رشتهٔ mاُمِ",)],
    ),
    ("OLSIZ-009", [(("هر 1 را به 0 و هر 0 را به 1 تغییر می‌دهیم",), 1)], [("هر 1 را به 0 و هر 1 را به 0 تغییر می‌دهیم",)]),
    ("OLSIZ-010", [(("f(N)", "s(n)=1", "s(n)=0"), 1)], [("f(N)", "sk(n)=1")]),
]
SEMANTIC_EXPECTED_REQUIRED_PAGES = {
    "OLFUN-002": [{2}, {2}],
    "OLFUN-003": [{3}],
    "OLFUN-004": [{4}],
    "OLFUN-005": [{5}],
    "OLFUN-001": [{6}, {6}, {7}],
    "OLSIZ-001": [{11}],
    "OLSIZ-002": [{28}],
    "OLSIZ-003": [{14}],
    "OLSIZ-004": [{16}],
    "OLSIZ-005": [{17}],
    "OLSIZ-006": [{18}],
    "OLSIZ-007": [{21}],
    "OLSIZ-008": [{22}],
    "OLSIZ-009": [{23}],
    "OLSIZ-010": [{25}],
}
CITATION_PDF_SPECS = [
    ("Frege1884", ("Frege", "1884")),
    ("Cantor1892", ("Cantor", "1892")),
]


def _mapping(value: object, label: str) -> dict[str, object]:
    require(isinstance(value, dict), f"{label} must be an object")
    return value


AUDIT_IDS = ["OLFUN-20260904", "OLSIZ-20260904"]
RULE_TO_FINDINGS = {
    "OLFUN-001-THEOREM": ["OLFUN-001"],
    "OLFUN-001-PROOF": ["OLFUN-001"],
    "OLSIZ-008+009": ["OLSIZ-008", "OLSIZ-009"],
}
NATIVE_ACCEPTANCE = [
    "one guarded LuaLaTeX diagnostic pass exits zero",
    "olcorrections sidecar and log contain exactly fifteen expected physical events",
    "all fifteen semantic findings are mapped without duplicate or missing audit identities",
    "the OLSIZ-002 problem correction and note execute only after its persisted source context is restored",
    "all corrected semantic deltas are bound to bounded page-local line windows rather than whole-document text search",
    "the exact Frege1884 and Cantor1892 source citations resolve from local one-pass seeds and write ordered AUX citation rows without external bibliography input",
    "all rendered probe pages receive complete visual inspection",
]
SOURCE_UNIT_IDENTITIES = {
    "OLP-0021": (7916, "d66599bdc39e09d80bcd3d02c257aef308a2589e8b6f23c7791cb938e1f0ec83"),
    "OLP-0023": (5640, "6e173bd7f87658e80b293ac6d7f95a36f68cd80b5bddf3d0f628c701e6685bba"),
    "OLP-0024": (9605, "6f81eed36763fbf88c1c6a2d67603c436567e46d02c45fcb5cb27c85d332556b"),
    "OLP-0029": (17813, "56a7e2689b7c7d9062fe17d6da50c8a8b6fb21b50852192f05dc31e63636c26b"),
    "OLP-0031": (5894, "6821b15121d8dab526ec888af8792f54168724ff4fcd2f29dcf8e56e64cdb42e"),
    "OLP-0032": (6213, "a738ab5a1fedd702373fecda2d0337f7a7d1e1279b147096c7dd001b066825f2"),
    "OLP-0034": (7827, "34e56fb7426e63eed603e95537caae2bd576600e564fad2be0f93b982f3caadf"),
    "OLP-0035": (5822, "f85f4365af77482af7a5d3891c76cb845c57fe59b6cc0de3aee945638df159f2"),
    "OLP-0036": (9945, "d933078b0271a7f13cf0aa98131ae75d6cedaf83f47952d3697ceeb070ba7759"),
    "OLP-0039": (9532, "8e118ca1ec17c49e1062b0b7a548d0181dd169ef39dea021043751f2a3179b41"),
    "OLP-0040": (7255, "9c15bf0a9a05128c40c63d42d8323d9cc9f060fafa7aea9fcf568154ec02522a"),
}
EXPECTED_BODY_HASHES = {
    "OLFUN-002": ("4789945cd11d0b189334d2ab6b85dba25263a2db5e893f1a2cf1d2588b6e51f9", "09554397df91f1a1606a1456cfcfaa80d61ad3f8b0e2faf9dacdd654f460cd44"),
    "OLFUN-003": ("0bc8d84a42fa189633215fbf9dfd4626d1889ea200ede7e9f2be00b774e0f025", "585e65436c218df4158eb8e145cb173292e39820b2a2180867e7c2c29e355243"),
    "OLFUN-004": ("72a6c20738ceda87b4cd495263aad867ca59ba96f0343e87c0cda93bf4013578", "e4d95c0e6b8afe11eb242a0d06f23172e3bb0b50d3cb08bf31b245b7115ff340"),
    "OLFUN-005": ("a454212a00b8e37b8c2d03b2aaba383b835da6f686d12ef3175443c51cc67a36", "a5be256b344bd9ba5d63a49fcd1f256bfe9db749bb88bd9a7d19a321c52e8ec2"),
    "OLFUN-001-THEOREM": ("8aebf99ed390beac4da4a44b0aa7399c77d2bf12e96932f779b63a4c5fbd1ae2", "e294da065edf0091fc5694486cf8c51c6f0438d3b2e778938739b073250b054e"),
    "OLFUN-001-PROOF": ("bfe7fc23f53f01373b86c6204e24c8a2335c49187e23fb9b5c92a2b5cf41424b", "7474ceccbc27f207420b9e7739af6417a777c6be88de8096868f4ef0418ae7fe"),
    "OLSIZ-001": ("868af0e666caa26a370e49744ae99f7970a5a3404cb3c1f27282e5b6c7a3232a", "f82513c20eb665bc8ce088f31d9e1799470e94e4b608a7d15b59959a4ca062ea"),
    "OLSIZ-002": ("0c3dcb99216e95d84b3ae01e396ae820f7626e48183f727f9b2fc0813133fb8c", "ddc7ffb72d647e5467f2bddbe0840d3ffc378496bedf4fe94efdd5916e843154"),
    "OLSIZ-003": ("9c0c8d9b8d2603fcbf40b98cea77332166ecec36be2cfbf4af61abbd35a2fbe1", "b99bfce84e543a285f8f5b1a48bcaf3d1a1a92a4d92eb4f8ab2ed644f4adc4a7"),
    "OLSIZ-004": ("0ede765e0176e77e4ee0eadf2902e3049115c1daeb4fbda730a74fc964158c48", "c12fe008cdb4dbff13112dc02bb62b48ed6c6d4ceda98860c033d50364a976e6"),
    "OLSIZ-005": ("b7d36db74bc7d2a5ed19b47ee2ed4bc7231d99e69aace9b78cdaeb5faa45d186", "e8bab2b2cc3eeb45a792d4fb584eaabbedfbb8a5124176cc03574fdd281c5aff"),
    "OLSIZ-006": ("6d6aece0a1e6b8d467a83809c6b9a4a8292e1490b9e737828fafbbb698998f59", "1c381c9c1678b75fe998db40277de02ba4874023fcc0b1c49577be047b2c81d3"),
    "OLSIZ-007": ("c8b11ddde014e04444d02fb0b91f2cff98eeb033f94408465617bf325ebfc098", "1fb5df863da40aae31d402eade7e8616cbade25a3868d6950fad770cc73c36ef"),
    "OLSIZ-008+009": ("bd99f819737871bde7f512f0d28efb0c2b9e7e4ae6ace69e1b9f2d88015738d6", "2eafb7f049c46e89ab7b7436286e67c18e0a8752888ebaac40e3bde4e0ad4147"),
    "OLSIZ-010": ("974a417d4cc98db4081e22254f41965de782904f5684dec7d4d18486d2f5e472", "8271d7506695ac5ef266107991fdd2fd6e5c33ca91397593b424952c25327634"),
}


def driver_preamble_through_boundary(data: bytes) -> bytes:
    boundary_at = data.find(DOCUMENT_BOUNDARY)
    require(boundary_at >= 0, "live standalone driver has no literal document boundary")
    boundary_end = boundary_at + len(DOCUMENT_BOUNDARY)
    return data[:boundary_end]


def reconstructed_driver_bytes() -> bytes:
    live_preamble = driver_preamble_through_boundary(
        read_file_bytes(LIVE_DRIVER)
    )[:-len(DOCUMENT_BOUNDARY)]
    calls = "\n".join(
        f"\\OLSACorrectionProbeUnit{{{unit}}}%\n {{{relative}}}"
        for unit, relative in EXPECTED_UNITS
    )
    return (
        live_preamble
        + CITATION_SEED.encode("utf-8")
        + CONDITIONAL_REFERENCE_SEED.encode("utf-8")
        + PROBE_PREFIX.encode("utf-8")
        + calls.encode("utf-8")
        + PROBE_SUFFIX.encode("utf-8")
    )


def _validate_file_record(
    value: object,
    *,
    label: str,
    expected_path: str,
    expected_unit: str | None = None,
    pinned_identity: tuple[int, str] | None = None,
) -> dict[str, object]:
    record = _mapping(value, label)
    keys = {"path", "bytes", "sha256"}
    if expected_unit is not None:
        keys.add("unit_id")
    require_exact_keys(record, keys, label)
    require(record.get("path") == expected_path, f"{label} path changed")
    if expected_unit is not None:
        require(record.get("unit_id") == expected_unit, f"{label} unit id changed")
    count = record.get("bytes")
    digest = record.get("sha256")
    require(is_json_integer(count) and count >= 0, f"{label} byte count must be a nonnegative JSON integer")
    require(
        isinstance(digest, str) and re.fullmatch(r"[0-9A-F]{64}", digest) is not None,
        f"{label} hash must be uppercase SHA-256",
    )
    path = ROOT / expected_path
    require(path.is_file(), f"{label} file missing: {expected_path}")
    require(count == file_size(path), f"{label} byte count mismatch")
    require(digest.casefold() == sha256_file(path), f"{label} hash mismatch")
    if pinned_identity is not None:
        pinned_size, pinned_hash = pinned_identity
        require(count == pinned_size and digest.casefold() == pinned_hash, f"{label} reviewed identity changed")
    return dict(record)


def _validate_preamble_record(value: object) -> dict[str, object]:
    label = "fixture driver preamble"
    record = _mapping(value, label)
    require_exact_keys(
        record,
        {"path", "boundary", "boundary_inclusive", "bytes", "sha256"},
        label,
    )
    expected_path = LIVE_DRIVER.relative_to(ROOT).as_posix()
    require(record.get("path") == expected_path, f"{label} path changed")
    require(record.get("boundary") == DOCUMENT_BOUNDARY.decode("ascii"), f"{label} boundary changed")
    require(record.get("boundary_inclusive") is True, f"{label} must include the boundary")
    count = record.get("bytes")
    digest = record.get("sha256")
    require(is_json_integer(count) and count >= 0, f"{label} byte count must be a nonnegative JSON integer")
    require(
        isinstance(digest, str) and re.fullmatch(r"[0-9A-F]{64}", digest) is not None,
        f"{label} hash must be uppercase SHA-256",
    )
    preamble = driver_preamble_through_boundary(read_file_bytes(LIVE_DRIVER))
    require(count == len(preamble), f"{label} byte count mismatch")
    require(digest.casefold() == sha256_bytes(preamble), f"{label} hash mismatch")
    require(
        (count, digest.casefold()) == LIVE_DRIVER_PREAMBLE_IDENTITY,
        f"{label} reviewed identity changed",
    )
    return dict(record)


def _validate_historical_continuity(
    value: object,
    preamble: dict[str, object],
) -> None:
    label = "fixture historical evidence continuity"
    continuity = _mapping(value, label)
    require_exact_keys(
        continuity,
        {
            "status", "historical_full_driver_locator_only",
            "historical_driver_preamble", "accepted_probe_tex",
            "accepted_native_qa", "accepted_complete_visual_qa",
            "preamble_bytes_unchanged", "probe_tex_bytes_unchanged",
            "post_boundary_driver_changes_out_of_scope",
        },
        label,
    )
    require(
        continuity.get("status") == "PASS_PREAMBLE_AND_PROBE_TEX_BYTES_UNCHANGED",
        f"{label} status changed",
    )
    historical_driver = _mapping(
        continuity.get("historical_full_driver_locator_only"),
        "historical full driver locator",
    )
    require_exact_keys(historical_driver, {"path", "bytes", "sha256"}, "historical full driver locator")
    require(
        historical_driver == {
            "path": LIVE_DRIVER.relative_to(ROOT).as_posix(),
            "bytes": HISTORICAL_FULL_DRIVER_IDENTITY[0],
            "sha256": HISTORICAL_FULL_DRIVER_IDENTITY[1].upper(),
        },
        "historical full driver locator changed",
    )
    historical_preamble = _mapping(
        continuity.get("historical_driver_preamble"),
        "historical driver preamble",
    )
    require_exact_keys(
        historical_preamble,
        {"boundary", "boundary_inclusive", "bytes", "sha256"},
        "historical driver preamble",
    )
    require(
        historical_preamble == {
            "boundary": DOCUMENT_BOUNDARY.decode("ascii"),
            "boundary_inclusive": True,
            "bytes": LIVE_DRIVER_PREAMBLE_IDENTITY[0],
            "sha256": LIVE_DRIVER_PREAMBLE_IDENTITY[1].upper(),
        },
        "historical driver preamble identity changed",
    )
    require(
        preamble["bytes"] == historical_preamble["bytes"]
        and str(preamble["sha256"]).casefold() == str(historical_preamble["sha256"]).casefold(),
        "current and historical driver preamble identities differ",
    )
    accepted_probe = _validate_file_record(
        continuity.get("accepted_probe_tex"),
        label="accepted historical source-corrections probe",
        expected_path=DRIVER.relative_to(ROOT).as_posix(),
        pinned_identity=DRIVER_IDENTITY,
    )
    _validate_file_record(
        continuity.get("accepted_native_qa"),
        label="accepted historical native QA",
        expected_path="evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_QA.json",
        pinned_identity=ACCEPTED_NATIVE_QA_IDENTITY,
    )
    _validate_file_record(
        continuity.get("accepted_complete_visual_qa"),
        label="accepted historical complete visual QA",
        expected_path="evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_VISUAL_QA.json",
        pinned_identity=ACCEPTED_VISUAL_QA_IDENTITY,
    )
    require(
        str(accepted_probe["sha256"]).casefold() == DRIVER_IDENTITY[1],
        "accepted probe TeX continuity identity changed",
    )
    for key in (
        "preamble_bytes_unchanged", "probe_tex_bytes_unchanged",
        "post_boundary_driver_changes_out_of_scope",
    ):
        require(continuity.get(key) is True, f"{label} {key} must be true")


def _skip_tex_space_and_comments(text: str, offset: int) -> int:
    while offset < len(text):
        if text[offset].isspace():
            offset += 1
            continue
        if text[offset] == "%":
            newline = text.find("\n", offset)
            offset = len(text) if newline < 0 else newline + 1
            continue
        break
    return offset


def _balanced_tex_argument(text: str, offset: int, label: str) -> tuple[str, int]:
    offset = _skip_tex_space_and_comments(text, offset)
    require(offset < len(text) and text[offset] == "{", f"{label} lacks a braced argument")
    start = offset + 1
    offset += 1
    depth = 1
    while offset < len(text):
        character = text[offset]
        if character == "\\":
            # Escaped braces are control symbols and do not delimit the group.
            # For a control word, later braces remain visible to this scanner.
            offset += 2 if offset + 1 < len(text) else 1
            continue
        if character == "%":
            newline = text.find("\n", offset)
            offset = len(text) if newline < 0 else newline + 1
            continue
        if character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0:
                return text[start:offset], offset + 1
        offset += 1
    raise ValidationError(f"{label} has an unterminated braced argument")


def parse_tex_command_arguments(text: str, command: str, arity: int) -> list[tuple[str, ...]]:
    pattern = re.compile(rf"(?m)^[ \t]*{re.escape(command)}(?=[ \t\r\n%]*\{{)")
    records: list[tuple[str, ...]] = []
    for declaration_index, match in enumerate(pattern.finditer(text), start=1):
        offset = match.end()
        arguments: list[str] = []
        for argument_index in range(arity):
            argument, offset = _balanced_tex_argument(
                text,
                offset,
                f"{command} declaration {declaration_index} argument {argument_index + 1}",
            )
            arguments.append(argument)
        records.append(tuple(arguments))
    return records


def validate_overlay(overlay_path: Path) -> list[dict[str, object]]:
    text = read_file_text(overlay_path)
    declarations = parse_tex_command_arguments(text, r"\OLSADeclareSourceCorrection", 5)
    expected_headers = [
        (unit, environment, finding)
        for unit, environment, finding, _occurrence in EXPECTED_DECLARATIONS
    ]
    require([row[:3] for row in declarations] == expected_headers, "overlay correction declaration order changed")
    require(len({row[2] for row in declarations}) == len(declarations), "overlay contains duplicate physical rule ids")
    require(
        text.count(r"\OLSADeclareSourceCorrection") == len(declarations) + 1,
        "unexpected source-correction command occurrence",
    )
    require(r"\RenewDocumentEnvironment{probdeferred}{m +b}" in text, "deferred problem wrapper is absent")
    require(
        r"\l_olsa_reference_id_tl {prob}{##2}" in text,
        "deferred problem wrapper no longer matches in prob context",
    )
    require(r"\OLSADeclareDeferredCorrectionAfter" in text, "deferred erratum hook support is absent")
    records: list[dict[str, object]] = []
    for unit, environment, finding, original, replacement in declarations:
        require(compact_text(original) != compact_text(replacement), f"correction has no semantic token delta: {finding}")
        original_hash = sha256_bytes(original.encode("utf-8"))
        replacement_hash = sha256_bytes(replacement.encode("utf-8"))
        require(
            (original_hash, replacement_hash) == EXPECTED_BODY_HASHES[finding],
            f"reviewed original/replacement body identity changed: {finding}",
        )
        records.append(
            {
                "unit_id": unit,
                "environment": environment,
                "physical_rule": finding,
                "original_body_sha256": original_hash,
                "replacement_body_sha256": replacement_hash,
            }
        )
    return records


def validate_errata(errata_path: Path) -> None:
    text = read_file_text(errata_path)
    after = parse_tex_command_arguments(text, r"\OLSADeclareAfter", 2)
    deferred = parse_tex_command_arguments(text, r"\OLSADeclareDeferredCorrectionAfter", 2)
    expected_normal_units = [unit for unit, _path in EXPECTED_UNITS if unit != "OLP-0031"]
    in_probe = {unit for unit, _path in EXPECTED_UNITS}
    require(
        [unit for unit, _body in after if unit in in_probe] == expected_normal_units,
        "adjacent source-correction errata order changed",
    )
    require(
        sum(unit == "OLSIZ-002" for unit, _body in deferred) == 1,
        "OLSIZ-002 deferred erratum must be declared exactly once",
    )
    require(not any(unit == "OLP-0031" for unit, _body in after), "OLSIZ-002 erratum is attached to the collection pass")
    hook_bodies = [body for _unit, body in after] + [body for _rule, body in deferred]
    for audit_ids, title in SEMANTIC_NOTE_SPECS:
        matching_bodies = [
            body for body in hook_bodies
            if compact_text(title) in compact_text(body)
        ]
        require(len(matching_bodies) == 1, f"source-correction erratum title missing or duplicated: {title}")
        note_body = matching_bodies[0]
        for audit_id in audit_ids:
            occurrences = re.findall(
                rf"(?<![A-Z0-9-]){re.escape(audit_id)}(?![A-Z0-9-])",
                note_body,
            )
            require(len(occurrences) == 1, f"erratum audit id missing or duplicated: {audit_id}")


def validate_fixture() -> tuple[dict[str, object], list[dict[str, object]], list[dict[str, object]]]:
    require(sha256_file(FIXTURE_MANIFEST) == FIXTURE_MANIFEST_SHA256, "source-corrections fixture manifest identity changed")
    fixture = _mapping(load_json(FIXTURE_MANIFEST), "source-corrections fixture manifest")
    require_exact_keys(
        fixture,
        {
            "schema", "status", "audit_ids", "driver_preamble",
            "historical_evidence_continuity", "dependencies",
            "source_units", "physical_rules", "physical_rule_count",
            "semantic_finding_count", "rule_to_findings", "output",
            "expected_trace_events", "deferred_problem_rule", "citation_keys",
            "citation_resolution", "conditional_reference_keys",
            "conditional_reference_resolution", "native_acceptance",
            "tex_run", "not_full_reader",
        },
        "source-corrections fixture manifest",
    )
    require(fixture.get("schema") == "farsi-combined-source-corrections-probe-fixture-v5", "fixture schema mismatch")
    require(fixture.get("status") == "FIXTURE_GENERATED_NOT_NATIVE_VALIDATED", "fixture status changed")
    require(fixture.get("audit_ids") == AUDIT_IDS, "fixture audit ids changed")
    for key in ("physical_rule_count", "semantic_finding_count", "expected_trace_events"):
        require(is_json_integer(fixture.get(key)), f"fixture {key} must be a JSON integer")
    require(fixture.get("physical_rules") == PHYSICAL_RULES, "fixture physical rule order changed")
    require(fixture.get("physical_rule_count") == len(PHYSICAL_RULES), "fixture physical rule count changed")
    require(fixture.get("semantic_finding_count") == len(SEMANTIC_AUDIT_IDS), "fixture semantic finding count changed")
    require(fixture.get("expected_trace_events") == len(EXPECTED_TRACE), "fixture trace count changed")
    require(fixture.get("rule_to_findings") == RULE_TO_FINDINGS, "fixture physical-to-semantic mapping changed")
    require(fixture.get("deferred_problem_rule") == "OLSIZ-002", "fixture deferred rule changed")
    require(fixture.get("citation_keys") == CITATION_KEYS, "fixture citation key order changed")
    require(
        fixture.get("citation_resolution") == "preamble_bibcite_seed_no_external_bibliography_worker",
        "fixture citation resolution changed",
    )
    require(
        fixture.get("conditional_reference_keys") == CONDITIONAL_REFERENCE_KEYS,
        "fixture conditional-reference key order changed",
    )
    require(
        fixture.get("conditional_reference_resolution") == "in_memory_r_at_seed_no_synthetic_aux_labels",
        "fixture conditional-reference resolution changed",
    )
    require(fixture.get("native_acceptance") == NATIVE_ACCEPTANCE, "fixture native acceptance contract changed")
    require(fixture.get("tex_run") is False, "fixture incorrectly claims a TeX run")
    require(fixture.get("not_full_reader") is True, "fixture must remain outside full-reader qualification")
    require(sha256_file(GENERATOR) == GENERATOR_SHA256, "source-corrections probe generator identity changed")

    expected_driver = reconstructed_driver_bytes()
    require(
        read_file_bytes(DRIVER) == expected_driver,
        "source-corrections fixture is stale or differs from the independently reconstructed live-driver probe",
    )
    generation_driver = _validate_preamble_record(fixture.get("driver_preamble"))
    _validate_historical_continuity(
        fixture.get("historical_evidence_continuity"),
        generation_driver,
    )

    output = _validate_file_record(
        fixture.get("output"),
        label="fixture output",
        expected_path=DRIVER.relative_to(ROOT).as_posix(),
        pinned_identity=DRIVER_IDENTITY,
    )

    raw_units = fixture.get("source_units")
    require(isinstance(raw_units, list) and len(raw_units) == len(EXPECTED_UNITS), "fixture source-unit inventory changed")
    units: list[dict[str, object]] = []
    for raw, (unit, relative) in zip(raw_units, EXPECTED_UNITS, strict=True):
        units.append(
            _validate_file_record(
                raw,
                label=f"fixture source unit {unit}",
                expected_path=(LOCALE / relative).relative_to(ROOT).as_posix(),
                expected_unit=unit,
                pinned_identity=SOURCE_UNIT_IDENTITIES[unit],
            )
        )

    dependencies = _mapping(fixture.get("dependencies"), "fixture dependencies")
    require_exact_keys(dependencies, {"runtime", "overlay", "errata"}, "fixture dependencies")
    runtime = _validate_file_record(
        dependencies.get("runtime"),
        label="fixture runtime",
        expected_path=RUNTIME.relative_to(ROOT).as_posix(),
        pinned_identity=(12907, RUNTIME_SHA256),
    )
    overlay = _validate_file_record(
        dependencies.get("overlay"),
        label="fixture overlay",
        expected_path="source/locale/fa-IR/standalone/source-corrections.tex",
        pinned_identity=OVERLAY_IDENTITY,
    )
    errata = _validate_file_record(
        dependencies.get("errata"),
        label="fixture errata",
        expected_path="source/locale/fa-IR/standalone-errata.tex",
        pinned_identity=ERRATA_IDENTITY,
    )

    driver_text = read_file_text(DRIVER)
    require(driver_text.count(r"\OLSASourceCorrectionsStart") == 1, "probe must start source-correction tracing exactly once")
    require(driver_text.count(r"\OLSASourceCorrectionsVerify") == 1, "probe must verify source-correction coverage exactly once")
    require(driver_text.count(r"\OLSAInstallDeferredSourceContext") == 1, "probe must install deferred source context exactly once")
    require(driver_text.count(r"\OLSACorrectionProbeUnit") == len(EXPECTED_UNITS) + 1, "probe unit wrapper or invocations changed")
    calls = re.findall(r"\\OLSACorrectionProbeUnit\{(OLP-\d{4})\}%\s*\n\s*\{([^}\r\n]+)\}", driver_text)
    require(calls == EXPECTED_UNITS, "probe source-unit call order changed")
    require(driver_text.count(r"\printproblems") == 1, "probe must read the deferred problem stream exactly once")
    start_at = driver_text.index(r"\OLSASourceCorrectionsStart")
    install_at = driver_text.index(r"\OLSAInstallDeferredSourceContext")
    final_call_at = driver_text.rindex(r"\OLSACorrectionProbeUnit")
    heading_at = driver_text.index(r"\section*{آزمونِ مسئلهٔ معوق}")
    print_at = driver_text.index(r"\printproblems")
    verify_at = driver_text.index(r"\OLSASourceCorrectionsVerify")
    require(start_at < install_at < final_call_at < heading_at < print_at < verify_at, "deferred probe execution order changed")
    require(r"\chapter*{آزمونِ مسئلهٔ معوق}" not in driver_text, "deferred readback must not open a chapter")
    seeded_keys = re.findall(r"\\bibcite\{([^}]+)\}", driver_text)
    require(seeded_keys == CITATION_KEYS, "source-corrections probe citation seeds changed")
    seeded_reference_keys = re.findall(r"\\@namedef\{r@([^}]+)\}", driver_text)
    require(
        seeded_reference_keys == CONDITIONAL_REFERENCE_KEYS,
        "source-corrections probe conditional-reference seeds changed",
    )
    require(
        not re.search(r"\\(?:nocite|bibliography|bibliographystyle|bibitem)\b", driver_text),
        "source-corrections probe gained an external bibliography command",
    )

    overlay_text = read_file_text(ROOT / str(overlay["path"]))
    require(bool(overlay_text), "fixture overlay is empty")
    correction_records = validate_overlay(ROOT / str(overlay["path"]))
    validate_errata(ROOT / str(errata["path"]))
    require(bool(generation_driver and output and runtime), "validated fixture records unexpectedly empty")
    return fixture, units, correction_records


def parse_trace(text: str) -> list[tuple[str, str, str, str]]:
    lines = text.splitlines()
    require(bool(lines), "empty olcorrections sidecar")
    require(lines[0] == "source_id|environment|finding_id|occurrence", "wrong olcorrections header")
    require(all(line for line in lines[1:]), "blank olcorrections row")
    rows: list[tuple[str, str, str, str]] = []
    for line in lines[1:]:
        columns = tuple(line.split("|"))
        require(len(columns) == 4, f"wrong olcorrections column count: {line!r}")
        rows.append(columns)  # type: ignore[arg-type]
    require(rows == EXPECTED_TRACE, f"olcorrections events or order changed: {rows!r}")
    require(len(rows) == len(set(rows)), "duplicate olcorrections event")
    return rows


def validate_log_markers(text: str) -> None:
    lines = text.splitlines()
    event_prefix = "OL-STANDALONE-SOURCE-CORRECTION|"
    coverage_prefix = "OL-STANDALONE-SOURCE-CORRECTION-COVERAGE|"
    event_lines = [line for line in lines if line.startswith(event_prefix)]
    coverage_lines = [line for line in lines if line.startswith(coverage_prefix)]
    require(event_lines == EXPECTED_LOG_MARKERS, f"source-correction log marker sequence changed: {event_lines!r}")
    coverage = f"{coverage_prefix}{len(EXPECTED_TRACE)}|{len(EXPECTED_TRACE)}"
    require(coverage_lines == [coverage], f"exact source-correction coverage marker missing: {coverage_lines!r}")
    marker_family = [line for line in lines if line.startswith("OL-STANDALONE-SOURCE-CORRECTION")]
    require(marker_family == event_lines + coverage_lines, "malformed source-correction marker sibling present")
    for forbidden in (
        "Wrong correction count",
        "Duplicate source body",
        "Token formula undefined",
        "Token element undefined",
    ):
        require(forbidden not in text, f"forbidden source-correction log marker: {forbidden}")


def validate_auxiliary(primary: Path, common: dict[str, object]) -> dict[str, object]:
    aux = primary / f"{JOB}.aux"
    aux_snapshot = require_bound_output(common, aux)
    aux_text = read_file_text(aux)
    citation_rows = re.findall(r"^\\citation\{([^}]*)\}", aux_text, re.MULTILINE)
    require(citation_rows == CITATION_KEYS, "source-corrections AUX citation rows changed")
    require(
        not re.search(r"^\\(?:bibdata|bibstyle|bibcite)\{", aux_text, re.MULTILINE),
        "source-corrections probe wrote external bibliography metadata",
    )
    labels = re.findall(r"^\\newlabel\{([^}]+)\}", aux_text, re.MULTILINE)
    require(len(labels) == len(set(labels)), "source-corrections probe wrote duplicate label keys")
    for key in EXPECTED_LABELS:
        require(labels.count(key) == 1, f"expected local label missing or duplicated: {key}")
        require(labels.count(key + "@cref") == 1, f"expected cleveref label missing or duplicated: {key}")
    for key in CONDITIONAL_REFERENCE_KEYS:
        require(key not in labels and key + "@cref" not in labels, f"conditional-reference seed leaked into AUX labels: {key}")
    for suffix in ("bbl", "blg", "bcf"):
        require(not (primary / f"{JOB}.{suffix}").exists(), f"unexpected bibliography artifact: .{suffix}")
    return {
        "path": relative_repo_path(aux),
        "sha256": aux_snapshot.sha256,
        "expected_local_labels": len(EXPECTED_LABELS),
        "expected_cleveref_labels": len(EXPECTED_LABELS),
        "total_unique_label_keys": len(labels),
        "citation_keys": CITATION_KEYS,
        "citation_rows": len(citation_rows),
        "external_bibliography_keys": 0,
        "conditional_reference_seeds_not_written": CONDITIONAL_REFERENCE_KEYS,
    }


def _pdf_compact(text: str) -> str:
    # Poppler recovers the Arabic base letters which PyMuPDF can lose, but the
    # TeX/HarfBuzz ToUnicode map may attach a combining mark before rather than
    # after its base and may interleave punctuation from nearby math.  Fold both
    # reviewed needles and extracted text identically: retain every base letter,
    # digit and math operator; discard marks, controls, whitespace and ordinary
    # punctuation (except the normalized minus sign).
    translation = str.maketrans(
        {
            "٠": "0", "١": "1", "٢": "2", "٣": "3", "٤": "4",
            "٥": "5", "٦": "6", "٧": "7", "٨": "8", "٩": "9",
            "۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4",
            "۵": "5", "۶": "6", "۷": "7", "۸": "8", "۹": "9",
            "−": "-", "–": "-", "—": "-", "√": None,
        }
    )
    value = unicodedata.normalize("NFD", text).translate(translation)
    return "".join(
        character
        for character in value
        if not unicodedata.category(character).startswith(("M", "C"))
        and not character.isspace()
        and (
            not unicodedata.category(character).startswith("P")
            or character == "-"
        )
    )


def _parse_pdftotext_output(data: bytes, expected_pages: int) -> tuple[list[str], list[list[str]]]:
    require(expected_pages > 0, "invalid expected Poppler page count")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValidationError(f"Poppler PDF text is not strict UTF-8: {exc}") from exc
    require("\x00" not in text, "Poppler PDF text contains NUL")
    require("\ufffd" not in text, "Poppler PDF text contains a replacement character")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    raw_pages = text.split("\f")
    if raw_pages and not raw_pages[-1].strip():
        raw_pages.pop()
    require(len(raw_pages) == expected_pages, "Poppler and PyMuPDF page counts differ")
    pages: list[str] = []
    lines_by_page: list[list[str]] = []
    for page_index, raw_page in enumerate(raw_pages):
        require(raw_page.strip(), f"Poppler page {page_index + 1} has no extracted text")
        lines = [line for line in raw_page.split("\n") if line.strip()]
        require(lines, f"Poppler page {page_index + 1} has no nonempty extracted line")
        pages.append(raw_page.strip("\n"))
        lines_by_page.append(lines)
    return pages, lines_by_page


def load_poppler_layout_text(
    pdf_path: Path, common: dict[str, object], expected_pages: int,
) -> tuple[list[str], list[list[str]], dict[str, object]]:
    receipt = _mapping(common.get("receipt"), "validated receipt")
    executables = receipt.get("executable_identities")
    require(isinstance(executables, list) and len(executables) == 1, "validated receipt lacks one LuaLaTeX executable")
    lualatex = _mapping(executables[0], "validated LuaLaTeX executable")
    lualatex_path = lualatex.get("path")
    require(isinstance(lualatex_path, str) and lualatex_path, "validated LuaLaTeX path is missing")
    executable = Path(lualatex_path).resolve().with_name("pdftotext.exe")
    require(executable.name.casefold() == "pdftotext.exe" and executable.is_file(), "Poppler pdftotext executable is missing")
    require(sha256_file(executable) == PDFTOTEXT_SHA256, "unreviewed Poppler pdftotext executable")
    poppler_dll = executable.with_name(POPPLER_DLL_NAME)
    require(poppler_dll.is_file(), "Poppler implementation DLL is missing")
    require(sha256_file(poppler_dll) == POPPLER_DLL_SHA256, "unreviewed Poppler implementation DLL")

    try:
        version_run = subprocess.run(
            [str(executable), "-v"], capture_output=True, check=False, timeout=30,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise ValidationError(f"cannot execute Poppler version probe: {exc}") from exc
    require(version_run.returncode == 0 and not version_run.stdout, "Poppler version probe failed or wrote stdout")
    try:
        version_text = version_run.stderr.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValidationError(f"Poppler version output is not strict UTF-8: {exc}") from exc
    version_lines = version_text.replace("\r\n", "\n").replace("\r", "\n").splitlines()
    require(
        bool(version_lines) and version_lines[0] == f"pdftotext version {PDFTOTEXT_VERSION}",
        "unreviewed Poppler pdftotext version",
    )

    pdf_bytes = read_file_bytes(pdf_path)
    require(sha256_bytes(pdf_bytes) == common.get("pdf_sha256"), "Poppler input PDF is not the receipt-bound PDF bytes")
    options = ["-layout", "-enc", "UTF-8", "-", "-"]
    try:
        extraction = subprocess.run(
            [str(executable), *options],
            input=pdf_bytes,
            capture_output=True,
            check=False,
            timeout=60,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise ValidationError(f"cannot execute Poppler text extraction: {exc}") from exc
    require(extraction.returncode == 0, "Poppler text extraction exited nonzero")
    require(not extraction.stderr, "Poppler text extraction emitted diagnostics")
    pages, lines_by_page = _parse_pdftotext_output(extraction.stdout, expected_pages)
    canonical_text = "\n\f\n".join(pages)
    return pages, lines_by_page, {
        "name": executable.name,
        "bytes": file_size(executable),
        "sha256": PDFTOTEXT_SHA256,
        "implementation_dll": {
            "name": POPPLER_DLL_NAME,
            "bytes": file_size(poppler_dll),
            "sha256": POPPLER_DLL_SHA256,
        },
        "version": PDFTOTEXT_VERSION,
        "options": options,
        "receipt_bound_pdf_stdin_sha256": sha256_bytes(pdf_bytes),
        "canonical_extracted_text_sha256": sha256_bytes(canonical_text.encode("utf-8")),
        "raw_stdout_bytes": len(extraction.stdout),
        "raw_stdout_sha256": sha256_bytes(extraction.stdout),
        "pages": len(pages),
        "nonempty_lines": sum(len(lines) for lines in lines_by_page),
    }


def _line_window_positions(
    lines_by_page: list[list[str]], fragments: tuple[str, ...],
    *, max_lines: int = MAX_SEMANTIC_WINDOW_LINES,
) -> list[tuple[int, int, int]]:
    require(fragments and 0 < max_lines <= MAX_SEMANTIC_WINDOW_LINES, "invalid semantic line-window request")
    needles = [_pdf_compact(fragment) for fragment in fragments]
    require(all(needles), "empty semantic needle after PDF folding")
    candidates: list[tuple[int, int, int]] = []
    for page_index, lines in enumerate(lines_by_page):
        for start in range(len(lines)):
            for end in range(start, min(len(lines), start + max_lines)):
                compact_window = _pdf_compact("\n".join(lines[start : end + 1]))
                if all(needle in compact_window for needle in needles):
                    candidates.append((page_index, start, end))
    # A single occurrence otherwise yields every larger window which contains
    # it.  Retain only inclusion-minimal windows so occurrence counts remain
    # meaningful while never joining text across a page boundary.
    return [
        candidate
        for candidate in candidates
        if not any(
            other[0] == candidate[0]
            and other != candidate
            and other[1] >= candidate[1]
            and other[2] <= candidate[2]
            for other in candidates
        )
    ]


def _audit_id_positions(lines_by_page: list[list[str]], audit_id: str) -> list[tuple[int, int, int]]:
    pattern = re.compile(rf"(?<![A-Z0-9-]){re.escape(audit_id)}(?![A-Z0-9-])")
    positions: list[tuple[int, int, int]] = []
    for page_index, lines in enumerate(lines_by_page):
        for line_index, line in enumerate(lines):
            positions.extend((page_index, line_index, line_index) for _match in pattern.finditer(line))
    return positions


def _precedes(left: tuple[int, int, int], right: tuple[int, int, int]) -> bool:
    return (left[0], left[2]) < (right[0], right[1])


def validate_pdf_pages(
    pages: list[str], lines_by_page: list[list[str]],
    *, semantic_expected_pages: dict[str, list[set[int]]] = SEMANTIC_EXPECTED_REQUIRED_PAGES,
) -> dict[str, object]:
    require(len(pages) == len(lines_by_page), "PDF page/line extraction counts differ")
    for phrase in REQUIRED_PDF_PHRASES:
        require(
            _line_window_positions(lines_by_page, (phrase,), max_lines=2),
            f"source-corrections PDF phrase missing from a bounded line window: {phrase}",
        )
    rejected = [
        phrase for phrase in REJECTED_PDF_PHRASES
        if _line_window_positions(lines_by_page, (phrase,))
    ]
    require(not rejected, f"source-corrections rejected PDF phrases present: {rejected}")

    note_evidence: dict[str, object] = {}
    note_title_position: dict[str, tuple[int, int, int]] = {}
    all_note_ids = [audit_id for ids, _title in SEMANTIC_NOTE_SPECS for audit_id in ids]
    require(sorted(all_note_ids) == sorted(SEMANTIC_AUDIT_IDS), "semantic note inventory does not cover the audit ids exactly")
    for audit_ids, title in SEMANTIC_NOTE_SPECS:
        title_positions = _line_window_positions(lines_by_page, (title,), max_lines=2)
        require(len(title_positions) == 1, f"erratum title missing or duplicated in PDF: {title}")
        title_position = title_positions[0]
        for audit_id in audit_ids:
            id_positions = _audit_id_positions(lines_by_page, audit_id)
            require(len(id_positions) == 1, f"adjacent audit id missing or duplicated in PDF: {audit_id}")
            require(id_positions[0][0] == title_position[0], f"audit id is not on its erratum-title page: {audit_id}")
            note_title_position[audit_id] = title_position
            note_evidence[audit_id] = {
                "title": title,
                "title_page_one_based": title_position[0] + 1,
                "title_line_start_one_based": title_position[1] + 1,
                "title_line_end_one_based": title_position[2] + 1,
                "audit_id_line_one_based": id_positions[0][1] + 1,
            }

    deferred_positions = _line_window_positions(lines_by_page, ("آزمونِ مسئلهٔ معوق",), max_lines=2)
    require(len(deferred_positions) == 1, "deferred-problem heading missing or duplicated")
    deferred_page = deferred_positions[0][0]
    require(note_title_position["OLSIZ-002"][0] >= deferred_page, "OLSIZ-002 note appeared before deferred readback")
    for audit_id, position in note_title_position.items():
        if audit_id != "OLSIZ-002":
            require(position[0] < deferred_page, f"ordinary erratum appeared in deferred section: {audit_id}")

    semantic_evidence: dict[str, object] = {}
    spec_ids = [audit_id for audit_id, _required, _rejected in SEMANTIC_DELTA_SPECS]
    require(sorted(spec_ids) == sorted(SEMANTIC_AUDIT_IDS), "semantic delta inventory does not cover the audit ids exactly")
    for audit_id, required_groups, rejected_groups in SEMANTIC_DELTA_SPECS:
        expected_page_sets = semantic_expected_pages.get(audit_id)
        require(
            isinstance(expected_page_sets, list) and len(expected_page_sets) == len(required_groups),
            f"reviewed semantic page-window inventory changed for {audit_id}",
        )
        required_records: list[dict[str, object]] = []
        for group_index, (fragments, expected_count) in enumerate(required_groups):
            positions = _line_window_positions(lines_by_page, fragments)
            require(len(positions) == expected_count, f"rendered semantic delta count changed for {audit_id}: {fragments!r}")
            actual_pages = {position[0] + 1 for position in positions}
            require(
                actual_pages == expected_page_sets[group_index],
                f"semantic delta escaped its reviewed page window for {audit_id}: {fragments!r}",
            )
            require(all(_precedes(position, note_title_position[audit_id]) for position in positions), f"semantic delta was found only in/after its erratum note: {audit_id}")
            required_records.append(
                {
                    "fragments": list(fragments),
                    "reviewed_pages_one_based": sorted(expected_page_sets[group_index]),
                    "positions": [
                        {
                            "page_one_based": page + 1,
                            "line_start_one_based": start + 1,
                            "line_end_one_based": end + 1,
                        }
                        for page, start, end in positions
                    ],
                }
            )
        for fragments in rejected_groups:
            require(not _line_window_positions(lines_by_page, fragments), f"legacy semantic line window remains for {audit_id}: {fragments!r}")
        semantic_evidence[audit_id] = {
            "required_page_local_line_windows": required_records,
            "rejected_page_local_line_window_groups_absent": [list(group) for group in rejected_groups],
        }

    citation_evidence: dict[str, object] = {}
    for citation_key, fragments in CITATION_PDF_SPECS:
        positions = _line_window_positions(lines_by_page, fragments, max_lines=3)
        require(len(positions) == 1, f"resolved citation missing or duplicated in PDF: {citation_key}")
        citation_evidence[citation_key] = {
            "fragments": list(fragments),
            "page_one_based": positions[0][0] + 1,
            "line_start_one_based": positions[0][1] + 1,
            "line_end_one_based": positions[0][2] + 1,
        }

    text = "\n\f\n".join(pages)
    require("!!" not in text and "\\OLSA" not in text, "raw TeX shorthand/control leaked into PDF text")
    return {
        "deferred_heading": {
            "page_one_based": deferred_page + 1,
            "line_start_one_based": deferred_positions[0][1] + 1,
            "line_end_one_based": deferred_positions[0][2] + 1,
        },
        "errata_notes": note_evidence,
        "semantic_deltas": semantic_evidence,
        "resolved_citations": citation_evidence,
    }


def validate(receipt_path: Path) -> dict[str, object]:
    clear_snapshot_cache()
    fixture, units, correction_records = validate_fixture()
    driver_sha = str(_mapping(fixture["output"], "fixture output")["sha256"])
    common = validate_diagnostic_receipt(
        receipt_path,
        job=JOB,
        driver=DRIVER,
        driver_sha256=driver_sha,
        allow_reference_warnings=True,
        allow_latex_rerun_warnings=True,
    )

    inputs = common["recorder_inputs"]
    fixture_dependencies = _mapping(fixture["dependencies"], "fixture dependencies")
    dependency_paths = [
        DRIVER,
        RUNTIME,
        ROOT / str(_mapping(fixture_dependencies["overlay"], "overlay")["path"]),
        ROOT / str(_mapping(fixture_dependencies["errata"], "errata")["path"]),
        *(ROOT / str(record["path"]) for record in units),
    ]
    require_recorder_inputs(inputs, dependency_paths)
    forbidden_inputs = [path for path in inputs if path.suffix.casefold() in {".bib", ".bst", ".bbl", ".blg", ".bcf"}]
    require(not forbidden_inputs, "source-corrections probe read bibliography inputs")

    sidecar = common["primary"] / f"{JOB}.olcorrections"
    sidecar_snapshot = require_bound_output(common, sidecar)
    sidecar_text = read_file_text(sidecar)
    trace = parse_trace(sidecar_text)
    validate_log_markers(common["log_text"])
    auxiliary = validate_auxiliary(common["primary"], common)

    fitz_pages, _fitz_blocks, fitz_lines, fitz_version, page_geometry = load_pdf_text(common["pdf"])
    require(len(fitz_pages) >= 13, "source-corrections diagnostic has too few pages for title, eleven units, and deferred readback")
    poppler_pages, poppler_lines, poppler_identity = load_poppler_layout_text(
        common["pdf"], common, len(fitz_pages),
    )
    fitz_text = "\n\f\n".join(fitz_pages)
    poppler_text = "\n\f\n".join(poppler_pages)
    semantic_locations = validate_pdf_pages(poppler_pages, poppler_lines)

    evidence = base_evidence(
        kind="combined-functions-size-source-corrections",
        common=common,
        fixture=DRIVER,
        fixture_manifest=FIXTURE_MANIFEST,
    )
    evidence.update(
        {
            "schema": "farsi-combined-source-corrections-native-probe-qa-v3",
            "status": "PASS_NATIVE_DIAGNOSTIC_PENDING_COMPLETE_VISUAL_INSPECTION_NOT_FULL_READER",
            "audit_ids": AUDIT_IDS,
            "validator": {
                "path": relative_repo_path(VALIDATOR),
                "bytes": file_size(VALIDATOR),
                "sha256": sha256_file(VALIDATOR),
            },
            "dependencies": [
                {
                    "path": relative_repo_path(path),
                    "bytes": file_size(path),
                    "sha256": sha256_file(path),
                }
                for path in dependency_paths
            ],
            "trace": {
                "path": relative_repo_path(sidecar),
                "sha256": sidecar_snapshot.sha256,
                "events": [list(row) for row in trace],
                "coverage": f"{len(trace)}/{len(EXPECTED_TRACE)}",
                "declaration_order": [list(row) for row in EXPECTED_DECLARATIONS],
                "deferred_rule_executes_last": trace[-1][2] == "OLSIZ-002",
            },
            "correction_body_identities": correction_records,
            "auxiliary": auxiliary,
            "pdf_text": {
                "pages": len(poppler_pages),
                "logical_text_extractor": poppler_identity,
                "logical_text_sha256": sha256_bytes(poppler_text.encode("utf-8")),
                "logical_nonempty_lines": sum(len(lines) for lines in poppler_lines),
                "required_corrected_phrases": len(REQUIRED_PDF_PHRASES),
                "rejected_legacy_phrases_absent": len(REJECTED_PDF_PHRASES),
                "adjacent_audit_ids": len(SEMANTIC_AUDIT_IDS),
                "semantic_locations": semantic_locations,
                "geometry_text_extractor": {
                    "name": "PyMuPDF",
                    "version": fitz_version,
                    "pages": len(fitz_pages),
                    "text_lines": sum(len(lines) for lines in fitz_lines),
                    "extracted_text_sha256": sha256_bytes(fitz_text.encode("utf-8")),
                },
                "page_geometry": page_geometry,
            },
            "checks": {
                "exact_fifteen_event_sidecar_and_log_order": True,
                "exact_coverage_marker": True,
                "fixture_generator_overlay_errata_runtime_and_eleven_source_hashes": True,
                "balanced_five_argument_declaration_parser_and_body_hashes": True,
                "corrected_pdf_semantic_page_local_line_windows_present_before_adjacent_notes": True,
                "rejected_legacy_pdf_semantic_page_local_line_windows_absent": True,
                "deferred_problem_context_readback_and_last_event": True,
                "local_label_and_cleveref_keys_preserved": True,
                "exact_source_citations_resolved_without_external_bibliography_worker_or_artifacts": True,
                "guard_mutex_tree_exit_and_log_receipt_recomputed": True,
            },
            "limitations": [
                "The one-pass bounded diagnostic may retain expected undefined-reference and rerun notices from external units; the two exact source citations are locally seeded, while undefined citations and external bibliography failures are rejected.",
                "Poppler semantic matching folds Arabic combining marks, bidi/control characters, whitespace, and ordinary punctuation because the reviewed LuaTeX ToUnicode map can reorder marks and interleave punctuation; exact source-unit, replacement-body, event-trace, and PDF-byte hashes retain the identity that this folded comparison alone cannot prove.",
                "Opaque, nonwhite extracted-span geometry is recorded, but extraction cannot prove freedom from occlusion or overlap. Every page still requires rendered full-page inspection.",
                "This diagnostic does not qualify the complete 722-unit reader.",
            ],
        }
    )
    return evidence


def self_test() -> dict[str, object]:
    valid = "source_id|environment|finding_id|occurrence\n" + "\n".join(
        "|".join(row) for row in EXPECTED_TRACE
    ) + "\n"
    parse_trace(valid)
    mutations = [
        "\n".join(valid.splitlines()[:-1]) + "\n",
        valid + "|".join(EXPECTED_TRACE[0]) + "\n",
        valid.replace("OLFUN-002|1", "OLFUN-002|2", 1),
        valid.replace("OLP-0021", "OLP-9999", 1),
        valid.replace("|ex|", "|proof|", 1),
    ]
    for mutation in mutations:
        expect_validation_error(parse_trace, mutation)

    coverage = (
        "OL-STANDALONE-SOURCE-CORRECTION-COVERAGE|"
        f"{len(EXPECTED_TRACE)}|{len(EXPECTED_TRACE)}"
    )
    marker_log = "\n".join(EXPECTED_LOG_MARKERS + [coverage])
    validate_log_markers(marker_log)
    wrong_coverage = (
        "OL-STANDALONE-SOURCE-CORRECTION-COVERAGE|"
        f"{len(EXPECTED_TRACE) - 1}|{len(EXPECTED_TRACE)}"
    )
    expect_validation_error(validate_log_markers, marker_log.replace(coverage, wrong_coverage))
    expect_validation_error(validate_log_markers, marker_log + "\n" + EXPECTED_LOG_MARKERS[0])
    expect_validation_error(
        validate_log_markers,
        marker_log + "\nOL-STANDALONE-SOURCE-CORRECTION|malformed",
    )

    semantic_lines: dict[str, list[str]] = {}
    for audit_id, required_groups, _rejected_groups in SEMANTIC_DELTA_SPECS:
        semantic_lines[audit_id] = [
            " | ".join(fragments)
            for fragments, expected_count in required_groups
            for _occurrence in range(expected_count)
        ]

    ordinary_lines = [
        "آزمونِ تصحیح‌های ممیزیِ منبع\n"
        "این سند فقط آزمونِ تشخیصیِ لایهٔ تصحیح است و خوانشگرِ نهایی نیست",
        "Frege 1884",
        "Cantor 1892",
    ]
    deferred_lines = ["آزمونِ مسئلهٔ معوق"]
    for audit_ids, title in SEMANTIC_NOTE_SPECS:
        destination = deferred_lines if audit_ids == ("OLSIZ-002",) else ordinary_lines
        for audit_id in audit_ids:
            destination.extend(semantic_lines[audit_id])
        destination.append(title + "\n" + " ".join(audit_ids))

    valid_lines = [ordinary_lines, deferred_lines]
    valid_pages = ["\n".join(lines) for lines in valid_lines]
    synthetic_expected_pages = {
        audit_id: [({2} if audit_id == "OLSIZ-002" else {1}) for _group in required_groups]
        for audit_id, required_groups, _rejected_groups in SEMANTIC_DELTA_SPECS
    }
    validate_pdf_pages(
        valid_pages, valid_lines, semantic_expected_pages=synthetic_expected_pages,
    )
    for rejected in REJECTED_PDF_PHRASES:
        bad_lines = [list(ordinary_lines), list(deferred_lines)]
        bad_lines[0].append(rejected)
        bad_pages = ["\n".join(lines) for lines in bad_lines]
        expect_validation_error(
            validate_pdf_pages, bad_pages, bad_lines,
            semantic_expected_pages=synthetic_expected_pages,
        )
    missing_semantic = [list(ordinary_lines), list(deferred_lines)]
    missing_semantic[0].remove(semantic_lines["OLFUN-002"][0])
    expect_validation_error(
        validate_pdf_pages,
        ["\n".join(lines) for lines in missing_semantic],
        missing_semantic,
        semantic_expected_pages=synthetic_expected_pages,
    )
    duplicate_id = [list(ordinary_lines), list(deferred_lines)]
    duplicate_id[0].append("OLSIZ-010")
    expect_validation_error(
        validate_pdf_pages,
        ["\n".join(lines) for lines in duplicate_id],
        duplicate_id,
        semantic_expected_pages=synthetic_expected_pages,
    )
    missing_citation = [list(ordinary_lines), list(deferred_lines)]
    missing_citation[0].remove("Frege 1884")
    expect_validation_error(
        validate_pdf_pages,
        ["\n".join(lines) for lines in missing_citation],
        missing_citation,
        semantic_expected_pages=synthetic_expected_pages,
    )
    wrong_page_scope = {
        audit_id: [set(pages) for pages in page_sets]
        for audit_id, page_sets in synthetic_expected_pages.items()
    }
    wrong_page_scope["OLFUN-002"][0] = {2}
    expect_validation_error(
        validate_pdf_pages, valid_pages, valid_lines,
        semantic_expected_pages=wrong_page_scope,
    )
    require(
        not _line_window_positions(
            [["cross-page-left"], ["cross-page-right"]],
            ("cross-page-left", "cross-page-right"),
        ),
        "semantic line-window matcher crossed a page boundary",
    )
    require(
        not _line_window_positions(
            [[f"bounded-window-{index}" for index in range(7)]],
            tuple(f"bounded-window-{index}" for index in range(7)),
        ),
        "semantic line-window matcher exceeded its six-line cap",
    )
    require(
        _pdf_compact("آزمونِ") == _pdf_compact("آزموِن")
        and _pdf_compact("آزمونِ") != _pdf_compact("آزموِ"),
        "PDF semantic fold no longer tolerates mark reordering while preserving base letters",
    )
    parsed_pages, parsed_lines = _parse_pdftotext_output(b"first\n\fsecond\n\f", 2)
    require(parsed_pages == ["first", "second"] and parsed_lines == [["first"], ["second"]], "Poppler parser self-test changed")
    expect_validation_error(_parse_pdftotext_output, b"first\n\f\f", 2)
    expect_validation_error(_parse_pdftotext_output, b"\xff", 1)
    expect_validation_error(_parse_pdftotext_output, b"bad\x00\f", 1)
    common_negative_controls = self_test_common_primitives()
    return {
        "schema": "farsi-functions-source-corrections-postbuild-self-test-v1",
        "status": "PASS",
        "negative_controls": len(mutations) + 14 + len(REJECTED_PDF_PHRASES) + common_negative_controls,
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
