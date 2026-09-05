# Additive standalone body API

Owner entry point: `\input{standalone/body.tex}` exactly once after the title/front matter. The entry point must already load the OpenLogic/LuaLaTeX/Babel Persian preamble, hyperref/cleveref, and deferred exercise machinery. The body owns the source about page, TOC, subject graph and internal variant appendix. It does not own the document class, root preamble, photo credits, bibliography, provenance section, or `\end{document}`.

## Files and contracts

- `runtime.tex` defines the exact-signature import dispatcher, source/context occurrence guard, label namespaces, reference aliases, trace stream and fail-closed coverage checks.
- `generated-ledger.tex` is mechanically generated from the hash-pinned 722-row closure manifest and unmodified Persian files by `build/make_standalone_ledger.py`.
- `context.tex` supplies narrowly scoped setup for retained material, disclosures distinguishing inherited editorial text from this reader, and the 16 inherited historical reference aliases. Their target labels are statically verified against literal source label definitions; final AUX convergence is still required.
- `typography.tex` promotes six exact inline formulas to displays in OLP-0668, OLP-0290, OLP-0291 and OLP-0369. The original baseline subfiles remain the actual inputs; comparison keys alone are whitespace-normalized, and the captured mathematical tokens are emitted unchanged. Following sentence punctuation is retained in the display where necessary. No font size is changed by this layer.
- `variants.tex` contains four alternative wrappers as documentary variants. Their 36 import edges become internal links to canonical content; no shared body is replayed. Variant part/chapter headings become sections within the variant appendix. The alternate source text remains unchanged.

`body.tex` loads optional owner-controlled `standalone-errata.tex` after runtime/ledger/context registration and before `\OLSAStart`. The owner can use `\OLSADeclareAfter{OLP-0267}{...}`: it executes after that unit's actual content, inside the loader group. Registering an existing key replaces its previous after hook; use only unoccupied keys or deliberately compose the existing callback. No default after hook occupies OLP-0267.

Typography registration loads after `context.tex` and before the errata file. Its protected paired-dollar scanner is activated only while reading one of the four stable target units. The non-target branch explicitly restores ordinary math-shift catcodes, including nested source imports. All unregistered formulas use the original catcode-3 math shifts. Each exact display rule must execute once; missing or repeated rules raise a package error. The `.oltypography` sidecar has header `source_id|rule|occurrence` and six data rows. The log also records six `OL-STANDALONE-TYPOGRAPHY|source-id|rule|1` events and final `OL-STANDALONE-TYPOGRAPHY-COVERAGE|6|6`. These are expected runtime results until a new owner build verifies them.

The documentary appendix uses a dedicated `OLSAVariantSection` counter for A.1 through A.4 and the distinct `olsa-variant` hyperlink prefix. It explicitly sets its running marks and flushes its pages before restoring local numbering definitions; it does not increment/reset the canonical chapter or section counters.

Exposed source context during loads: `\OLStandaloneCurrentID`, `\OLStandaloneCurrentPath`, and `\OLStandaloneCurrentNamespace`. Label namespaces do not change `\theolpart`, `\theolchapter`, or `\theolsection`, preserving semantic layout hooks. Deferred exercises save a separate reference context with `\OLSASetReferenceContext`.

## Coverage is source plus logical context

There are exactly 722 unique source paths and 774 expected body occurrences. Fifty-two files are deliberately specialized twice by the baseline: once with the FOL tag false for propositional logic and again with it true for first-order logic. Suppressing those by filename alone would remove the FOL chapters. The guard therefore identifies an occurrence by `OLP-id/FOL` or `OLP-id/PL`; a repeated request in the same context is suppressed. The generated order model follows literal imports, nested subfiles, the existing default tag values, and FOL tag changes. A changed runtime tag branch fails the exact-order gate rather than silently lowering coverage.

The 59 proof-theory units are integrated after first-order logic; proof-search is added after normalization, omitted rule tables appear with the sequent-calculus chapter, and the isolated cut-elimination fragment is explicitly contextualized after largest-cut elimination. Other retained units are inserted at named subject anchors. The older alternative axiom-provability treatment remains adjacent to the canonical treatment with its own label namespace and remapped self-references. Four alternative drivers occupy the internal documentary appendix.

## Static and later runtime checks

Run from any directory:

```powershell
python C:\interlanguage-production\openlogic-farsi-standalone\repo\build\make_standalone_ledger.py --check --self-test
```

This replays every baseline source hash, resolves every declared source import, confirms all 722 placements, unique namespace targets, source-defined alias targets, deterministic generated bytes, and in-memory positive/negative trace tests. It launches no TeX.

After the owner performs a guarded TeX build, validate its actual source-start trace:

```powershell
python C:\interlanguage-production\openlogic-farsi-standalone\repo\build\make_standalone_ledger.py --trace <output-directory>\<jobname>.olunits
```

The trace header is `id|source_path|namespace|FOL_context|occurrence`. Each line is a real body-entry event; the occurrence field is one for that source/context key. The log also contains `OL-STANDALONE-ENTER`, `EXIT`, `SKIP`, `SUPPRESSED-VARIANT-EDGE`, and final `COVERAGE` markers. Compare FLS coverage and source hashes separately: repetitive FLS input records are not body-occurrence counts.

The additive typography check rehashes all 828 staged files, pins all six formula payloads, checks reversible punctuation/prose transport, and runs mutation/duplicate/source-scope negative tests without TeX:

```powershell
python C:\interlanguage-production\openlogic-farsi-standalone\repo\source\locale\fa-IR\standalone\tests\check_typography.py
```

Append `--trace-file <new-output-directory>\<jobname>.oltypography` after an owner-managed build to require all six actual display events. Optionally add `--trace-log <new-output-directory>\<jobname>.log` to check the log markers as well. Positive trace replay plus missing-row, duplicate-row, wrong-count and wrong-source negative tests run by default. `--write-evidence` regenerates the scoped `evidence/STANDALONE_TYPOGRAPHY_QA.json` receipt. These static/model checks are not a substitute for TeX expansion and full-page visual verification.

## Known validation still required

No TeX engine was invoked by the body implementer. Static checks do not prove macro expansion, full tag-sensitive formula correctness, cross-reference convergence, page layout, float placement, Unicode/RTL rendering, PDF links, or byte reproducibility. The owner must run those deterministic gates through the machine-wide TeX mutex/full-tree runner. The generated ledger records provisional placement choices, not invented Persian scholarly consultation or a finished-reader claim. All 722 baseline files remain untouched.
