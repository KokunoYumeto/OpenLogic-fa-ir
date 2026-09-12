# Persian OpenLogic: kinds of functions and functions as relations

Full aligned source/canon review of OLP-0022 and OLP-0023. Seven complete Persian scholarly page images were actually consulted. Evidence is retrospective, not an assertion of original translation-time consultation. Candidates and documented correction overlays are for the existing edition owner; this is not a rebuilt reader or whole-corpus certification.

## Review priorities

- Keep codomain, range, at least one and at most one distinct. Test actual Persian token expansion, not just untranslated macro syntax.
- Use the attested نمودار تابع for a function graph; retain all graph formulas and the same-domain/same-codomain condition on function equality.
- Explain functional uniqueness without silently assuming totality on an arbitrary ambient domain.
- Disclose the convention switch: the preceding relation section restricts both coordinates, while function restriction here restricts only inputs. Do not change either frozen definition.
- Record the successor-label and functional-label attestation gaps rather than inventing exact scholarly attestations.
- Confidence is editorial 0-3, not calibrated probability. Human review is a later opportunity, not a gate.

## Scholarly pages actually consulted

- نظریهٔ مجموعه‌ها; محسن خانی, افشین زارعی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/jozve-kamel.pdf). PDF SHA-256: dbd518c80232921264ab5d79b79be01fe42efe8c01a766327db248b2d261de04. Canon PDFs are privately retained, not redistributed.
- ریاضیات گسسته و کاربردها; علیرضا غفاری حدیقه, مگردیچ تومانیان; مؤسسه چاپ و انتشارات دانشگاه جامع امام حسین (ع). [Source](https://hadigheha.github.io/books/teaching/Textbooks/Tarkibiyat.pdf). PDF SHA-256: 8f79c45a926c1cea819c4fefa86383f2a65ae23b1d526baaf99cf2506bb9f317. Canon PDFs are privately retained, not redistributed.
- FA-OL-CANON-0003:P0008, PDF 8, printed 7: First set-theoretic axiom and footnote2. Directly pairs اصل گسترش with extensionality and equal-membership set equality. It does not eliminate the source function-equality hypothesis of a shared domain and codomain.
- FA-OL-CANON-0003:P0014, PDF 14, printed 13: Definition19: pairs, products, relation, restriction and domain. Relation-as-pair-set and first-coordinate-only restriction are explicit. This agrees with the present function restriction, but differs from the earlier OLP two-coordinate relation restriction. Keep those conventions distinct.
- FA-OL-CANON-0003:P0015, PDF 15, printed 14: Image; functional relation and function; composition and converse. تابعال is paired with English functional and requires uniqueness; notation F:A to B additionally fixes domain A and bounds the range by B. The exact form تابع‌وار is NOT attested here. Class-theoretic scope is not imported into OLP set functions.
- FA-REL-P044, PDF 44, printed 34: Section2.2: function definition and domain/codomain/range. Direct assignment syntax and distinction between domain, codomain and attained range. Its box prints equality implies equal values, not the converse required by OLP extensionality; use K8 plus the actual source for that implication.
- FA-REL-P045, PDF 45, printed 35: Graph as subset of a Cartesian product; function restriction. Direct evidence for نمودار as the set of function pairs, not merely a coordinate plot. Function restriction is intersection with C times B, keeping the codomain. The canon graph display contains a redundant free y qualifier; do not copy that into the clean OLP formula.
- FA-REL-P046, PDF 46, printed 36: Kinds of functions; arrow diagrams; injectivity and surjectivity. Direct definitions distinguish at most one preimage from at least one, and show the equality-of-values injectivity criterion. The source controls the four examples and their domains. Script direction does not reverse mathematical arrows.
- FA-REL-P047, PDF 47, printed 37: Bijective correspondences, identity, and operations on functions. Direct evidence for bijective correspondence and identity terminology, and the well-definedness expression. The translated successor and constant labels are contextual labels, not verbatim attestations on this page.

## FA-0022-C01: Heading and taxonomy

Action: retain_after_fresh_review; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P046.

Source:
```latex
\olsection{Kinds of Functions}

\begin{explain}
It will be useful to introduce a kind of taxonomy for some of the
kinds of functions which we encounter most frequently.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{انواع توابع}

\begin{explain}
مفید است که نوعی رده‌بندی برای برخی از
انواع توابعی که بیشتر با آن‌ها روبه‌رو می‌شویم معرفی کنیم.
```

Retain انواع توابع and the introductory classification. The canon heading انواع تابع‌ها directly supports this mathematical grouping; رده‌بندی is ordinary explanatory wording, not an added formal taxonomy.

Alternatives: No material alternative recorded; none invented.

## FA-0022-C02: Onto intuition

Action: correct; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P044, FA-REL-P046.

Source:
```latex
To start, we might want to consider functions which have the property
that every member of the codomain is a value of the function. Such
functions are called !!{surjective}, and can be pictured as in
\olref{fig:surjective}.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
برای آغاز، ممکن است بخواهیم توابعی را بررسی کنیم که هر عضو
هم‌دامنهٔ آن‌ها مقدار تابع برای دست‌کم یک ورودی باشد. چنین
توابعی پوشا نامیده می‌شوند و می‌توان آن‌ها را چنان‌که در
\olref{fig:surjective} آمده است به تصویر کشید.
```

Unpack having a codomain member as a value into its being the value at at least one input. This is exactly the source meaning, not injectivity or a claim that every codomain member is distinct. دامنه and هم‌دامنه remain distinct.

Alternatives: No material alternative recorded; none invented.

## FA-0022-C03: Surjective diagram and caption

Action: correct; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P044, FA-REL-P046.

Source:
```latex
\begin{figure}
  \olasset{assets/diagrams/surjective.tikz}
  \caption{!!^a{surjective} function has every !!{element} of the
    codomain as a value.}
  \ollabel{fig:surjective}
\end{figure}
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{figure}
  \olasset{assets/diagrams/surjective.tikz}
  \caption{در تابع پوشا، هر عضو هم‌دامنه
    مقدار تابع برای دست‌کم یک ورودی است.}
  \ollabel{fig:surjective}
\end{figure}
\end{explain}
```

Replace the calque هر عضو ... را به‌عنوان یک مقدار دارد with a sentence identifying an attained value and an input. The locale token expands to عضو. Preserve the source figure, reference and arrows without RTL mirroring.

Alternatives: No material alternative recorded; none invented.

## FA-0022-C04: Surjectivity definition and quantified condition

Action: correct; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P044, FA-REL-P046.

Source:
```latex
\begin{defn}[!!^{surjective} function]
A function $f \colon A \rightarrow B$ is \emph{!!{surjective}} iff $B$
is also the range of~$f$, i.e., for every $y \in B$ there is at least
one $x \in A$ such that~$f(x) = y$, or in symbols:
\[
  (\forall y \in B)(\exists x \in A)f(x) = y.
\]
We call such a function !!a{surjection} from $A$ to $B$.
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}[تابع پوشا]
تابع $f \colon A \rightarrow B$ \emph{پوشا} است اگر و تنها اگر $B$
همان بردِ~$f$ باشد؛ یعنی برای هر $y \in B$ دست‌کم
یک $x \in A$ وجود دارد چنان‌که~$f(x) = y$، یا به زبان نمادین:
\[
  (\forall y \in B)(\exists x \in A)f(x) = y.
\]
چنین تابعی را نگاشت پوشا از $A$ به $B$ می‌نامیم.
\end{defn}
```

Place پوشا next to the subject, then state the biconditional and equality of codomain with range. At least one input is not exactly one. Preserve both the quantified formula and surjection from A to B; the noun نگاشت پوشا is the attested نگاشت plus the attested adjective.

Alternatives: No material alternative recorded; none invented.

## FA-0022-C05: Proof obligation for surjectivity

Action: retain_after_fresh_review; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P044, FA-REL-P046.

Source:
```latex
\begin{explain}
If you want to show that $f$ is !!a{surjection}, then you need to show
that every object in $f$'s codomain is the value of $f(x)$ for some
input $x$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
اگر می‌خواهید نشان دهید که $f$ نگاشت پوشا است، باید نشان دهید
که هر شیء در هم‌دامنهٔ $f$ مقدار $f(x)$ برای یک
ورودی $x$ است.
```

Retain the requirement to find some input for each codomain object. The quantifier order is codomain member first, corresponding input second; it is not a single input for all outputs. شیء here denotes an element, not a new technical sort.

Alternatives: No material alternative recorded; none invented.

## FA-0022-C06: Induced surjection to the range

Action: correct; confidence 2/3: Content and codomain change explicit; choice between construction verbs is contextual register judgment.
Canon: FA-REL-P044, FA-REL-P046.

Source:
```latex
Note that any function \emph{induces} !!a{surjection}. After all,
given a function $f \colon A \to B$, let $f' \colon A \to \ran{f}$ be
defined by $f'(x) = f(x)$. Since $\ran{f}$ is \emph{defined} as
$\Setabs{f(x) \in B}{x \in A}$, this function $f'$ is guaranteed to be
!!a{surjection}
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
توجه کنید که از هر تابع می‌توان یک نگاشت پوشا \emph{به دست آورد}.
برای تابع $f \colon A \to B$، تابع $f' \colon A \to \ran{f}$ را با
ضابطهٔ $f'(x) = f(x)$ تعریف می‌کنیم. چون $\ran{f}$ \emph{بنا بر تعریف} برابر است با
$\Setabs{f(x) \in B}{x \in A}$، این تابع $f'$
نگاشت پوشا است.
\end{explain}
```

Use به دست آورد and ضابطه for the explicit construction already in the source. Keep f prime, unchanged pointwise values and the new codomain ran(f). This does not claim the original f was onto its original B. Even an empty-domain function induces the empty-to-empty surjection. Alternatives are stylistic, not new mathematical mechanisms.

Alternatives: القا می‌کند is possible disciplinary prose, but its compressed nominal usage here adds no information beyond the displayed construction.

Expert-review question: Review the contextual choice به دست آورد for induces; the selected pages attest the construction vocabulary, not this exact sentence.

## FA-0022-C07: Injectivity intuition

Action: retain_after_fresh_review; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P044, FA-REL-P046.

Source:
```latex
\begin{explain}
Now, any function maps each possible input to a unique output. But
there are also functions which never map different inputs to the same
outputs. Such functions are called !!{injective}, and can be pictured
as in \olref{fig:injective}.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
حال هر تابع هر ورودی ممکن را به خروجی یکتایی نگاشت می‌کند. اما
توابعی نیز وجود دارند که هرگز ورودی‌های متفاوت را به
خروجی یکسان نگاشت نمی‌کنند. چنین توابعی یک‌به‌یک نامیده می‌شوند و می‌توان آن‌ها را
چنان‌که در \olref{fig:injective} آمده است به تصویر کشید.
```

Retain the contrast between unique output for each input (all functions) and distinct outputs for distinct inputs (injectivity). Output uniqueness alone must not become injectivity. The page diagrams and definitions support the contrast.

Alternatives: No material alternative recorded; none invented.

## FA-0022-C08: Injective figure caption

Action: correct; confidence 2/3: Mathematical criterion directly attested; input synonym is an explicit contextual decision.
Canon: FA-REL-P044, FA-REL-P046.

Source:
```latex
\begin{figure}
  \olasset{assets/diagrams/injective.tikz}
  \caption{!!^a{injective} function never maps two different
    arguments to the same value.}
  \ollabel{fig:injective}
\end{figure}
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{figure}
  \olasset{assets/diagrams/injective.tikz}
  \caption{تابع یک‌به‌یک هرگز دو
    ورودی متفاوت را به مقدار یکسان نگاشت نمی‌کند.}
  \ollabel{fig:injective}
\end{figure}
\end{explain}
```

Use ورودی, already explained as the function argument in OLP-0021, consistently with this paragraph. Two distinct arguments do not mean two distinct propositions. The canon gives the distinct-domain-element criterion; it is not a verbatim attestation of every input/output phrase.

Alternatives: آرگومان is mathematically possible but unnecessarily changes the locally established explanatory term.

Expert-review question: ورودی is a contextual explanatory label supported by the assignment definition; confirm preferred wording without changing the quantified claim.

## FA-0022-C09: Injectivity formal definition

Action: retain_after_fresh_review; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P046.

Source:
```latex
\begin{defn}[!!^{injective} function] 
A function $f \colon A \rightarrow B$ is \emph{!!{injective}} iff for
each $y \in B$ there is at most one $x \in A$ such that~$f(x) = y$. We
call such a function !!a{injection} from $A$ to~$B$.
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}[تابع یک‌به‌یک]
تابع $f \colon A \rightarrow B$ \emph{یک‌به‌یک} است اگر و تنها اگر برای
هر $y \in B$ حداکثر یک $x \in A$ وجود داشته باشد چنان‌که~$f(x) = y$.
چنین تابعی را نگاشت یک‌به‌یک از $A$ به~$B$ می‌نامیم.
\end{defn}
```

Retain یک‌به‌یک, حداکثر یک and the type A to B. A codomain element may have no preimage; at most one does not impose surjectivity. Keep the noun نگاشت یک‌به‌یک and all variables unchanged.

Alternatives: No material alternative recorded; none invented.

## FA-0022-C10: Equality criterion and actual plural realization

Action: correct; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P044, FA-REL-P046.

Source:
```latex
\begin{explain}
If you want to show that $f$ is !!a{injection}, you need to show that
for any !!{element}s $x$ and $y$ of $f$'s domain, if $f(x)=f(y)$, then
$x=y$. 
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
اگر می‌خواهید نشان دهید که $f$ نگاشت یک‌به‌یک است، باید نشان دهید که
برای هر $x$ و $y$ که اعضای دامنهٔ $f$ هستند، اگر $f(x)=f(y)$، آنگاه
$x=y$.
\end{explain}
```

The token !!{element}s expands to اعضا. With the following ی it becomes اعضای, so اعضای از دامنه is ungrammatical; remove از to obtain اعضای دامنه. The quantified statement still ranges over any x and y in the domain and retains f(x)=f(y) implies x=y.

Alternatives: No material alternative recorded; none invented.

## FA-0022-C11: Constant function counterexample

Action: retain_after_fresh_review; confidence 2/3: Counterexample checked; exact constant-function label not directly quoted from these pages.
Canon: FA-REL-P044, FA-REL-P046.

Source:
```latex
\begin{ex}
The constant function $f\colon \Nat \to \Nat$ given by $f(x) = 1$ is
neither !!{injective}, nor !!{surjective}.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{ex}
تابع ثابت $f\colon \Nat \to \Nat$ که با $f(x) = 1$ داده می‌شود،
نه یک‌به‌یک است و نه پوشا.
```

Retain the constant-one function and both negations. Inputs0 and1 collide; codomain0 is omitted. The canon supplies function/injective/onto criteria; ثابت is the contextual name for the displayed constant formula, not a verbatim attestation on these pages.

Alternatives: No material alternative recorded; none invented.

Expert-review question: The selected canon pages do not explicitly name تابع ثابت; the displayed source definition fixes the meaning.

## FA-0022-C12: Identity example

Action: retain_after_fresh_review; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P047, FA-REL-P046.

Source:
```latex
The identity function $f\colon \Nat \to \Nat$ given by $f(x) = x$ is
both !!{injective} and !!{surjective}.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
تابع همانی $f\colon \Nat \to \Nat$ که با $f(x) = x$ داده می‌شود،
هم یک‌به‌یک است و هم پوشا.
```

تابع همانی is directly attested with the identity formula. The natural-number identity is both injective and onto, including0. Keep both conjunctions, not merely bijective as a shortening.

Alternatives: No material alternative recorded; none invented.

## FA-0022-C13: Successor example and local consistency

Action: correct; confidence 2/3: Formula, proof and within-chapter consistency verified; exact successor-term attestation remains a documented gap.
Canon: FA-REL-P044, FA-REL-P046, FA-REL-P047.

Source:
```latex
The successor function $f \colon \Nat \to \Nat$ given by $f(x) = x+1$
is !!{injective} but not !!{surjective}.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
تابع جانشین $f \colon \Nat \to \Nat$ که با $f(x) = x+1$ داده می‌شود،
یک‌به‌یک است اما پوشا نیست.
```

Use تابع جانشین to agree with the source-aligned successor explanation in OLP-0021 rather than introducing an unexplained alternative پسین. Retain x+1, injectivity and non-surjectivity. Neither selected page directly attests the successor label; the claim is grounded in the source formula and the previously defined context, not a fabricated dictionary citation.

Alternatives: پسین is a possible contextual alternative, but creates an unnecessary second name for the same function in consecutive sections.

Expert-review question: Confirm a direct disciplinary attestation of تابع جانشین when adding a natural-number canon; the mathematical meaning is already explicit and no review wait is required.

## FA-0022-C14: Even/odd piecewise surjection

Action: retain_after_fresh_review; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P045, FA-REL-P046.

Source:
```latex
The function $f \colon \Nat \to \Nat$ defined by:
\[
  f(x) =
  \begin{cases}
    \frac{x}{2} & \text{if $x$ is even} \\
    \frac{x+1}{2} & \text{if $x$ is odd.}
  \end{cases}
\]
is !!{surjective}, but not !!{injective}.
\end{ex}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
تابع $f \colon \Nat \to \Nat$ که به‌صورت زیر تعریف می‌شود:
\[
  f(x) =
  \begin{cases}
    \frac{x}{2} & \text{اگر $x$ زوج باشد} \\
    \frac{x+1}{2} & \text{اگر $x$ فرد باشد.}
  \end{cases}
\]
پوشا است اما یک‌به‌یک نیست.
\end{ex}
```

Keep even and odd conditions, the two numerators and both denominators. Every output y is attained at2y, whereas inputs1 and2 both give1. At0 the even case returns0. The conditions inside math text are individually reviewed, not accepted merely because the math checker masks prose.

Alternatives: No material alternative recorded; none invented.

## FA-0022-C15: Bijection and one-to-one correspondence

Action: retain_after_fresh_review; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P046, FA-REL-P047.

Source:
```latex
\begin{explain}
Often enough, we want to consider functions which are both
!!{injective} and !!{surjective}. We call such functions
!!{bijective}. They look like the function pictured in
\olref{fig:bijective}. !!^{bijection}s are also sometimes called
\emph{one-to-one correspondences}, since they uniquely pair elements
of the codomain with elements of the domain.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
اغلب می‌خواهیم توابعی را بررسی کنیم که هم
یک‌به‌یک و هم پوشا هستند. چنین توابعی را
دوسویی می‌نامیم. آن‌ها مانند تابعی هستند که در
\olref{fig:bijective} به تصویر کشیده شده است. تناظرهای دوسویی را گاهی
\emph{تناظرهای یک‌به‌یک} نیز می‌نامند، زیرا اعضای
هم‌دامنه را به‌طور یکتا با اعضای دامنه جفت می‌کنند.
```

Retain both constituent properties and تناظرهای یک‌به‌یک as the synonym for دوسویی. D47 explicitly pairs تناظر یک به یک with دوسویی. Expand plural locale tokens correctly; pairing is between domain and codomain, not a symmetry assumption.

Alternatives: No material alternative recorded; none invented.

## FA-0022-C16: Bijective diagram caption

Action: retain_after_fresh_review; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P046, FA-REL-P047.

Source:
```latex
\begin{figure}
  \olasset{assets/diagrams/bijective.tikz}
  \caption{!!^a{bijective} function uniquely pairs the elements of the
    codomain with those of the domain.}
  \ollabel{fig:bijective}
\end{figure}
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{figure}
  \olasset{assets/diagrams/bijective.tikz}
  \caption{تابع دوسویی اعضای
    هم‌دامنه را به‌طور یکتا با اعضای دامنه جفت می‌کند.}
  \ollabel{fig:bijective}
\end{figure}
\end{explain}
```

Retain جفت می‌کند as the source pairing explanation of a one-to-one correspondence. Both sides have exactly one partner. It is explanatory wording supported by the correspondence definition, not a claim that the canon has the same verb. Preserve the figure unmirrored.

Alternatives: No material alternative recorded; none invented.

## FA-0022-C17: Bijection formal definition

Action: retain_after_fresh_review; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P046, FA-REL-P047.

Source:
```latex
\begin{defn}[!!^{bijection}] 
A function $f \colon A \to B$ is \emph{!!{bijective}} iff it is both
!!{surjective} and !!{injective}. We call such a function
!!a{bijection} from $A$ to~$B$ (or between $A$ and~$B$).
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}[تناظر دوسویی]
تابع $f \colon A \to B$ \emph{دوسویی} است اگر و تنها اگر هم
پوشا و هم یک‌به‌یک باشد. چنین تابعی را
تناظر دوسویی از $A$ به~$B$ (یا میان $A$ و~$B$) می‌نامیم.
\end{defn}
```

Retain the biconditional, both surjective and injective, and the two type descriptions from A to B or between A and B. تناظر دوسویی combines the directly attested correspondence and bijective wording. No inverse-function theorem is added.

Alternatives: No material alternative recorded; none invented.

## FA-0023-C01: Section heading

Action: retain_after_fresh_review; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0003:P0015, FA-REL-P045.

Source:
```latex
\olsection{Functions as Relations}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{توابع به‌منزلهٔ روابط}
```

Retain توابع به‌منزلهٔ روابط: functions represented by particular relations, not all relations being functions. The canon explicitly constructs functions from relations.

Alternatives: No material alternative recorded; none invented.

## FA-0023-C02: Function-induced relation and set representation

Action: correct; confidence 2/3: All mathematical claims and qualification retained; philosophical idiom requires an editorial register judgment.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0003:P0015, FA-REL-P044, FA-REL-P045.

Source:
```latex
\begin{explain} 
A function which maps !!{element}s of~$A$ to !!{element}s of~$B$
obviously defines a relation between $A$ and~$B$, namely the relation
which holds between $x$ and $y$ iff $f(x) = y$.  In fact, we might
even---if we are interested in reducing the building blocks of
mathematics for instance---\emph{identify} the function~$f$ with this
relation, i.e., with a set of pairs.  This then raises the question:
which relations define functions in this way?
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
تابعی که اعضای~$A$ را به اعضای~$B$
نگاشت می‌کند، آشکارا رابطه‌ای میان $A$ و~$B$ تعریف می‌کند:
این رابطه میان $x$ و $y$ برقرار است اگر و تنها اگر $f(x) = y$.
حتی می‌توانیم---برای نمونه، اگر بخواهیم ریاضیات را بر مفاهیم بنیادیِ
کمتری بنا کنیم---تابع~$f$ را با این رابطه، یعنی با مجموعه‌ای از
زوج‌ها، \emph{یکی در نظر بگیریم}. آنگاه این پرسش پیش می‌آید:
کدام رابطه‌ها به این شیوه تابع تعریف می‌کنند؟
\end{explain}
```

Correct both اعضا از occurrences to the token-realized possessive اعضای. Unpack reducing the building blocks as basing mathematics on fewer fundamental notions. Retain the conditional motivation and the question of which relations qualify; there is no claim that every relation is a function. Canon supports pair-set representation, while the frozen source governs this philosophical motivation.

Alternatives: تقلیل اجزای سازنده and دست به یکی‌انگاری زدن are literal but more opaque than the explicit mathematical construction.

Expert-review question: The philosophical/expository wording is a contextual rendering, not a verbatim target-language formula in the canon.

## FA-0023-C03: Function graph as an ordered-pair set

Action: correct; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P045, FA-OL-CANON-0003:P0014.

Source:
```latex
\begin{defn}[Graph of a function] Let $f\colon A \to B$ be a function.
The \emph{graph} of~$f$ is the relation $R_f \subseteq A \times B$
defined by
\[
R_f = \Setabs{\tuple{x,y}}{f(x) = y}.
\]
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}[نمودار یک تابع] فرض کنید $f\colon A \to B$ یک تابع باشد.
\emph{نمودارِ}~$f$ رابطهٔ $R_f \subseteq A \times B$ است که
به‌صورت زیر تعریف می‌شود:
\[
R_f = \Setabs{\tuple{x,y}}{f(x) = y}.
\]
\end{defn}
```

Use the directly attested نمودار تابع for the defined subset of A times B. The displayed set formula makes clear that this is not limited to coordinate plotting. Do not import the textbook display’s redundant y qualifier or change any OLP pair/formula.

Alternatives: گراف is a loan used elsewhere for graph-theoretic structures; the exact function-graph canon here supports نمودار.

## FA-0023-C04: Extensional equality with fixed domain and codomain

Action: correct; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-OL-CANON-0003:P0008, FA-REL-P044, FA-REL-P045.

Source:
```latex
\begin{explain}
The graph of a function is uniquely determined, by extensionality.
Moreover, extensionality (on sets) will immediately vindicate the
implicit principle of extensionality for functions,
whereby if $f$ and~$g$ share a domain and codomain then they are
identical if they agree on all values.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
نمودار یک تابع بنا بر اصل گسترش به‌طور یکتا تعیین می‌شود.
از اصل گسترش برای مجموعه‌ها، اصل گسترش برای توابع نیز نتیجه می‌شود؛
همان اصلی که تا اینجا به‌طور ضمنی به کار برده‌ایم:
اگر $f$ و~$g$ دامنه و هم‌دامنهٔ یکسانی داشته باشند و برای هر
ورودی مقدار یکسانی بدهند، دو تابع برابرند.
```

Unpack the consequence of set extensionality into equality of functions that have the same domain and codomain and agree at every input. Preserve both typing hypotheses. K8 supplies the equal-membership direction; the D44 box alone supplies only the reverse implication and is not claimed as proof. Do not infer a codomain from a bare graph.

Alternatives: No material alternative recorded; none invented.

## FA-0023-C05: Functional relation on its own domain

Action: correct; confidence 2/3: Concept directly attested; selected lexical form is explicitly not verbatim attested.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0003:P0015.

Source:
```latex
Similarly, if a relation is ``functional'', then it is the graph of a function. 
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
به همین ترتیب، رابطه‌ای که هر مؤلفهٔ نخست را حداکثر به یک مؤلفهٔ دوم مربوط کند («تابع‌وار» باشد)، نمودار تابعی بر دامنهٔ همان رابطه است.
\end{explain}
```

Explain functional as at most one second coordinate for each first, and say the resulting function is on the relation’s own domain. A merely functional relation is not necessarily total on a preset larger A. The next proposition supplies that extra existence hypothesis. K15 attests تابعال, not تابع‌وار; retain the source quotation label only with its explicit mathematical explanation.

Alternatives: Substituting تابعال would follow this witness exactly but introduce a different unfamiliar label; retaining an explained تابع‌وار preserves this edition’s continuity.

Expert-review question: Compare تابع‌وار with the exact witness تابعال in future glossary harmonization. The uniqueness/domain distinction must remain whichever label is chosen.

## FA-0023-C06: Graph characterization: uniqueness and totality

Action: correct; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-OL-CANON-0003:P0015, FA-REL-P044, FA-REL-P045.

Source:
```latex
\begin{prop}\ollabel{prop:graph-function}
Let $R \subseteq A \times B$ be such that:
\begin{enumerate}
\item If $Rxy$ and $Rxz$ then $y = z$; and 
\item for every $x \in A$ there is some $y \in B$ such that $\tuple{x,
y} \in R$.  
\end{enumerate}
Then $R$ is the graph of the function $f\colon A \to B$ defined by
$f(x) = y$ iff $Rxy$. 
\end{prop}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prop}\ollabel{prop:graph-function}
فرض کنید $R \subseteq A \times B$ چنان باشد که:
\begin{enumerate}
\item اگر $Rxy$ و $Rxz$، آنگاه $y = z$؛ و
\item برای هر $x \in A$ یک $y \in B$ وجود دارد چنان‌که $\tuple{x,
y} \in R$.
\end{enumerate}
آنگاه $R$ نمودار تابع $f\colon A \to B$ است که به‌وسیلهٔ
$f(x) = y$ اگر و تنها اگر $Rxy$ تعریف می‌شود.
\end{prop}
```

Preserve both hypotheses and their order: uniqueness, then existence for every x in A with a y in B. Update only the graph label to نمودار. The pointwise iff defining f is retained; no arbitrary choice among multiple outputs is permitted.

Alternatives: No material alternative recorded; none invented.

## FA-0023-C07: Proof: make the given existence hypothesis explicit

Action: correct; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-OL-CANON-0003:P0015, FA-REL-P044, FA-REL-P047.

Source:
```latex
\begin{proof}
Suppose there is a $y$ such that $Rxy$.  If there were another $z \neq
y$ such that $Rxz$, the condition on~$R$ would be violated. Hence, if
there is a $y$ such that $Rxy$, this $y$ is unique, and so $f$ is
well-defined.  Obviously, $R_f = R$.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
به‌ازای هر ورودی در دامنه، شرط دوم وجود یک $y$ را تضمین می‌کند چنان‌که $Rxy$. اگر $z \neq
y$ دیگری وجود داشت چنان‌که $Rxz$، شرط مربوط به~$R$ نقض می‌شد. پس اگر
یک $y$ وجود داشته باشد چنان‌که $Rxy$، این $y$ یکتا است و بنابراین $f$
خوش‌تعریف است. آشکارا $R_f = R$.
\end{proof}
```

Start by invoking the proposition’s second hypothesis for every domain input. The source proof had left that invocation implicit; this is explanatory expansion, not a claim of a false theorem. Retain the uniqueness contradiction and R_f=R. خوش‌تعریف is directly attested.

Alternatives: No material alternative recorded; none invented.

## FA-0023-C08: Identification caveat and conditional forward references

Action: correct; confidence 2/3: Scope and conditional forms checked; expository register is a reasoned contextual choice.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0003:P0015, FA-REL-P045.

Source:
```latex
\begin{explain}
Every function $f\colon A \to B$ has a graph, i.e., a relation on $A
\times B$ defined by $f(x) = y$. On the other hand, every relation~$R
\subseteq A \times B$ with the properties given in
\olref{prop:graph-function} is the graph of a function~$f \colon A \to
B$. Because of this close connection between functions and their
graphs, we can think of a function simply as its graph. In other
words, functions can be identified with certain relations, i.e., with
certain sets of tuples. \oliflabeldef{sfr:rel:ref:sec}{Note, though,
that the spirit of this ``identification'' is as in
\olref[sfr][rel][ref]{sec}: it is not a claim about the metaphysics of
functions, but an observation that it is convenient to \emph{treat}
functions as certain sets. One reason that this is so convenient, is
that w}{W}e can now consider performing similar operations on
functions as we performed on relations (see
\olref[sfr][rel][ops]{sec}). In particular:
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
هر تابع $f\colon A \to B$ نموداری دارد؛ یعنی رابطه‌ای به‌صورت زیرمجموعه‌ای از $A
\times B$ که با $f(x) = y$ تعریف می‌شود. از سوی دیگر، هر رابطهٔ~$R
\subseteq A \times B$ که ویژگی‌های داده‌شده در
\olref{prop:graph-function} را داشته باشد، نمودار تابعی~$f \colon A \to
B$ است. به‌سبب این پیوند نزدیک میان توابع و
نمودارهایشان، می‌توانیم تابع را همان نمودار آن در نظر بگیریم. به
بیان دیگر، می‌توان توابع را با روابطی معین، یعنی با
مجموعه‌هایی معین از چندتایی‌ها، یکی در نظر گرفت. \oliflabeldef{sfr:rel:ref:sec}{بااین‌حال،
منظور از این «یکی در نظر گرفتن» همان است که در
\olref[sfr][rel][ref]{sec} توضیح دادیم: ادعا نمی‌کنیم که ماهیت توابع چیست؛
فقط می‌گوییم که برای کار ریاضی مفید است توابع را مجموعه‌هایی معین
\emph{در نظر بگیریم}. یکی از فایده‌های این روش آن است
که اکنون می‌توانیم}{اکنون می‌توانیم} همان‌گونه که روی روابط عملیات انجام دادیم،
روی توابع نیز عملیات مشابهی انجام دهیم (نگاه کنید به
\olref[sfr][rel][ops]{sec}). به‌ویژه:
\end{explain}
```

Use نمودار consistently and specify a relation represented as a subset of A times B, as the immediately preceding definition states. Unpack the metaphysics caveat into not asserting the nature of functions but using a useful set representation. Preserve the conditional caveat, its absence branch, and both cross-references. Selected canon supports representation, not a metaphysical conclusion.

Alternatives: روح این یکی‌انگاری and مشاهده‌ای مبنی بر مناسب‌بودن are compressed calques; the revision states the same limited claim explicitly.

Expert-review question: Check the adult scholarly phrasing of the philosophical caveat; mathematical representation is not an ontological assertion.

## FA-0023-C09: Restriction: domain only and unchanged codomain

Action: retain_after_fresh_review; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P045, FA-OL-CANON-0003:P0014.

Source:
```latex
\begin{defn}\ollabel{defn:funimage}
Let $f \colon A \to B$ be a function with $C\subseteq A$.

The \emph{restriction} of~$f$ to~$C$ is the
function~$\funrestrictionto{f}{C}\colon C \to B$ defined by
$(\funrestrictionto{f}{C})(x) = f(x)$ for all $x \in C$. In other
words, $\funrestrictionto{f}{C} = \Setabs{\tuple{x, y} \in R_f}{x \in
C}$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}\ollabel{defn:funimage}
فرض کنید $f \colon A \to B$ تابعی باشد و $C\subseteq A$ برقرار باشد.

\emph{تحدیدِ}~$f$ به~$C$ تابع
~$\funrestrictionto{f}{C}\colon C \to B$ است که به‌صورت زیر تعریف می‌شود:
$(\funrestrictionto{f}{C})(x) = f(x)$ برای هر $x \in C$. به
بیان دیگر، $\funrestrictionto{f}{C} = \Setabs{\tuple{x, y} \in R_f}{x \in
C}$.
```

Retain تحدید, C subset A, the function C to B, pointwise equality and the graph-comprehension formula. D45 directly supports first-coordinate restriction with unchanged B. Do not inherit the earlier OLP two-coordinate convention here. The linebreak before a nonbreaking space is typographic, not a mathematical change.

Alternatives: No material alternative recorded; none invented.

## FA-0023-C10: Image/application of a subset

Action: retain_after_fresh_review; confidence 2/3: Image definition directly attested; secondary operation label not verbatim in selected pages.
Canon: FA-OL-CANON-0003:P0015, FA-REL-P044.

Source:
```latex
The \emph{application} of~$f$ to~$C$ is $\funimage{f}{C} =
\Setabs{f(x)}{x \in C}$. We also call this the \emph{image} of~$C$
under~$f$.
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\emph{اعمالِ}~$f$ بر~$C$ برابر است با $\funimage{f}{C} =
\Setabs{f(x)}{x \in C}$. این را \emph{تصویرِ}~$C$
تحت~$f$ نیز می‌نامیم.
\end{defn}
```

Retain اعمال as the source secondary operation label, and تصویر as the directly attested image term. The image is the set of values at inputs in C, not the full codomain and not the function restricted to C.

Alternatives: No material alternative recorded; none invented.

Expert-review question: اعمال is a contextual rendering of application; تصویر is the directly attested term, and the displayed formula removes ambiguity.

## FA-0023-C11: Range equals image of domain

Action: retain_after_fresh_review; confidence 3/3: The complete aligned wording and its mathematical scope were checked against the frozen source and the stated Persian passages; score is editorial, not a probability.
Canon: FA-REL-P044, FA-OL-CANON-0003:P0015.

Source:
```latex
\begin{explain}
It follows from these definitions that $\ran{f} =
\funimage{f}{\dom{f}}$, for any function~$f$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
از این تعریف‌ها نتیجه می‌شود که $\ran{f} =
\funimage{f}{\dom{f}}$ برای هر تابع~$f$ برقرار است.
```

Retain ran(f)=f[dom(f)] for every function. The canon range is all attained values, not codomain; this identity needs no onto assumption and includes the empty function.

Alternatives: No material alternative recorded; none invented.

## FA-0023-C12: Disclosed restriction-convention caveat and next operations

Action: correct; confidence 2/3: Definitions and counterexample checked; note placement is editorial. No universal false-theorem claim is made.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0003:P0015, FA-REL-P045.

Source:
```latex
\oliflabeldef{sfr:rel:ops:sec}{These notions are exactly as one would
expect, given the definitions in \olref[sfr][rel][ops]{sec} and our
identification of functions with relations. But two other
operations---inverses and relative products---require a little more
detail. We will provide that in \olref[inv]{sec} and
\olref[cmp]{sec}.}{}
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\oliflabeldef{sfr:rel:ops:sec}{این مفاهیم را می‌توان با تعریف‌های
\olref[sfr][rel][ops]{sec} و در نظر گرفتن توابع به‌صورت روابط مقایسه کرد.
\emph{یادداشت ویراستاری:} تعریف تصویر با تعریف قبلی سازگار است؛
اما قرارداد تحدید در اینجا تفاوت دارد. در تحدید تابع، فقط ورودی‌ها
به زیرمجموعهٔ دامنه محدود می‌شوند و هم‌دامنه تغییر نمی‌کند؛
در تعریف پیشینِ تحدید رابطه، هر دو مؤلفه به مجموعهٔ تعیین‌شده محدود می‌شدند.
دو عمل دیگر---وارون‌ها و حاصل‌ضرب‌های نسبی---به
جزئیات اندکی بیشتر نیاز دارند. آن جزئیات را در
\olref[inv]{sec} و
\olref[cmp]{sec} ارائه خواهیم کرد.}{}
\end{explain}
```

Replace the unqualified exactly-as-expected bridge with a disclosed editorial comparison: image agrees, but restriction switches from both coordinates to inputs only. This is a convention clarification; neither frozen definition is replaced. Preserve the conditional enclosure and the inverse/relative-product forward references. The minimal graph {(0,1)} distinguishes the operations.

Alternatives: Silently changing one restriction definition would alter source mathematics. Leaving the bridge unexplained obscures a real convention switch.

Expert-review question: Review whether to retain this labelled note inline or in an edition-wide convention box; it must not imply the source proposition is false.

## Validation boundary

Every substantive source and target character lies in an ordered non-overlapping reviewed span. Formal tokens are checked across inline, bracketed, multline and align mathematics. Text arguments in mathematics are separately aligned and manually reviewed for exact connective, quantifier and number-family meaning.
Finite tests support the written reasoning; they are not universal formal proofs. No new PDF was built or visually certified. Frozen owner inputs and reader releases are unchanged; corrections enter the owner’s normal next-batch build and visual QA.
Attribution: Open Logic Project and contributors, under existing CC BY 4.0 notices. https://github.com/OpenLogicProject/OpenLogic . Existing edition: https://github.com/KokunoYumeto/OpenLogic-fa-ir . Canon sources retain separate rights.
