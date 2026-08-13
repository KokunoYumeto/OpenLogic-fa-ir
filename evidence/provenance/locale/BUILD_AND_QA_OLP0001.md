# OLP-0001 Iranian-Persian build and QA receipt

- Locale/register: `fa-IR`, scholarly Iranian Persian.
- Unit: `OLP-0001`, `content/open-logic-about.tex`.
- Source authority: Open Logic commit `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`.
- Source SHA-256: `E4F2E2EC5D9957FA71DF41E9ED100641FE08230F63AF6065EAAFCB3D37346F4A`.
- Target SHA-256: `2E400AC320BDBCCFAD6EF2A3520E0ABA53BA92D1ABCFB04F202A30CD67908DCD`.
- Locale SHA-256: `0AAF1CA41D3CAA6E6CC53AA3DEA75251E65428290FF9613209ABF9D92F7A49A3`.
- Config SHA-256: `DF8A82CE6D3DCE9E9BA1621D03E52B2FBDEFABE4F34FC290F9A531E92678A85B`.
- Driver SHA-256: `29EB420105DD253FD66CF6E1A7C94A7D3DC52E24C14D43AF287962643C5ECD9F`.

## Checks completed

- Source/target semantic replay: all nine propositions in the source About text preserved, including the incomplete/draft caveat, planned features, six CC reuse verbs, attribution condition, and both destinations.
- Static parity: PASS after removing a content-level LTR helper from the displayed domain. Source path/hash, ordered structural commands, two URLs, heading/outline text, 25 caption keys, 15 `cleveref` keys, nine boilerplate macro signatures/placeholders, balanced braces, NFC, and script-residual gates pass.
- Independent post-correction AI replay: PASS for all nine semantic propositions, exact structure/URLs, locale contract, build log, localized metadata/outline, link annotations, and full-page visual rendering.
- TeX source uses Iranian Persian `ی/ک` and ordinary U+200C half-spaces. It has no embedded bidi-format controls, Arabic Yeh/Kaf leakage, presentation-form characters, Arabic prose leakage, or unapproved English prose. URLs, domains, and named technical brands are intentionally invariant.
- Build: two serial passes of `lualatex -interaction=nonstopmode -halt-on-error about-fa-ir.tex`; LuaHBTeX 1.25.7 / MiKTeX 26.5. No fatal error, undefined control sequence, missing character, overfull box, or underfull box was reported.
- Nonblocking build warnings retained in the log: repeated upstream `hyperref` option, two upstream file-provides-name warnings, font script/language declarations, and deprecated memoir `\addtodef` use.
- A post-QA hygiene change replaced an intentional literal trailing TeX control-space with the equivalent `\space`; static checks and both build passes were replayed afterward.
- PDF: one Letter page, 48,535 bytes, SHA-256 `D7CE4D015EC6E9C77F856CC4AD3E3358222785C25D50CC0B8D4070AB9DBC815A`.
- PDF metadata and outline title are both `دربارهٔ پروژهٔ منطق باز`; author metadata is `پروژهٔ منطق باز`.
- Link annotations: exact URIs `https://github.com/OpenLogicProject/OpenLogic/wiki/Contributing` and `http://openlogicproject.org/`.
- Visual QA: PASS on the complete one-page PDF rendered at 144 dpi. No clipping, overlap, broken shaping, or Latin/RTL collision was seen. Render witness SHA-256 `0A9D3A739F3054D3DCAE4DB18A334E21ECF5DAE259C9A470907E9CF4A408BBF6`; temporary PNG deleted after inspection.
- Extraction witness: 1,634 characters; zero U+FFFD; zero Arabic Presentation Forms; U+202A/U+202B/U+202C counts 30/14/44. Extracted-text SHA-256 `C007AC4524A4834614815267973EEC321BD436C73C51DC4ED341BA06468F68FB`.

## Honest limits

- The PDF is not claimed to be tagged-PDF or accessibility certified. The editable source preserves 23 ZWNJs in this unit, while this PDF extractor returned zero; Babel/LuaTeX also inserts directional controls in extracted text. The editable TeX remains the authoritative searchable/copyable target.
- `human_review=none`. The independent AI replay does not stand for native-community certification.
- This is one accepted scheduling unit in a 722-unit complete-edition closure, not a complete Open Logic Persian edition and not a publication checkpoint.
