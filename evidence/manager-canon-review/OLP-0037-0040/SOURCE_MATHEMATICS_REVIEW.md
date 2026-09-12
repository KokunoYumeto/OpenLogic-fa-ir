# Source mathematics and editorial decisions: OLP-0037–0040

This is a complete review of the four frozen source files and their Persian counterparts, not a new reader release. Exact raw-source, localized-input, candidate and canon identities are in choices-evidence.json. Source authority is the frozen Open Logic Project revision recorded there. The mathematical content was read directly; the ten cited scholarly pages were inspected as full rendered pages, not merely searched for keywords.

## What changed

- OLP-0037 states Schroder–Bernstein and deliberately defers its proof. Persian now describes the two directions of constructing injections instead of suggesting a case split. The theorem, deferred reference, Potter citation key and page numbers remain unchanged.
- OLP-0038 keeps the inclusive meaning of enumerable: finite, empty or countably infinite. It makes the empty initial segment explicit and defines ceiling precisely as the least integer greater than or equal to the argument. All parity and integer-enumeration formulas are retained.
- OLP-0039 restricts the no-bijection-with-the-naturals explanation to infinite sets, repairs the reversed digit/string indices and the repeated bit-flip direction, and restores four missing memberships in the illustrative array. It also repairs the malformed conditional around an optional footnote. Editorial additions are visibly identified as such.
- OLP-0040 explains why an exhaustive surjective image list may require removal of repetitions before it is a bijective enumeration. The particular characteristic-sequence map is also injective, and that justification is now explicit. Its undefined output index is removed. Two retained but disabled English blocks are translated into Persian and remain disabled; their dormant mathematical defects are disclosed and corrected.

The output has 57 aligned review spans and 25 replacement records. These counts are bookkeeping, not independent certification or a count of 25 false theorems. Several records disclose or clarify the same source defect. Every original source and localized input is preserved.

## Governing conventions and mathematical reasoning

### OLP-0037: no missing proof

Injections in opposite directions imply a bijection, including the empty case: if one set is empty, the injection from the other into it forces both to be empty. The general Schroder–Bernstein theorem does not require Choice. The source explicitly postpones its proof; adding a proof here would change the section's intended scope.

Khani's set-theory pages 51–52 distinguish the theorem from the Choice-dependent cardinal-comparison route. The displayed orbit proof on page52 contains problematic claims: injective maps alone do not make every orbit infinite or all such orbits disjoint. That proof is not copied, adopted or treated as evidence for its own correctness. The page is used only for the terminology and the explicit distinction about Choice. The historical attribution remains inherited from the source's Potter citation, not newly verified against Potter.

### OLP-0038: finite bounds, empty sets and integers

The opening initial segment has cardinality n and runs from0 through n−1. The later definition runs from0 through n, using n as the last index; this is a change of dummy parameter, not an off-by-one error. The empty set is separately declared enumerable. The clarification preserves those conventions rather than silently replacing them with a strict countably-infinite definition found in part of the Persian canon.

The four `!!{element}sی` forms realize as «اعضای» in the actual locale. Their suffix is not an untranslated plural marker. The contextual uses were read; no global suffix deletion is made.

The identity enumerates the naturals, and n+1 enumerates the positive naturals. The even/odd formulas are not onto the whole natural-number codomain; their corestrictions enumerate their stated images. The square-number exercise starts at1, not0.

For the integer enumeration, even input2k gives k and odd input2k+1 gives −k−1. These disjoint images cover the integers. The inverse is2z for nonnegative z and −2z−1 for negative z. The displayed values through input6 are all correct. The ceiling description follows the Persian textbook's function terminology and includes the exact least-integer meaning, not unrestricted nearest-integer rounding.

The surjection/injection characterization exercise is valid. For a nonempty finite enumeration of size k, repeating it with input n modulo k gives a surjection from the naturals. A surjection gives each output its least preimage; an injection into the naturals gives an increasing enumeration of its image. The empty injection exists, but a function from the naturals to the empty set does not. No arbitrary choice family is required.

For binary unions, injections into the naturals can be combined using even indices for members of A and odd indices for members of B outside A. Induction gives finite unions, including the empty union when admitted. No unsupported claim about arbitrary countable unions is added.

### OLP-0039: diagonalization and all 24 displayed cells

A singleton is enumerable but has no bijection with the naturals. The empty set is enumerable despite having no surjection from the naturals. These counterexamples require qualification of the unrestricted introductory equivalence. The repaired paragraph is about infinite A; both actual diagonal targets are infinite. The informal general strict-cardinality comparison is given an explicit sufficient Choice background, not a claim that full Choice is its weakest necessary assumption. The actual diagonal proofs do not need it.

In the string array, s_n(m) means digit m of string n. The proof constructs d(n)=1−s_n(n); both bit-flip directions are necessary. For each n, d differs from the nth listed string at n. Repeated rows do not undermine this argument. Strings with their only1 at distinct indices show the target is infinite, so a finite enumeration cannot exhaust it either. The candidate supplies the finite-list scope explanation.

For the powerset diagonal, D consists of n absent from the nth listed set. It is a subset of the naturals and differs from every listed set at the corresponding index. Its existence uses ordinary separation; no choice operation is involved.

The illustrative sets are the naturals, the odd naturals, {0,1,4}, and {2,3,4,…}. The first row must therefore display3,4,5, and the fourth row must display5. All four missing memberships are restored. The blank cell at row2/column2 stays blank. The anti-diagonal still excludes0 and1, includes2 and excludes3. The new regression reads the actual candidate's 24 explicit cells, rather than checking only a separately hard-coded diagonal. The original table fails at exactly four cells.

The function exercise's outer list starts at1, whereas each function's domain starts at0. A counter-diagonal can set g(0)=0 and g(i)=f_i(i)+1 for i≥1, or use g(n)=f_(n+1)(n)+1. The exercise is valid; the candidate does not insert its solution into the exercise.

The source's `oliflabeldef` is defined with three mandatory arguments. The frozen footnote expression supplies only two braced groups before the next environment command. The repair puts the footnote in the true branch, leaves the false branch empty, and makes the following explanatory sentence unconditional. A balanced-argument parser accepts the repaired expression and rejects the original. No actual TeX execution or rendered-PDF verification is claimed here.

### OLP-0040: reduction direction and dormant material

To establish that A is not enumerable from known nonenumerability of B, the useful surjection goes A→B, or the useful injection B→A. The direction of the reduction between enumeration problems is the reverse of the enumeration-producing map. The source and translation preserve this distinction.

A surjection can repeat values: n↦floor(n/2) sends the natural enumeration to0,0,1,1,… . That list is exhaustive but is not a bijective enumeration. Retaining first-occurrence indices and listing those indices increasingly gives the required finite or infinite bijection. If A is empty, surjectivity makes B empty too. This is a set-theoretic construction, not a claim of algorithmically decidable equality.

For the particular characteristic-sequence map, a subset N determines exactly one binary string, and a string determines exactly its support. The map is bijective. Even naturals map to1010…, the empty set to000…, and the whole domain to111… under zero-based indexing. Removing an undefined k merely makes this already determined output name consistent.

All six active reduction exercises are sound. Injection transfer uses the inverse only on the injection's image. Coordinate parity maps natural-valued functions and natural-number sequences onto binary sequences. A set of pairs maps to {n:(n,0) is in that set}, covering every subset of the naturals. The binary surjections include all sequences with fixed prefix01 and arbitrary tail, giving an injection of binary strings. For real numbers, the ternary0/2 series gives an injection: at the first differing index, the leading difference exceeds the largest possible opposing tail. No unqualified uniqueness of binary real expansions is used.

The dormant explanation keeps the coordinate1 projection but calls it coordinate1, not the first coordinate. The unbound codomain name Y is replaced by the already bound B. The n-zero output is made infinite by appending an infinite zero tail; even for n=0 this is a valid constant-zero sequence and is not onto. The dormant partial-function exercise remains correct: total functions into a singleton form a singleton, while partial functions into it correspond to arbitrary subsets of their input domain. Partial does not mean a nonterminating algorithm.

## Canon limits and review priorities

The disciplinary canon supports the terms for mappings, domain/codomain/image, injection, surjection, bijection, cardinal comparison, countability, ceiling and the diagonal constructions. Exact local attestations for the retained labels «کاهش», «پسین», «قطری‌سازی» and «جزئی» are not established by these selected pages. Their mathematical meanings are explicitly constrained by the source, their uncertainty is recorded at the relevant choice, and their editorial confidence is provisional. No invented lexical attestation or calibrated-probability claim is made.

## Integration boundary

Use the complete hash-bound candidates and source-transform.json. Twenty-three active changes have balanced TeX declarations. The two disabled-comment translations are physical-source-only changes: unescaped percent signs would be discarded if their text were used as TeX macro arguments. Apply them to derived source before tokenization, preserve the percent prefixes, and verify the full candidate hash. Do not activate them or overwrite frozen originals.

The actual owner's physical-source generator and declaration parser were read. A parser roundtrip and an independent application of the complete source recipe verify this handoff, but do not establish that the owner has installed it, run the full722 reader, generated EPUBs or published a successor. Those remain real edition-production steps, with TeX serialized by the global mutex. The current packet is usable corrected source and review evidence, not a substitute for those deliverables.

Attribution and rights: Open Logic Project and contributors retain their existing CC BY4.0 attribution. Persian scholarly PDFs, images and full extracted pages remain private consultation copies and are not included in this packet.
