# OLP-0008 Iranian-Persian build and QA receipt

- Locale/register: `fa-IR`, scholarly Iranian Persian.
- Unit: `OLP-0008`,
  `content/sets-functions-relations/sets/unions-and-intersections.tex`.
- Source authority: official Open Logic commit
  `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`.
- Source SHA-256:
  `2AD0EEC70308CEEFF2A4158B2DEE60E59A9B1CF9268FC95C4BB1DA05F65AD60D`.
- Target SHA-256:
  `1015C403DB83903E04890FE7CB9B28ABF3AC2E2A4A32E652BCE62224C0A1EAD5`.
- Unit build config / locale layer / terminology ledger SHA-256:
  `E011A5A2CB4290BD0BB725A443FB07036531307C7884C5E3735FAF8CA2E545D9` /
  `B5477C8248F8A63FE27ABE108802F37E1F71E8969B093E2591E9110940AEBF6E` /
  `F6B4A20C143B8CAFBA4ACF5C3DA5ECC8AB5DCFAEA173968E266579683012BF6A`.
- Section wrapper SHA-256:
  `629773BE98FED885B39A938477DB91D9B5891E35C3BAC1B16C7873B4601D022A`.

## Checks completed

- Direct and independent semantic replay: PASS after restoring one omitted
  Open Logic `!!{element}s` token without changing the Persian proposition.
  Inclusive union, repetition, subset and empty-set examples, intersection and
  disjointness, the existential and universal arbitrary-family conditions, the
  finite family example, the `A in B` problem, indexed-family progression,
  directional set difference and the proper-subset problem preserve the pinned
  source. No nonempty-family condition absent from the source was introduced.
- Structural replay: PASS for 213 TeX commands in exact order, 46 environment
  events, 27 Open Logic text tokens and all 72 math segments. All three TikZ
  assets, three labels, four references and the localized file ID are exact.
  Checker SHA-256:
  `B8DA8841A80CFF3739B4074E8D7F1838BE714479D56C8A67BA9B45DBC02EA9E5`.
- Unicode/source checks: NFC, Iranian `ی/ک`, balanced braces, 57 ordinary
  source ZWNJs, no other source bidi controls or Presentation Forms, no Arabic
  code-point leakage and no English reader fallback.
- Locale correction: added lower- and upper-case cleveref names for `section`.
  The prior accepted Extensionality label is imported with `xr`; the resulting
  reader link is a real `/GoToR` action to the admitted OLP-0005 PDF, while the
  three figure references are internal `/GoTo` actions.
- Independent AI review directly against English: PASS. Nonblocking adverse
  terms `مجموعه‌های جدا از هم` and `تفاضل مجموعه‌ای` remain explicitly defined
  and ledgered. `human_review=none`.
- Build: two clean serial LuaLaTeX passes using LuaHBTeX 1.25.7 / MiKTeX 26.5;
  no fatal error, undefined reference or control sequence, missing character,
  overfull box or underfull box. Only unchanged upstream hyperref and class
  warnings remain.
- PDF: three Letter pages, 134,566 bytes, SHA-256
  `23E5E6E25A1040449632A1F7644BCC6769FA104785BBB5346E940C4C4B3DD2CC`.
  `/Lang=fa-IR`; localized title/author and one localized outline; four links.
- Log SHA-256:
  `FCAFE87D39716EE6BD6D0E2E1DE5EF5322E7ACAD46AED23864418A474B20DBA6`.
- Every page was rendered at 180 dpi and visually inspected: PASS for shaping,
  margins, mixed-direction set formulas, all three union/intersection/difference
  diagrams and their captions, stable counters, cross-reference localization,
  clipping, overlap and tofu. Page render witness SHA-256 values:
  `AF80C0BC68EFBB72E5D8C5154B6337DCAE11D4B1BE7D41F889F96D964CCD6D55`,
  `0055CC8F23FE112A2B2A82744ACB789A279F4D66E78C7C0D294FD0EC3B660FDF`,
  `5903D707773EBA0BFA531644794672EAC753607888889BB544CEF233B3F7F91F`.
  Temporary PNGs are not release files.
- Poppler layout extraction: 6,943 characters, zero U+FFFD, zero Presentation
  Forms, no `??` or English `Section`; SHA-256
  `F6ADE6DBD2BB1B94EB8052740C6F4154EF6D9F58DEB005F619673C85F6C4286E`.

## Honest limits

The PDF is not tagged-PDF or accessibility certified. Poppler drops all 57
source ZWNJs and inserts directional controls (U+202A/U+202B/U+202C:
170/83/253); punctuation or mixed math may serialize in visual rather than
logical order. Editable TeX is authoritative. This is unit 8 of 722, not a
complete Persian edition or public checkpoint.
