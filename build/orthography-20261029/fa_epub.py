"""Apply the two Persian changes (fa_fix.fix) to the reader text of the current EPUB and build the matching HTML reader.

EPUB: every .xhtml file (units, front matter, nav) and the OPF metadata are changed; dcterms:modified becomes
2026-10-29. The evidence/*.json provenance records keep their recorded text. Entry order is kept and the mimetype
entry stays first and stored. HTML reader: the bundle's web runtime with book-data.js = the new EPUB in base64, as
web/build_web.py does (without its fixed-hash check).
usage: python -I fa_epub.py OLD_EPUB WEB_DIR OUT_DIR"""
import base64
import hashlib
import json
import pathlib
import re
import sys
import zipfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fa_fix import fix  # noqa: E402

old, web, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
out.mkdir(parents=True, exist_ok=True)
STEM = "OPENLOGIC_fa-IR_ORTHOGRAPHY_20261029"
new_epub = out / ("03_" + STEM + "_READER_722.epub")
sha = lambda b: hashlib.sha256(b).hexdigest()

totals = {"files_changed": 0, "ezafe_he_hamza": 0, "ezafe_heh_yeh_above": 0, "enumeration_noun": 0,
          "enumeration_indefinite": 0}
with zipfile.ZipFile(old) as zin, zipfile.ZipFile(new_epub, "w") as zout:
    for info in zin.infolist():
        data = zin.read(info.filename)
        name = info.filename
        if name.endswith(".xhtml") or name.endswith(".opf"):
            text = data.decode("utf-8")
            new, counts = fix(text)
            if name.endswith(".opf"):
                new, n = re.subn(r'(<meta property="dcterms:modified">)[^<]+(</meta>)', r"\g<1>2026-10-29T00:00:00Z\g<2>", new)
                assert n == 1, "dcterms:modified not found"
            if new != text:
                totals["files_changed"] += 1
                for k in counts:
                    totals[k] += counts[k]
            data = new.encode("utf-8")
        zi = zipfile.ZipInfo(name, info.date_time)
        zi.external_attr = info.external_attr
        if name == "mimetype":
            zi.compress_type = zipfile.ZIP_STORED
            zout.writestr(zi, data)
        else:
            zi.compress_type = zipfile.ZIP_DEFLATED
            zout.writestr(zi, data, compresslevel=9)

raw = new_epub.read_bytes()
with zipfile.ZipFile(new_epub) as z:
    assert z.testzip() is None
    assert z.namelist()[0] == "mimetype" and z.getinfo("mimetype").compress_type == zipfile.ZIP_STORED
    left = sum(z.read(n).decode("utf-8").count("هٔ") + z.read(n).decode("utf-8").count("برشماری")
               for n in z.namelist() if n.endswith(".xhtml"))
    units = [n for n in z.namelist() if n.startswith("OEBPS/text/unit-") and n.endswith(".xhtml")]
totals["left_in_xhtml"] = left
totals["unit_files"] = len(units)

# HTML reader, same runtime files as web/build_web.py
reader = out / "reader"
files = {n: (web / n).read_bytes() for n in ("index.html", "reader.css", "reader.js", "vendor/jszip.min.js",
                                              "vendor/epub.min.js", "vendor/JSZIP-LICENSE.md",
                                              "vendor/EPUBJS-LICENSE.txt")}
files["book-data.js"] = b'window.OPENLOGIC_BOOK_BASE64="' + base64.b64encode(raw) + b'";\n'
manifest = {
    "schema": "openlogic-fa-chapter-html/1", "language": "fa-IR", "edition_variant": "orthography-20261029",
    "source_units": 722, "reading_occurrences": 774, "epub_sha256": sha(raw),
    "source_description_fa": "تمام متن EPUB بازبینی حساب رشته (۱۵ اکتبر ۲۰۲۶) با دو اصلاح: کسره‌ی اضافه پس از «ه» با «‌ی» نوشته می‌شود و «شمارش» جای «برشماری» را می‌گیرد.",
    "ai_disclosure_fa": "ساخت و آزمون خوانشگر پایه: OpenAI Codex — GPT-6 Astra، تلاش Ultra. اعمال دو اصلاح این نسخه: Claude Opus 5.5 (Anthropic). تأیید انسانی ادعا نمی‌شود.",
    "dependencies": {"epubjs": "0.3.93 / BSD-2-Clause", "jszip": "3.10.1 / MIT"},
    "files": {n: {"bytes": len(b), "sha256": sha(b)} for n, b in sorted(files.items())},
}
files["READING-MANIFEST.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
for n, b in files.items():
    p = reader / n
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(b)
archive = out / ("04_" + STEM + "_HTML_READER_722.zip")
with zipfile.ZipFile(archive, "w") as z:
    for n, b in sorted(files.items()):
        zi = zipfile.ZipInfo(n, (2026, 10, 29, 0, 0, 0))
        zi.compress_type = zipfile.ZIP_DEFLATED
        zi.create_system = 3
        zi.external_attr = 0o100644 << 16
        z.writestr(zi, b, compresslevel=9)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None and all(z.read(n) == b for n, b in files.items())
totals["epub"] = {"bytes": len(raw), "sha256": sha(raw)}
totals["html_zip"] = {"bytes": archive.stat().st_size, "sha256": sha(archive.read_bytes())}
print(json.dumps(totals, ensure_ascii=False, indent=1))
