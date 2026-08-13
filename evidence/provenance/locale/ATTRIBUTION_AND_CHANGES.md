# Attribution and changes

## Upstream work

- Work: *Open Logic Text*, by the Open Logic Project.
- Project site: <http://openlogicproject.org/>
- Source repository: <https://github.com/OpenLogicProject/OpenLogic>
- License identified by the upstream text: Creative Commons Attribution 4.0 International (CC BY 4.0), <https://creativecommons.org/licenses/by/4.0/>.
- Pinned source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`.
- Translated unit: `OLP-0001`, upstream path `content/open-logic-about.tex`.
- Upstream unit SHA-256: `E4F2E2EC5D9957FA71DF41E9ED100641FE08230F63AF6065EAAFCB3D37346F4A`.

## Translation and changes

- Target locale: Iranian Persian (`fa-IR`).
- Date of this translation draft: 2026-08-13.
- The prose of `OLP-0001` was translated into scholarly Iranian Persian while retaining its structure, links, qualifications, and attribution conditions.
- All reader-facing strings in the upstream `open-logic-locale.sty` were localized. Internal command names, localization keys, environment keys, placeholders, and link targets were retained.
- A minimal locale configuration defines a locale-scoped left-to-right helper for future Latin identifiers. The OLP-0001 content itself preserves the upstream command sequence and does not invoke that helper. No project-wide logic vocabulary was introduced for this unit.
- An isolated LuaLaTeX driver was added for the translated unit. It uses Babel's Persian locale data, Unicode bidirectional processing, and explicit Persian-font fallbacks.
- The upstream source files were not modified. The isolated unit was compiled twice with LuaLaTeX, rendered, extracted, and checked against the pinned source; exact evidence is in `BUILD_AND_QA_OLP0001.md`.

This is a machine-produced translation with independent AI semantic, structural, build, and visual replay. It has not received review by a Persian-speaking human subject-matter editor. The upstream license and repository remain authoritative.

## Current admitted coverage

The branch now contains paired-accepted Iranian-Persian units `OLP-0001`
through `OLP-0010`: the About text, corpus root, naïve-set-theory part driver,
Sets chapter driver, Extensionality, Subsets and Power Sets, Some Important
Sets, Unions and Intersections, Pairs and Products, and Russell's Paradox. Units 0005–0010
have clean isolated reader builds and exact localization IDs. The Persian
wrapper additionally isolates complete stable Latin counters
so their visual order remains invariant inside RTL headings. Units 0002–0004
remain source/structure/semantic accepted but are not separately built because
their imports are not yet closed. This is current checkpoint history, not a
claim that the 722-unit Persian edition is complete.
