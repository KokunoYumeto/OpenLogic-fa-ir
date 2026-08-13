# OLP-0007 Iranian-Persian build and QA receipt

- Locale/register: `fa-IR`, scholarly Iranian Persian.
- Unit: `OLP-0007`, `content/sets-functions-relations/sets/important-sets.tex`.
- Source authority: official Open Logic commit
  `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`.
- Source SHA-256:
  `B1B998CAD3FA5AEF48670F755245F86EFE00B239D332A50E764147602405FB32`.
- Target SHA-256:
  `CDC437750FE229D26DB7E8FD8651350549906375B0AF744B4058AF1B4EAF9F84`.
- Locale config / terminology ledger SHA-256:
  `89E92D847278C31595E0360E9CD7FF8AFDA38DD11AEF81C7243FCA4C266B9C5F` /
  `5085DADC36BE7AC417DCDE453A56DF19C7420FFC174B81A5B2F7D72E7537013E`.
- Section wrapper / unit build-config SHA-256:
  `629773BE98FED885B39A938477DB91D9B5891E35C3BAC1B16C7873B4601D022A` /
  `C6C6E2125B40B4B6E5FD9479BA75F7B9353F6C4D1C7D3AA43AF7B6FE91092218`.

## Checks completed

- Direct semantic replay: PASS after removing one non-emptiness implication
  absent from the English source. The four number systems; inclusion directions
  and strictness witnesses; conditional real-line reference; positive integers
  and binary digits; finite strings, empty string, enumeration and length; and
  one-way infinite sequences are preserved.
- Structural replay: PASS for 95 commands, 14 environment events, four text
  tokens and all 26 math segments, including both multiline displays and five
  localized math-internal text fields. Locale ID, `compsci` tag and conditional
  label/reference are exact.
- Unicode/source checks: NFC, Iranian `ی/ک`, balanced braces, 28 ordinary source
  ZWNJs, no other source bidi controls or Presentation Forms and no English
  reader fallback.
- Independent AI review directly against English: PASS after correction.
  `human_review=none`.
- Build: two clean serial LuaLaTeX passes using LuaHBTeX 1.25.7 / MiKTeX 26.5;
  no fatal error, undefined control sequence, missing character, overfull box or
  underfull box.
- PDF: one Letter page, 110,800 bytes, SHA-256
  `E9261EC31F6CB9C12D1C1C746FA27EA65EC9BCEE66039E729CAB0EB70A373D6D`.
  `/Lang=fa-IR`; localized title/author and one localized outline; zero links.
- Log SHA-256:
  `9B4AD3E8C18FBE57116539CC86BC2EFC63FB9EA295058724FC081CBEA24CC6B3`.
- Every page rendered at 144 dpi and visually inspected: PASS for shaping,
  margins, mixed-direction formulas, inclusion signs, binary enumeration and
  stable identifiers. Render witness SHA-256:
  `DCFAFD7EB58171626ECFD3272CE0A4D0F4A5078D68AA4129D2ADA4612F871BCB`;
  temporary PNG deleted after inspection.
- Poppler layout extraction: 2,782 characters, zero U+FFFD and zero Arabic
  Presentation Forms; SHA-256
  `C4A9691A4F289A23A4C63D5BCFF91F110557D4E4432920C323914511818F961A`.

## Honest limits

The PDF is not tagged-PDF or accessibility certified. Poppler drops all 28
source ZWNJs and inserts directional controls (U+202A/U+202B/U+202C:
59/28/87); counters, combining sequences or punctuation can serialize in
visual rather than logical order. Editable TeX is authoritative. This is unit
7 of 722, not a complete Persian edition or publication checkpoint.
