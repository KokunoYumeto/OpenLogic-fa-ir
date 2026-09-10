# Independent source challenge

Date: 2026-09-10. Result: all three claimed source corrections are mathematically justified and present in the inspected candidates. No concrete candidate defect was found within this bounded scope.

Scope: read the complete English source and Persian candidate for OLP-0016, OLP-0017, and OLP-0018, plus CORRECTIONS.json and SEMANTIC_CHECKS.json. Assess only the three source corrections, immediate-predecessor cardinality, and graph carrier/arrow/diagram preservation. Paths below are relative to `the review package`; line numbers are one-based. This is an independent mathematical comparison, not a certificate of Persian idiom, canon consultation, the whole translation, or rendered layout. Published variants, production, templates, validators, and external source provenance were not audited.

## Three correction challenges

1. **Prefix nonlinearity: correction sustained.** English `OLP-0016/source.en.tex:73–79` defines the prefix relation on all finite words over A and then asserts nonlinearity without an alphabet-size hypothesis. Counterexamples: if A is empty, A* consists of the empty word alone, so its prefix order is linear; if A={a}, every word is a^n and a^m is a prefix of a^n exactly when m≤n, again a linear order. Conversely, two distinct letters a,b in A give incomparable one-letter words, and the source's witnesses ab,ba work too. Thus nonlinearity holds exactly when A has at least two elements. Candidate `OLP-0016/candidate.fa-IR.tex:74–81` preserves the relation and its orientation, adds the sufficient hypothesis at line 79, and explicitly covers the empty/singleton exceptions at line 81. CORRECTIONS IDs: `FA0016-PREFIX-SCOPE`, `FA0016-PREFIX-NOTE`. No further correction needed.

2. **Branch carrier X→A: correction sustained.** English `OLP-0018/source.en.tex:91–95` declares T=(A,≤), B⊆A, but quantifies over undefined X∖B. Candidate `OLP-0018/candidate.fa-IR.tex:90–97` uses A∖B at line 93 and discloses the edit at line 97. A chain B is maximal exactly when every z in A∖B is incomparable with some u in B: otherwise B∪{z} is a larger chain; conversely, any larger chain supplies such an addable z. The witness u may depend on z; the candidate preserves that quantifier order and both negated comparisons. Negative control: in the two-node chain A={r,t}, r<t, taking B={r} and mistakenly X={r} makes the old condition vacuous, falsely admitting a nonmaximal chain. With A∖B, z=t correctly defeats it. Edge cases: on A={r}, B=∅ fails and B=A passes; in the fork r<a and r<b with a,b incomparable, {r,a} passes, witnessed against b by a. Finite branches remain allowed. CORRECTIONS IDs: `FA0018-BRANCH-DOMAIN`, `FA0018-BRANCH-NOTE`. No further correction needed.

3. **Nonempty prefix-closed subset: correction sustained.** English `OLP-0018/source.en.tex:50–53` requires a root belonging to the carrier, but lines 114–117 call every prefix-closed A⊆Nat* a subtree. A=∅ satisfies the closure implication vacuously and has no root. Nonemptiness repairs this under the section's rooted-tree convention. It is also sufficient: choose s∈A; prefix closure puts the empty word in A, where it is the unique least element. For any t∈A, its downset {u∈A : u⊑t} consists exactly of its finitely many prefixes, well-ordered by length. Candidate `OLP-0018/candidate.fa-IR.tex:115–120` adds nonemptiness, retains downward prefix closure, and explains the reason. A={empty word} is a valid one-node tree; A={empty word,〈0,1〉} is a useful failed-closure control because 〈0〉 is missing. This does not assert that every arbitrary subset inducing a rooted order is prefix-closed: {〈0〉} already shows that converse would fail. Nor does it assert finite branching for all these subtrees; Nat* itself remains an example with infinitely many children. CORRECTIONS IDs: `FA0018-NONEMPTY-SUBTREE`, `FA0018-SUBTREE-NOTE`. No further correction needed.

## Immediate predecessors and diagram preservation

**At most one is preserved for arbitrary source trees.** English `OLP-0018/source.en.tex:57–80` and candidate `OLP-0018/candidate.fa-IR.tex:56–79` use the cover relation (no intervening z) and state at most one predecessor; the candidate says `حداکثر یک` at line 67. Independently, two distinct predecessors y₁,y₂ of x lie in its well-ordered downset and hence are comparable. If y₁<y₂<x, y₁ is not immediate; the reverse case excludes y₂. The strict downset used in the proof inherits well-ordering from the non-strict downset in the definition.

Counterexample to “exactly one”: the ordinal chain ω+1 satisfies the source tree definition, has root 0, and its nonroot node ω has no immediate predecessor, since n<n+1<ω for every n<ω. This confirms the argument recorded in SEMANTIC_CHECKS.json without relying on its finite tables. The earlier “exactly one parent” sentence, English lines 37–38 / candidate lines 36–37, describes the preceding finite illustrated tree (English lines 22–34 / candidate lines 21–33); it must not be generalized to all trees. No such strengthening occurs in the candidate proposition. In contrast, nonempty prefix-closed sets of finite words do give each nonroot word its unique immediate predecessor by deleting the last symbol; that special fact does not narrow the general tree definition.

**No carrier, arrow, or diagram-code drift found.** In OLP-0017, English lines 25–40 / candidate lines 24–39 retain G=(V,E), E⊆V², the explicit carrier, and isolated vertices. Candidate lines 33–34 explicitly orient the arrow v₁→v₂ iff (v₁,v₂)∈E. The example, English lines 44–68 / candidate lines 43–67, preserves V={1,2,3,4}, V′={1,2,3}, and E={(1,1),(1,2),(1,3),(2,3)}: vertex 4 remains isolated in the first graph, absent from the second, and the loop and three other arrows are unchanged. E alone cannot distinguish these two graphs, so retaining V matters. The tree picture retains root r, children a,b, children c,d,e of a, `grow'=up`, and its undirected drawing option `-`; the ancestor prose retains upward traversal from x to y.

One read-only mechanical comparison found both graph TikZ blocks and the tree TikZ block exactly equal as decoded text between source and candidate. Ordered inline/display math spans, after whitespace removal, numbered 117/117 (orders), 26/26 (graphs), and 109/109 (trees). Their sole difference was the intended `$z \in X \setminus B$` → `$z \in A \setminus B$` at zero-based tree span 75. Each of the six correction-record `after` strings cited above occurs exactly once in its candidate. These are textual checks, not a TeX rendering or semantic proof of unrelated prose. SEMANTIC_CHECKS.json's domain-0–3 tables were read but not rerun or treated as universal proofs.

## Exact input identities

SHA-256 of raw file bytes, measured 2026-09-10T00:09:01Z. These hashes identify the local snapshots actually reviewed, not an independently authenticated upstream revision.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| OLP-0016/source.en.tex | 6308 | `79593789022FEF31C0609B9C94856E2AEF5CD5E88E92864E782BB6E6E5F4BCE4` |
| OLP-0016/candidate.fa-IR.tex | 9557 | `DB775A8B66B6144197CEB46569C7576554FAFDB972ADAD78FE70313715B54CB2` |
| OLP-0017/source.en.tex | 2939 | `DEC624EF4E71903B72A9F0B5FCC6A15A2E0F897F9EBE881DD9C9E21333AEEE75` |
| OLP-0017/candidate.fa-IR.tex | 4179 | `B2E5C39D1AB9106F6D773A5967A5E5D36396FC9B1618B80B61603E66699724FC` |
| OLP-0018/source.en.tex | 5102 | `A158F1CE5B84C8C3F681DD6347B22491D1B67A91E110138B9CB6833E3D9DC23C` |
| OLP-0018/candidate.fa-IR.tex | 7959 | `3D6703AC05B23C1D8DE0BFE07348BA5D97AC6F23C6FBC8318C6FA7A6E293A14B` |
| CORRECTIONS.json | 4149 | `907BBBBF170EF0194D2C8C4947D6B375CB6999BA4632C7C5DDD768DE91A2C552` |
| SEMANTIC_CHECKS.json | 1416 | `5F6D5F91AD8B96464C2CE54ADA1D1569F4B013EF2BBB7336BA1E9E2FB1DEC3DE` |

Disposition: this single bounded challenge is complete; no unresolved mathematical defect within its scope. Only this report was written. No production/candidate/template/validator edits, TeX runs, publication, task messages, or agent creation. No further pass is prescribed.

