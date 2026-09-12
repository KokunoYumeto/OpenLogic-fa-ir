# Persian OpenLogic: inverses, composition and partial functions

Full source/canon review of OLP-0024, OLP-0025 and OLP-0026. Eight whole Persian scholarly pages were directly consulted. This is retrospective review, not a claim about original translation-time consultation. The package contains corrected candidates, exact overlays, full aligned editorial records and a source-error report; no rebuilt reader or whole-corpus certification is claimed.

## Review priorities

- Repair the missing nonempty-domain qualification in the left-inverse proposition and its proof; explicitly retain both empty-set boundary cases.
- Preserve the source Axiom of Choice caveat for arbitrary right inverses. Do not attach a Choice requirement to a bijection or a partial injection.
- Preserve composition order: first f, then g. A nonempty intersection of range and domain is not the condition for a total composite on the original input set.
- Keep the permitted input set of a partial function distinct from its actual domain of definition, and undefined values distinct from zero.
- Use the consulted canon for inverse, graph, composition, partial-function and choice terminology. Expose exact-label gaps for total and serial; no fictitious attestations.
- Confidence is editorial 0-3, not calibrated probability. Human review is a later opportunity, not a gate.

## Scholarly pages actually consulted

- نظریهٔ مجموعه‌ها; محسن خانی, افشین زارعی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/jozve-kamel.pdf). PDF SHA-256: dbd518c80232921264ab5d79b79be01fe42efe8c01a766327db248b2d261de04. Canon PDFs are privately retained, not redistributed.
- منطق ریاضی; محسن خانی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/chapter2_0.pdf). PDF SHA-256: 0f3fb75ed1fcb0cbc669c04493acf520888e1ebfd62795bb28fc510bc41c7e79. Canon PDFs are privately retained, not redistributed.
- ریاضیات گسسته و کاربردها; علیرضا غفاری حدیقه, مگردیچ تومانیان; مؤسسه چاپ و انتشارات دانشگاه جامع امام حسین (ع). [Source](https://hadigheha.github.io/books/teaching/Textbooks/Tarkibiyat.pdf). PDF SHA-256: 8f79c45a926c1cea819c4fefa86383f2a65ae23b1d526baaf99cf2506bb9f317. Canon PDFs are privately retained, not redistributed.
- FA-OL-CANON-0003:P0015, PDF 15, printed 14: Functional relations, actual domain and range, composition and converse. Uniqueness, domain/range and first-R-then-Q relational composition are explicit. Converse of an arbitrary relation is not necessarily an inverse function. Do not import class-theoretic scope or infer totality on a larger ambient set.
- FA-OL-CANON-0003:P0018, PDF 18, printed 17: Definition29 and axiom12: choice functional and Axiom of Choice. Direct terminology and selection of one member of each nonempty set. Relevant to fibres of a general surjection. One fixed default element for a nonempty domain is not the same as making arbitrary infinitely many choices.
- FA-OL-CANON-0001:P0085, PDF 85, printed 84: Register-machine semantics and Definition165. Direct partial-function vocabulary in mathematical logic. Computable partial functions are a special case: OLP does not require all partial functions to be computable. The page does not directly attest تام or سریال, which remain explicitly provisional labels with full definitions.
- FA-REL-P044, PDF 44, printed 34: Definition of function and domain/codomain/range. Direct assignment and unique-value syntax. The equality box gives only equal functions imply equal values; it is not independent evidence for the opposite implication.
- FA-REL-P045, PDF 45, printed 35: Graph as set of pairs, numerical function rules and restriction. Direct نمودار for a function graph as a subset of a Cartesian product. Preserve the cleaner OLP formula instead of the canon display’s redundant y qualifier.
- FA-REL-P046, PDF 46, printed 36: Injective/surjective definitions and arrow diagrams. At most one preimage versus at least one preimage; collisions distinguish injectivity from functionality. Diagram orientation is mathematical and must not be mirrored with RTL prose.
- FA-REL-P049, PDF 49, printed 39: Composition definition, arrow diagram and domain discussion. Direct g composed with f and g(f(x)), first f then g. LIMIT: the lower page discusses a restricted domain and a nonempty intersection condition; that is NOT the OLP condition for a total composition on all original inputs. Do not import a nonempty-intersection rule or exclude an empty composite.
- FA-REL-P050, PDF 50, printed 40: Composition laws and inverse of a bijection. Direct function-inverse label معکوس, reversed arrows and both identity laws. The edition’s وارون is retained with معکوس explicitly introduced as its synonym. Left/right inverse labels are explained by the source equations, not falsely attributed verbatim to this page.

## FA-0024-C01: Inverse heading and undoing a map

Action: correct; confidence 2/3: Inverse concept directly attested; synonymous and successor naming decisions explicitly contextual.
Canon: FA-REL-P044, FA-REL-P050.

Source:
```latex
\olsection{Inverses of Functions}

\begin{explain}
We think of functions as maps. An obvious question to ask about
functions, then, is whether the mapping can be ``reversed.'' For
instance, the successor function $f(x) = x + 1$ can be reversed, in
the sense that the function $g(y) = y - 1$ ``undoes'' what $f$ does.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{وارون‌های توابع}

\begin{explain}
توابع را همچون نگاشت‌ها در نظر می‌گیریم. پس پرسشی طبیعی دربارهٔ
توابع این است که آیا می‌توان نگاشت را «وارونه کرد». برای
نمونه، تابع جانشین $f(x) = x + 1$ را می‌توان وارونه کرد، به
این معنا که تابع $g(y) = y - 1$ نتیجهٔ کار $f$ را به ورودی اولیه برمی‌گرداند.
```

Retain وارون as the lane term, explicitly paired with the canon معکوس in the definition below. Replace the vague خنثی می‌کند with returning to the original input. Standardize جانشین with the preceding reviewed sections; source formula x+1 remains explicit.

Alternatives: معکوس is directly attested; وارون is retained for edition continuity with its synonym introduced, not falsely called the verbatim label on D50.

Expert-review question: Exact successor label remains a contextual choice; the formula and the prior introduction fix its meaning.

## FA-0024-C02: Domain and codomain prevent invalid reversal

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P044, FA-REL-P050.

Source:
```latex
But we must be careful. Although the definition of~$g$ defines a
function $\Int \to \Int$, it does not define a \emph{function} $\Nat
\to \Nat$, since $g(0) \notin \Nat$.  So even in simple cases, it is
not quite obvious whether a function can be reversed; it may depend on
the domain and codomain.

This is made more precise by the notion of an inverse of a function.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
اما باید دقت کنیم. گرچه ضابطهٔ~$g$ تابعی
$\Int \to \Int$ تعریف می‌کند، یک \emph{تابع} $\Nat
\to \Nat$ تعریف نمی‌کند، زیرا $g(0) \notin \Nat$. بنابراین حتی در موارد ساده نیز
کاملاً آشکار نیست که آیا می‌توان تابعی را وارونه کرد؛ این امر ممکن است به
دامنه و هم‌دامنه بستگی داشته باشد.

مفهوم وارون یک تابع این نکته را دقیق‌تر بیان می‌کند.
\end{explain}
```

Retain the integer versus natural-number distinction and g(0) outside Nat. The source here explicitly includes0 in Nat. This is an inverse-domain issue, not a computational failure or a permission to add a new value at0.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C03: Two-sided inverse definition

Action: correct; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P050, FA-REL-P049.

Source:
```latex
\begin{defn}
A function $g \colon B \to A$ is an \emph{inverse} of a function $f
\colon A \to B$ if $f(g(y)) = y$ and $g(f(x)) = x$ for all $x \in A$
and $y \in B$.
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}
تابع $g \colon B \to A$ یک \emph{وارون (معکوس)} برای تابع $f
\colon A \to B$ است اگر $f(g(y)) = y$ و $g(f(x)) = x$ برای همهٔ $x \in A$
و $y \in B$ برقرار باشند.
\end{defn}
```

Introduce وارون (معکوس), the latter directly attested for functions. Preserve g:B to A and both identity laws for their respective domains. Neither law alone is the definition of a two-sided inverse.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C04: Inverse notation

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P050.

Source:
```latex
If $f$ has an inverse~$g$, we often write $f^{-1}$ instead of~$g$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
اگر $f$ وارونی مانند~$g$ داشته باشد، اغلب $f^{-1}$ را به‌جای~$g$ می‌نویسیم.
```

Retain f to the negative-one notation for an inverse, not the reciprocal1/f or a negative exponent evaluation. The canon pairs this symbol with the inverse map.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C05: Tentative inverse and uniqueness/existence obstruction

Action: correct; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P044, FA-REL-P046, FA-REL-P050.

Source:
```latex
\begin{explain}
Now we will determine when functions have inverses. A good candidate
for an inverse of $f\colon A \to B$ is $g\colon B \to A$ ``defined
by''
\[
g(y) = \text{``the'' $x$ such that $f(x) = y$.}
\]
But the scare quotes around ``defined by'' (and ``the'') suggest that
this is not a definition.  At least, it will not always work, with
complete generality. For, in order for this definition to specify a
function, there has to be one and only one~$x$ such that $f(x) =
y$---the output of~$g$ has to be uniquely specified. Moreover, it has
to be specified for every $y \in B$.  If there are $x_1$ and $x_2 \in
A$ with $x_1 \neq x_2$ but $f(x_1) = f(x_2)$, then $g(y)$ would not be
uniquely specified for $y = f(x_1) = f(x_2)$. And if there is no~$x$
at all such that $f(x) = y$, then $g(y)$ is not specified at all.  In
other words, for $g$ to be defined, $f$~must be both !!{injective} and
!!{surjective}.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
اکنون بررسی می‌کنیم توابع چه هنگام وارون دارند. یک پیشنهاد طبیعی
برای وارون $f\colon A \to B$ تابع $g\colon B \to A$ است که آن را با عبارت زیر
«تعریف می‌کنیم»:
\[
g(y) = \text{«آن» $x$ که $f(x) = y$ باشد.}
\]
اما گیومه‌های دور «تعریف می‌کنیم» (و «آن») هشدار می‌دهند که
هنوز تعریفی معتبر در همهٔ حالت‌ها نداریم. این عبارت همیشه
تابعی را مشخص نمی‌کند: باید دقیقاً یک~$x$
وجود داشته باشد که $f(x) =
y$---خروجی~$g$ باید به‌طور یکتا مشخص شود. افزون بر این، باید
برای هر $y \in B$ مشخص شده باشد. اگر $x_1$ و $x_2 \in
A$ چنان باشند که $x_1 \neq x_2$ اما $f(x_1) = f(x_2)$، آنگاه $g(y)$ برای
$y = f(x_1) = f(x_2)$ به‌طور یکتا مشخص نخواهد شد. و اگر هیچ~$x$
وجود نداشته باشد که $f(x) = y$، آنگاه $g(y)$ اصلاً مشخص نمی‌شود. به
بیان دیگر، برای آنکه $g$ تعریف شود، $f$ باید هم یک‌به‌یک و هم
پوشا باشد.
```

Replace the calqued نامزدی مناسب and در کلیت کامل with a natural proposed definition and its explicit validity limitation. Fix variable-attached Persian suffixes. Preserve the quoted tentative definition, both collisions and missing-preimage cases, and the injective-plus-surjective requirement. The quoted math-text آن remains to express the source definite article; its meaning is reviewed, not assumed from masking.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C06: Left and right inverse conventions

Action: correct; confidence 2/3: Identity direction certain; exact one-sided terminology not directly printed on selected pages.
Canon: FA-REL-P044, FA-REL-P049, FA-REL-P050.

Source:
```latex
Let's go slowly. We'll divide the question into two: Given a
function~$f\colon A \to B$, when is there a function $g\colon B \to A$
so that $g(f(x)) = x$? Such a $g$ ``undoes'' what $f$ does, and is
called a \emph{left inverse} of~$f$. Secondly, when is there a
function $h\colon B \to A$ so that $f(h(y)) = y$? Such an $h$ is
called a \emph{right inverse} of~$f$---$f$ ``undoes'' what $h$~does.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
گام‌به‌گام پیش برویم. پرسش را به دو بخش تقسیم می‌کنیم: با داشتن
تابع~$f\colon A \to B$، چه هنگام تابعی مانند $g\colon B \to A$
وجود دارد که $g(f(x)) = x$؟ تابع $g$ پس از اعمال $f$، ورودی اولیه را بازمی‌گرداند و
\emph{وارون چپِ}~$f$ نامیده می‌شود. دوم، چه هنگام
تابعی مانند $h\colon B \to A$ وجود دارد که $f(h(y)) = y$؟ تابع $h$
\emph{وارون راستِ}~$f$ نامیده می‌شود---$f$ پس از اعمال $h$، ورودی اولیه را بازمی‌گرداند.
\end{explain}
```

Explain undoing as returning to the initial input. Use the canon noun-plus-variable construction تابع g / تابع h instead of attaching an indefinite Persian suffix directly to a Latin variable. Keep g after f for a left inverse, f after h for a right inverse. Left/right is composition notation, not reading direction. The canon gives composition order and two-sided identities, not verbatim one-sided labels.

Alternatives: No material alternative recorded; none invented.

Expert-review question: وارون چپ/راست are explicitly equation-defined contextual labels; do not attribute these precise labels to D50.

## FA-0024-C07: Source repair: left inverse requires a nonempty domain

Action: correct; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P044, FA-REL-P046, FA-REL-P050.

Source:
```latex
\begin{prop}
If $f\colon A \to B$ is !!{injective}, then there is a \emph{left
inverse}~$g\colon B \to A$ of~$f$ so that $g(f(x)) = x$ for all $x
\in A$.
\end{prop}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prop}
اگر $f\colon A \to B$ یک‌به‌یک باشد و دامنهٔ آن ناتهی باشد، آنگاه \emph{وارون
چپی} مانند~$g\colon B \to A$ برای~$f$ وجود دارد چنان‌که $g(f(x)) = x$ برای همهٔ $x
\in A$.

\emph{یادداشت ویراستاری:} شرط ناتهی‌بودن دامنه در متن مبدأ نیامده است.
اگر دامنه تهی و هم‌دامنه ناتهی باشد، تابع تهی یک‌به‌یک است،
اما هیچ تابعی از هم‌دامنه به دامنه وجود ندارد؛ بنابراین وارون چپ ندارد.
اگر هر دو مجموعه تهی باشند، تابع تهی وارون خودش است.
\end{prop}
```

Add the missing nonempty-domain hypothesis and a labelled source-error note. The empty function from empty A to nonempty B is injective but cannot have g:B to A. Both-empty sets have the empty inverse; that valid case is expressly retained in the note. No source formula or original is changed. This is a real omitted hypothesis, not merely style.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C08: Left inverse proof and a fixed default element

Action: correct; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P044, FA-REL-P046, FA-REL-P050, FA-OL-CANON-0003:P0018.

Source:
```latex
\begin{proof}
Suppose that $f\colon A \to B$ is !!{injective}. Consider a $y \in B$.
If $y \in \ran{f}$, there is an $x \in A$ so that $f(x) = y$. Because
$f$ is !!{injective}, there is only one such~$x \in A$. Then we can
define: $g(y) = x$, i.e., $g(y)$ is ``the'' $x \in A$ such that $f(x)
= y$.  If $y \notin \ran{f}$, we can map it to any~$a \in A$. So, we
can pick an $a \in A$ and define $g\colon B \to A$ by:
\[
g(y) = \begin{cases}
    x & \text{if $f(x) = y$}\\
    a & \text{if $y \notin \ran{f}$.}
\end{cases}
\]
It is defined for all $y \in B$, since for each such $y \in \ran{f}$
there is exactly one $x \in A$ such that $f(x) = y$. By definition, if
$y = f(x)$, then $g(y) = x$, i.e., $g(f(x)) = x$.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
فرض کنید $f\colon A \to B$ یک‌به‌یک باشد و دامنهٔ آن ناتهی باشد. یک $y \in B$ را در نظر بگیرید.
اگر $y \in \ran{f}$، یک $x \in A$ وجود دارد چنان‌که $f(x) = y$. چون
$f$ یک‌به‌یک است، تنها یک~$x \in A$ با این ویژگی وجود دارد. پس می‌توانیم
تعریف کنیم: $g(y) = x$؛ یعنی $g(y)$ همان $x \in A$ است که $f(x)
= y$. اگر $y \notin \ran{f}$، می‌توانیم آن را به یک عضو دلخواه~$a \in A$ نگاشت کنیم. پس
می‌توانیم یک $a \in A$ برگزینیم و $g\colon B \to A$ را به‌صورت زیر تعریف کنیم:
\[
g(y) = \begin{cases}
    x & \text{اگر $f(x) = y$}\\
    a & \text{اگر $y \notin \ran{f}$ باشد.}
\end{cases}
\]
این تابع برای همهٔ $y \in B$ تعریف شده است، زیرا برای هر $y \in \ran{f}$
دقیقاً یک $x \in A$ وجود دارد چنان‌که $f(x) = y$. بنا بر تعریف، اگر
$y = f(x)$، آنگاه $g(y) = x$؛ یعنی $g(f(x)) = x$.
\end{proof}
```

State the same nonempty-domain assumption in the proof. Replace malformed x-in-A suffixes by ordinary Persian noun constructions. For attained y choose its unique preimage; otherwise use one fixed a in A. Selecting that single default does not require the Axiom of Choice. Preserve the piecewise formula and all its conditions.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C09: Left inverse implies injectivity: exercise

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P046, FA-REL-P050.

Source:
```latex
\begin{prob}
Show that if $f\colon A \to B$ has a left inverse~$g$, then $f$~is
!!{injective}.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
نشان دهید اگر $f\colon A \to B$ وارون چپی مانند~$g$ داشته باشد، آنگاه $f$
یک‌به‌یک است.
\end{prob}
```

Retain the complete source exercise, including the left inverse g. Its conclusion follows from applying g to equal outputs. No nonempty-domain assumption is needed for this converse, so none is added.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C10: Surjection has a right inverse: proposition

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0003:P0018.

Source:
```latex
\begin{prop}
    If $f\colon A \to B$ is !!{surjective}, then there is a
    \emph{right inverse}~$h\colon B \to A$ of~$f$ so that $f(h(y)) =
    y$ for all~$y \in B$.
\end{prop}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prop}
    اگر $f\colon A \to B$ پوشا باشد، آنگاه
    \emph{وارون راستی} مانند~$h\colon B \to A$ برای~$f$ وجود دارد چنان‌که $f(h(y)) =
    y$ برای همهٔ~$y \in B$.
\end{prop}
```

Retain the right inverse type and identity. The source proof immediately states its general Choice dependence; do not suppress that caveat or attach the left-inverse empty-domain repair here.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C11: Selecting preimages for a right inverse

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P044, FA-REL-P046, FA-OL-CANON-0003:P0018.

Source:
```latex
\begin{proof}
Suppose that $f\colon A \to B$ is !!{surjective}. Consider a $y \in
B$. Since $f$~is !!{surjective}, there is an $x_y \in A$ with $f(x_y)
= y$.  Then we can define: $h(y) = x_y$, i.e., for each $y \in B$ we
choose some $x \in A$ so that $f(x) = y$; since $f$~is !!{surjective}
there is always at least one to choose from.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
فرض کنید $f\colon A \to B$ پوشا باشد. یک $y \in
B$ را در نظر بگیرید. چون $f$ پوشا است، یک $x_y \in A$ وجود دارد که $f(x_y)
= y$. پس می‌توانیم تعریف کنیم: $h(y) = x_y$؛ یعنی برای هر $y \in B$
یک $x \in A$ برمی‌گزینیم چنان‌که $f(x) = y$؛ چون $f$ پوشا است،
همواره دست‌کم یک مورد برای انتخاب وجود دارد.
```

Retain x indexed by y, choosing one preimage for every codomain member. At least one preimage does not make the choice unique. The footnote, separately reviewed next, is part of the proof and remains intact.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C12: Axiom of Choice footnote and special cases

Action: correct; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-OL-CANON-0003:P0018, FA-REL-P046, FA-REL-P050.

Source:
```latex
\footnote{Since $f$ is
!!{surjective}, for every~$y \in B$ the set $\Setabs{x}{f(x) = y}$ is
nonempty. Our definition of~$h$ requires that we choose a single $x$
from each of these sets. That this is always possible is actually not
obvious---the possibility of making these choices is simply assumed as an axiom. 
In other words, this proposition assumes the so-called Axiom of
Choice, an issue we will \oliflabeldef{sth:choice::chap}{revisit in \olref[sth][choice][]{chap}}{gloss over}. 
However, in many specific cases, e.g., when $A = \Nat$ or is finite, or when $f$ is !!{bijective},
the Axiom of Choice is not required. (In the particular case when $f$ is !!{bijective}, for each $y \in B$ the set 
$\Setabs{x}{f(x) = y}$ has exactly one !!{element}, so that there is no choice to make.)}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\footnote{چون $f$
پوشا است، برای هر~$y \in B$ مجموعهٔ $\Setabs{x}{f(x) = y}$
ناتهی است. تعریف ما از~$h$ ایجاب می‌کند که از هریک از این مجموعه‌ها یک $x$
برگزینیم. اینکه این کار همواره ممکن است در واقع
آشکار نیست---امکان انجام این انتخاب‌ها صرفاً به‌عنوان یک اصل موضوع پذیرفته می‌شود.
به بیان دیگر، این گزاره «اصل انتخاب» را مفروض می‌گیرد؛ موضوعی که
\oliflabeldef{sth:choice::chap}{در \olref[sth][choice][]{chap} دوباره بررسی خواهیم کرد}{در اینجا به‌تفصیل به آن نمی‌پردازیم}.
بااین‌حال، در بسیاری از موارد خاص، مثلاً هنگامی که $A = \Nat$ یا متناهی است، یا هنگامی که $f$ دوسویی است،
به اصل انتخاب نیازی نیست. (در حالت خاصی که $f$ دوسویی است، برای هر $y \in B$ مجموعهٔ
$\Setabs{x}{f(x) = y}$ دقیقاً یک عضو دارد؛ پس هیچ انتخابی در کار نیست.)}
```

اصل انتخاب and nonempty selection families are directly attested. Preserve arbitrary simultaneous selection, the optional chapter reference, and the finite/Nat/bijective exceptions. Change چشم می‌پوشیم to not discussing the issue in detail: the absent-chapter branch must not suggest that the axiom is being dropped. Unique singleton preimages need no Choice; a well-order on Nat supplies least preimages.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C13: Right inverse proof conclusion

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P046, FA-REL-P050.

Source:
```latex
By definition, if $x = h(y)$,
then $f(x) = y$, i.e., for any $y \in B$, $f(h(y)) = y$.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
بنا بر تعریف، اگر $x = h(y)$،
آنگاه $f(x) = y$؛ یعنی برای هر $y \in B$، $f(h(y)) = y$.
\end{proof}
```

Retain the conclusion f(h(y))=y for every codomain y. The conclusion is not g(f(x))=x, and does not assert injectivity of the original f.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C14: Right inverse implies surjectivity: exercise

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P046, FA-REL-P050.

Source:
```latex
\begin{prob}
Show that if $f\colon A \to B$ has a right inverse~$h$, then $f$~is
!!{surjective}.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
نشان دهید اگر $f\colon A \to B$ وارون راستی مانند~$h$ داشته باشد، آنگاه $f$
پوشا است.
\end{prob}
```

Preserve the source exercise; h(y) explicitly supplies a preimage. This implication requires no new Choice assumption, because h is already supplied.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C15: A single two-sided inverse for a bijection

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P046, FA-REL-P050.

Source:
```latex
\begin{explain}
  By combining the ideas in the previous proof, we now get that every
  !!{bijection} has an inverse, i.e., there is a single function
  which is both a left and right inverse of~$f$.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
  با ترکیب ایده‌های برهان پیشین، اکنون نتیجه می‌گیریم که هر
  تناظر دوسویی وارونی دارد؛ یعنی تابع واحدی وجود دارد
  که هم وارون چپ و هم وارون راستِ~$f$ است.
\end{explain}
```

Retain the single function being both a left and a right inverse. Do not read تابع واحد as constant function or infer arbitrary surjections have two-sided inverses.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C16: Bijection inverse proposition

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P046, FA-REL-P050.

Source:
```latex
\begin{prop}\ollabel{prop:bijection-inverse}
If $f\colon A \to B$ is !!{bijective}, there is a
function~$f^{-1}\colon B \to A$ so that for all $x \in A$,
$f^{-1}(f(x)) = x$ and for all $y \in B$, $f(f^{-1}(y)) = y$.
\end{prop}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prop}\ollabel{prop:bijection-inverse}
اگر $f\colon A \to B$ دوسویی باشد، تابعی مانند
~$f^{-1}\colon B \to A$ وجود دارد چنان‌که برای همهٔ $x \in A$،
$f^{-1}(f(x)) = x$ و برای همهٔ $y \in B$، $f(f^{-1}(y)) = y$.
\end{prop}
```

Retain the type B to A and the two separately quantified identities. Unique preimages define the inverse without Choice; the empty bijection is included.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C17: Source proof intentionally assigned as an exercise

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P050.

Source:
```latex
\begin{proof}
Exercise.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
تمرین.
\end{proof}
```

تمرین faithfully translates the source proof text Exercise. It is not a translator placeholder; do not invent a proof or remove the exercise structure.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C18: Inverse construction exercise

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P044, FA-REL-P050.

Source:
```latex
\begin{prob}
Prove \olref[sfr][fun][inv]{prop:bijection-inverse}. You have to
define~$f^{-1}$, show that it is a function, and show that it is an
inverse of~$f$, i.e., $f^{-1}(f(x)) = x$ and $f(f^{-1}(y)) = y$ for
all $x \in A$ and $y \in B$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
گزارهٔ \olref[sfr][fun][inv]{prop:bijection-inverse} را اثبات کنید. باید
~$f^{-1}$ را تعریف کنید، نشان دهید تابع است، و نشان دهید
وارون~$f$ است؛ یعنی $f^{-1}(f(x)) = x$ و $f(f^{-1}(y)) = y$ برای
همهٔ $x \in A$ و $y \in B$.
\end{prob}
```

Keep all three obligations: define the inverse, prove it is a function, and check both identities with the stated quantifiers. Preserve the labelled proposition reference.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C19: Inverse on the range and notational abuse

Action: correct; confidence 2/3: Domain/range and inverse construction exact; editorial phrasing contextual.
Canon: FA-REL-P044, FA-REL-P046, FA-REL-P050.

Source:
```latex
\begin{explain}
There is a slightly more general way to extract inverses. We saw in
\olref[kin]{sec} that every function $f$ induces !!a{surjection} $f'
\colon A \to \ran{f}$ by letting $f'(x) = f(x)$ for all $x \in A$.
Clearly, if $f$~is !!{injective}, then $f'$~is !!{bijective}, so that
it has a unique inverse by \olref{prop:bijection-inverse}. By a very
minor abuse of notation, we sometimes call the inverse of $f'$ simply
``the inverse of~$f$.''
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
روش اندکی کلی‌تری برای به دست آوردن وارون وجود دارد. در
\olref[kin]{sec} دیدیم که از هر تابع $f$ می‌توان یک نگاشت پوشا $f'
\colon A \to \ran{f}$ را با قرار دادن $f'(x) = f(x)$ برای همهٔ $x \in A$ به دست آورد.
آشکار است که اگر $f$ یک‌به‌یک باشد، آنگاه $f'$ دوسویی است، پس
بنا بر \olref{prop:bijection-inverse} وارون یکتایی دارد. با تسامحی بسیار
جزئی در نمادگذاری، گاهی وارون $f'$ را صرفاً
«وارون~$f$» می‌نامیم.
\end{explain}
```

Use the explicit construction phrase به دست آورد consistently with reviewed0022. Preserve replacement of codomain by ran(f); the inverse of an injection is a function on its range, not automatically on all original B. The uniqueness claim is mathematically supported by the later uniqueness result, although the cited bijection proposition states existence. Keep the disclosed mild notational abuse.

Alternatives: No material alternative recorded; none invented.

Expert-review question: تسامح در نمادگذاری is an explanatory register choice, not a verbatim attestation on these pages.

## FA-0024-C20: Left and right inverses coincide

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P049, FA-REL-P050.

Source:
```latex
\begin{prop}\ollabel{prop:left-right}%
  Show that if $f\colon A \to B$ has a left inverse~$g$ and a right
  inverse~$h$, then $h = g$.
\end{prop}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prop}\ollabel{prop:left-right}%
  نشان دهید اگر $f\colon A \to B$ وارون چپی مانند~$g$ و وارون
  راستی مانند~$h$ داشته باشد، آنگاه $h = g$.
\end{prop}
```

Retain both inverse hypotheses and h=g. The calculation g(y)=g(f(h(y)))=h(y) proves the conclusion; neither one-sided hypothesis alone suffices.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C21: Proof and referenced exercise retained

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P049, FA-REL-P050.

Source:
```latex
\begin{proof}
  Exercise.
\end{proof}

\begin{prob}
  Prove \olref[sfr][fun][inv]{prop:left-right}.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
  تمرین.
\end{proof}

\begin{prob}
  گزارهٔ \olref[sfr][fun][inv]{prop:left-right} را اثبات کنید.
\end{prob}
```

Preserve both the Exercise proof marker and the subsequent instruction to prove the labelled proposition. These are distinct original structures, not duplicate translation work or missing generated content.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C22: At most one inverse

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P050.

Source:
```latex
\begin{prop}\ollabel{prop:inverse-unique}
Every function~$f$ has at most one inverse.
\end{prop}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prop}\ollabel{prop:inverse-unique}
هر تابع~$f$ حداکثر یک وارون دارد.
\end{prop}
```

Retain حداکثر یک: functions may have no inverse. This is uniqueness conditional on existence, not a new existence claim for every function.

Alternatives: No material alternative recorded; none invented.

## FA-0024-C23: Uniqueness proof

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P049, FA-REL-P050.

Source:
```latex
\begin{proof}
  Suppose $g$ and $h$ are both inverses of~$f$. Then in particular
  $g$~is a left inverse of~$f$ and $h$~is a right inverse. By
  \olref{prop:left-right}, $g = h$.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
  فرض کنید $g$ و $h$ هر دو وارون~$f$ باشند. آنگاه به‌ویژه
  $g$ وارون چپِ~$f$ و $h$ وارون راست آن است. بنا بر
  \olref{prop:left-right}، $g = h$.
\end{proof}
```

Preserve reduction of two two-sided inverses to the preceding left/right result. The names g,h and equation g=h remain correctly ordered.

Alternatives: No material alternative recorded; none invented.

## FA-0025-C01: Composition heading, optional inverse context and compatibility

Action: correct; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P049, FA-REL-P050, FA-OL-CANON-0003:P0015.

Source:
```latex
\olsection{Composition of Functions}

\begin{explain}
\oliflabeldef{sfr:fun:inv:sec}{We saw in \olref[inv]{sec} that the
inverse~$f^{-1}$ of !!a{bijection}~$f$ is itself a function. Another
operation on functions is composition: w}{W}e can define a new
function by composing two functions, $f$ and~$g$, i.e., by first
applying $f$ and then~$g$. Of course, this is only possible if the
ranges and domains match, i.e., the range of~$f$ must be a subset of
the domain of~$g$. \oliflabeldef{sfr:rel:ops:sec}{This operation on
functions is the analogue of the operation of relative product on
relations from \olref[rel][ops]{sec}.}{}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{ترکیب توابع}

\begin{explain}
\oliflabeldef{sfr:fun:inv:sec}{در \olref[inv]{sec} دیدیم که
$f^{-1}$، یعنی وارونِ تناظر دوسویی~$f$، خود یک تابع است. عمل دیگری
که روی توابع انجام می‌دهیم، ترکیب است. اکنون می‌توانیم}{می‌توانیم} تابعی جدید را با
ترکیب دو تابع $f$ و~$g$ تعریف کنیم؛ یعنی نخست
$f$ و سپس~$g$ را اعمال کنیم. البته این کار تنها هنگامی ممکن است که
بردها و دامنه‌ها سازگار باشند؛ یعنی بردِ~$f$ باید زیرمجموعه‌ای از
دامنهٔ~$g$ باشد. \oliflabeldef{sfr:rel:ops:sec}{این عمل روی
توابع همانند عمل حاصل‌ضرب نسبی روی
روابط است که در \olref[rel][ops]{sec} معرفی شد.}{}
```

Repair the stacked inverse/ezafe construction without changing either conditional arm. Retain first f then g, range(f) subset domain(g), and the relation-product analogy. D49 directly gives g(f(x)); its later nonempty-intersection sentence is not imported as the OLP total-composition criterion.

Alternatives: No material alternative recorded; none invented.

## FA-0025-C02: Diagram explanation and assignment syntax

Action: correct; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P044, FA-REL-P049.

Source:
```latex
A diagram might help to explain the idea of composition. In
\olref{fig:composition}, we depict two functions $f \colon A \to B$
and $g \colon B \to C$ and their composition~$(\comp{f}{g})$. The
function $(\comp{f}{g}) \colon A \to C$ pairs each !!{element} of~$A$
with !!a{element} of~$C$. We specify which !!{element} of~$C$
!!a{element} of $A$ is paired with as follows: given an input $x \in
A$, first apply the function $f$ to~$x$, which will output some $f(x)
= y \in B$, then apply the function $g$ to~$y$, which will output some
$g(f(x)) = g(y) = z \in C$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
یک نمودار می‌تواند به توضیح ایدهٔ ترکیب کمک کند. در
\olref{fig:composition} دو تابع $f \colon A \to B$
و $g \colon B \to C$ و ترکیبشان~$(\comp{f}{g})$ را نشان می‌دهیم. تابع
$(\comp{f}{g}) \colon A \to C$ به هر عضو از~$A$
عضوی از~$C$ نسبت می‌دهد. برای مشخص کردن اینکه کدام عضو از~$C$
به عضوی از $A$ نسبت داده می‌شود، این روش را به کار می‌بریم: با داشتن ورودی $x \in
A$، نخست تابع $f$ را بر~$x$ اعمال می‌کنیم که مقدار $f(x)
= y \in B$ را به دست می‌دهد؛ سپس تابع $g$ را بر~$y$ اعمال می‌کنیم که مقدار
$g(f(x)) = g(y) = z \in C$ را به دست می‌دهد.
```

Use the canon assignment construction به هر ... نسبت می‌دهد and follow x to y to z. Retain all three types and the order of every formula. The indefinite element token plus ی realizes عضوی correctly; do not delete that suffix or insert a duplicate article. The source arrows are not reversed for Persian.

Alternatives: No material alternative recorded; none invented.

## FA-0025-C03: Composition figure caption

Action: correct; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P049.

Source:
```latex
\begin{figure}
  \olasset[2\olphotowidth]{assets/diagrams/composition.tikz}
  \caption{The composition $g \circ f$ of two functions $f$ and~$g$.}
  \ollabel{fig:composition}
\end{figure}
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{figure}
  \olasset[2\olphotowidth]{assets/diagrams/composition.tikz}
  \caption{$g \circ f$، ترکیب دو تابع $f$ و~$g$.}
  \ollabel{fig:composition}
\end{figure}
\end{explain}
```

Replace the calqued ترکیب ... از دو تابع with a short caption naming g circle f as the composition. Preserve all variables and the asset/figure label.

Alternatives: No material alternative recorded; none invented.

## FA-0025-C04: Composition definition

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P049, FA-OL-CANON-0003:P0015.

Source:
```latex
\begin{defn}[Composition]
Let $f\colon A \to B$ and $g\colon B \to C$ be functions. The
\emph{composition} of $f$ with~$g$ is $\comp{f}{g} \colon A \to C$,
where $(\comp{f}{g})(x) = g(f(x))$.
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}[ترکیب]
فرض کنید $f\colon A \to B$ و $g\colon B \to C$ تابع باشند.
\emph{ترکیبِ} $f$ با~$g$ برابر است با $\comp{f}{g} \colon A \to C$،
که در آن $(\comp{f}{g})(x) = g(f(x))$.
\end{defn}
```

Retain ترکیب and the typed formula from A to C. The verified macro comp(f,g) expands to g circle f, matching g(f(x)). Relative product first R then S matches the same order; no alternative convention is silently introduced.

Alternatives: No material alternative recorded; none invented.

## FA-0025-C05: Successor then doubling example

Action: correct; confidence 2/3: Operation order verified; precise successor label remains provisional.
Canon: FA-REL-P049, FA-REL-P044.

Source:
```latex
\begin{ex}
Consider the functions $f(x) = x + 1$, and $g(x) = 2x$. Since
$(\comp{f}{g})(x) = g(f(x))$, for each input~$x$ you must first take
its successor, then multiply the result by two. So their composition
is given by $(\comp{f}{g})(x) = 2(x+1)$.
\end{ex}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{ex}
توابع $f(x) = x + 1$ و $g(x) = 2x$ را در نظر بگیرید. چون
$(\comp{f}{g})(x) = g(f(x))$، برای هر ورودی~$x$ باید نخست
جانشین آن را بگیرید و سپس حاصل را در دو ضرب کنید. پس ترکیب آن‌ها
به‌وسیلهٔ $(\comp{f}{g})(x) = 2(x+1)$ داده می‌شود.
\end{ex}
```

Standardize جانشین with the reviewed preceding sections and retain first add1, then double. The result is2(x+1), not2x+1. The exact successor noun is a contextual label fixed by the formula, not directly quoted from D49.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Retain the explicit successor-term attestation limitation from0022/0024; do not mistake consistency for a new canon citation.

## FA-0025-C06: Composition of injections: exercise

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P046, FA-REL-P049.

Source:
```latex
\begin{prob}
Show that if $f \colon A \to B$ and $g \colon B \to C$ are both
!!{injective}, then $\comp{f}{g}\colon A \to C$ is !!{injective}.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
نشان دهید اگر $f \colon A \to B$ و $g \colon B \to C$ هر دو
یک‌به‌یک باشند، آنگاه $\comp{f}{g}\colon A \to C$ نیز یک‌به‌یک است.
\end{prob}
```

Keep both injectivity hypotheses and the correct composite type. Equality after g reduces to equality after f, then to input equality. No surjectivity or nonempty assumption is added.

Alternatives: No material alternative recorded; none invented.

## FA-0025-C07: Composition of surjections: exercise

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P046, FA-REL-P049.

Source:
```latex
\begin{prob}
Show that if $f \colon A \to B$ and $g \colon B \to C$ are both
!!{surjective}, then $\comp{f}{g}\colon A \to C$ is !!{surjective}.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
نشان دهید اگر $f \colon A \to B$ و $g \colon B \to C$ هر دو
پوشا باشند، آنگاه $\comp{f}{g}\colon A \to C$ نیز پوشا است.
\end{prob}
```

Keep both surjectivity hypotheses. For a given output, find a preimage under g and then one under f. This single-output existence proof is not a global choice of a right inverse.

Alternatives: No material alternative recorded; none invented.

## FA-0025-C08: Graph of a composite: exercise

Action: correct; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P045, FA-REL-P049, FA-OL-CANON-0003:P0015.

Source:
```latex
\begin{prob}
Suppose $f \colon A \to B$ and $g \colon B \to C$. Show that the graph
of $\comp{f}{g}$ is $R_f \mid R_g$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
فرض کنید $f \colon A \to B$ و $g \colon B \to C$. نشان دهید نمودار
$\comp{f}{g}$ برابر است با $R_f \mid R_g$.
\end{prob}
```

Use attested نمودار and retain graph(comp(f,g))=R_f mid R_g. Relational product uses an intermediate value with f first, g second. Keep the source exercise unsolved.

Alternatives: No material alternative recorded; none invented.

## FA-0026-C01: Partial functions heading and relaxed requirement

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-OL-CANON-0001:P0085, FA-OL-CANON-0003:P0015.

Source:
```latex
\olsection{Partial Functions}

\begin{explain}
It is sometimes useful to relax the definition of function so that it
is not required that the output of the function is defined for all
possible inputs. Such mappings are called \emph{partial functions}.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{توابع جزئی}

\begin{explain}
گاه سودمند است تعریف تابع را چنان تضعیف کنیم که لازم نباشد
خروجی تابع برای همهٔ ورودی‌های ممکن تعریف شده باشد. چنین
نگاشت‌هایی \emph{توابع جزئی} نامیده می‌شوند.
\end{explain}
```

تابع جزئی is directly attested in mathematical logic. Retain allowing undefined inputs, not requiring some inputs to be undefined. The computational witness does not imply that all OLP partial functions are computable.

Alternatives: No material alternative recorded; none invented.

## FA-0026-C02: Partial assignment and actual domain

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-OL-CANON-0001:P0085, FA-OL-CANON-0003:P0015, FA-REL-P044.

Source:
```latex
\begin{defn}
A \emph{partial function} $f \colon A \pto B$ is a mapping which
assigns to every !!{element} of~$A$ at most one !!{element} of~$B$.
If $f$ assigns an element of~$B$ to $x \in A$, we say $f(x)$ is
\emph{defined}, and otherwise \emph{undefined}. If $f(x)$ is defined,
we write $f(x) \fdefined$, otherwise $f(x) \fundefined$. The
\emph{domain} of a partial function~$f$ is the subset of~$A$ where it
is defined, i.e., $\dom{f} = \Setabs{x \in A}{f(x) \fdefined}$.
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}
یک \emph{تابع جزئی} $f \colon A \pto B$ نگاشتی است که
به هر عضو از~$A$ حداکثر یک عضو از~$B$ نسبت می‌دهد.
اگر $f$ عضوی از~$B$ را به $x \in A$ نسبت دهد، می‌گوییم $f(x)$
\emph{تعریف‌شده} است، و در غیر این صورت \emph{تعریف‌نشده}. اگر $f(x)$ تعریف‌شده باشد،
می‌نویسیم $f(x) \fdefined$، وگرنه $f(x) \fundefined$. \emph{دامنهٔ}
تابع جزئی~$f$ زیرمجموعهٔ~$A$ متشکل از همهٔ عناصری است که تابع روی آن‌ها
تعریف شده است؛ یعنی $\dom{f} = \Setabs{x \in A}{f(x) \fdefined}$.
\end{defn}
```

Retain at most one output for each permitted input. Defined and undefined are different statuses, not numeric outputs. The actual domain is the subset of A where values exist, not necessarily all A. Preserve both definedness symbols and the domain comprehension; عضو and عناصر denote the same members, not two mathematical sorts.

Alternatives: No material alternative recorded; none invented.

## FA-0026-C03: Total functions are a special case

Action: retain_after_fresh_review; confidence 2/3: Concept source/canon-grounded; exact total label not directly attested on selected pages.
Canon: FA-OL-CANON-0001:P0085, FA-OL-CANON-0003:P0015, FA-REL-P044.

Source:
```latex
\begin{ex}
Every function $f\colon A \to B$ is also a partial function. Partial
functions that are defined everywhere on~$A$---i.e., what we so far
have simply called a function---are also called \emph{total}
functions.
\end{ex}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{ex}
هر تابع $f\colon A \to B$ یک تابع جزئی نیز هست. توابع
جزئی‌ای که در همه‌جای~$A$ تعریف شده‌اند---یعنی همان توابعی که تاکنون
صرفاً تابع نامیده‌ایم---\emph{تام} نیز نامیده
می‌شوند.
\end{ex}
```

Retain the inclusion of total functions among partial functions and the requirement of definition everywhere on A. تام is a provisional lane label explained completely by this condition; the selected pages do not print the exact label.

Alternatives: کامل risks confusion with logical completeness; changing to it without direct evidence would not improve this passage.

Expert-review question: Seek direct disciplinary evidence for تام or an alternative total-function label in later computability canon expansion; the condition here is unambiguous.

## FA-0026-C04: Reciprocal partial-function example

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P045, FA-OL-CANON-0001:P0085.

Source:
```latex
\begin{ex}
The partial function $f \colon \Real \pto \Real$ given by $f(x) = 1/x$
is undefined for $x = 0$, and defined everywhere else.
\end{ex}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{ex}
تابع جزئی $f \colon \Real \pto \Real$ که با $f(x) = 1/x$
داده می‌شود، در $x = 0$ تعریف‌نشده و در همه‌جای دیگر تعریف‌شده است.
\end{ex}
```

Retain the real reciprocal, undefined at0 and defined elsewhere. Undefined at0 must not be translated as equal to0, infinity, or a missing translation.

Alternatives: No material alternative recorded; none invented.

## FA-0026-C05: Partial inverse exercise

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-OL-CANON-0001:P0085, FA-OL-CANON-0003:P0015, FA-REL-P046, FA-REL-P050.

Source:
```latex
\begin{prob}
Given $f\colon A \pto B$, define the partial function $g\colon B \pto
A$ by: for any $y \in B$, if there is a unique $x \in A$ such that
$f(x) = y$, then $g(y) = x$; otherwise $g(y) \fundefined$.  Show that
if $f$ is injective, then $g(f(x)) = x$ for all $x \in \dom{f}$, and
$f(g(y)) = y$ for all $y \in \ran{f}$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
با داشتن $f\colon A \pto B$، تابع جزئی $g\colon B \pto
A$ را چنین تعریف کنید: برای هر $y \in B$، اگر دقیقاً یک $x \in A$ وجود داشته باشد
چنان‌که $f(x) = y$، آنگاه $g(y) = x$؛ وگرنه $g(y) \fundefined$. نشان دهید
اگر $f$ یک‌به‌یک باشد، آنگاه $g(f(x)) = x$ برای همهٔ $x \in \dom{f}$، و
$f(g(y)) = y$ برای همهٔ $y \in \ran{f}$.
\end{prob}
```

Preserve the general construction of g at values with exactly one preimage, undefined otherwise. Injectivity is required only for the two requested identities over dom(f) and ran(f), not for defining g in the first place. Unique preimages require no Choice. Keep both domain restrictions.

Alternatives: No material alternative recorded; none invented.

## FA-0026-C06: Graph of a partial function

Action: correct; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-REL-P045, FA-OL-CANON-0001:P0085, FA-OL-CANON-0003:P0015.

Source:
```latex
\begin{defn}[Graph of a partial function]
Let $f\colon A \pto B$ be a partial function. The \emph{graph} of~$f$
is the relation $R_f \subseteq A \times B$ defined by
\[
R_f = \Setabs{\tuple{x,y}}{f(x) = y}.
\]
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}[نمودار یک تابع جزئی]
فرض کنید $f\colon A \pto B$ تابعی جزئی باشد. \emph{نمودارِ}~$f$
رابطهٔ $R_f \subseteq A \times B$ است که به‌صورت زیر تعریف می‌شود:
\[
R_f = \Setabs{\tuple{x,y}}{f(x) = y}.
\]
\end{defn}
```

Use نمودار as for the preceding total-function graph and retain the ordered-pair formula. f(x)=y describes defined values only. No pair with an undefined marker is inserted into the graph.

Alternatives: No material alternative recorded; none invented.

## FA-0026-C07: Functional relation and seriality

Action: correct; confidence 2/3: Uniqueness/totality distinction directly grounded; exact serial label remains provisional.
Canon: FA-OL-CANON-0003:P0015, FA-OL-CANON-0001:P0085, FA-REL-P044.

Source:
```latex
\begin{prop}
Suppose $R \subseteq A \times B$ has the property that whenever $Rxy$
and $Rxy'$ then $y = y'$.  Then $R$ is the graph of the partial
function $f\colon A \pto B$ defined by: if there is a $y$ such that
$Rxy$, then $f(x) = y$, otherwise $f(x) \fundefined$.  If $R$ is also
\emph{serial}, i.e., for each $x \in A$ there is a $y \in B$ such that
$Rxy$, then $f$ is total.
\end{prop}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prop}
فرض کنید $R \subseteq A \times B$ این ویژگی را داشته باشد که هرگاه $Rxy$
و $Rxy'$، آنگاه $y = y'$. پس $R$ نمودار تابع جزئی
$f\colon A \pto B$ است که چنین تعریف می‌شود: اگر یک $y$ وجود داشته باشد چنان‌که
$Rxy$، آنگاه $f(x) = y$، وگرنه $f(x) \fundefined$. اگر $R$ افزون بر این
\emph{سریال} باشد، یعنی برای هر $x \in A$ یک $y \in B$ وجود داشته باشد چنان‌که
$Rxy$، آنگاه $f$ تام است.
\end{prop}
```

Use نمودار consistently. Preserve uniqueness per input, the undefined alternative, and the separate seriality/existence condition for totality on A. سریال is retained as an explicitly defined provisional source-label equivalent, not claimed verbatim attested by the selected canon.

Alternatives: چپ‌تام would also require direct lexical evidence; a silent new label would not resolve the attestation gap.

Expert-review question: Exact سریال label needs a direct relational-logic witness in future terminology refinement. Keep the fully stated every-input existence condition whichever label is selected.

## FA-0026-C08: Graph proof for a partial function

Action: retain_after_fresh_review; confidence 3/3: Full aligned wording, hypotheses and mathematical scope checked against frozen source and the cited Persian passages; editorial score, not a probability.
Canon: FA-OL-CANON-0003:P0015, FA-OL-CANON-0001:P0085, FA-REL-P044, FA-REL-P049.

Source:
```latex
\begin{proof}
Suppose there is a $y$ such that $Rxy$.  If there were another $y'
\neq y$ such that $Rxy'$, the condition on $R$ would be
violated. Hence, if there is a $y$ such that $Rxy$, that $y$ is
unique, and so $f$ is well-defined.  Obviously, $R_f = R$ and $f$ is
total if~$R$ is serial.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
فرض کنید یک $y$ وجود دارد چنان‌که $Rxy$. اگر $y'
\neq y$ دیگری وجود داشت چنان‌که $Rxy'$، شرط مربوط به $R$
نقض می‌شد. بنابراین، اگر یک $y$ وجود داشته باشد چنان‌که $Rxy$، آن $y$
یکتا است و ازاین‌رو $f$ خوش‌تعریف است. آشکارا $R_f = R$ و $f$ در صورتی
تام است که~$R$ سریال باشد.
\end{proof}
```

Retain conditional uniqueness rather than claiming an output for every input. That is enough for a well-defined partial function. Seriality supplies totality; with empty A the empty relation is serial and the empty function is total. خوش‌تعریف is directly attested on D49.

Alternatives: No material alternative recorded; none invented.

## Validation boundary

Every substantive source and target character lies in an ordered non-overlapping reviewed span. Formal tokens are checked across inline, bracketed, multline and align mathematics. Text arguments in mathematics are separately aligned and manually reviewed for exact connective, quantifier and number-family meaning.
Finite tests support the written reasoning; they are not universal formal proofs. No new PDF was built or visually certified. Frozen owner inputs and reader releases are unchanged; corrections enter the owner’s normal next-batch build and visual QA.
Attribution: Open Logic Project and contributors, under existing CC BY 4.0 notices. https://github.com/OpenLogicProject/OpenLogic . Existing edition: https://github.com/KokunoYumeto/OpenLogic-fa-ir . Canon sources retain separate rights.
