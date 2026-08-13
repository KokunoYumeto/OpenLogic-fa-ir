# OLP-0006 Iranian-Persian build and QA receipt

- Locale/register: `fa-IR`, scholarly Iranian Persian.
- Unit: `OLP-0006`, `content/sets-functions-relations/sets/subsets.tex`.
- Source authority: official Open Logic commit
  `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`.
- Source SHA-256:
  `5D982F62C40325CF75DA4517ADD45CA073E23FB9463CFB3ADFB9AAFBB8582E46`.
- Target SHA-256:
  `B8755941AFB97FC801C6FF9F03B54522AE64AC4D321DF207D77C1CE85AC1B4F4`.
- Locale config SHA-256:
  `89E92D847278C31595E0360E9CD7FF8AFDA38DD11AEF81C7243FCA4C266B9C5F`.
- Terminology/adverse ledger SHA-256:
  `2798CCB74460E6F5938F56E58714BB591BD13AE970DFD2FDA66CC7A2C3D249FB`.
- Localized section wrapper SHA-256:
  `629773BE98FED885B39A938477DB91D9B5891E35C3BAC1B16C7873B4601D022A`.
- Unit build-config SHA-256:
  `E0AA6C83B35A4DA9F68E30FED9649C6239456653E62D7076115EECF08A5CB2B1`.

## Checks completed

- Direct semantic replay: PASS. The distinctions among membership, subset and
  proper subset; both inclusion/equality directions; the mutual-inclusion
  proposition; bounded universal and existential quantifiers; power-set
  inclusion; the eight subsets of a three-element set; and both unsolved
  problems are preserved.
- Structural replay: PASS for the exact 137-command sequence, 22 environment
  events, 14 semantic text tokens and all 65 math segments. The source label
  `forallxina` is retained and the localized ID is exactly
  `\olfileid[fa-IR]{sfr}{set}{sub}`.
- Unicode/source checks: NFC, Iranian `ی/ک`, balanced braces, Arabic/Persian
  separation, 36 ordinary source ZWNJs, no other source-level directional
  controls, no Presentation Forms and no unapproved English reader prose.
- Independent AI review directly against English: PASS; no correction
  required. A separate post-build replay passed the wrapper-only counter
  isolation described below. `human_review=none`.
- Build: two clean serial LuaLaTeX passes using LuaHBTeX 1.25.7 / MiKTeX 26.5.
  The final log has no fatal error, undefined control sequence, missing
  character, overfull box or underfull box.
- The Persian reader wrapper isolates each complete stable Latin counter with
  `\babelsublr`; exact visual inspection confirms `set.1` through `set.7` and
  both problem identifiers rather than bidi-reversed `1.set` forms. The
  translated unit and formal identifiers were not altered.
- PDF: one Letter page, 97,145 bytes, SHA-256
  `43F48D1014ADD993170439E43ECF10D83E2C3DEAC3ABFD72F4405FEFC3BC76D6`.
- PDF `/Lang` is `fa-IR`; title is `زیرمجموعه‌ها و مجموعه‌های توانی`;
  author is `پروژهٔ منطق باز`; one localized outline entry and zero link
  annotations.
- Two-pass log SHA-256:
  `C831B596B6E1CCB78CA859D30BF4110269C427CF7BD08628DC54A9A82EE724CE`.
- Complete-page visual QA at 144 dpi: PASS. No clipping, overlap, tofu,
  shaping failure, formula loss or mixed-direction collision was observed.
  Render witness SHA-256:
  `9836AAC16953DB4FA263ECCE047DDEF01DB028B7E901FC513D51015A9E6AEDCC`;
  the temporary PNG was deleted after inspection.
- Poppler layout extraction: 3,590 characters, zero U+FFFD and zero Arabic
  Presentation Forms; SHA-256
  `3EF42D6D32A37A0AECA51D1D25AE10ACD1DB8AC8B5866A33CF60A613CC5F9A5E`.

## Honest limits

The PDF is not tagged-PDF or accessibility certified. Poppler drops all 36
source ZWNJs, inserts directional controls (U+202A/U+202B/U+202C:
104/33/137), and may serialize visually correct Latin counters as `1.set`.
Combining sequences and punctuation can also round-trip differently. The
editable TeX and visual PDF are authoritative for their respective surfaces.
This is unit 6 of a 722-unit closure, not a complete Persian edition or
publication checkpoint.
