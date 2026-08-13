# OLP-0009 Iranian-Persian build and QA receipt

- Locale/register: `fa-IR`, scholarly Iranian Persian.
- Unit: `OLP-0009`,
  `content/sets-functions-relations/sets/pairs-and-products.tex`.
- Source authority: official Open Logic commit
  `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`.
- Source SHA-256:
  `3DB7F0241D387B49488F70E78062C24192B813873618F761565D97BD7249431C`.
- Target SHA-256:
  `9474699C22D159D4F715B48E49B727E9BEAD8AE93F3BEBBD62C1CBD186C92BC5`.
- Unit build config / locale layer / terminology ledger SHA-256:
  `3E491BAB04BE0A5BF06EAC58638E3DBD5123E45CE5D351D4B99B32F744556199` /
  `B5477C8248F8A63FE27ABE108802F37E1F71E8969B093E2591E9110940AEBF6E` /
  `3FC6A4B6D0F8AC569C4362E36A2BC1DCEBBD39827CF52761E03CB2E415D97189`.

## Checks completed

- Direct and independent semantic replay: PASS. Ordered-pair equality and
  coordinate order, the exact Wiener--Kuratowski coding, left-associated
  tuples, Cartesian-product membership and enumeration, recursive powers,
  the `nm` and `n^k` counting claims, words over a set and the source's
  length-zero-sequence convention all preserve the pinned source.
- Structural replay: PASS for 177 TeX commands in exact order, 30 environment
  events, 12 Open Logic text tokens and 78 invariant math segments (72 inline,
  five display and one `align*`). Both labels, the same-unit reference, the
  `rcccc` array and the localized file ID are exact. Checker SHA-256:
  `91387B8796F5F44E682F4D7C6D1C11B3AD678DACCAFFAD04D3778786FDB0BD12`.
- Unicode/source checks: NFC, Iranian `ی/ک`, balanced braces, 57 ordinary
  source ZWNJs, no other source bidi controls or Presentation Forms, no Arabic
  code-point leakage and no English reader fallback.
- Independent AI review directly against English: PASS. Nonblocking adverse
  distinctions for ordered pair, ordered tuple, Cartesian product, word and
  sequence remain ledgered. `human_review=none`.
- Build: two clean serial LuaLaTeX passes using LuaHBTeX 1.25.7 / MiKTeX 26.5;
  no fatal error, undefined reference or control sequence, missing character,
  overfull box or underfull box. Only unchanged upstream hyperref and class
  warnings remain.
- PDF: two Letter pages, 133,844 bytes, SHA-256
  `94D935230548E75B1E411C12FA24A4154F22DA923A96CC42743F84A3D705F4FB`.
  `/Lang=fa-IR`; localized title/author and one localized outline; the
  same-unit reference is one internal `/GoTo` annotation.
- Log SHA-256:
  `82CE0EF56563CAC5B02045D27CC4B3705678233DC42A73A248FC8F573F952B8D`.
- Every page was rendered at 180 dpi and visually inspected: PASS for shaping,
  margins, mixed-direction tuple and product formulae, the product grid,
  proof-end marker, stable counters, clipping, overlap and tofu. Page render
  witness SHA-256 values:
  `7E3F3D0C345755150FB534AC3C668113AC4D433E2494DE81A96BB3BC199191E7`,
  `CDB92623EC2BA39043ED1C60EB209FA196601C1910146DA3481411ACB47129BE`.
  Temporary PNGs are not release files.
- Poppler layout extraction: 5,034 characters, zero U+FFFD, zero Presentation
  Forms and no `??`; SHA-256
  `C4B951A613CC0008AFECFD67BEEA5B596B376058EDD259E1F39EE1BF44A1F40F`.

## Source oddities preserved

The disjointness proof reuses the same second-coordinate name where arbitrary
second coordinates are implicit; the product grid silently assumes an
enumeration of `B` and omits visible commas; “any sequence” is broader than
the later finite-power display; and this unit writes `\emptyset` for the empty
sequence despite an earlier `\Lambda` convention. None was silently repaired.

## Honest limits

The PDF is not tagged-PDF or accessibility certified. Poppler drops all 57
source ZWNJs and inserts directional controls (U+202A/U+202B/U+202C:
159/60/219); punctuation or mixed mathematics may serialize in visual rather
than logical order, and copied mathematics approximates some angle brackets
and inequality signs. Editable TeX is authoritative. This is unit 9 of 722,
not a complete Persian edition or public checkpoint.
