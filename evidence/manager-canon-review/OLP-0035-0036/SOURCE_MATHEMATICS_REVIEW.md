# Equinumerosity, comparison, and Cantor's theorem: mathematical review

Authority: the exact OLP-0035 equinumerous-sets.tex and OLP-0036 comparing-size.tex blobs at frozen revision9620cc73f9c8e0ad003c514a5d3748f29611c4c0. Their source and target identities are in SOURCE_IDENTITIES.json. Both complete files and both original Persian translations were read by the main reviewer. This is not independent mathematical or human certification.

## Equinumerosity and both enumeration branches

Equinumerosity means existence of a bijection, not equality, inclusion or an arbitrary pairing. Identity gives reflexivity, inversion of a bijection gives symmetry, and composition of bijections gives transitivity. Empty sets cause no failure: the empty identity and its inverse are bijections. The source's composition argument order is fixed by its explicit equation comp(g,f)(n)=f(g(n)); keep these macro arguments, not a guessed printed order.

If f:A→B is a bijection, then A is empty exactly when B is empty. In both conditional source variants, the empty-set parenthetical incorrectly invokes g(x)=y, although g is the enumeration introduced only in the other case. The argument must refer to the already fixed surjection f. Replace exactly those two occurrences with f(x)=y. This is known OLSIZ-006, not a new finding or a false proposition.

For nonempty A, if g:PosInt→A is onto, f∘g is onto B: choose y in B, use surjectivity of f for x, then of g for n, and compute f(g(n))=y. These pointwise existential steps require no simultaneous choice of a preimage for every y. In the alternative branch g is a bijection from Nat or a finite initial segment onto A; composition is a bijection with the same domain and range B. Reverse direction uses f inverse. Both variants remain in the candidate; neither is dismissed merely because a particular reader selects only one.

The union exercise assumes both A∩B and C∩D empty. Combine the given bijections f:A→C and g:B→D by cases. Disjoint domains make the definition unambiguous, disjoint ranges prevent cross-case collisions, and surjectivity of f and g covers C∪D. Every hypothesis is needed for this simple construction and preserved.

For an infinite enumerable A, take an enumeration and the increasing sequence of indices at which genuinely new values first appear. Infinitude ensures infinitely many such indices. Their values are distinct and cover A: every element has a least occurrence index, which enters the sequence. This yields a bijection Nat→A after the fixed indexing shift. No computability of the least-occurrence test and no choice from a family of arbitrary sets is assumed.

## Comparison and the choice convention

The non-strict relation is existence of an injection A→B. It is reflexive and transitive by identity and composition. It is not symmetric: empty injects into a singleton, but not conversely. Nor does it assert A⊆B. An injection identifies its domain bijectively with its actual image; the image has exactly, not merely at least, the same size. The source's weaker “at least” sentence is true and is not charged as an error.

The strict relation is an injection A→B with no bijection A→B. It is irreflexive, not merely “not reflexive.” Its transitivity can use Cantor–Schröder–Bernstein: if A<B<C and A≈C, compose B→C with C≈A to get B→A, alongside A→B. The theorem gives A≈B, contradicting A<B. Thus the strict relation is transitive. The exercise is sound, but its infinite case should not be justified solely by finite integer-size tests.

The equivalence “A enumerable iff A injects into Nat” uses no Choice: from a surjective enumeration assign to each element its least occurrence index; conversely, enumerate the image subset of Nat increasingly, or extend inverse-on-image by one default when nonempty. Empty is handled separately.

The next equivalence, “A nonenumerable iff Nat is strictly smaller than A,” needs a background principle ensuring that an infinite A has a countably infinite subset. The Axiom of Choice is sufficient: well-order A and choose its successive least unused elements. A nonenumerable A is infinite; these elements inject Nat into A, while a bijection would contradict nonenumerability. In the reverse direction, an infinite enumerable A is equinumerous with Nat by the preceding exercise, contradicting strictness.

The candidate labels the use of Choice for this general comparison, while leaving the first equivalence and Cantor's theorem unqualified. It does not claim that full Choice is the weakest equivalent principle, that the statement is false in ZFC, or that an independence proof was established here. The selected Persian canon expressly introduces well-ordering/Choice in its cardinal comparison background. Without that background, the source definition in terms of enumerable/nonenumerable remains controlling; the comparison statement must not be silently presented as a definition.

## Cantor's theorem, both proof variants, and empty A

The singleton map x↦{x} is injective by extensionality, including when A is empty. To exclude a surjection g:A→Pow(A), define D={x∈A:x∉g(x)}. For each x∈A, definition gives x∈D iff x∉g(x), hence x∈g(x) iff x∉D. Thus g(x) differs from D at x, so D is outside the range. Since D is a subset of A, it is an element of Pow(A); therefore g is not onto. For A empty, D is empty and belongs to Pow(empty)={empty}, while g has empty range. This is still a valid argument.

The long source variant concludes its arbitrary-element argument with “for each x in overline(A)” instead of “for each x in A.” This is known OLSIZ-007. Restricting the conclusion to the diagonal subset cannot establish exclusion from the entire range: that subset can be empty, for example with g(x)=A on nonempty A. The candidate corrects this one domain occurrence.

The two preceding conditional sentences express the two directions of the same incompatibility, rather than by themselves establishing a full biconditional. The defining set-comprehension already supplies the full biconditional. The candidate explicitly invokes that definition in the conclusion; no additional theorem premise is introduced.

The short conditional proof assumes a bijection, forms D, uses surjectivity to take y with g(y)=D and obtains y∈g(y) iff y∉g(y). It is valid. Its two math-text “iff” phrases, equations, identifiers and conditional availability are preserved.

The later explanatory paragraph's “there is always an element of A” is read per chosen input x. The candidate makes that dependence explicit so that it does not assert existence of an element when A is empty. No theorem is restricted to nonempty sets.

The final injection exercise is sound without Choice or a use of Cantor–Schröder–Bernstein. Assume injective g:Pow(A)→A. Define D={g(B):B⊆A and g(B)∉B}; this is a subset of A. Let x=g(D). If x∉D, taking B=D makes x∈D. If x∈D, there is B with g(B)=g(D) and g(B)∉B; injectivity gives B=D and hence x∉D. Both cases contradict themselves. The translated hint retains the set-of-images definition, not the different diagonal used in the theorem.

## Primary quotation, canon and limits

Frege1884 §70 was checked against the acquired German Project Gutenberg transcription, not a scanned facsimile. The original says the plates and knives are uniquely related in both directions by their relative placement. The Persian quotation now makes both directions explicit. The waiter, knives, plates and right-hand-side relation are retained; the historical illustration is not an added analogy. Exact downloaded HTML and extracted quotation hashes are in ORIGINAL_QUOTATION_PROVENANCE.json. The existing citation key and section locator remain unchanged.

Nine complete Persian scholarly pages were consulted and indexed: Khani/Zarei set theory PDF8,23,51,53; Khani foundations PDF114,115; Ghaffari Hadigheh/Toumanian PDF50,55,56. They directly attest extensionality as اصل گسترش, irreflexivity as پادبازتابی, equinumerosity as هم‌توان, and the retained inverse/composition/relation-property vocabulary. Do not substitute merely non-reflexive for irreflexive, identity of sets for equinumerosity, or an effective enumeration for an arbitrary one.

The caption/name Cantor and the existing Cantor1892 and Russell source links are retained. This batch verifies their mathematical content and source alignment, not a new archival investigation of every historical influence/date claim. Such historical attribution remains an explicitly marked later-review item rather than fabricated original-source consultation.

Finite tests below supplement the universal arguments; they do not prove the infinite statements. No reader, PDF or EPUB is rebuilt or newly visually certified here. Frozen originals remain unchanged. Human review is a later opportunity, not a gate.
