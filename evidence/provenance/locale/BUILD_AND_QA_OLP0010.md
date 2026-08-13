# OLP-0010 Iranian-Persian build and QA receipt

- Locale/register: `fa-IR`, scholarly Iranian Persian.
- Unit: `OLP-0010`,
  `content/sets-functions-relations/sets/russells-paradox.tex`.
- Source authority: official Open Logic commit
  `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`.
- Source SHA-256:
  `9A76315CD0D9CF89D27E90A9B87138B1C95AEA98E0D26DE3FE12D897B8C4D10D`.
- Target SHA-256:
  `040B0431DA0D24CE6CFC12BDFCBD1B0970E8FD9397A4A6FB3D8EF36B93287886`.
- Unit build config / locale layer / terminology ledger SHA-256:
  `E0DFDDDA23F9E39528800AB9D87959BB01D02D97B5A8ADC21CE61453FA34C692` /
  `B5477C8248F8A63FE27ABE108802F37E1F71E8969B093E2591E9110940AEBF6E` /
  `E71B8975B1278D687B040C552AB75F1E3DBF49F9CD4B377594DAD10DB52821B0`.

## Checks completed

- Direct and independent semantic replay: PASS. Extensionality remains a
  conditional uniqueness principle, not an existence/comprehension axiom;
  unrestricted comprehension, Russell's set, the biconditional contradiction,
  both directions of the novice explanation and the hypothetical universal set
  all preserve the pinned source.
- Structural replay: PASS for 55 invariant TeX commands, 12 environment
  events, 10 Open Logic text tokens and 34 invariant math segments (33 inline
  and one display). The label and conditional cross-reference are exact.
  Checker SHA-256:
  `F76F4AC4692CB492F1C2FA19A7FF38ECCBA5611D8623530FBB38209BCC02756A`.
- Unicode/source checks: NFC, balanced braces, Iranian Persian orthography,
  Arabic/Persian separation, no source bidi controls or Presentation Forms,
  and no English reader fallback.
- Independent AI review directly against English: PASS. `human_review=none`.
- Build: two clean serial LuaLaTeX passes using LuaHBTeX 1.25.7 / MiKTeX 26.5;
  no fatal error, undefined reference or control sequence, missing character,
  overfull box, underfull box or emergency stop.
- PDF: one Letter page, 79,593 bytes, SHA-256
  `31A1E1D8319DAE9F04536ACC1C129B49184E7C69B369F8A6D7323C8EEF204368`.
  `/Lang=fa-IR`; localized title/author and outline; zero annotations, forms or
  JavaScript.
- Log / Poppler extraction SHA-256:
  `C8A26C046EDC72DD48153E1A08CD600F64801EB83D3C2D4219C532F56A26BB79` /
  `E7A0E9E8DD4EBB7547A35D8F8F02C43F025159F97CE7098B394C013F8574800A`.
- The complete page was rendered at 180 dpi and independently inspected:
  PASS for shaping, margins, mixed-direction formulas, proof-end marker,
  clipping, overlap and tofu. Render witness SHA-256:
  `230E2DBE13B73ABB006B25C766803AC105966E4BA33ABD08C71B0EA86BDE9FC0`.

## Source oddities preserved

The source's doubled whitespace, “the phi's” shorthand, source-only accent
commands and explicit spacing groups were not silently normalized. The
conditional cumulative-part reference correctly produces no link in this
isolated unit build because the referenced part label is absent.

## Honest limits

The PDF is not tagged-PDF or accessibility certified and does not declare RTL
viewer direction. Poppler extraction contains 286 balanced directional
controls, drops all 73 source ZWNJs and serializes every visible `\notin` as
slash plus `∈`; other extractors may reverse RTL runs or emit replacement
characters. Editable TeX is authoritative. This is unit 10 of 722, not a
complete Iranian-Persian edition.
