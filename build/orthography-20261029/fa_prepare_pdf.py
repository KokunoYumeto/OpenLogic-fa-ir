"""Prepare a separate PDF build tree for the Persian orthography fix.

Copies source/ and 00_control/ from the extracted bundle into WORK/pdf, applies fa_fix.fix() to the single-file
direct source and writes it as the standalone driver (as the bundle README describes for the embedded-source
build), and applies the same fix to every other .tex/.sty/.bib file in the copied locale tree.
usage: python -I fa_prepare_pdf.py BUNDLE WORK"""
import json
import pathlib
import shutil
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fa_fix import fix  # noqa: E402

bundle, work = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
pdf = work / "pdf"
if pdf.exists():
    sys.exit("pdf tree exists already: " + str(pdf))
shutil.copytree(bundle / "source", pdf / "source")
shutil.copytree(bundle / "00_control", pdf / "00_control")

totals = {}
direct = (bundle / "direct" / "02-matn-e-manteq-e-baz-fa-ir.tex").read_text(encoding="utf-8")
fixed, counts = fix(direct)
driver = pdf / "source" / "locale" / "fa-IR" / "open-logic-standalone-fa-IR.tex"
driver.write_text(fixed, encoding="utf-8", newline="")
totals["direct"] = counts
(work / "01_OPENLOGIC_fa-IR_ORTHOGRAPHY_20261029_PDF_SOURCE_722.tex").write_text(fixed, encoding="utf-8", newline="")

changed = 0
for p in sorted((pdf / "source").rglob("*")):
    if p.suffix not in (".tex", ".sty", ".bib") or p == driver:
        continue
    t = p.read_text(encoding="utf-8")
    f, c = fix(t)
    if f != t:
        p.write_text(f, encoding="utf-8", newline="")
        changed += 1
totals["other_files_changed"] = changed
print(json.dumps(totals, ensure_ascii=False))
