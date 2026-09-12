# Independent mathematical/source audit: OLP0037–OLP0040

Completed: 2026-09-12. Status: this finite audit is complete.

The theorem statements and all eleven active exercises in these four files are mathematically valid in their ordinary classical set-theoretic setting. This audit confirms three previously recorded defects and identifies three additional active defects: an unrestricted characterization of non-enumerability that fails for finite sets, a claim that a surjective image list is already a bijective enumeration, and four missing memberships in an illustrative array. None refutes either diagonal theorem or the particular characteristic-sequence reduction.

Confidence is editorial judgment supported by the stated evidence, not a probability. Recommendations are confined to this report; no source, translation, reader, or production artifact was changed. Nothing is awaiting human review.

## Scope, exact identities, and method

Authority is commit `9620cc73f9c8e0ad003c514a5d3748f29611c4c0` in the bare repository specified in the private task input. Exactly these four source blobs were read completely, including editorial environments and comments, using bounded, path-specific `git show --no-ext-diff --no-textconv COMMIT:PATH`. Their total size is 18,821 bytes. No neighboring source, manager candidate, translation, canon, or historical task artifact was inspected.

All source paths below are relative to `content/sets-functions-relations/size-of-sets/`. Line numbers are one-based physical lines of the frozen blobs. SHA-256 hashes were computed from raw `git show` byte streams before decoding or adding line numbers; Git object IDs identify the corresponding blobs.

| Unit | File | Bytes | Lines | Git blob ID (SHA-1) |
| --- | --- | ---: | ---: | --- |
| OLP0037 | `schroder-bernstein.tex` | 1,998 | 53 | `d2991de0a022b5dc45023eab8b325687389c62f5` |
| OLP0038 | `enumerability-alt.tex` | 4,749 | 135 | `5831c156510ef82d8c2fd86931ef804c420415a6` |
| OLP0039 | `non-enumerability-alt.tex` | 6,574 | 162 | `e5d08be5a2ea95a2102a36b405781e94ab285611` |
| OLP0040 | `reduction-alt.tex` | 5,500 | 140 | `09807d97768d2d474a89e31bf660f4abcd03e069` |

Raw-content SHA-256:

```text
OLP0037  7b99b3e032e24e425383734ce80ad9a5cc37d018c09205e02f37b927d50bb56a
OLP0038  9a9060e57403586c0f8a81353c1d9c81049869e486b4dc032fbf32542023ba8f
OLP0039  a075f6c63879101314fb20fa493acfb38d78ff24095bb55914f2af4527e1ad3e
OLP0040  f7717d8394048096cf7a65bc87a1a1ed15861cdfb8c7edb23429d5256d954d11
```

The sole comparison record was read in full:

`manager source-audit registry: source-audits/2026-09-04-size-of-sets/FINDINGS.json`

Its size is 12,592 bytes and SHA-256 is `9b6e836c8432eb75d331913983603796d6557da6ec3ad71b846b2a248374cd07`. All ten IDs, `OLSIZ-001` through `OLSIZ-010`, were compared for duplication. Its OLP0039/0040 source hashes exactly match this audit. Other-file claims in that record were used only to compare defect identities; those other source files and the record's translation claims were not independently audited. Instructions embedded in the comparison record did not expand this task.

The identifiers `IMR-20260912-01` through `-03` below are local report identifiers, not additions to the shared registry. No TeX or Lean process, external research/publication, other-task message, new agent, cleanup, or workspace-wide Git operation was used.

## Confirmed existing defects

### OLSIZ-008 — reversed meaning of the two indices

Location: OLP0039, `non-enumerability-alt.tex`, lines 64–66; controlling array lines 69–74 and conclusion lines 93–95.

The prose calls $s_n(m)$ “the $n$th digit of the $m$th string.” The list, row labels, function notation, and later conclusion require the **mth digit of the nth string**. For example, take the zeroth string to be `01000…` and the first to be `00000…`. The row convention gives $s_0(1)=1$, whereas the reversed prose identifies this with the zeroth digit of the first string, which is 0.

Minimal correction: interchange “$n$th” and “$m$th” in the digit/string description, retaining the array and formulas. This is an erroneous index description; diagonal entries $s_n(n)$ themselves are unchanged by transposition, so the diagonal argument remains sound. Editorial confidence: high, fixed by the off-diagonal entries and the proof's conclusion. Deduplication: exactly `OLSIZ-008`; no new ID.

### OLSIZ-009 — one bit-flip direction is repeated

Location: OLP0039, lines 80–84; controlling cases lines 86–90.

The verbal instruction repeats “every $1$ to a $0$” and omits changing 0 to 1. The cases correctly define $d(n)=1-s_n(n)$. Merely changing ones to zeros does not ensure a different string: an injective list can have $s_0=000\ldots$ and, for each $n\geq1$, $s_n$ with its unique 1 at position $n+1$. Its diagonal is all zeros; leaving those zeros unchanged reproduces $s_0$.

Minimal correction: change the second flip instruction to “every $0$ to a $1$.” The formula and formal disagreement argument need no correction. Editorial confidence: high, by formula comparison and counterexample. Deduplication: exactly `OLSIZ-009`.

### OLSIZ-010 — unbound output index

Location: OLP0040, `reduction-alt.tex`, lines 52–54; controlling inverse construction lines 63–72.

The definition names $f(N)$ as $s_k$ without defining or binding $k$. This is a notation defect, not a failure to specify the intended characteristic sequence: the component conditions uniquely determine a binary sequence for each $N$.

Minimal correction: use “the string $s$ such that $s(n)=1$ iff $n\in N$, and $s(n)=0$ otherwise,” or define $f(N)(n)$ directly. Existence follows by assigning exactly one of 0 and 1 at each natural-number coordinate; uniqueness follows by pointwise equality. Editorial confidence: high, because the coordinate rule supplies the exact repair. Deduplication: exactly `OLSIZ-010`, not a new occurrence of `OLSIZ-004` in this file.

## Additional active defects

### IMR-20260912-01 — absence of a bijection with the naturals does not characterize non-enumerability for arbitrary sets

Location: OLP0039, lines 26–31; related general-method explanation lines 33–37. Governing definition: OLP0038, lines 39–43 and 57–61.

Classification: mathematical error in the unrestricted explanatory equivalence. The subsequent theorems remain true.

The phrase “to say that $A$ is nonenumerable is to say that there is no bijection” $\mathbb N\to A$ omits the infinite-set qualification. Under the actual definition every finite set is enumerable. In particular, $A=\{a\}$ is enumerable via a bijection $\{0\}\to A$, but there is no bijection $\mathbb N\to A$. There is nevertheless a surjection $\mathbb N\to A$, namely the constant function. Thus absence of a bijection and the following “no function … exhausts all of $A$” are not equivalent for arbitrary nonempty $A$.

The empty case also matters: $\varnothing$ is explicitly enumerable, while there is neither a bijection nor a surjection $\mathbb N\to\varnothing$. Accordingly, merely showing “no function $\mathbb N\to A$ is surjective” is insufficient for non-enumerability unless $A\ne\varnothing$ is established.

Minimal correction: begin the bijection characterization with “For an infinite set $A$.” Alternatively use the exact general characterization “$A$ is non-enumerable iff $A\ne\varnothing$ and no surjection $\mathbb N\to A$ exists.” Both diagonal targets are nonempty and infinite, so this changes explanatory scope, not their conclusions.

Deduplication: no matching defect among `OLSIZ-001`–`010`; this is separate from the known index and bit-flip errors. Editorial confidence: high, witnessed by the singleton and empty set.

### IMR-20260912-02 — a surjective image list need not be a bijective enumeration

Location: OLP0040, lines 34–38; application lines 74–80. Governing definition: OLP0038, lines 39–43.

Classification: false general assertion about the constructed list, with a missing justification in the particular proof. The enumerability implication itself is correct.

The text says that if $x_1,x_2,\ldots$ enumerates $A$ and $f:A\to B$ is surjective, then $f(x_1),f(x_2),\ldots$ enumerates $B$. A surjection may introduce repetitions, while an enumeration here must be bijective. Counterexample with both sets infinite: enumerate $A=\mathbb N$ increasingly and let $f(n)=\lfloor n/2\rfloor$ onto $B=\mathbb N$. Its image list is $0,0,1,1,2,2,\ldots$, not an enumeration under that definition. A finite-target counterexample takes $B=\{0\}$ and $f$ constant.

Minimal general correction: say the image list contains every element of $B$, and deleting repeated values while keeping their first occurrences gives an enumeration. Equivalently invoke OLP0038's surjection characterization, handling the empty case separately. For a finite enumeration use its finite index set; for an infinite enumeration use $\mathbb N$. First-occurrence indices form an ordered subset of that domain, so reindexing gives a finite initial segment or $\mathbb N$. If $A$ is empty, surjectivity forces $B$ empty, already enumerable. No choice principle is needed.

In this particular proof the characteristic map is actually injective as well as surjective. If $N\ne M$, some $n$ belongs to exactly one, so $f(N)(n)\ne f(M)(n)$. Adding this observation before lines 74–80 proves that the displayed list is bijective. The source proves surjectivity explicitly but omits that observation. Alternatively, the general first-occurrence correction suffices.

Deduplication: no matching defect in `OLSIZ-001`–`010`; `OLSIZ-010` concerns the unbound symbol, a different issue. Editorial confidence: high, by the repeated-value counterexample and direct injectivity proof.

### IMR-20260912-03 — four omitted memberships in the subset array

Location: OLP0039, lines 134–144, specifically lines 141 and 144. The row rule is in line 135 and the sets in lines 137–138.

Classification: erroneous illustrative table entries; the anti-diagonal conclusion is unaffected.

The rule says to write $m$ in column $m$ iff $m\in N_n$. The examples specify $N_0=\{0,1,2,\ldots\}$ and $N_3=\{2,3,4,\ldots\}$. Yet row $N_0$ leaves columns 3, 4, and 5 blank, and row $N_3$ leaves column 5 blank. These are explicit columns preceding the final ellipsis, not unspecified later entries.

Minimal correction: insert 3, 4, and 5 in their columns in row $N_0$, and 5 in its column in row $N_3$. All four insertions are forced by membership in the stated sets. Leave row $N_2$ column 2 blank because $2\notin\{0,1,4\}$. The stated diagonal result remains correct: exclude 0 and 1, include 2, exclude 3.

Deduplication: this is not `OLSIZ-001`, which records an omitted integer-function value in a different file and table. No existing ID records these memberships. Editorial confidence: high, by the array's explicit membership rule.

## Checks by source unit

### OLP0037 — theorem, boundary cases, and deliberate deferral

Lines 23–32 state Schröder–Bernstein in the correct direction: injections $A\to B$ and $B\to A$ imply a bijection $A\to B$. No finiteness or nonemptiness hypothesis is needed. If $A=\varnothing$, existence of $B\to A$ forces $B=\varnothing$, and the empty bijection works; the reverse case is symmetric. For finite sets the two injections give the two finite cardinal inequalities and hence equality.

The theorem does not require the axiom of choice. This report does not construct or attribute a general proof: lines 34–42 explicitly defer the proof, conditionally referencing `sfr:cardinals:card-sb:sec` and then asking the reader to accept the result. The absence of a local proof is intentional exposition, not a defect.

Lines 44–51 correctly describe proving equinumerosity by giving two injections. “Difficult” is pedagogical judgment. Historical attribution and the cited Potter pages were not verified, and the deferred section was not inspected. No erroneous active mathematical statement was found in this unit.

### OLP0038 — definitions, conventions, examples, and every exercise

Definitions, lines 21–43 and 57–66: $\mathbb N$ starts at 0. An enumeration has a nonempty finite initial domain $\{0,\ldots,n\}$ or domain $\mathbb N$; the empty set is declared enumerable separately. Thus “enumerable” means at most countable, not necessarily countably infinite or computably enumerable.

The earlier $\{0,\ldots,n-1\}$ takes $n$ to be cardinality; the definition's $\{0,\ldots,n\}$ takes $n$ to be the last index. This is a change of dummy parameter, not an off-by-one error. For size $k>0$ use last index $k-1$. For size 0 the standard interpretation of the initial segment is $\{i\in\mathbb N:i<0\}=\varnothing$; the enumerable definition explicitly handles it. Writing finite domains as $\{i:i<k\}$ would clarify the notation, but changing the convention is not required for correctness.

Examples, lines 69–74 and 83–92: identity enumerates $\mathbb N$, successor enumerates positive naturals, $2n$ enumerates evens, and $2n+1$ enumerates odds. Their inverses on those ranges are identity, $m-1$, $m/2$, and $(m-1)/2$.

A codomain convention needs care in lines 84–92: the last two maps are written $\mathbb N\to\mathbb N$, where they are not surjective, but then said to enumerate their images. Strictly, their corestrictions $\mathbb N\to2\mathbb N$ and $\mathbb N\to(2\mathbb N+1)$ are bijections. Reading “enumerates” as referring to these natural corestrictions makes the examples correct. This is a formal exposition clarification, not an incorrect parity example or a reason to alter either formula.

Exercise, lines 77–80: both equivalences hold, including finite and empty cases. From a nonempty finite enumeration $e$ with domain of size $k$, $n\mapsto e(n\bmod k)$ is a surjection from $\mathbb N$; an infinite enumeration already is one. From a surjection $f\colon\mathbb N\to A$, assign each $a$ its least preimage to obtain an injection $A\to\mathbb N$. From an injection $g:A\to\mathbb N$, list $g[A]$ increasingly and apply the inverse of $g$ on its image. This gives a finite enumeration or one with domain $\mathbb N$. The empty injection exists, while no map $\mathbb N\to\varnothing$ does; the exercise correctly includes the empty exception.

Exercise, lines 95–97: $e(n)=(n+1)^2$ bijectively enumerates the displayed positive squares. Excluding 0 is fixed by the problem's list, not an error.

Integer example, lines 99–123: the ceiling and case formulas agree. For $n=2k$ the value is $k$; for $n=2k+1$ it is $-(k+1)$. Their disjoint images cover $\mathbb Z$. The inverse sends $z\geq0$ to $2z$ and $z<0$ to $-2z-1$. Every displayed value, including 3 at $n=6$, is correct.

Union exercises, lines 126–132: given injections $u:A\to\mathbb N$ and $v:B\to\mathbb N$, set $h(x)=2u(x)$ for $x\in A$, and $h(x)=2v(x)+1$ for $x\in B\setminus A$. Parity separates the branches, so $h$ injects $A\cup B$ into $\mathbb N$. This handles overlaps and empty sets. Induction gives every finite union; if $n=0$ is admitted, its union is empty. No assertion about arbitrary countable unions without additional choice assumptions is needed.

No active mathematical error was found under these initial-segment and corestriction conventions. The malformed introductory English in line 21 does not change the mathematics.

### OLP0039 — diagonal proofs and function exercise

Binary sequences, lines 43–53 and 61–103: the objects are all $\mathbb N$-indexed binary sequences, not finite strings, computable sequences, or real numbers modulo alternative digit expansions. For any $\mathbb N$-indexed list $(s_n)$, put $d(n)=1-s_n(n)$. Every coordinate lies in $\{0,1\}$, and $d(n)\ne s_n(n)$ proves $d\ne s_n$ for every index. Repeated rows do not affect this argument; injectivity of the list is unnecessary.

Finite-case exposition: lines 62–63 move from an enumeration of a subset to an infinite list, although finite subsets also have enumerations. Lines 99–102 use the same shorthand. It suffices to say “any $\mathbb N$-indexed list” and note that the target is infinite: sequences with a unique 1 at position $k$ are distinct for distinct $k$. Alternatively, for a finite list of length $k$, complement the $i$th listed sequence at coordinate $i$ for $i<k$, and put zeros at later coordinates. Finite lists cannot exhaust the target either. This is an omitted boundary explanation, not a failed diagonal construction.

Power set, lines 118–129: for any list $(N_n)$, $D=\{n\in\mathbb N:n\notin N_n\}$ exists by separation and belongs to $\mathcal P(\mathbb N)$. At coordinate $n$, membership in $D$ is opposite membership in $N_n$, so $D\ne N_n$. Claiming $D=N_k$ gives $k\in D$ iff $k\notin D$. The target is nonempty and infinite, as witnessed by its distinct singletons. Neither surjectivity nor injectivity of the attempted list is assumed.

Array, lines 134–151: apart from the four omissions recorded above, all shown memberships and initial membership decisions for $D$ agree with the formula. The doubled “iff if” in line 135 is a prose typo.

Exercise, lines 154–159: the list is one-based but arguments start at 0. A total counter-diagonal respecting both conventions is

$$g(0)=0,\qquad g(i)=f_i(i)+1\quad(i\geq1).$$

Then $g(i)\ne f_i(i)$ for each listed function. Alternatively put $g(n)=f_{n+1}(n)+1$ for all $n\in\mathbb N$, differing from $f_i$ at input $i-1$. The exercise is valid. A one-based list is harmless when the shift or the value at 0 is explicit.

### OLP0040 — reduction direction, examples, and every active exercise

Direction, lines 20–40: to deduce non-enumerability of $A$ from known non-enumerability of $B$, a surjection must go $A\to B$; an injection may go $B\to A$. Enumerability of $A$ would then imply enumerability of $B$. The source uses the correct direction. This is a set-theoretic reduction, not an effective algorithm with a computability requirement.

Characteristic map, lines 48–85: under the hypothetical enumeration of $\mathcal P(\mathbb N)$, every subset appears. The map sends a subset to its characteristic sequence; the inverse sends $s$ to $\{n:s(n)=1\}$. Both inverse identities hold pointwise. Even naturals yield `101010…` because position 0 is even; the empty set yields `000…`, and all naturals yield `111…`. These examples are correct. The one-based outer list $N_1,N_2,\ldots$ is a reindexing of $\mathbb N$ and does not change coordinates inside a sequence. The notation defect and omitted injectivity/first-occurrence explanation are precisely the findings above.

Injection exercise, lines 42–45: if $g:B\to A$ is injective and $e:I\to A$ enumerates $A$, restrict to $J=\{i\in I:e(i)\in g[B]\}$. Increasingly list $J$ and send each listed index $i$ to the unique $b$ with $g(b)=e(i)$. This enumerates nonempty $B$ or establishes its explicit empty case. If $B$ is non-enumerable, this contradicts enumerability of $A$. Membership in $g[B]$ need not be algorithmically decidable; the set-theoretic construction is enough.

Functions exercise, lines 106–109: for $X=\mathbb N^{\mathbb N}$, define $q(f)(n)=f(n)\bmod2$. This surjects onto binary sequences because every binary sequence is itself a natural-valued function and maps to itself.

Sets-of-pairs exercise, lines 112–115: the map

$$R\longmapsto\{n:(n,0)\in R\}$$

surjects from $\mathcal P(\mathbb N\times\mathbb N)$ onto $\mathcal P(\mathbb N)$: a preimage of $U$ is $U\times\{0\}$. Taking the power set, rather than just pairs, is essential and correctly stated.

Sequences exercise, lines 118–120: $\mathbb N^\omega$ is the same function space in sequence notation. Coordinatewise parity again surjects onto binary sequences. Repeating this idea is pedagogical overlap, not an invalid exercise.

Surjections exercise, lines 130–133: for each binary sequence $s$, define

$$j(s)(0)=0,\qquad j(s)(1)=1,\qquad j(s)(n+2)=s(n).$$

Every $j(s)$ lies in the specified set $S$ of surjections onto $\{0,1\}$. Distinct tails give distinct functions, so $j$ is injective. Alternatively the tail map $t\mapsto(n\mapsto t(n+2))$ surjects $S$ onto binary sequences, with $j$ as a right inverse. Thus $S$ is non-enumerable; excluding the two constant functions causes no problem.

Reals exercise, lines 136–137: an explicit injection from binary sequences is

$$r(s)=\sum_{n=0}^{\infty}\frac{2s(n)}{3^{n+1}}\in[0,1].$$

The series converges by geometric comparison. If sequences first differ at $k$, orient them so $s(k)=1$ and $t(k)=0$. Then

$$r(s)-r(t)\geq\frac{2}{3^{k+1}}-\sum_{n>k}\frac{2}{3^{n+1}}=\frac{1}{3^{k+1}}>0.$$

The injection principle proves non-enumerability of $\mathbb R$. This explicitly avoids assuming uniqueness of binary expansions, which fails at dyadic rationals. The exercise relies on the ordinary real-number construction and convergent geometric series; it is valid with those background facts.

## Commented-out material and mathematical assumptions

The following material was read as part of the exact blobs, but is commented out and is not active mathematical content in OLP0040.

Lines 88–104: the proposed $h\colon\mathbb N\to\mathrm{Bin}^{\omega}$ at lines 98–103 outputs a finite string of $n$ zeros. This is a codomain error, including $n=0$, whose output is the empty finite string. It is a dormant occurrence of the same defect pattern as `OLSIZ-005`; that registry ID's recorded source location is in `reduction.tex`, not this file. Do not count it as a new active defect here. If activated, replace the output by a genuine infinite sequence, for example constant $0^\omega$, which gives the required non-surjective map.

In that comment, lines 92–94 call $s(1)$ the “first” element. Under the zero-based coordinate convention the first is $s(0)$; either projection nevertheless surjects onto $\{0,1\}$, so the counterexample's mathematics is valid. Line 98's $Y$ is also unbound and should be the intended binary-sequence target if restored. These dormant notation issues do not affect active content.

Lines 123–128: the disabled partial-functions exercise is valid. There is exactly one total map $\mathbb N\to\{0\}$. Partial maps from positive integers to $\{0\}$ correspond bijectively to their arbitrary domains, i.e. subsets of positive integers, whose power set is non-enumerable. “Partial” must permit every subset as domain, without a finiteness or computability restriction.

Classical assumptions: the characteristic-function argument explicitly uses that membership holds or does not hold (OLP0040, lines 56–57); binary complement has the same classical setting. Power sets, function sets, separation, and recursion on the naturals have their usual meanings. The exhibited countability transformations use least natural indices and unique inverse values, not an axiom of choice.

The phrase “more elements” in OLP0039, lines 29–31, is informal. Read as the strict cardinal comparison $|\mathbb N|<|A|$, it presupposes an injection $\mathbb N\to A$ as well as no bijection. Without choice, that extra property should not silently be inferred for an arbitrary infinite set. For the actual targets it is explicit: send $n$ to the binary sequence with its sole 1 at $n$, or to $\{n\}$. This is a convention/assumption clarification, not a counterexample to either theorem.

## Completion record

Complete source read: all 490 lines of the four frozen blobs, including comments. Independent checks: definitions and boundary cases; both diagonal constructions; reduction and index directions; every displayed mathematical example; all eleven active exercises; and the disabled partial-functions exercise. Deduplication: all ten existing IDs compared, with `OLSIZ-008`, `009`, and `010` confirmed at matching source hashes.

The only task writes are this report and the private `TASK_INPUT_VERBATIM.md` beside it, both created with `apply_patch`. The latter preserves the request as supplied. No other artifact or task requires an action for this audit to be complete. The corrections above are concrete report recommendations, not edits or a human-dependent gate.

Public-copy transformations: the private registry path is replaced by its relative identity; two mathematical colon spellings are normalized to the equivalent LaTeX colon command. No mathematical conclusions or audit findings are changed.
