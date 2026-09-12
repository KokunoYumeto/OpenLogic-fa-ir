# Independent mathematical source review: OLP-0033 and OLP-0034

Date: 2026-09-12. Frozen revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`.

## Result and scope

The two stated theorems, their two diagonal proofs, the additional reduction proof, and all nine exercises are mathematically sound under the chapter's definition of enumerable. Two errors occur in surrounding exposition: an unrestricted enumeration criterion omits the empty-set exception, and an example wrongly types a finite binary string as an infinite binary sequence. Neither error invalidates the stated theorems or exercises. A stray subscript in the characteristic-function definition is a notational blemish with a uniquely determined reading, not a substantive proof gap.

This was one bounded, independent SOURCE audit. Both target blobs were read completely. No owner source was edited or translated; no Persian or canon assessment was made. Manager0031–0032 were not re-audited. Only the permitted `enumerability.tex` was additionally consulted for definitions and indexing. `zig-zag.tex` was unnecessary and was not read. There were no workspace Git scans, TeX/Lean runs, downloads, finite-test substitutes for proof, cleanup operations, messages to other tasks or people, or publication operations.

Only this report and `TASK_INPUT_VERBATIM.md` were written, using `apply_patch`. The latter preserves the current task request verbatim. Source quotations and locators below refer to the frozen source, not to a translation or mutable checkout. Repository path components preserved in the verbatim request are solely literal retrieval instructions; no personal attribution is made.

## Exact source identities and retrieval

The requested bare repository was used with `git --git-dir=<the repository path supplied in TASK_INPUT_VERBATIM.md> show REV:PATH`. Source content came from that command's raw standard-output bytes. SHA256 was computed directly on those bytes before decoding or adding line numbers. `git rev-parse REV:PATH` supplied the Git blob identities, and `git cat-file -s BLOB` independently agreed with both target byte counts. No working-tree copy, line-ending normalization, or Git status/diff/add/enumeration was used.

All paths in this table are repository-relative. Line locators below are one-based physical lines in these exact blobs; the common directory is `content/sets-functions-relations/size-of-sets/`.

| ID | Exact path | Bytes | Git blob identity | SHA256 |
| --- | --- | ---: | --- | --- |
| OLP-0033 / N | `content/sets-functions-relations/size-of-sets/non-enumerability.tex` | 9198 | `35cea38a1e8e549de28e34fc49efc82fcbac57b5` | `4471def29c2da48dcb01635adf692cd0bc89cb6885636db149f4b2d86ff4e9fa` |
| OLP-0034 / R | `content/sets-functions-relations/size-of-sets/reduction.tex` | 5540 | `cadd3684985dbd36adf5fbf04606a1b11bcf4f07` | `0d6d2e3280698668b837cef6dcf3134b86d2a4b48831ae516e6e33e42898c79a` |
| Definition reference / E, not an audit target | `content/sets-functions-relations/size-of-sets/enumerability.tex` | 12006 | `6989a613f747328379955bbff156703dc304320f` | `bf6be35c0e393cb6e1d227f8e9024df4216792e663f23beb7277045487acfa67` |

N has 214 physical lines and R has 138. The definition lookup displayed E:1–155, but the only passages used as mathematical premises were E:27–32, 37–50, 64, 87–90, 104–116, and 118–122. No theorem, proof, or exercise in E was independently re-audited. The full-blob hash for E identifies the reference bytes; it does not claim a full-file review.

## Governing definitions

- E:87–90 defines an enumeration of a **nonempty** set A as any surjection from the positive integers to A. E:113–116, local label `defn:enumerable` under `\olfileid{sfr}{siz}{enm}`, defines enumerable as empty or having an enumeration. E:64 explicitly counts the empty list as enumerating the empty set.
- E:27–32 and 37–50 permit repetitions and require every listed element to occur at a finite position. E:104–110 explains how to extend a nonempty finite list by repeating its last element. Thus a nonempty finite enumerable set also admits a positive-integer-indexed enumeration.
- E:118–122 uses n ↦ n−1 from the positive integers onto `\Nat`; accordingly this report writes P = {1,2,3,…} and N₀ = {0,1,2,…}. The report's source alias N must not be confused with N₀.
- In N:43–44, 56–59, and 87–99, `\Bin^\omega` consists of all total binary sequences with coordinates numbered by P. Write B = {0,1}. A zero-based presentation of the same sequence space is equivalent by the fixed shift n ↔ n−1; it is not a substantive change.
- “Any surjective function” in E:88–89 imposes no computability requirement. The function sets and partial-function sets in these targets are ordinary set-theoretic function sets. No membership test, sequence, or enumeration is assumed to be computable.

Arguments below use ordinary classical set reasoning. None requires the axiom of choice, countable choice, a general selection of preimages of an arbitrary surjection, or the principle that every infinite set has a countably infinite subset.

## Confirmed errors and their exact extent

### N-F1 — Missing nonemptiness restriction in the general criterion

**Locators:** N:25–31, especially 26–27; the purported sufficiency/equivalence at N:33–38. Governing exception: E:64, 87–90, and 113–116.

**Classification:** a literally false unrestricted statement, and a missing hypothesis in the surrounding criterion. This is not a gap in either subsequent theorem proof.

N:26–27 says that for any enumerable A there is a surjection P → A. Take A = ∅. The chapter expressly makes ∅ enumerable, but no total function P → ∅ exists: its value at 1 would have to be an element of ∅. In particular no such surjection exists. This same counterexample disproves the unrestricted implication “no surjection P → A, therefore A is nonenumerable” used as a general method at N:33–38. Equivalently, ∅ admits no one-way infinite list of its elements but is still enumerable by the empty list.

The one-direction assertion at N:28–29 that a nonenumerable set admits no such surjection is correct. What fails is the converse without the nonemptiness condition, and the preceding universal assertion about enumerable sets.

The opening discussion at N:20–23 concerns infinite sets. If that is understood as a continuing restriction on A, the argument is correct; the literal wording “For any … set A” fails to carry that restriction explicitly. This contextual mitigation does not remove the concrete empty-set counterexample to the unrestricted sentence.

**Local mathematical repair, proposed only:** state the criterion for A ≠ ∅ (or for infinite A):

> For nonempty A, A is enumerable exactly when there is a surjection P → A. To prove a set nonenumerable by excluding all such surjections, also establish that it is nonempty.

Both theorem targets meet this side condition explicitly: the constant-zero sequence belongs to B^P, and ∅ belongs to the power set of P. No theorem conclusion needs changing.

### R-F1 — A finite string is assigned an infinite-sequence codomain

**Locators:** R:95–100, specifically the formula at 97 and claimed type at 99–100.

**Classification:** a false typing claim in an illustrative example. It does not invalidate the reduction principle, its direction warning, or the earlier reduction proof.

The displayed h(n) is explicitly a string of **n zeroes**. As a sequence its domain is {1,…,n}, whereas an element of B^P must have a value at every positive integer. For every n, h(n) lacks a value at coordinate n+1; already h(1) = (0) is not an element of B^P. Consequently the displayed rule does not define the asserted function h:P → B^P. It defines a function into finite binary strings. No convention extending finite strings by infinitely many zeroes is stated here; the underbrace explicitly makes the displayed length finite.

**Local mathematical repair, proposed only:** set h(n)(j) = 0 for every n,j ∈ P. This is a well-typed function P → B^P whose image is the singleton consisting of the infinite constant-zero sequence. The constant-one sequence is omitted, so h is not surjective. This proves exactly the intended point: a mere function from an enumerable domain into B^P does not imply that B^P is enumerable.

### R-N1 — A stray k in the characteristic-function definition

**Locators:** R:51–54, using `s_k` for the sequence assigned to an arbitrary Z; compare R:63–69.

**Classification:** an unbound/redundant notational subscript, not a confirmed mathematical proof gap or false theorem.

There is no specified relationship between k and the arbitrary input Z. Nevertheless the stated conditions uniquely determine the output pointwise: χ_Z(n) = 1 when n ∈ Z, and 0 otherwise. Existence follows by defining this value for every n ∈ P; uniqueness follows because two sequences satisfying that condition agree at every coordinate. The value therefore does not depend on choosing k or finding an already enumerated sequence.

Writing `f(Z)=χ_Z`, or simply using s without k, removes the ambiguity. The proof subsequently uses only this characteristic sequence and supplies its explicit inverse construction. There is no assumption that a list of all binary sequences already exists, and no choice principle is hidden in the notation.

## Complete theorem, proof, and exercise inventory

Numbers N-T1 etc. are audit identifiers, not invented source labels. Unlabelled exercises are located by their complete environment bounds and opening subject.

| Audit ID | Source scope | Source identifier or subject | Disposition |
| --- | --- | --- | --- |
| N-T1 | N:46–49 statement; 51–137 proof | `thm:nonenum-bin-omega` under `\olfileid{sfr}{siz}{nen}` | True; diagonal proof complete |
| N-T2 | N:147–150 statement; 152–177 proof | `thm:nonenum-pownat` under `\olfileid{sfr}{siz}{nen}` | True; diagonal proof complete |
| N-E1 | N:202–204 | Power set of `\Nat`; unlabelled | True; explicit solution below |
| N-E2 | N:206–212 | `sfr:siz:nen:prob:f-posint`; all functions P → P | True; explicit solution below |
| R-E1 | R:41–45 | Injection g:B → A; unlabelled | True; explicit enumeration transfer below |
| R-P1 | R:47–83 | Proof by reduction of `\olref[nen]{thm:nonenum-pownat}` | Complete modulo harmless notation R-N1 |
| R-E2 | R:103–106 | All sets of pairs of positive integers; unlabelled | True; explicit solution below |
| R-E3 | R:108–112 | `sfr:siz:red:prob:nat-nat`; all functions N₀ → N₀ | True; hinted surjection supplied below |
| R-E4 | R:114–117 | `\Nat^\omega`; unlabelled | True; explicit solution below |
| R-E5 | R:119–125 | Total and partial functions P → {0}; unlabelled | Both claims true; explicit solutions below |
| R-E6 | R:127–132 | All surjections P → B; unlabelled | True; explicit solution below |
| R-E7 | R:134–136 | Real numbers; unlabelled | True; explicit solution below |

R contains no new theorem environment: R-P1 is an additional proof of N-T2. The two target files contain exactly three proof environments and nine exercise environments. All are covered here.

## Universal checks of the three supplied proofs

### N-T1: Nonenumerability of infinite binary sequences

Let an arbitrary purported enumeration be e:P → B^P, and write s_i = e(i). For every n ∈ P define d(n)=1−s_n(n). Since s_n is total and binary, d is a total binary sequence. For every k ∈ P,

`d(k) = 1 − s_k(k) ≠ s_k(k)`.

Therefore d ≠ s_k for each k, so e omits d. This universally excludes every surjection P → B^P. The constant-zero sequence witnesses nonemptiness, so the correct enumeration criterion yields nonenumerability.

The indices in N:56–59 and 117–125 are correct: i identifies a row/sequence, j identifies a coordinate, and if d were row k the comparison must use coordinate k. Repeated rows do not affect the argument. Infinite sequences are specified by a total pointwise rule; no step presumes that an infinite temporal computation has finished. N:110–115's “and so on” is followed by the fully quantified argument at 117–125, so it is harmless compression.

### N-T2: Nonenumerability of the power set of P

Let Z_i, i ∈ P, be any list of subsets of P. Define D = {n ∈ P : n ∉ Z_n}. This is a subset of P and hence an element of its power set. For arbitrary k ∈ P,

`k ∈ D ⇔ k ∉ Z_k`.

Thus k belongs to exactly one of D and Z_k, so D ≠ Z_k. The list omits D, whatever its entries. The power set is nonempty because it contains ∅, completing the nonenumerability inference.

N:159–175 has the correct membership direction and correct diagonal index. In N:164–166, the explicit bound n ∈ P in the definition itself guarantees D ⊆ P; the added observation about the Z_n being subsets is harmless explanatory redundancy. No choice of a distinguishing point is made across arbitrary pairs: the point for row k is explicitly k.

The visualization at N:179–200 also checks out. Column j records membership of integer j, rather than the j-th element in a compressed listing of a set. Blank entries stand for nonmembership. The four displayed rows respectively include their own diagonal integers 1, 2, and 4 and omit 3; therefore D omits 1,2,4 and contains 3, exactly as N:198–199 says. These finite entries illustrate the universal proof; they do not establish it.

### R-P1: Reduction using characteristic sequences

Define F:𝒫(P) → B^P by F(Z)(n)=χ_Z(n). For any s ∈ B^P the explicitly determined set Z_s={n ∈ P : s(n)=1} satisfies F(Z_s)=s at every coordinate. Hence F is surjective (indeed bijective). If Z_i, i ∈ P, enumerated 𝒫(P), then F(Z_i), i ∈ P, would enumerate B^P: given s, its particular preimage Z_s appears as some Z_i, so s=F(Z_i). This contradicts N-T1.

R:55–58's examples are correct with positive indexing: the positive even integers map to 010101…, ∅ to 000…, and P to 111…. R:63–69 gives the actual inverse construction, and R:71–82 composes it with the assumed enumeration in the correct direction. Apart from R-N1's redundant k, no proof gap was found.

## Universal solutions checking all nine exercises

### N-E1, N:202–204 — The power set of N₀

Given any list A_1,A_2,… of subsets of N₀, set

`D = {m ∈ N₀ : m ∉ A_(m+1)}`.

For each row k ≥ 1, use the coordinate m=k−1. Then k−1 ∈ D iff k−1 ∉ A_k, so D ≠ A_k. This diagonal correctly handles both the zero-based elements and the one-based list. Since ∅ is an element of 𝒫(N₀), the latter is nonempty and the argument establishes nonenumerability.

It would also be valid to use D′={n ∈ P : n ∉ A_n} as a subset of N₀ and omit 0: every row still has its own distinguishing coordinate n. A diagonal need not use every element of the ground set. No missing-zero defect is present in the exercise itself.

### N-E2, N:206–212 — All total functions P → P

Given any list f_1,f_2,… of total functions P → P, define d(n)=f_n(n)+1. This is defined for every n ∈ P and is again positive-integer-valued. For each k, d(k)>f_k(k), so d ≠ f_k. The function space is nonempty, for example because it contains the constant-one function. Thus it is nonenumerable, and d is precisely the explicit witness requested.

This is an assertion about all total functions. Even if the individual rows happened to be computable, their arbitrary set-theoretic enumeration need not be effective, and d need not be computable. No claim about nonenumerability of the set of computable functions is implied.

### R-E1, R:41–45 — Transfer along an injection

Use C for the exercise's set B to distinguish it from the binary alphabet. Suppose g:C → A is injective and C is nonenumerable. Since ∅ is enumerable, C ≠ ∅; the injection then implies A ≠ ∅. Assume for contradiction that A is enumerable, and let a:P → A be a surjection.

The set I={n ∈ P : a(n) ∈ g[C]} is nonempty. Let n₀=min I, and let c₀ be the unique c ∈ C with g(c)=a(n₀). Define b:P → C by

- b(n) is the unique c with g(c)=a(n), when a(n) ∈ g[C];
- b(n)=c₀ otherwise.

Injectivity makes the inverse values unique. For every c ∈ C, surjectivity of a gives some n with a(n)=g(c), and then b(n)=c. Thus b is surjective and contradicts the nonenumerability of C.

The padding by c₀ avoids gaps without requiring an algorithm to filter the enumeration. The least index n₀ is determined by a and g. There is no axiom of choice, no arbitrary infinite family of preimage selections, and no presumption that membership in g[C] is decidable. For the more general assertion that an injection into an enumerable set makes its domain enumerable, an empty domain is handled separately as enumerable by definition.

### R-E2, R:103–106 — All sets of pairs of positive integers

The target is T=𝒫(P×P), the set of **sets of pairs**, not just P×P. Define H:T → 𝒫(P) by

`H(R) = {n ∈ P : (n,1) ∈ R}`.

For every Z ⊆ P, the relation R_Z=Z×{1} belongs to T and H(R_Z)=Z. H is therefore surjective. An enumeration of T would compose with H to enumerate 𝒫(P), contrary to N-T2. This argument does not need an enumeration of pairs or any result from `zig-zag.tex`.

### R-E3, R:108–112 — All total functions N₀ → N₀

Let X=N₀^(N₀). Define H:X → B^P by H(f)(n)=f(n−1) mod 2 for n ≥ 1. The shift is necessary in this chosen formula because the sequence coordinates start at 1 and the function arguments start at 0.

Given s ∈ B^P, define f_s(m)=s(m+1) for all m ∈ N₀. This is a total natural-number-valued function, and for every n ≥ 1,

`H(f_s)(n) = s(n) mod 2 = s(n)`.

So H is surjective, exactly in the direction requested by the hint. If X were enumerable, B^P would be enumerable, contradicting N-T1. No function computability restriction may be inserted into X.

### R-E4, R:114–117 — Infinite natural-number sequences

Write a natural-number sequence as t:P → N₀. Define H(t)(n)=t(n) mod 2. Every binary sequence s is itself a natural-number sequence, and H(s)=s. This is an explicit surjection from N₀^P onto B^P, yielding nonenumerability by N-T1. If sequence positions are instead numbered from 0, conjugate this construction by the fixed index shift. That is a notation convention, not an extra theorem assumption.

### R-E5, R:119–125 — Total and partial functions into {0}

Use P_tot and Q_part for the exercise's function sets, keeping P for positive integers. There is exactly one total function p:P → {0}, namely p(n)=0 for every n. Thus P_tot={p}, and n ↦ p is an enumeration of P_tot.

Under the standard convention that a partial function may have any domain D ⊆ P, including D=∅ and D=P, define H:Q_part → B^P by

`H(q)(n) = 1 if n ∈ dom(q), and 0 otherwise`.

For each s ∈ B^P put D_s={n ∈ P : s(n)=1} and take q_s to be the unique function D_s → {0}. Then H(q_s)=s, so H is surjective and Q_part is nonenumerable. In fact q ↦ dom(q) is a bijection Q_part → 𝒫(P). The nowhere-defined partial function supplies the preimage of the constant-zero sequence; the everywhere-defined zero function supplies the preimage of the constant-one sequence. Definedness, not the always-zero output value, carries the information.

The standard partial-function convention includes total functions. Even an alternative convention restricting to proper domains would not falsify the exercise: force argument 1 to be undefined, encode s(n) by whether argument n+1 is defined, and decode those shifted arguments. That gives a surjection from this smaller partial-function class onto B^P. No such alternative convention is attributed to the source.

The exercise concerns all partial functions, not just partial computable functions. The latter restriction would change the claim and is not authorized by the wording.

### R-E6, R:127–132 — All surjections P → B

Let S be exactly the surjective binary-valued functions. Define H:S → B^P by H(u)(n)=u(n+2). Given arbitrary s ∈ B^P, define

`u_s(1)=0,  u_s(2)=1,  u_s(n+2)=s(n) for every n ≥ 1`.

The first two entries guarantee that u_s is surjective even when s is constant. Thus u_s ∈ S and H(u_s)=s. H is a surjection onto B^P, so S cannot be enumerable. Merely embedding arbitrary binary sequences without these fixed entries would not guarantee membership in S; the construction checks that required hypothesis explicitly.

### R-E7, R:134–136 — Real numbers

Define J:B^P → ℝ by

`J(s) = Σ_(n=1)^∞ 2s(n)/3^n`.

The series exists: its nonnegative partial sums increase and are bounded by Σ 2/3^n=1, so completeness of ℝ gives a limit in [0,1]. To prove injectivity, take distinct s,t and let k be their least differing coordinate. Interchange s and t if necessary so that s(k)=1 and t(k)=0. Absolute convergence and the geometric tail give

`J(s) − J(t) ≥ 2/3^k − Σ_(n=k+1)^∞ 2/3^n = 1/3^k > 0`.

Thus J is injective. Apply R-E1 with C=B^P and A=ℝ: because B^P is nonenumerable, ℝ is nonenumerable. This is a reduction argument with an explicit injection and a proved separation bound.

The use of ternary digits 0 and 2 avoids assuming uniqueness of ordinary binary expansions: the analogous binary series identifies 1000… and 0111…. The source supplies only the exercise, not an erroneous expansion proof; no such error is charged to it. The bound above proves injectivity for the entire binary-sequence domain, including sequences with constant tails.

## Remaining exposition, conventions, and choice accounting

**General reduction direction, R:20–39.** For a surjection F:A → C and nonempty enumerable A with enumeration e:P → A, the composition F∘e is surjective onto C. For any c ∈ C, there exists a with F(a)=c, then an n with e(n)=a; hence (F∘e)(n)=c. This does not choose preimages simultaneously. If A=∅ and a surjection F exists, C=∅ and is enumerable separately. Thus the general preservation claim survives the empty case. To transfer nonenumerability of C to A, the arrow goes from A onto C; an injection goes from C into A, as proved in R-E1.

**Correct wrong-direction example, R:85–95.** The projection g:B^P → B, g(s)=s(1), is surjective: the constant-zero and constant-one sequences witness its two outputs. Its codomain is finite and enumerable. Thus a surjection *from* a nonenumerable set does not establish nonenumerability of its codomain. For a nonsurjective F:A → C, the image of a list covering A is exactly F[A], so it necessarily omits C\F[A]. The surrounding principle is correct; R-F1 is the separate typing error in the subsequent illustration.

**Informal size language, N:30–31.** The quoted word “more” is an informal gloss here. The proofs establish the precise nonenumerability statements without invoking a general comparison or selection principle for arbitrary infinite sets. For the two theorem targets, even the stronger cardinal-size interpretation has explicit witnesses in the needed direction: n ↦ the characteristic sequence of {n} injects P into B^P, and n ↦ {n} injects P into 𝒫(P). Their nonenumerability rules out enumerating them by P. No extra defect is inferred from this informal wording beyond the explicit empty-set overstatement already recorded in N-F1.

**Infinite objects and complement notation.** The diagonals d and D depend on the given list; the overbar does not assert a fixed sequence independent of that list or the complement of one fixed row. Membership in D is obtained by negating the diagonal proposition n ∈ Z_n. Sequences are total functions on their index set, so defining all coordinates by a rule suffices. Finite prefixes alone do not define infinite sequences, which is precisely why R-F1 is an actual error.

**All functions versus computable functions.** There are only countably many finite program descriptions. For a class of functions computed by such programs, assign to each computable function the least code of a program computing it; this is an injection into a countable code set. The subset of codes need not be decidable for this set-theoretic counting argument. Hence the corresponding computable-function classes are enumerable in the chapter's sense. The nonenumerability exercises remain true because they quantify over all indicated functions. No uniform effective enumeration, effective test of definedness, or computable diagonal is claimed or needed.

**Optional versus required choice.** Every constructed family above has an explicit formula. The characteristic-function inverse, the fixed-column relation, the parity encodings, the partial-function domains, and the prefixed surjections have specified preimages. R-E1 uses a unique inverse on the image of an injection and a least available enumeration index, not an arbitrary selection from infinitely many sets. Fixing one element of a known nonempty set would also suffice there and would not require the axiom of choice, but even that discretionary selection was avoided in the supplied proof. Real-series limits use ordinary completeness of ℝ, not a choice of representations for each real. Any general choice axiom would therefore be optional background, not a premise required for these arguments.

## Terminal record

Completed: exact target-byte identities; full mathematical-scope inventory; universal checks of all supplied proofs; explicit solutions of every exercise; concrete witnesses for the two exposition errors; separate classification of notation and harmless compression. No substantive theorem-proof gap or false exercise was confirmed. No plausible doubt has been promoted to a finding.

The audit is complete. The source remains unchanged. The only proposed source corrections are N-F1, R-F1, and the optional notation clarification R-N1, all described here for the owner's later work. No translation, human-review prerequisite, publication action, further audit pass, or pending task action is introduced.
