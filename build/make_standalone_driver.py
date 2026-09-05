"""Generate an additive driver from SHA-bound, unchanged release preambles.

Frozen content files are never written. A separately audited render-time layer
applies exact source-bound corrections. Run from any directory; no TeX invocation.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import tempfile

ROOT = Path(__file__).resolve().parents[1]
LOCALE = ROOT / 'source/locale/fa-IR'
INPUTS = {
    'open-logic-complete-fa-IR.tex': '904ad566cefdd196193db1aa23182c01f624daf132d0e659b95aac50f583956d',
    'open-logic-complete-fa-IR-readable-letter-r2.tex': 'dd4e8adcf16711523491df2d4bb9785e40c24d2a321aa37978f51e138bae9e50',
}

CORRECTION_INPUTS = {
    'source/locale/fa-IR/standalone/source-corrections.tex': '31aa63c81c38709d90ee68302f391548098094f5d1a26757bb6b3dfd3d0ea410',
    'source/locale/fa-IR/standalone-errata.tex': '77efdcb3fc8848406bda7f2f766491da23abb72e2c6971a71734bd6d93379d63',
    'evidence/SOURCE_CORRECTIONS_PROBE_FIXTURE.json': '10e1807b301424415c7feac2b663264cda064dd75779da0b3b3cbc99bcd564b5',
    'evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_QA.json': '6afcaadc1c1997ef4a537b9aba469c470f8caf82322c36fca729dadec4d3d1ce',
    'evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_VISUAL_QA.json': '3a1f7e00ddccbf4ae10faab58d86e019ca8ac129bfbdb96646a1295146a7800d',
    'evidence/SHARED_SOURCE_AUDIT_OLSIZ_20260904.json': '9abf143608a4fb407eede521966a33a744b4d5b9e037e5bb35bcaa18aeb28134',
}
HISTORICAL_NATIVE_OVERLAY_SHA256 = '9f9875f14dbcf20f6482cdc40f2eff1787c6a084708eed154be521d6c600ac60'
AUDIT_AUTHORITIES = {
    'OLFUN-20260904': {
        'review_sha256': 'bc183d34b6ac57cc00e2df76d00277cdd2fabee293d12beb142d2e27344f8d24',
        'findings_sha256': 'eee57facbea44f65a19a816fb12cbc86be0b18e21dcffeeed943f52f7e332960',
        'findings': [f'OLFUN-{number:03d}' for number in range(1, 6)],
    },
    'OLSIZ-20260904': {
        'review_sha256': '26913176baacbda5ae8a47bcc82ccf0366b0763313e6eeeb45df59e64249a1f9',
        'findings_sha256': '9b6e836c8432eb75d331913983603796d6557da6ec3ad71b846b2a248374cd07',
        'findings': [f'OLSIZ-{number:03d}' for number in range(1, 11)],
    },
}
HISTORICAL_CORRECTED_UNITS = [
    'OLP-0021', 'OLP-0023', 'OLP-0024', 'OLP-0029', 'OLP-0031',
    'OLP-0032', 'OLP-0034', 'OLP-0035', 'OLP-0036', 'OLP-0039', 'OLP-0040',
]
HISTORICAL_PHYSICAL_RULES = [
    'OLFUN-002', 'OLFUN-003', 'OLFUN-004', 'OLFUN-005',
    'OLFUN-001-THEOREM', 'OLFUN-001-PROOF', 'OLSIZ-001', 'OLSIZ-002',
    'OLSIZ-003', 'OLSIZ-004', 'OLSIZ-005', 'OLSIZ-006', 'OLSIZ-007',
    'OLSIZ-008+009', 'OLSIZ-010',
]
CURRENT_CORRECTED_UNITS = [
    'OLP-0021', 'OLP-0023', 'OLP-0024', 'OLP-0029', 'OLP-0031',
    'OLP-0032', 'OLP-0034', 'OLP-0035', 'OLP-0036', 'OLP-0039', 'OLP-0040',
    'OLP-0091', 'OLP-0133', 'OLP-0164', 'OLP-0165', 'OLP-0179', 'OLP-0180',
    'OLP-0193', 'OLP-0220', 'OLP-0273', 'OLP-0286', 'OLP-0362', 'OLP-0379',
    'OLP-0391', 'OLP-0526', 'OLP-0527', 'OLP-0569', 'OLP-0570', 'OLP-0599',
]
CURRENT_PHYSICAL_RULES = [
    'OLFUN-002', 'OLFUN-003', 'OLFUN-004', 'OLFUN-005',
    'OLFUN-001-THEOREM', 'OLFUN-001-PROOF', 'OLSIZ-001', 'OLSIZ-002',
    'OLSIZ-003', 'OLSIZ-004', 'OLSIZ-005', 'OLSIZ-006', 'OLSIZ-007',
    'OLSIZ-008+009', 'OLSIZ-010',
    *[f'OLEMPH-{number:03d}' for number in range(1, 8)],
    'OLVIS-0362', 'OLVIS-0379', 'OLVIS-0391', 'OLVIS-0569', 'OLVIS-0570',
    'OLVIS-0599', 'OLVIS-0091', 'OLVIS-0133-OVERFLOW', 'OLVIS-0133-COMMA',
    'OLVIS-0164', 'OLVIS-0165', 'OLVIS-0193', 'OLVIS-0220', 'OLVIS-0273',
    'OLVIS-0286', 'OLVIS-0526', 'OLVIS-0527',
]
CURRENT_SEMANTIC_FINDINGS = [
    *[f'OLFUN-{number:03d}' for number in range(1, 6)],
    *[f'OLSIZ-{number:03d}' for number in range(1, 11)],
    *[f'OLEMPH-{number:03d}' for number in range(1, 8)],
    'OLVIS-0362', 'OLVIS-0379', 'OLVIS-0391', 'OLVIS-0569', 'OLVIS-0570',
    'OLVIS-0599', 'OLVIS-0091', 'OLVIS-0133-OVERFLOW', 'OLVIS-0133-COMMA',
    'OLVIS-0164', 'OLVIS-0165', 'OLVIS-0193', 'OLVIS-0220', 'OLVIS-0273',
    'OLVIS-0286', 'OLVIS-0526', 'OLVIS-0527',
]
CURRENT_EXACT_RULE_COUNT = 39
CURRENT_RUNTIME_EVENT_COUNT = 40
CURRENT_DOCUMENT_TEXT_SUBSTITUTIONS = 24
assert len(CURRENT_PHYSICAL_RULES) == CURRENT_EXACT_RULE_COUNT
assert len(CURRENT_SEMANTIC_FINDINGS) == CURRENT_EXACT_RULE_COUNT
assert len(CURRENT_CORRECTED_UNITS) == 29


def sha(data):
    return hashlib.sha256(data).hexdigest()


def bound_project_read(relative):
    data = (ROOT / relative).read_bytes()
    assert sha(data) == CORRECTION_INPUTS[relative], relative
    return data

def bound_read(name):
    data = (LOCALE / name).read_bytes()
    assert sha(data) == INPUTS[name], name
    return data.decode('utf-8-sig').replace('\r\n', '\n')


correction_bytes = {path: bound_project_read(path) for path in CORRECTION_INPUTS}
assert correction_bytes['source/locale/fa-IR/standalone-errata.tex'].count(
    br'\noindent\textbf{'
) == 16
correction_fixture = json.loads(
    correction_bytes['evidence/SOURCE_CORRECTIONS_PROBE_FIXTURE.json'].decode('utf-8-sig')
)
assert correction_fixture['schema'] == 'farsi-combined-source-corrections-probe-fixture-v5'
assert correction_fixture['audit_ids'] == list(AUDIT_AUTHORITIES)
assert correction_fixture['driver_preamble'] == {
    'path': 'source/locale/fa-IR/open-logic-standalone-fa-IR.tex',
    'boundary': r'\begin{document}',
    'boundary_inclusive': True,
    'bytes': 8212,
    'sha256': 'C6E31F3488F61233B446D848D80C0CC04D319D99D6C77C1FA28ADDFC4907CE47',
}
assert correction_fixture['historical_evidence_continuity']['status'] == 'PASS_PREAMBLE_AND_PROBE_TEX_BYTES_UNCHANGED'
assert correction_fixture['historical_evidence_continuity']['preamble_bytes_unchanged'] is True
assert correction_fixture['historical_evidence_continuity']['probe_tex_bytes_unchanged'] is True
assert correction_fixture['historical_evidence_continuity']['post_boundary_driver_changes_out_of_scope'] is True
assert correction_fixture['physical_rules'] == HISTORICAL_PHYSICAL_RULES
assert correction_fixture['physical_rule_count'] == 15
assert correction_fixture['semantic_finding_count'] == 15
assert correction_fixture['expected_trace_events'] == 15
assert [row['unit_id'] for row in correction_fixture['source_units']] == HISTORICAL_CORRECTED_UNITS
assert correction_fixture['dependencies']['overlay']['sha256'].lower() == HISTORICAL_NATIVE_OVERLAY_SHA256
assert correction_fixture['dependencies']['errata']['sha256'].lower() == CORRECTION_INPUTS['source/locale/fa-IR/standalone-errata.tex']

correction_native_qa = json.loads(
    correction_bytes['evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_QA.json'].decode('utf-8-sig')
)
assert correction_native_qa['status'] == 'PASS_NATIVE_DIAGNOSTIC_PENDING_COMPLETE_VISUAL_INSPECTION_NOT_FULL_READER'
assert correction_native_qa['audit_ids'] == list(AUDIT_AUTHORITIES)
assert correction_native_qa['trace']['coverage'] == '15/15'
assert len(correction_native_qa['trace']['events']) == 15
native_dependencies = {
    row['path']: row['sha256'] for row in correction_native_qa['dependencies']
}
assert native_dependencies['source/locale/fa-IR/standalone/source-corrections.tex'] == HISTORICAL_NATIVE_OVERLAY_SHA256
assert native_dependencies['source/locale/fa-IR/standalone-errata.tex'] == CORRECTION_INPUTS['source/locale/fa-IR/standalone-errata.tex']
assert {
    event[0] for event in correction_native_qa['trace']['events']
} == set(HISTORICAL_CORRECTED_UNITS)

correction_visual_qa = json.loads(
    correction_bytes['evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_VISUAL_QA.json'].decode('utf-8-sig')
)
assert correction_visual_qa['status'] == 'PASS_COMPLETE_VISUAL_INSPECTION_NATIVE_DIAGNOSTIC_NOT_FULL_READER'
assert correction_visual_qa['source_pdf']['pages'] == 29
assert correction_visual_qa['semantic_qa_receipt']['sha256'] == CORRECTION_INPUTS['evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_QA.json']

olsiz_binding = json.loads(
    correction_bytes['evidence/SHARED_SOURCE_AUDIT_OLSIZ_20260904.json'].decode('utf-8-sig')
)
assert olsiz_binding['audit_id'] == 'OLSIZ-20260904'
assert olsiz_binding['finding_count'] == 10
assert [row['id'] for row in olsiz_binding['required_findings']] == AUDIT_AUTHORITIES['OLSIZ-20260904']['findings']
assert olsiz_binding['authority']['review_sha256'].lower() == AUDIT_AUTHORITIES['OLSIZ-20260904']['review_sha256']
assert olsiz_binding['authority']['findings_sha256'].lower() == AUDIT_AUTHORITIES['OLSIZ-20260904']['findings_sha256']

base = bound_read('open-logic-complete-fa-IR.tex').split(r'\begin{document}', 1)[0]
wrapper = bound_read('open-logic-complete-fa-IR-readable-letter-r2.tex')
layout = wrapper[wrapper.index(r'\AddToHook{class/memoir/after}'):wrapper.index(r'\input{open-logic-complete-fa-IR.tex}')]

# Localize only glyphs produced in Persian text nodes.  Babel's LuaTeX-level
# mapdigits transform runs after TeX has written counter/anchor/AUX tokens and
# skips math nodes, so the purely numeric cleveref metadata below remains
# parseable while visible Persian prose, headings and folios use U+06F0--U+06F9.
# English language spans remain ASCII and protect machine-readable identifiers.
babel_persian = r'\babelprovide[import=fa,main,onchar=ids fonts]{persian}'
assert base.count(babel_persian) == 1
base = base.replace(
    babel_persian,
    r'\babelprovide[import=fa,main,onchar=ids fonts,mapdigits]{persian}',
)

# The previous counter-specific fixes referred to these exact AUX namespaces:
# 16.5 -> fol:syn:ass; 23.7 -> fol:com:ide; 43.2 -> lam:cr:pb.
old = re.search(r'  % Three source proofs.*?(?=  \\hypersetup)', layout, re.S)
assert old
layout = layout[:old.start()] + r'''
  % Scope by stable semantic namespace, never by mutable chapter numbers.
  \AddToHook{env/proof/begin}{%
    \edef\OLStandaloneSection{\theolpart:\theolchapter:\theolsection}%
    \ifdefstring{\OLStandaloneSection}{fol:syn:ass}{\fontsize{12pt}{15pt}\selectfont}{}%
    \ifdefstring{\OLStandaloneSection}{fol:com:ide}{\fontsize{13pt}{16pt}\selectfont}{}%
    \ifdefstring{\OLStandaloneSection}{lam:cr:pb}{\fontsize{13.5pt}{17pt}\selectfont}{}%
  }%
  \AddToHook{env/defn/begin}{%
    \edef\OLStandaloneSection{\theolpart:\theolchapter:\theolsection}%
    \ifdefstring{\OLStandaloneSection}{pt:nat:rp}{\fontsize{13.5pt}{17pt}\selectfont}{}%
  }%
''' + layout[old.end():]

# Suppress revision text in the running footer. Exact revisions belong to the
# technical provenance page, not title/subject or the reader's main prose.
start = base.index(r'\makeatletter' + '\n' + r'\renewcommand*{\@gitFootRev}')
end = base.index(r'\includeenv{editorial}', start)
base = base[:start] + r'''
\makeatletter
\renewcommand*{\@gitFootRev}{}
\makeatother
\renewcommand*{\ifgitinfo}{}

''' + base[end:]

identity = r'''% Additive standalone edition. Generated by build/make_standalone_driver.py.
% Inherited source files are immutable; see evidence/DRIVER_PROVENANCE.json.
\PassOptionsToClass{14pt,oneside,openany}{memoir}
\newcommand*{\OLCompletePDFTitle}{متن منطق باز}
\newcommand*{\OLCompleteEditionSubtitle}{منطق صوری و فرامنطق}
\newcommand*{\OLCompletePDFSubject}{خوانشگر یکپارچهٔ فارسی معیار؛ منطق صوری، فرامنطق و مبانی منطق ریاضی}
\newcommand*{\OLCompletePDFKeywords}{منطق صوری؛ فرامنطق؛ نظریهٔ مجموعه‌ها؛ نظریهٔ برهان؛ محاسبه‌پذیری؛ تمامیت؛ ناتمامیت}
\newcommand*{\OLReleaseDOIBlock}{%
  {\normalsize شناسهٔ پایدار مجموعه:
   \foreignlanguage{english}{\babelsublr{10.5281/zenodo.21921852}}\par}%
}
'''

body = r'''
\begin{document}
\begin{titlingpage}
\begin{center}
\vspace*{2.2cm}
{\HUGE\bfseries\sffamily متن منطق باز\par}
\vspace{0.9cm}
{\huge منطق صوری و فرامنطق\par}
\vspace{1.3cm}
{\Large پروژهٔ منطق باز\par}
\vspace{1cm}
{\large خوانشگر یکپارچهٔ فارسی معیار\par}
\vspace{0.5cm}
{\normalsize همراه با نظریهٔ برهان و متن‌های تکمیلی\par}
\vspace{1cm}
\OLReleaseDOIBlock
\end{center}
\vfill
\noindent
در این خوانشگر، مطالب نسخهٔ فارسیِ منبع تثبیت‌شده در یک سند گرد آمده‌اند.
بخش‌های تکمیلی و صورت‌های بدیلِ سازمان‌دهی منبع نیز در همین سند جای دارند؛
ازاین‌رو برای پی‌گیری ارجاع‌های درون کتاب به فایل دیگری نیاز نیست.
  \medskip
  \noindent
  این ترجمهٔ تغییریافته با مجوز
  \href{https://creativecommons.org/licenses/by/4.0/}%
    {\foreignlanguage{english}{CC BY 4.0}}
عرضه می‌شود. اثر اصلی از پروژهٔ منطق باز است؛ این انتشار به معنای تأیید
آن پروژه نیست. این ویرایش اصلاحِ گردآوری و صفحه‌آراییِ ترجمهٔ موجود است،
نه ادعای بازبینی انسانیِ تازهٔ سراسر ترجمه.
\end{titlingpage}

\pagestyle{giheadings}
\input{standalone/body.tex}

\clearpage
\chapter*{دربارهٔ این ویرایش}
\markboth{دربارهٔ این ویرایش}{دربارهٔ این ویرایش}
\addcontentsline{toc}{chapter}{دربارهٔ این ویرایش}
این سند یک مجموعهٔ جامع از متن‌های منطق باز است، نه گزینش مطالب برای یک
درس معین. یادداشت‌های ویراستاریِ منبع حفظ شده‌اند و از وضعیت پیش‌نویسِ
برخی مطالب خبر می‌دهند. نظم تازه، صورت‌های بدیل و قطعه‌های مستقل را از
مسیر اصلی متمایز می‌کند و ارجاع‌های آنها را در همین سند نگه می‌دارد.
\par\medskip
همهٔ \babelsublr{722} پروندهٔ موروثیِ ترجمه بدون تغییرِ بایت نگه داشته
شده‌اند. فهرست ماشینیِ همراهِ منبع، جایگاه، شیوهٔ درج و شناسهٔ هر پرونده
را ثبت می‌کند. صورت‌های بدیلِ راه‌انداز به معنای فصل‌های ریاضیِ تازه نیستند.
یک لایهٔ افزوده، سی‌ونه قاعدهٔ تصحیحِ دقیق و وابسته به متن منبع را تنها
پس از تطابق با متن تثبیت‌شده اعمال می‌کند. یکی از این قواعد در دو جای
خوانشگر به کار می‌رود؛ ازاین‌رو گزارش اجرایی چهل رخداد را ثبت می‌کند.
پانزده قاعده یافته‌های ممیزیِ تابع‌ها و اندازهٔ مجموعه‌ها را اصلاح می‌کنند؛
هفت قاعده نشانهٔ جاافتادهٔ تأکید را بازمی‌گردانند؛ و هفده قاعده به
صفحه‌آراییِ موضعی و یک ویرگولِ تکراری می‌پردازند. در مجموع، این قواعد
سی‌ونه یافته را در بیست‌ونه واحد منبع پوشش می‌دهند.
شانزده عنوانِ یادداشتِ موضعی در کنار واحدهای مربوط، شناسه و دامنهٔ
تصحیح‌ها را آشکار می‌کنند. چهار یادداشتِ پیشین نیز یگانگی در اصلِ گسترش،
جهتِ استلزام در بحثِ مدل‌های نااستاندارد، روشن‌سازیِ دامنهٔ سور و
اعتبارسنجیِ خروجیِ ماشینِ تورینگِ همگانی را ثبت می‌کنند. یادداشتِ سور
ادعای اثباتِ خطای معنایی در صورتِ چاپیِ منبع ندارد؛ حفظِ پروندهٔ اصلی نیز
به معنای تأییدِ خطاهای مشخص‌شده نیست.
\par\medskip
حروف فارسی با قلم شِهرزاد و حروف لاتین با قلم‌های
\foreignlanguage{english}{TeX Gyre Pagella / Heros} چیده شده‌اند.
فرمول‌ها در جهت چپ به راست و نثر فارسی در جهت راست به چپ باقی می‌مانند.
\par\medskip
\noindent منشأ فنیِ متن انگلیسی:
\begin{flushleft}\foreignlanguage{english}{\small\ttfamily
9620cc73f9c8e0ad003c514a5d3748f29611c4c0}\end{flushleft}
\noindent منشأ فنیِ ترجمهٔ فارسی:
\begin{flushleft}\foreignlanguage{english}{\small\ttfamily
95fed67628b4e9113ca7890441082b470e0a1b29}\end{flushleft}
\noindent مخزنِ منبع و پرونده‌های بازتولید:
\href{https://github.com/KokunoYumeto/OpenLogic-fa-ir}{\babelsublr{OpenLogic-fa-ir}}

\photocredits
\nocite{Frege1953,Peter1967}
\bibliographystyle{\olpath/bib/natbib-oup}
% Bibliographic titles and imprints are Latin-script data, not RTL prose.
% Keep only the chapter heading/marks in Persian, inside the LTR list.
\begingroup
\begin{otherlanguage}{english}
\renewcommand{\bibsection}{%
  \begin{otherlanguage}{persian}%
  \chapter*{کتاب‌نامه}%
  \addcontentsline{toc}{chapter}{کتاب‌نامه}%
  \markboth{کتاب‌نامه}{کتاب‌نامه}%
  \end{otherlanguage}%
}
\bibliography{standalone-bibliography}
\end{otherlanguage}
\endgroup
\end{document}
'''
target = LOCALE / 'open-logic-standalone-fa-IR.tex'
data = (identity + layout + base + body).encode('utf-8')
receipt = {
    'schema': 'farsi-standalone-driver-provenance-v3',
    'generator': {
        'path': Path(__file__).resolve().relative_to(ROOT).as_posix(),
        'bytes': Path(__file__).stat().st_size,
        'sha256': sha(Path(__file__).read_bytes()),
    },
    'source_preambles': INPUTS,
    'output': target.relative_to(ROOT).as_posix(),
    'sha256': sha(data),
    'bytes': len(data),
    'physical_replacement_events': CURRENT_EXACT_RULE_COUNT,
    'expected_runtime_events': CURRENT_RUNTIME_EVENT_COUNT,
    'semantic_findings': CURRENT_EXACT_RULE_COUNT,
    'corrected_source_units': len(CURRENT_CORRECTED_UNITS),
    'frozen_source_files_changed': 0,
    'source_correction_overlay': {
        'file': 'source/locale/fa-IR/standalone/source-corrections.tex',
        'sha256': CORRECTION_INPUTS['source/locale/fa-IR/standalone/source-corrections.tex'],
        'adjacent_notes_file': 'source/locale/fa-IR/standalone-errata.tex',
        'adjacent_notes_sha256': CORRECTION_INPUTS['source/locale/fa-IR/standalone-errata.tex'],
        'audit_ids': list(AUDIT_AUTHORITIES),
        'audit_authorities': AUDIT_AUTHORITIES,
        'semantic_findings': CURRENT_SEMANTIC_FINDINGS,
        'units': CURRENT_CORRECTED_UNITS,
        'physical_rules': CURRENT_PHYSICAL_RULES,
        'exact_rule_count': CURRENT_EXACT_RULE_COUNT,
        'expected_runtime_events': CURRENT_RUNTIME_EVENT_COUNT,
        'derived_document_text_substitutions': CURRENT_DOCUMENT_TEXT_SUBSTITUTIONS,
        'source_match_policy': 'whitespace-normalized source-environment body; exact source-file and overlay-argument bytes pinned separately',
        'semantic_finding_count': CURRENT_EXACT_RULE_COUNT,
        'corrected_source_unit_count': len(CURRENT_CORRECTED_UNITS),
        'combined_fixture': {
            'path': 'evidence/SOURCE_CORRECTIONS_PROBE_FIXTURE.json',
            'sha256': CORRECTION_INPUTS['evidence/SOURCE_CORRECTIONS_PROBE_FIXTURE.json'],
            'driver_preamble': correction_fixture['driver_preamble'],
            'historical_evidence_continuity_status': correction_fixture['historical_evidence_continuity']['status'],
            'accepted_probe_tex_sha256': correction_fixture['historical_evidence_continuity']['accepted_probe_tex']['sha256'],
        },
        'native_probe_qa': {
            'path': 'evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_QA.json',
            'sha256': CORRECTION_INPUTS['evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_QA.json'],
            'status': correction_native_qa['status'],
        },
        'complete_visual_probe_qa': {
            'path': 'evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_VISUAL_QA.json',
            'sha256': CORRECTION_INPUTS['evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_VISUAL_QA.json'],
            'status': correction_visual_qa['status'],
            'pages_inspected': correction_visual_qa['source_pdf']['pages'],
        },
        'olsiz_local_binding': {
            'path': 'evidence/SHARED_SOURCE_AUDIT_OLSIZ_20260904.json',
            'sha256': CORRECTION_INPUTS['evidence/SHARED_SOURCE_AUDIT_OLSIZ_20260904.json'],
        },
        'historical_15_rule_native_trace_and_complete_visual_probe_qa_passed': True,
        'current_full_reader_runtime_trace_pending': True,
        'full_reader_qa_passed': False,
    },
    'bibliography': {
        'derived_file': 'source/locale/fa-IR/standalone-bibliography.bib',
        'provenance': 'evidence/STANDALONE_BIBLIOGRAPHY_PROVENANCE.json',
        'original_unchanged': True,
        'rendering': 'LTR otherlanguage English body; explicit Persian chapter heading and marks; requires native visual QA',
    },
    'numeral_policy': {
        'persian_text_digits': 'Babel LuaTeX mapdigits; U+06F0--U+06F9',
        'math_direction': 'LTR',
        'math_digits': 'unchanged by mapdigits',
        'counter_aux_anchor_tokens': 'ASCII numeric expansion retained',
        'technical_identifiers': 'explicit English language spans retain ASCII',
        'research': 'evidence/FARSI_MATHEMATICAL_NOTATION_RESEARCH.md',
        'native_probe_required': True,
    },
    'adjacent_notes': {'rendered_note_headings': 16,
                        'audited_body_correction_units': HISTORICAL_CORRECTED_UNITS,
                        'other_correction_note_units': ['OLP-0005', 'OLP-0194', 'OLP-0267'],
                        'notation_clarification': ['OLP-0643'],
                        'scope_evidence': 'evidence/OLP0643_SCOPE_CLARIFICATION.json',
                        'source_audits': AUDIT_AUTHORITIES},
    'font_scope_migration': {
        '16.5/proof': 'fol:syn:ass', '23.7/proof': 'fol:com:ide',
        '43.2/proof': 'lam:cr:pb', '3.2/defn (former supplement)': 'pt:nat:rp',
    },
    'build_status': 'not-compiled',
}
receipt_path = ROOT / 'evidence/DRIVER_PROVENANCE.json'
receipt_data = (json.dumps(receipt, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def atomic_write(path: Path, content: bytes) -> None:
    """Replace a generated input atomically so a reader never sees half UTF-8."""
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent, prefix=f'.{path.name}.', suffix='.tmp'
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, 'wb') as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify deterministic generated bytes without writing')
    args = parser.parse_args()
    if args.check:
        if not target.is_file() or target.read_bytes() != data:
            raise SystemExit('Standalone driver does not match generator')
        if not receipt_path.is_file() or receipt_path.read_bytes() != receipt_data:
            raise SystemExit('Driver provenance does not match generator')
    else:
        atomic_write(target, data)
        atomic_write(receipt_path, receipt_data)
    print(json.dumps(receipt, ensure_ascii=False))


if __name__ == '__main__':
    main()
