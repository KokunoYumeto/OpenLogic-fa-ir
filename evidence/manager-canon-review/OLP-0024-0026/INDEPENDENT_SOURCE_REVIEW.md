# Independent mathematical review: inverses, composition, and partial functions

Date: 2026-09-12. Status: complete for the requested source review. No human review or response is a prerequisite for using these findings.

## Source identity and review boundary

The only English source read was the three requested blobs from the designated `source_repo.git`, at frozen commit `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. All paths below are relative to that repository, with prefix `content/sets-functions-relations/functions/`.

| File | Git blob object ID | Source lines |
| --- | --- | --- |
| `inverses.tex` | `ac0fc68e981f0200816aa0adf3ccb138b68eeb6d` | 1–177 |
| `composition.tex` | `fb74e6199d824e0fca91e3395a522269fdadef9c` | 1–67 |
| `partial-functions.tex` | `a3c8ea8f74047333b67bf00f6c8c9a7d1ace9bcf` | 1–75 |

These are Git object hashes, not SHA-256 file digests. The commit was verified to be a commit object; each blob was resolved and read directly through Git without checking out or modifying the source. Line references refer to those frozen blobs.

This independent review covers source mathematics only. It does not certify Persian wording or a compiled reader. The manager separately checked the composition macro and diagram-source identity, recorded in FIGURE_AND_MACRO_IDENTITY.json.

## Findings and immediate actions

| ID | Source location | Classification | Action |
| --- | --- | --- | --- |
| M1 | `inverses.tex` 62–84 | Genuine source error when empty sets are admitted | Add `A ≠ ∅` to the left-inverse proposition and proof; fix one element of `A` once; add the labelled empty-case note below. |
| M2 | `inverses.tex` 91–114 | Correct, with an explicit Choice qualification | Preserve the existing footnote. The unrestricted theorem for all surjections is equivalent to AC over ZF; the stated exceptions require no AC. |
| M3 | `inverses.tex` 127–151, 154–174 | Correct; optional explanation | Distinguish an inverse on the image from a total left inverse on the original codomain. Bijection inversion and inverse uniqueness require no AC. |
| M4 | `composition.tex` 15–21, 24–49, 52–65 | Correct at the stated mathematical level | Preserve first `f`, then `g`; preserve range inclusion and graph-product order. No added nonemptiness assumptions are needed. |
| M5 | `partial-functions.tex` 42–47 | Correct; useful domain clarification | For an injective partial map, state actual inverse domain `ran(f)` and range `dom(f)`. No AC or ambient nonemptiness is needed. |
| M6 | `partial-functions.tex` 20–34, 50–72 | Correct; useful explanation | Distinguish right uniqueness from seriality, and totality from surjectivity. Empty relations obey the same definitions. |

Exactly one mathematical correction is established in the permitted source. The remaining recommendations expand explanations; they are not additional source defects. Confidence in M1 and the proofs below is high because there is an explicit counterexample and direct set-theoretic derivations. This is an editorial assessment, not a calibrated probability.

## 1. Left inverses: the precise failure and repair

### Counterexample and exact criterion

The proposition at `inverses.tex` 63–65 asserts that injectivity alone gives a total function `g : B → A` satisfying `g(f(x)) = x`. Take `A = ∅`, `B = {0}`, and the unique empty function `f : ∅ → {0}`. It is injective, since there are no domain elements violating injectivity. A left inverse would have to be a total function `{0} → ∅`, which does not exist. Although the displayed inverse identity has no instances to check, the required function still has to exist.

The proof's unsupported step is at lines 73–74: it selects an element `a ∈ A` without a nonemptiness hypothesis. For a given total function `f : A → B`, the exact statement, provable in ZF without AC, is

`f has a total left inverse ⇔ f is injective and (A ≠ ∅ or B = ∅).`

Necessity: if `g ∘ f = id_A`, then `f(x) = f(x')` implies `x = g(f(x)) = g(f(x')) = x'`. If `A = ∅` and `g : B → A` exists, `B` must be empty. Sufficiency: use the construction below when `A ≠ ∅`; when `B = ∅`, existence of the original total `f` forces `A = ∅`, and its empty inverse works.

| Ambient sets | Total `f : A → B` | Injectivity / surjectivity | Inverses |
| --- | --- | --- | --- |
| `A = ∅`, `B = ∅` | Unique empty function | Both | Unique empty function is both a left and a right inverse. |
| `A = ∅`, `B ≠ ∅` | Unique empty function | Injective, not surjective | No total function `B → A`, hence no total left, right, or two-sided inverse. |
| `A ≠ ∅`, `B = ∅` | No total function | Not an instance of any theorem about a given total `f` | Do not call a nonexistent map a counterexample. |
| `A ≠ ∅`, `B ≠ ∅` | Ordinary case | Depends on `f` | Left inverses exist exactly for injections, without AC. Right inverses imply surjectivity; their existence for all surjections uses AC. |

For an already injective `f`, the only failure of left-inverse existence is `A = ∅` with `B ≠ ∅`. The empty-to-empty case is valid but is not covered by a repaired proposition that explicitly assumes `A ≠ ∅`; the note should restore it explicitly.

### Validated replacement proposition and proof

Proposition: If `A ≠ ∅` and `f : A → B` is injective, there is a left inverse `g : B → A` such that `g(f(x)) = x` for every `x ∈ A`.

Proof: Fix one `a₀ ∈ A`, possible because `A ≠ ∅`. For `y ∈ B`, define `g(y)` to be the unique `x ∈ A` such that `f(x) = y` if `y ∈ ran(f)`, and define `g(y) = a₀` otherwise. In the first case existence follows from membership in the range and uniqueness from injectivity. In the second case the fixed value belongs to `A`. Thus every `y ∈ B` receives exactly one value in `A`. For `x ∈ A`, the value `f(x)` lies in the range, whose unique preimage is `x`, so `g(f(x)) = x`.

Equivalently, the graph is the set

`{(y,x) ∈ B × A : f(x) = y} ∪ ((B \ ran(f)) × {a₀}).`

The two pieces have disjoint input sets. This explicitly verifies existence and functionality. Selecting a single witness `a₀` from one nonempty set is ordinary existential reasoning in ZF, not AC; that same element supplies every value outside the range. Unique preimages also require no AC.

Suggested labelled note, editorial identifier `note:left-inverse-empty-sets`, immediately following this proof:

> Empty sets. If `A = B = ∅`, the unique empty function is its own inverse. If `A = ∅` and `B ≠ ∅`, the empty function `A → B` is injective but has no left inverse `B → A`, since no such total function exists. If `A ≠ ∅` and `B = ∅`, no total function `A → B` exists. Consequently an injective total function has a left inverse exactly when `A ≠ ∅` or `B = ∅`.

The identifier is proposed for the edition's normal label mechanism; this review has not inspected a global label inventory or compiled a TeX wrapper. The mathematical repair is fully validated. Adding only a proof assumption while leaving the proposition unchanged would not repair the statement. A vague instruction to choose an element only when needed would likewise not repair the counterexample.

The converse exercise at lines 86–89 is correct without any new hypothesis: its proof is the injectivity argument above and applies also to empty sets.

## 2. Right inverses, Choice, and inverse types

### What the footnote actually establishes

At `inverses.tex` 98–111, the proof selects one preimage from each fiber, and the footnote expressly states that the general proposition assumes the Axiom of Choice. This is an accurate qualification, not a concealed logical gap.

For a surjection `f : A → B`, put `F_y = {x ∈ A : f(x) = y}`. Every `F_y` is nonempty. A right inverse is precisely a function `h` on `B` such that `h(y) ∈ F_y` for every `y`. AC gives such a selection, and therefore `f(h(y)) = y`.

Conversely, suppose every surjection has a right inverse. For any set-indexed family `(X_i)_{i∈I}` of nonempty sets, form the disjoint union `E = {(i,x) : i ∈ I and x ∈ X_i}` and the surjection `p : E → I`, `p(i,x) = i`. A right inverse `s` has `s(i) = (i,c(i))` with `c(i) ∈ X_i`, yielding a choice function. This proves that the unrestricted right-inverse theorem is equivalent to AC over ZF. If `I = ∅`, all functions involved are empty and no exceptional choice is necessary.

The source's examples of cases not requiring AC are valid:

- If `A = ℕ`, set `h(y) = min F_y`; every nonempty subset of the natural numbers has a least element.
- If `A` is finite, fix a finite ordering of this one set and choose the first member of each fiber. Its image `B` is finite as well. No AC is needed.
- If `f` is bijective, every fiber is a singleton. Reverse the graph directly, as below.

More generally, an already well-ordered `A` suffices. This does not assert that every set admits a well-order without AC. Nor should the natural-number example be replaced by the different assertion that arbitrary fibers indexed by a countable `B` always admit a selection in ZF.

The converse exercise at lines 116–119 requires no AC: for any `y ∈ B`, the value `h(y) ∈ A` witnesses `y = f(h(y))`, so `f` is surjective. A right inverse is itself injective: equality of two of its values implies equality of their images under `f`.

If a surjection has `A = ∅` or `B = ∅`, both are empty: surjectivity forces `B = ∅` when `A = ∅`, and totality forces `A = ∅` when `B = ∅`. The unique empty right inverse works. There is no missing nonemptiness hypothesis here.

### Bijections and injections inverted on their images

For a bijection `f : A → B`, define

`G = {(y,x) ∈ B × A : f(x) = y}.`

Surjectivity supplies an output of `G` at each `y ∈ B`, and injectivity makes it unique. Thus `G` is the graph of a total function `f⁻¹ : B → A`, constructed as a subset of `B × A` in ZF. Both equations `f⁻¹(f(x)) = x` for `x ∈ A` and `f(f⁻¹(y)) = y` for `y ∈ B` follow immediately. Every `x ∈ A` is attained by `f⁻¹` at `f(x)`, so `ran(f⁻¹) = A`. This includes `A = B = ∅` and requires no appeal to the corrected nonempty-domain proposition or to AC.

For an injective total `f : A → B` that is not necessarily onto `B`, its corestriction `f' : A → ran(f)` is bijective. Its canonical inverse is

`(f')⁻¹ : ran(f) → A`, with domain `ran(f)` and range `A`.

That is exactly the construction described at lines 145–151. It exists even when `A = ∅` and `B ≠ ∅`: it is then the empty function `∅ → ∅`. It is not a total function on the original nonempty `B`. Extending it to a total left inverse on `B` requires the condition established in section 1.

| Construction | Inputs where the inverse is defined | Actual range | Choice requirement |
| --- | --- | --- | --- |
| Two-sided inverse of bijective total `f : A → B` | `B` | `A` | None |
| Canonical image inverse of injective total `f : A → B` | `ran(f)` | `A` | None |
| Total left inverse of an injection, when it exists | `B` | `A` | None; one fixed element suffices outside the image when `A ≠ ∅` |
| Right inverse of a surjection, when selected | `B` | A subset `h[B] ⊆ A` on which `f` is bijective onto `B` | AC for the unrestricted existence theorem; particular selections may be definable without it |
| Canonical inverse of injective partial `f : A ⇀ B` | `ran(f)` | `dom(f)` | None |

Total left inverses need not be unique outside `ran(f)`. For example, for the inclusion `{0,1} → {0,1,2}`, a left inverse fixes `0,1` and may send `2` to either one. Right inverses need not be unique either: the constant surjection `{0,1} → {0}` admits either preimage as the selected value. These facts do not contradict uniqueness of a two-sided inverse.

For lines 154–174, if `g` is a left inverse and `h` is a right inverse of the same `f`, then for every `y ∈ B`,

`g(y) = g(f(h(y))) = h(y).`

Hence `g = h`, including when `B = ∅`, and two-sided inverse uniqueness follows. No Choice or nonempty-set assumption occurs in this argument.

## 3. Composition: order, existence, graph, and exercises

### Order and domain requirement

The order is explicit at `composition.tex` 16–17, 29–31, and 42: first apply `f`, then `g`, obtaining `g(f(x))`. The caption at line 34 calls this `g ∘ f`. Accordingly the expression `\comp{f}{g}` in this source denotes that mathematical operation. The example at lines 46–49 is correct: for `f(x) = x+1` and `g(x) = 2x`, `(g ∘ f)(x) = 2(x+1)`. The reversed composite would be `2x+1`.

For total `f : A → B` and total `g : D → C`, the expression `g(f(x))` defines a total function on all of `A` exactly when `ran(f) ⊆ D = dom(g)`. Necessity follows because every value actually reached by `f` must be an admissible input for `g`; sufficiency follows by applying the two total functions successively. The source states this inclusion at lines 18–19. It does not require equality of the range and the next domain.

In its displayed definition, `g : B → C`, so the condition follows automatically from `ran(f) ⊆ B`. More generally, even the declared codomain of `f` need not be contained in `dom(g)` if all actual outputs are: `f : {0} → {0,1}`, `f(0)=0`, composes on all of `{0}` with `g : {0} → {0}`, `g(0)=0`.

If range inclusion fails, the relative product still exists as a relation and determines a partial composite with domain

`{x ∈ dom(f) : f(x) ∈ dom(g)}`.

It is not a total function on the whole declared input set. For example, if `f : {0} → {0,1}` has `f(0)=1` and `g` is defined only at `0`, the partial composite has empty domain. Explaining this distinction is an expansion of the source's discussion of total functions, not a defect in its inclusion requirement.

### Relative-product calculation

Writing relative product in traversal order, first `R`, then `S`, means

`R | S = {(x,z) : ∃y ((x,y) ∈ R and (y,z) ∈ S)}.`

For the functions in the exercise at lines 63–64 and `x ∈ A`, `z ∈ C`,

`(x,z) ∈ R_f | R_g`

`⇔ ∃y ∈ B (f(x) = y and g(y) = z)`

`⇔ g(f(x)) = z`

`⇔ (x,z) ∈ R_(g∘f).`

This proves the requested graph equality under that explicitly stated convention. Relation traversal order `R_f | R_g` and function notation `g ∘ f` describe the same operation; their written orders do not constitute a reversal error. The referenced relation chapter was not among the three permitted files, so its separate definition was not inspected. Neither that dependency nor the rendered macro or diagram is represented here as independently verified. No contrary convention or source defect is evidenced in the permitted files.

### Exercise proofs, with empty cases

Injectivity (lines 53–54): if `g(f(x)) = g(f(x'))`, injectivity of `g` gives `f(x) = f(x')`, and injectivity of `f` gives `x = x'`. Thus `g ∘ f` is injective.

Surjectivity (lines 58–59): fix any `z ∈ C`. Surjectivity of `g` gives a `y ∈ B` with `g(y)=z`; surjectivity of `f` gives an `x ∈ A` with `f(x)=y`. Hence `(g ∘ f)(x)=z`. This is existential reasoning for each fixed `z`, not the selection of a single function of witnesses for all `z`; no AC is needed.

Both proofs remain valid for empty sets. If `A = ∅`, any well-typed composite is empty and injective; it is onto `C` exactly when `C = ∅`. If both original functions are surjective and `A = ∅`, first `B = ∅` and then `C = ∅`, so the surjectivity conclusion still holds. If `B = ∅`, totality of `f` forces `A = ∅`. If `C = ∅`, totality of `g` forces `B = ∅` and hence `A = ∅`. No extra nonemptiness assumptions belong in these exercises.

Do not strengthen them to incorrect converses: an injective composite forces `f` injective, but need not make `g` injective on all of `B`; a surjective composite forces `g` surjective, but need not make `f` onto `B`. A single example witnesses both failed strengthenings: take `A=C={0}`, `B={0,1}`, `f(0)=0`, and `g(0)=g(1)=0`. The composite is bijective, but `g` is not injective and `f` is not surjective.

## 4. Partial inverses and graphs

### Exact interpretation of the inverse exercise

For `f : A ⇀ B`, write `D = dom(f) ⊆ A` for its actual domain and `I = ran(f) ⊆ B`. This follows the source's explicit domain definition at `partial-functions.tex` 21–27. In formulas involving partial values, interpret `f(x)=y` as asserting that `f(x)` is defined and equals `y`. This makes explicit the convention already used in the exercise and graph definition.

The exercise at lines 43–47 defines `g(y)` only when the fiber

`F_y = {x ∈ D : f(x)=y}`

has exactly one element. Consequently, for arbitrary partial `f`,

`dom(g) = U = {y ∈ I : F_y is a singleton}`,

`ran(g) = {x ∈ D : F_(f(x)) = {x}}`,

and the graph is

`R_g = {(y,x) ∈ B × A : (x,y) ∈ R_f and ∀x' ∈ A ((x',y) ∈ R_f ⇒ x'=x)}.`

This defines a partial function in ZF without AC: the graph keeps exactly the reversed pairs whose corresponding fiber has a unique element. For `y ∈ U`, one always has `f(g(y))=y`. The resulting `g` is itself injective, since `g(y)=g(y')=x` implies `y=f(x)=y'`.

If `f` is injective on its actual domain, every nonempty fiber is a singleton. Hence `U=I`, `R_g` is the full converse of `R_f`, `dom(g)=I`, and `ran(g)=D`. For each `x ∈ D`, the unique preimage of `f(x)` is `x`, so `g(f(x))=x`. For each `y ∈ I`, the definition of `g(y)` gives `f(g(y))=y`. Both nested expressions are defined at precisely the inputs asserted in the exercise.

Equivalently, `f`, restricted and corestricted, is a bijection `D → I`; the canonical partial inverse is its bijective inverse `I → D`, regarded as a partial map `B ⇀ A`. The compositions are partial identities: `g ∘ f` is the identity on `D`, and `f ∘ g` is the identity on `I`. They are identities on all of `A` and `B` only when `D=A` and `I=B`, respectively. In particular, `g` is total on its ambient input set `B` exactly when `I=B`, and its range is all of `A` exactly when `D=A`.

This inverse requires no nonemptiness assumption. The empty graph is an injective partial function for all ambient `A,B`, and its canonical inverse is again the empty graph, with both actual domain and range empty.

The injectivity condition is material. If `A={0,1}`, `B={b}`, and `f(0)=f(1)=b`, the exercise's `g` is undefined at `b`, because the fiber has two elements. Thus neither `g(f(0))=0` nor the claimed identity on all of `ran(f)` would be valid after dropping injectivity. This is a counterexample to a possible mistranslation or strengthening, not to the actual conditional exercise.

For a nonempty example demonstrating the domain distinction, let `A={0,1}`, `B={b,c}`, with `f(0)=b` and `f(1)` undefined. Then `dom(f)={0}`, `ran(f)={b}`, `g(b)=0`, and `g(c)` is undefined. The inverse's actual range is `{0}`, not the whole ambient `A`.

The canonical inverse is unique because its graph and its undefined cases are prescribed. The two identity equations alone, restricted to `D` and `I`, do not forbid additional values off `I`. In the last example, extending `g` by `g(c)=1` preserves those restricted equations. Therefore any expanded uniqueness statement should retain the converse-graph definition or the exact domain `I`; do not infer uniqueness among arbitrary partial extensions from the restricted equations alone.

### Functionality, injectivity, seriality, and totality

The graph condition at lines 59–60 is right uniqueness:

`∀x ∈ A ∀y,y' ∈ B ((x,y) ∈ R and (x,y') ∈ R ⇒ y=y').`

It permits at most one output at each input, including none. For each `x` with an output, uniqueness permits us to assign that output; at the other inputs the function is undefined. The resulting partial function has graph exactly `R`. For fixed ambient sets `A,B`, it is the unique partial function with that graph: any such function has the same defined inputs and the same values. No AC is needed, because outputs are unique wherever they exist. The graph alone does not recover unspecified ambient sets; the same empty graph can be typed using many different ambient pairs.

Injectivity is the different, left-uniqueness condition

`∀x,x' ∈ A ∀y ∈ B ((x,y) ∈ R and (x',y) ∈ R ⇒ x=x').`

Seriality here means `∀x ∈ A ∃y ∈ B ((x,y) ∈ R)`, exactly as explicitly defined at lines 63–64. For a right-unique relation, seriality holds if and only if the induced partial function is total on `A`. The source states the forward implication, which is correct; adding the converse is a straightforward explanation.

These conditions must not be conflated:

- The relation `{(0,0),(0,1)} ⊆ {0} × {0,1}` is serial but not right unique, and therefore is not a partial-function graph.
- The empty relation on `{0} × {0}` is right unique but not serial, and defines an everywhere-undefined partial function.
- The graph `{(0,0)} ⊆ {0} × {0,1}` is right unique and serial, hence total, but its function is not onto `{0,1}`. Surjectivity quantifies over the output set, unlike seriality.
- The graph `{(0,0),(1,0)} ⊆ {0,1} × {0}` is right unique and serial but not injective. Functionality does not mean distinct inputs have distinct outputs.

### All empty-graph cases

For `R=∅ ⊆ A × B`, right uniqueness and left uniqueness are always true, the induced partial function has `dom(f)=ran(f)=∅`, and seriality holds exactly when `A=∅`.

| Ambient sets for the empty partial map | Total on `A`? | Is the empty graph serial from `A`? | Canonical inverse total on `B`? |
| --- | --- | --- | --- |
| `A=∅`, `B=∅` | Yes | Yes | Yes |
| `A=∅`, `B≠∅` | Yes | Yes | No |
| `A≠∅`, `B=∅` | No | No | Yes |
| `A≠∅`, `B≠∅` | No | No | No |

In all four rows the partial map and its canonical inverse exist, are injective on their actual domains, and satisfy the exercise's two identities on the empty actual domain and range. In the third row there is a valid partial function `A ⇀ ∅`, although there is no total function `A → ∅`. In the second row the empty function `∅ → B` is total even though it is not onto nonempty `B`. These are consequences of the definitions, not exceptions requiring new hypotheses.

## Verification and completion record

The report's conclusions rest on the general proofs and explicit counterexamples above. As a separate deterministic check, an in-memory exhaustive enumeration covered every carrier size from 0 through 3, without creating scripts or other infrastructure. All checks passed:

| Finite check | Instances |
| --- | --- |
| Total functions: exact left-inverse criterion; right-inverse existence versus surjectivity in the finite setting; canonical bijective inverses | 60 |
| Existing left/right inverse pairs: equality | 10 |
| Composable total-function pairs: injectivity, surjectivity, and graph-relative-product equality | 1,678 |
| Partial functions: unique-preimage construction; inverse equations and domain/range for injections | 144 |
| Binary relations: reconstruction when right unique; seriality versus totality; empty-relation boundary | 689 |

Finite enumeration does not establish any assertion about infinite choice; those assertions are supported by the explicit ZF/AC arguments in section 2. Source identity and numbered passages were read from the frozen Git blobs. No TeX or linguistic QA is claimed.

Completed: all four requested mathematical challenges, the validated repair text and labelled note, full empty-case classifications, Choice distinctions, graph proofs, exercise proofs, counterexamples, and defect-versus-expansion classification. No mathematical issue remains unresolved within this source scope. No source or translation file was edited.

Next actionable integration: apply M1 in the ongoing edition, using the replacement proposition, proof, and labelled note in section 1. Preserve the existing Choice qualification and the valid formulas in M2–M6. Use the optional expansions where they help explain actual domains or prevent ambiguity. Integration into the edition belongs to the ongoing revision, outside this report's two-file write boundary; it is not a human-dependent hold on this completed review.
