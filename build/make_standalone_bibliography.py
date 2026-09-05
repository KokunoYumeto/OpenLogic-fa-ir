#!/usr/bin/env python3
"""Derive six evidence-backed BibTeX repairs; never edit the frozen bibliography.

Run with Python 3.10+ from any directory. --check performs no writes. No network,
TeX, subprocess, publication, or repository operations occur in this generator.
The source SHA and exact replacements intentionally fail closed on source drift.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = ROOT / "source/bib/open-logic.bib"
STYLE = ROOT / "source/bib/natbib-oup.bst"
DERIVED = ROOT / "source/locale/fa-IR/standalone-bibliography.bib"
EVIDENCE = ROOT / "evidence/STANDALONE_BIBLIOGRAPHY_PROVENANCE.json"
REPORT = EVIDENCE.with_suffix(".md")
EXPECTED_ORIGINAL_SHA256 = "4b4249139c74de1df579b77b29f6d8edf087450cc05f03f771e3661f5eaeb54f"
EXPECTED_STYLE_SHA256 = "c3cb1272ab13900bb117f9cc3ba4028ef9f40bcb4943ca852c569c7a2c31e733"
OBSERVED_DATE = "2026-09-04"
WARNING_LOG = "tmp/pdfs/standalone/20260904T150754407Z-2e0e00a5b01940298bd4fe2d0c520d6d/primary/primary-bibtex-01.blg"
WARNING_LOG_SHA256 = "ad5b60460d3e1a240cc0f04bc2a3283de0a025b60373bf88e8b88fe63414f9a2"

# Bibliographic cataloguing facts, not copies of the third-party source documents.
# URLs and locators are exact. Full external PDFs/HTML are not republished here.
SOURCES = {
    "berkeley_title": {
        "url": "https://www.maths.tcd.ie/pub/HistMath/People/Berkeley/Analyst/Analyst.pdf#page=7",
        "title": "George Berkeley, The Analyst; edited by David R. Wilkins (2002)",
        "source_kind": "Scholarly edition reproducing the 1734 London title-page imprint",
        "locator": "PDF page 7, reproduced title page; text note at PDF pages 3-4 and 6",
        "verified_facts": "London, J. Tonson, 1734; Addressed is the title-page spelling. Dublin has a different imprint.",
        "inspection": "PDF fetched and title page rendered/visually inspected; this is a typeset reproduction, not a claimed scan of the original leaf.",
        "fetched_pdf_bytes": 217555,
        "fetched_pdf_sha256": "c79159de3dcf3521d4d8698ce31868edf0125d92fe5f2c121ee62aabb0927bc4",
    },
    "hume_set": {
        "url": "https://digital.lb-oldenburg.de/urn/urn:nbn:de:gbv:45:1-1208",
        "title": "Landesbibliothek Oldenburg: A Treatise Of Human Nature, ESTC T4002",
        "source_kind": "Holding library catalogue for its digitized first edition",
        "locator": "Erschienen, Anmerkung, and Baende (volumes) fields",
        "verified_facts": "Whole set dated 1739-1740; John Noon for volumes I-II; volume III expressly excepted to Longman.",
        "inspection": "Library catalogue transcription read through web retrieval; no claim that original title-page images were visually inspected.",
    },
    "hume_three": {
        "url": "https://digital.lb-oldenburg.de/brandes/content/titleinfo/51571",
        "title": "Landesbibliothek Oldenburg: Vol. III (1740), Of Morals",
        "source_kind": "Holding library catalogue with a transcribed title-page imprint",
        "locator": "Teil eines Werkes; Verleger; Erschienen; Anmerkung",
        "verified_facts": "Volume III appeared in London in 1740, printed for Thomas Longman.",
    },
    "frege_catalogue": {
        "url": "https://ci.nii.ac.jp/ncid/BA41275874",
        "title": "CiNii Books: The foundations of arithmetic, 2nd revised edition (1953)",
        "source_kind": "National Institute of Informatics union library catalogue",
        "locator": "Bibliographic Information: statement of responsibility, publisher, year and edition",
        "verified_facts": "Frege is the author; J. L. Austin supplied the English translation; B. Blackwell, 1953, second revised edition.",
    },
    "frege_roles": {
        "url": "https://plato.stanford.edu/entries/frege/catalog.html",
        "title": "Chronological Catalog of Frege's Work",
        "source_kind": "Supplementary scholarly bibliography, used to corroborate an inherited role",
        "locator": "Locations of English Translations of Frege's Writings: Austin, J. L. (1953)",
        "verified_facts": "Austin is identified as both editor and translator. The editor role is already present in the frozen bibliography and is preserved, not invented.",
    },
    "hilbert_publisher": {
        "url": "https://link.springer.com/book/10.1007/978-3-540-69444-1",
        "title": "David Hilbert's Lectures on the Foundations of Arithmetic and Logic 1917-1933",
        "source_kind": "Publisher's book catalogue",
        "locator": "Editors; About this book; Bibliographic Information",
        "verified_facts": "William Ewald and Wilfried Sieg edited the 2013 Springer volume of Hilbert's lecture notes. Hilbert remains the inherited author for source citation compatibility.",
    },
    "mactutor_article": {
        "url": "https://mathshistory.st-andrews.ac.uk/HistTopics/Real_numbers_2/",
        "title": "The real numbers: Stevin to Hilbert",
        "source_kind": "Original MacTutor web article, University of St Andrews",
        "locator": "Article heading; author/update footer; institutional footer",
        "verified_facts": "Written by J. J. O'Connor and E. F. Robertson; last updated October 2005; this is a web article, not a journal publication.",
    },
    "weston_author": {
        "url": "https://sites.google.com/view/taweston/home",
        "title": "Tom Weston, author website",
        "source_kind": "Author's own publication list",
        "locator": "Expository papers: The Banach-Tarski paradox",
        "verified_facts": "The author classifies this work as an expository paper and links the publicly accessible PDF below.",
    },
    "weston_pdf": {
        "url": "https://drive.google.com/file/d/1bxbRw0tPe1caUAzLB0ytcrUXegwESU8n/view",
        "download_url": "https://drive.google.com/uc?export=download&id=1bxbRw0tPe1caUAzLB0ytcrUXegwESU8n",
        "title": "The Banach-Tarski Paradox, Tom Weston",
        "source_kind": "PDF linked directly by the author",
        "locator": "First-page title/author; PDF information dictionary CreationDate",
        "verified_facts": "16-page expository paper by Tom Weston. Embedded creation date D:20030904153700 corroborates the inherited 2003 year, but is not an independent publication-date certificate.",
        "inspection": "Downloaded anonymously; first-page text and metadata inspected. The legacy UMass URL timed out; the author-maintained link is used instead.",
        "fetched_pdf_bytes": 210911,
        "fetched_pdf_sha256": "52c5bde3a52d4ad4815df8046cfcf2f0e1c6f5fd9f59b96a8495194d3e66f107",
    },
}

DECISIONS = {
    "Berkeley1734": {
        "warning": "missing publisher",
        "decision": "Add the London first-edition publisher J. Tonson, convert unsupported place to address, and correct Adressed to Addressed from the title page.",
        "source_ids": ["berkeley_title"],
    },
    "Hume1740": {
        "warning": "missing publisher",
        "decision": "Represent the generic whole-work entry as the three-volume first edition, 1739--1740. Qualify John Noon to volumes 1--2 and Thomas Longman to volume 3; retain the citekey Hume1740.",
        "source_ids": ["hume_set", "hume_three"],
        "scope_note": "The source citation in set-theory/cardinals/hp.tex refers to Book I, Part III, section 1. Keeping the whole-work title/set record also covers that 1739 volume; it does not misassign Book I to Longman's 1740 volume III.",
    },
    "Frege1953": {
        "warning": "cannot use both author and editor fields",
        "decision": "Keep Frege as author. Render Austin's editor and translator roles in the supported note field. Normalize the publisher to the catalogue imprint Basil Blackwell.",
        "source_ids": ["frege_catalogue", "frege_roles"],
        "rendered_role_note": "Edited and translated by J. L. Austin",
    },
    "EwaldSieg2013": {
        "warning": "cannot use both author and editor fields",
        "decision": "Keep Hilbert as inherited author. Move the genuine Ewald/Sieg editor credit to a supported note rather than discard it or change citation authorship.",
        "source_ids": ["hilbert_publisher"],
        "rendered_role_note": "Edited by William Ewald and Wilfried Sieg",
        "inherited_editor_name_forms": ["Ewald, William Bragg", "Sieg, Wilfried"],
    },
    "OConnorRobertson:RN": {
        "warning": "empty journal",
        "decision": "Use misc with howpublished identifying the MacTutor website and a note recording its October 2005 update. Do not fabricate a journal.",
        "source_ids": ["mactutor_article"],
    },
    "Weston2003": {
        "warning": "empty journal",
        "decision": "Use misc with howpublished identifying an author-hosted expository paper. Preserve the inherited 2003 date, supported but not independently certified by PDF creation metadata. Use the working PDF link from the author's site.",
        "source_ids": ["weston_author", "weston_pdf"],
    },
}

ENTRY_START = re.compile(rb"(?mi)^@[a-z]+\s*\{\s*([^\s,{}]+)\s*,")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def entries(data: bytes) -> list[tuple[str, int, int]]:
    """Locate entries in this one SHA-pinned file, without reserializing BibTeX.

    The format is verified by exact source identity. Partitioning at existing
    entry starts also retains comments, blank lines, and mixed line endings.
    This deliberately is not a general-purpose BibTeX parser.
    """
    starts = list(ENTRY_START.finditer(data))
    result = [(m[1].decode("ascii"), m.start(), starts[i + 1].start() if i + 1 < len(starts) else len(data))
              for i, m in enumerate(starts)]
    keys = [key for key, _, _ in result]
    if len(keys) != 141 or len(set(keys)) != len(keys):
        raise ValueError("Expected exactly 141 unique citekeys in the pinned bibliography")
    return result


def once(block: bytes, old: bytes, new: bytes) -> bytes:
    if block.count(old) != 1:
        raise ValueError(f"Expected exactly one byte patch target: {old!r}")
    return block.replace(old, new, 1)


def repair(key: str, block: bytes) -> bytes:
    nl = b"\r\n" if b"\r\n" in block else b"\n"
    if key == "Berkeley1734":
        block = once(block, b"Adressed", b"Addressed")
        return once(block, b"place = {London}", b"address = {London}," + nl + b"  publisher = {J. Tonson}")
    if key == "Hume1740":
        block = once(block, b"year   = {1740}", b"year   = {1739--1740}")
        return once(block, b"address = {London}", b"address = {London}," + nl +
                    b"  publisher = {John Noon (vols.~1--2); Thomas Longman (vol.~3)}," + nl +
                    b"  note = {First edition in three volumes: volumes 1--2 (1739), volume 3 (1740)}")
    if key == "Frege1953":
        block = once(block, b"editor = {J. L. Austin}", b"note = {Edited and translated by J. L. Austin}")
        return once(block, b"publisher = {Basil Blackwell \\& Mott}", b"publisher = {Basil Blackwell}")
    if key == "EwaldSieg2013":
        return once(block, b"Editor = {Ewald, William Bragg and Sieg, Wilfried}",
                    b"Note = {Edited by William Ewald and Wilfried Sieg}")
    if key == "OConnorRobertson:RN":
        block = once(block, b"@Article{", b"@misc{")
        return once(block, b"year   = {2005},", b"year   = {2005}," + nl +
                    b"  howpublished = {{MacTutor History of Mathematics Archive}, University of St Andrews}," + nl +
                    b"  note = {Web article, last updated October 2005},")
    if key == "Weston2003":
        block = once(block, b"@Article{", b"@misc{")
        block = once(block, b"year   = {2003},", b"year   = {2003}," + nl +
                     b"  howpublished = {Expository paper, author's website},")
        return once(block, b"http://people.math.umass.edu/~weston/oldpapers/banach.pdf",
                    SOURCES["weston_pdf"]["url"].encode("ascii"))
    return block


def make_outputs() -> dict[Path, bytes]:
    original = ORIGINAL.read_bytes()
    if sha(original) != EXPECTED_ORIGINAL_SHA256:
        raise ValueError("Immutable original bibliography SHA-256 mismatch; no output written")
    if sha(STYLE.read_bytes()) != EXPECTED_STYLE_SHA256:
        raise ValueError("Inherited bibliography style identity changed; re-audit field support")
    source_entries = entries(original)
    chunks = [original[:source_entries[0][1]]]
    records = []
    for key, start, end in source_entries:
        before = original[start:end]
        after = repair(key, before)
        chunks.append(after)
        record = {"citekey": key, "before_sha256": sha(before), "after_sha256": sha(after),
                  "byte_identical": before == after}
        if key in DECISIONS:
            record.update(DECISIONS[key])
            record.update({"before_entry": before.decode("utf-8"), "after_entry": after.decode("utf-8")})
            if before == after:
                raise ValueError(f"Intended repair made no change: {key}")
        elif before != after:
            raise ValueError(f"Untouched entry changed: {key}")
        records.append(record)
    derived = b"".join(chunks)
    derived_entries = entries(derived)
    if [x[0] for x in source_entries] != [x[0] for x in derived_entries]:
        raise ValueError("Citation keys or their order changed")
    unchanged = [r for r in records if r["byte_identical"]]
    changed = [r for r in records if not r["byte_identical"]]
    if len(unchanged) != 135 or {r["citekey"] for r in changed} != set(DECISIONS):
        raise ValueError("The repair set is not exactly the six authorized entries")
    for key, start, end in derived_entries:
        if key not in DECISIONS:
            continue
        block = derived[start:end]
        has_author = re.search(rb"(?mi)^\s*author\s*=", block) is not None
        has_editor = re.search(rb"(?mi)^\s*editor\s*=", block) is not None
        if has_author and has_editor:
            raise ValueError(f"Unsupported author/editor combination remains in {key}")
        if key in {"Berkeley1734", "Hume1740"} and not re.search(rb"(?mi)^\s*publisher\s*=\s*\{[^}]+\}", block):
            raise ValueError(f"Missing publisher remains in {key}")
        if key in {"OConnorRobertson:RN", "Weston2003"} and (
            not block.startswith(b"@misc{") or re.search(rb"(?mi)^\s*journal\s*=", block)):
            raise ValueError(f"Web/expository material misclassified in {key}")

    provenance = {
        "schema": "standalone-bibliography-derived-metadata-v1",
        "sources_observed_date": OBSERVED_DATE,
        "original": {"path": "source/bib/open-logic.bib", "bytes": len(original), "sha256": sha(original), "modified": False},
        "style": {"path": "source/bib/natbib-oup.bst", "sha256": EXPECTED_STYLE_SHA256,
                  "compatibility": "ENTRY at lines 54-78 supports note and howpublished, not translator. book at lines 931-982 warns on author+editor but renders note. misc at lines 1136-1149 renders howpublished/note/url without requiring journal."},
        "observed_warning_log": {"path": WARNING_LOG, "sha256": WARNING_LOG_SHA256, "warnings": 6},
        "generator": {"path": "build/make_standalone_bibliography.py", "sha256": sha(Path(__file__).read_bytes())},
        "derived": {"path": "source/locale/fa-IR/standalone-bibliography.bib", "bytes": len(derived), "sha256": sha(derived)},
        "validation": {"all_citekeys_preserved": True, "citekey_order_preserved": True,
                       "entry_count": 141, "changed_entries": 6, "untouched_entries_byte_identical": 135,
                       "source_prefix_and_interentry_bytes_preserved": True,
                       "static_six_warning_conditions_resolved": True,
                       "bibtex_or_tex_executed": False,
                       "runtime_warning_clearance": "Must be checked by the root's guarded next build; not claimed by static validation."},
        "intended_driver_include": r"\bibliography{standalone-bibliography}",
        "sources": SOURCES,
        "entry_identity_audit": records,
        "uncertainty": ["Weston2003: embedded PDF creation date corroborates 2003 but does not establish an independently certified publication date.",
                        "Hume1740: the citekey is retained verbatim while the whole-work publication span is corrected to 1739--1740.",
                        "Frege1953: Austin's inherited editor role is retained in rendered prose and corroborated by the scholarly catalogue; the primary union catalogue explicitly verifies the translator role."],
    }
    rows = []
    for key, decision in DECISIONS.items():
        citations = ", ".join(f"[{SOURCES[s]['title']}]({SOURCES[s]['url']})" for s in decision["source_ids"])
        rows.append(f"- `{key}`: {decision['decision']} Sources: {citations}.")
    report = "\n".join([
        "# Standalone bibliography: six derived metadata repairs", "",
        f"Primary metadata checked on {OBSERVED_DATE}. No TeX, BibTeX or publication was run by this generator.", "",
        f"Frozen original: `source/bib/open-logic.bib`, SHA-256 `{sha(original)}`. It remains unchanged.",
        f"Derived file: `source/locale/fa-IR/standalone-bibliography.bib`, {len(derived)} bytes, SHA-256 `{sha(derived)}`.", "",
        "All 141 citekeys and their order are preserved. Only the six entries below change; the other 135 entries, source prefix, whitespace and mixed line endings are copied byte-for-byte. Exact before/after entries and all entry hashes are in the JSON receipt.", "",
        "## Decisions", "", *rows, "",
        "## Rendering contract", "",
        "The immutable natbib-oup style has no translator field. Its note field preserves editor/translator credits visibly while retaining inherited citation authors. Its misc type accurately represents the two non-journal works through howpublished, URL and note. No journal or publisher was invented to silence a warning.", "",
        r"Root-owned driver integration: `\bibliography{standalone-bibliography}`.", "",
        "## Boundaries and uncertainty", "",
        "Static checks establish byte preservation, exact citekey conservation, and removal of the six known metadata conditions. A fresh guarded build must establish actual BibTeX warning clearance and rendered bibliography quality.", "",
        "Hume's unchanged citekey ends in 1740, but the corrected whole-set year is 1739--1740. The qualified publisher text is not a claim of joint publication. Weston's 2003 date is retained from the source and corroborated by the author-linked PDF's creation metadata, not treated as an independently certified publication date. Austin's editor credit is inherited and additionally corroborated by the scholarly Frege catalogue; the primary union catalogue directly establishes the translation credit.", "",
        "## Primary artifact locators", "",
        "- Berkeley: reproduced London title page, PDF page 7; title-page image inspected. SHA-256 and the distinction from a scan are recorded in JSON.",
        "- Hume: Oldenburg's catalogue fields transcribe the imprints and distinguish the three volumes. No visual title-page-scan inspection is claimed.",
        "- Weston: author's Expository papers list links a 16-page PDF; its title/author and PDF creation metadata were inspected and its bytes hashed.", "",
        "Regenerate with `python build/make_standalone_bibliography.py`; verify without writes with `python build/make_standalone_bibliography.py --check`.", "",
    ])
    return {DERIVED: derived, EVIDENCE: (json.dumps(provenance, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
            REPORT: report.encode("utf-8")}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify generated bytes without writing")
    args = parser.parse_args()
    outputs = make_outputs()
    for path, data in outputs.items():
        if args.check:
            if not path.is_file() or path.read_bytes() != data:
                raise ValueError(f"Generated artifact missing or stale: {path.relative_to(ROOT)}")
        elif not path.is_file() or path.read_bytes() != data:
            path.parent.mkdir(parents=True, exist_ok=True)
            temporary = path.with_name(path.name + ".next")
            temporary.write_bytes(data)
            temporary.replace(path)
    if sha(ORIGINAL.read_bytes()) != EXPECTED_ORIGINAL_SHA256:
        raise ValueError("Immutable bibliography changed during generation")
    print(json.dumps({"status": "PASS_CHECK" if args.check else "PASS_GENERATED", "entries": 141,
                      "changed": 6, "untouched_byte_identical": 135,
                      "original_sha256": EXPECTED_ORIGINAL_SHA256, "derived_sha256": sha(outputs[DERIVED]),
                      "tex_executed": False}, indent=2))


if __name__ == "__main__":
    main()
