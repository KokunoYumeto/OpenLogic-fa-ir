Public rendering: the implementation-only input-file locator is replaced and whitespace added after two set-builder colons; mathematical content is unchanged. Original independent report SHA-256: abc7ccc8357cfd3391b8380d3c68a352cac0ea0b390a9ef4e11b36ece47d26de. This challenge assesses source mathematics, not Persian linguistic quality.

# Independent mathematical source review

Completed 2026-09-12. This bounded review checks the three requested mathematical questions against frozen English. It contains no assessment of Persian wording or translation choices.

The restriction passage needs an explicit convention caveat: the two operations can produce different sets of pairs. The graph proposition is correct with its two stated hypotheses; making its use of existence explicit clarifies an abbreviated proof. All four function-kind examples are correct. Confidence in these findings is high because each follows directly from the displayed definitions, finite counterexamples, or explicit witnesses below; this is an editorial confidence judgment, not a calibrated probability.

## Frozen source and exact locations

Read from frozen English at commit `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Paths below are relative to `content/sets-functions-relations/`; line numbers refer to the frozen files.

| File | Passages used |
| --- | --- |
| `relations/operations.tex` | 28–32: restriction and application; 35–47: successor example |
| `functions/functions-relations.tex` | 24–39: graph, extensionality, and “functional”; 42–58: proposition and proof; 78–100: restriction, image, range, and comparison with relation operations |
| `functions/function-kinds.tex` | 29–48: surjectivity and changing the codomain to the range; 64–74: injectivity; 76–95: four examples; 112–115: bijectivity |

Logical-text SHA-256 identities, computed from the `git show` lines encoded as UTF-8 with LF separators and one final LF (not asserted to be raw Git blob byte hashes):

```text
relations/operations.tex                 73c8bdb301aca93f687a06a045533d75d30088ae711f5e1dfd577b7864f8d3d5
functions/function-kinds.tex             4d30902b7c66720afabb8b079294106a685aefba0dc02ca10d9921bb554db0ac
functions/functions-relations.tex        e2e46c0270c44b6f54861a4565f3829b1b5f91a7f72dca84046361e5abf622c3
```

## 1. Restriction: a real difference of conventions

The earlier definition is “The restriction of R to A is … R ∩ A²” (`operations.tex`, 28–29). Renaming that restricting set to C, it retains pairs whose **two** coordinates lie in C:

\[
R\cap C^2=\{(x,y)\in R:x\in C\text{ and }y\in C\}.
\]

The later definition explicitly gives a function from C to the original B and retains only the input condition (`functions-relations.tex`, 79–85). Thus, for C ⊆ A,

\[
R_{f|_C}=R_f\cap(C\times B)
=\{(x,f(x)):x\in C\}.
\]

Take precisely A = {0}, B = {1}, f(0) = 1, C = {0}. Regard its graph G = {(0,1)} as a binary relation on U = {0,1}, so G ⊆ U². Both restriction operations can now be compared on the same ambient relation without a typing objection:

\[
G\cap C^2=\{(0,1)\}\cap\{(0,0)\}=\varnothing,
\qquad
R_{f|_C}=\{(0,1)\}.
\]

Here C = A, so function restriction even returns the whole original function, while the earlier relation restriction returns the empty relation. A one-pair graph with distinct input and output already suffices. An empty graph cannot separate these operations, and a one-element ambient set cannot provide the required distinct coordinates.

Generally,

\[
R_f\cap C^2=\{(x,f(x)):x\in C,\ f(x)\in C\},
\]

whose domain is {x ∈ C : f(x) ∈ C}. Consequently,

\[
R_f\cap C^2=R_{f|_C}\quad\Longleftrightarrow\quad f[C]\subseteq C.
\]

This is an equality of graphs; a graph by itself does not encode a chosen codomain. Even when the graphs coincide, the later function restriction is explicitly declared C → B. Merely assuming A = B does not force the equality: C must be closed under f. The earlier successor example restricted to the natural numbers (`operations.tex`, 35–45) does have this closure property, so that example is correct but does not expose the distinction. With C = ∅, the two graphs agree vacuously.

The image operation, in contrast, agrees exactly with the earlier relational application:

\[
R_f[C]=\{y: \exists x\in C\ ((x,y)\in R_f)\}
=\{f(x):x\in C\}=f[C].
\]

The displayed conclusion ran(f) = f[dom(f)] (`functions-relations.tex`, 93–94) is also correct, including for the empty function.

**Editorial finding.** The sentence “These notions are exactly as one would expect” (95–97, within a conditional cross-reference block) is underexplained compatibility prose accompanying a convention switch. It is not a separately stated false theorem or a defective definition of function restriction. If read as asserting that both later operations are literally the earlier relation operations applied to graphs, its restriction component is false, as the counterexample proves. Calling it wholly harmless would miss that concrete discrepancy; calling the function definition or the whole passage mathematically false would overstate it.

Recommended caveat, attached to the function restriction definition or to the concluding comparison:

> Here restriction of a function means restricting its inputs: the graph of f restricted to C is R_f ∩ (C × B), and its codomain remains B. The earlier restriction of a relation, R_f ∩ C², retains pairs with both coordinates in C. These graphs coincide exactly when f[C] ⊆ C. The definition of image agrees with the earlier relational application.

This addresses the precise difference without changing either definition or labeling the valid range identity erroneous.

## 2. Functionality, existence, and the graph proposition

For “functional” in the at-most-one-output sense, let

\[
D=\operatorname{dom}(R)=\{x: \exists y\ ((x,y)\in R)\}.
\]

For each x ∈ D, existence follows from membership in D; functionality gives uniqueness. Therefore R is the graph of the assignment D → ran(R), and also of a function D → B for any specified B containing ran(R). No totality on a larger, arbitrarily preset A follows. Thus the introductory sentence “if a relation is ‘functional’, then it is the graph of a function” (`functions-relations.tex`, 39) is valid on its own domain under this meaning. It does not say that any ambient A works. No definition of “functional” outside the three authorized files was consulted or assumed.

The proposition (`prop:graph-function`, 42–51) explicitly assumes BOTH:

1. If Rxy and Rxz, then y = z: at most one output for each input.
2. For every x ∈ A, some y ∈ B satisfies Rxy: at least one output for each input of the specified A.

Together with R ⊆ A × B, these say exactly that R determines one value in B for every x ∈ A.

Two small counterexamples show why both conditions matter:

- Uniqueness without existence: A = {0}, B = {1}, R = ∅. Hypothesis 1 holds vacuously, but hypothesis 2 fails. R is the graph of a function ∅ → {1}, not a function {0} → {1}. A nonempty version is R = {(0,1)} ⊆ {0,2} × {1}: input 2 has no value.
- Existence without uniqueness: A = {0}, B = {0,1}, R = {(0,0),(0,1)}. Hypothesis 2 holds, but hypothesis 1 fails; no function has this graph.

The printed proof (53–58) starts “Suppose there is a y such that Rxy,” establishes conditional uniqueness, and then calls f well-defined. That argument uses hypothesis 2 implicitly to supply a y for every x ∈ A. Its conditional-uniqueness sentences alone would not establish totality; in the context of the stated hypotheses, the conclusion is correct. Making the existence step explicit is a clarification of omitted reasoning, not a correction of a false proposition or a counterexample to its proof.

A precise expanded proof is:

> Fix x ∈ A. By hypothesis 2 there exists y ∈ B with Rxy, and by hypothesis 1 this y is unique. Define f(x) to be this unique y. This defines a function A → B. For every x ∈ A and y ∈ B, f(x) = y if and only if Rxy, so its graph is R.

If A = ∅, the same reasoning has no inputs to assign and yields the unique empty graph. There is no need to introduce a nonemptiness assumption or a choice principle.

## 3. Four examples, codomain scope, and empty boundaries

All four examples (`function-kinds.tex`, 76–95) are correct. The three source files do not fix whether the natural numbers start at 0 or 1; the proofs below work with either convention. Write m for their least member.

| Map, with domain and codomain both ℕ | Concrete verification |
| --- | --- |
| f(x) = 1 | Not injective: f(1) = f(2) = 1 with 1 ≠ 2. Range = {1}, so it is not surjective onto ℕ: 2 is missing. |
| f(x) = x | Injective because equality of outputs is equality of inputs. Surjective because every y ∈ ℕ has preimage x = y. Hence bijective. |
| f(x) = x + 1 | Injective by cancellation. Range = ℕ ∖ {m}, so m has no preimage. It is not surjective onto ℕ. |
| f(x) = x/2 for even x, and (x+1)/2 for odd x | Both branches give natural-number values. Every y ∈ ℕ has the even preimage x = 2y, so the map is surjective. It is not injective because f(1) = f(2) = 1. |

For the last example, every positive y has exactly the two preimages 2y − 1 and 2y. If 0 ∈ ℕ, zero has the sole preimage 0. This exception does not affect either classification; no branch or quantifier needs correction.

Surjectivity is relative to the declared codomain B: it means ran(f) = B. The source correctly says that a function **induces** a surjection by giving the same assignment the codomain ran(f) (44–48). It does not assert that every f : A → B is already surjective onto B. Changing only the codomain illustrates the distinction:

- The constant example ℕ → {1} becomes surjective, but remains noninjective.
- The successor example ℕ → ℕ ∖ {m} becomes bijective.
- The identity assignment ℕ → ℕ ∪ {a}, for a ∉ ℕ, remains injective but becomes nonsurjective.

Injectivity depends on collisions between inputs; changing to another legitimate codomain containing all outputs does not change those collisions. The source's “at most one” preimage condition (65–66) permits codomain elements with no preimage. Surjectivity adds at least one; bijectivity combines them into exactly one preimage for every codomain element. Functionality, by contrast, gives at most one OUTPUT for each INPUT, and must not be confused with injectivity.

Identifying a function with its graph determines its domain and range, but not a larger specified codomain. For example, {(0,0)} is the same graph for {0} → {0} and {0} → {0,1}; only the first declaration is surjective. The shared-domain-and-codomain qualification in the source's extensionality passage (`functions-relations.tex`, 33–37) is sufficient and correct. It must not be used to infer that the graph alone recovers the codomain.

The empty cases follow directly from the quantifiers:

| Domain A and codomain B | Existence and classification |
| --- | --- |
| A = ∅, B = ∅ | Exactly one function, with empty graph. It is injective and surjective, hence bijective, vacuously. |
| A = ∅, B ≠ ∅ | Exactly one function, with empty graph and range ∅. It is injective, but not surjective: each y ∈ B has no preimage. |
| A ≠ ∅, B = ∅ | No total function A → B exists. The empty relation is functional but fails the graph proposition's existence hypothesis. The vacuity of a surjectivity formula over B does not create a function. |

Thus the construction A → ran(f) remains a surjection when A is empty: it is then ∅ → ∅. Function restriction to C = ∅ always yields ∅ → B, whose surjectivity still depends on whether B is empty; f[∅] = ∅ in every case.

## Completion

All three requested challenges are resolved in this report. No mathematical counterexample was found to the graph proposition, its conclusion under both hypotheses, the four examples, or the range identity. The concrete restriction discrepancy supports the scoped caveat above, and the proof supports an explicit existence sentence. No source or translation edits were made. No mathematical decision remains pending for this bounded review.
