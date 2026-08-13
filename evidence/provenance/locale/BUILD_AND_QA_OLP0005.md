# OLP-0005 Iranian-Persian build and QA receipt

- Locale/register: `fa-IR`, scholarly Iranian Persian.
- Unit: `OLP-0005`, `content/sets-functions-relations/sets/basics.tex`.
- Source authority: official Open Logic commit
  `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`.
- Source SHA-256:
  `8BC9151AF0985E6E20C374AA38CDDD1ADD7A8DFFBABCCC94B89F324F62C40F8C`.
- Target SHA-256:
  `129320E9EEA66762B41C28C6970DBAC6A87D84433AEC529A18BDE8AE903F849C`.
- Locale config SHA-256:
  `89E92D847278C31595E0360E9CD7FF8AFDA38DD11AEF81C7243FCA4C266B9C5F`.
- Terminology/adverse ledger SHA-256:
  `57927CE90D40A51B21B4DAD86DBDDC4CD5A94D867CC0FD9C0E92A1940D3E5FD0`.
- Localized section wrapper SHA-256:
  `F7E4623B4AA48A7D1E4451154169B5494A6F033711B8F5C3CFCC1C95068D996E`.
- Unit build-config SHA-256:
  `0CAB1CA27024291944A76A22D4B9B328638A11041552F0E2135BA91D3106766E`.

## Checks completed

- Direct semantic replay: PASS. Set, element/member, membership and empty-set
  definitions; order and multiplicity independence; both directions of
  extensionality; uniqueness; all three examples; set-builder notation;
  perfect number and proper divisor; equality proof method; and the
  at-most-one-empty-set problem are preserved.
- The source mismatch between prose “less than 10” and the displayed
  `0 \leq x \leq 10` is preserved exactly and recorded as adverse evidence.
- Structural replay: PASS for the 91-command sequence, 20 environment events,
  three tagblocks, 14 text tokens and all 52 math skeletons. The base ID is
  unchanged and the upstream-required locale marker is
  `\olfileid[fa-IR]{sfr}{set}{bas}`.
- Unicode/source checks: NFC, Iranian `ی/ک`, balanced braces, Arabic/Persian
  separation, no source-level directional controls apart from ordinary U+200C
  Persian half-spaces, no presentation forms, and no unapproved English prose.
- Independent AI review directly against English: PASS; no correction
  required. `human_review=none`.
- Build: two clean serial LuaLaTeX passes using LuaHBTeX 1.25.7 / MiKTeX 26.5.
  The log has no fatal error, undefined control sequence, missing character,
  overfull box or underfull box.
- The reader wrapper intentionally omits upstream `open-logic-debug.sty`:
  besides adding non-reader margin diagnostics, its margin-note page-number
  lookup is incompatible with this bidi representation.
- PDF: one Letter page, 99,043 bytes, SHA-256
  `D6A1B72BC058E8B8B3A33CF6337E53B0128B4D63A6D4AA32520B18216BB49FD9`.
- PDF `/Lang` is `fa-IR`; title is `اصل گسترش`; author is
  `پروژهٔ منطق باز`; one localized outline entry and zero link annotations.
- Two-pass log SHA-256:
  `C4376540EB1BB3F00C8DC49ACA4F9AEA4267B758CB1978B8C8676D9EFF367F12`.
- Complete-page visual QA at 144 dpi: PASS. No clipping, overlap, tofu,
  shaping failure, formula loss or mixed-direction collision was observed.
  Render witness SHA-256:
  `E360255AF7C66088D7B87D20F66B3F31B78D1CAF85747758E7850A56335657F4`;
  the temporary PNG was deleted after inspection.
- Poppler layout extraction: 4,293 characters, zero U+FFFD and zero Arabic
  Presentation Forms; SHA-256
  `9B830BBCC8EA366BCB89137CA5AE69D2AD9477666A8D874DE2B3D5CC0FB858D9`.

## Honest limits

The PDF is not tagged-PDF or accessibility certified. Poppler drops all 67
source ZWNJs and inserts directional controls (U+202A/U+202B/U+202C:
112/41/153); combining sequences and punctuation may round-trip differently
in other extractors. The editable TeX is authoritative. This is unit 5 of a
722-unit closure, not a complete Persian edition or publication checkpoint.
