# Orthography revision, 29 October 2026

Two changes requested by a Persian-speaking reader
([OpenLogic-translations issue 1](https://github.com/KokunoYumeto/OpenLogic-translations/issues/1)):

1. The ezafe after a final silent he is written ه‌ی (he, zero-width non-joiner, yeh) instead of هٔ or ۀ.
2. "Enumeration" is شمارش instead of برشماری, with its plural, ezafe and indefinite forms (برشماری‌ای becomes
   شمارشی). The verb برشمردن, the adjective برشمردنی and the noun برشمارنده are unchanged.

`fa_fix.py` makes both changes. `python fa_fix.py dry FILE` lists every noun it would change, with context.

- **PDF.** Extract the complete source ZIP of 15 October
  (`02_OPENLOGIC_fa-IR_SEQUENT_REVIEWED_20261015_COMPLETE_WEB_EPUB_SOURCE_722.zip`) and run
  `python fa_prepare_pdf.py BUNDLE WORK`. It copies the R11 source tree, applies the changes to the single-file source
  and writes that file as the standalone driver. `build_pdf.ps1` (in WORK) then runs LuaLaTeX and BibTeX; the build
  converged after seven LuaLaTeX passes at 1,203 pages.
- **EPUB and HTML.** `python fa_epub.py OLD_EPUB WEB_DIR OUT_DIR` applies the changes to the reader text of the
  15 October EPUB (its XHTML files and OPF metadata) and builds the HTML reader with the web runtime from the same ZIP.
  The `evidence/` records inside the EPUB keep the text they recorded. EPUBCheck 5.3.0 reports no errors or warnings.

Counts: in the EPUB, 10,165 ezafe spellings and 115 uses of the noun in 708 files; in the PDF source, 8,889 and 170.
The PDF is built from the R11 text, so it does not have the corrections of 14 and 15 October that the EPUB and HTML
have.

The changes were made by Claude Opus 5.5 (Anthropic). No human review is claimed.
