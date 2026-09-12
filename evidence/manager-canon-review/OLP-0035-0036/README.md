# Persian OpenLogic: equinumerosity and comparing sizes

Complete retrospective source/canon review of OLP-0035 and0036. Nine full Persian scholarly pages were consulted; the embedded Frege quotation was compared with its cited German primary text. Every substantive source and target span is mapped. This is corrected source production, not a compiled-reader or full-corpus certification.

## Review priorities

- Correct both premature g references to f in the two empty-set proof variants (known OLSIZ-006).
- Correct the arbitrary-element diagonal conclusion to all x in A (known OLSIZ-007), and invoke its defining biconditional.
- Distinguish irreflexive from merely not reflexive and extensionality from extension terminology.
- Disclose the Choice background of the general nonenumerability/cardinal-comparison equivalence; do not attach it to Cantor’s theorem.
- Preserve both conditional proof branches and exact Frege/Cantor/Russell citation identities.
- Confidence is editorial 0-3, not calibrated probability. Human review is a later opportunity, not a gate.

## Scholarly pages actually consulted

- نظریهٔ مجموعه‌ها; محسن خانی, افشین زارعی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/jozve-kamel.pdf). PDF SHA-256: dbd518c80232921264ab5d79b79be01fe42efe8c01a766327db248b2d261de04. Canon PDFs are privately retained, not redistributed.
- مبانی منطق و نظریهٔ مجموعه‌ها; محسن خانی; دانشگاه صنعتی اصفهان. [Source](https://mohsen-khani.github.io/logic97-1/jozve/logic-full.pdf). PDF SHA-256: 565558b76701858236844f19663de27ee10a8d72fd8b007e69b85159ac49f86d. Canon PDFs are privately retained, not redistributed.
- ریاضیات گسسته و کاربردها; علیرضا غفاری حدیقه, مگردیچ تومانیان; مؤسسه چاپ و انتشارات دانشگاه جامع امام حسین (ع). [Source](https://hadigheha.github.io/books/teaching/Textbooks/Tarkibiyat.pdf). PDF SHA-256: 8f79c45a926c1cea819c4fefa86383f2a65ae23b1d526baaf99cf2506bb9f317. Canon PDFs are privately retained, not redistributed.
- FA-OL-CANON-0003:P0008, PDF 8, printed 7: First axiom, explicit English footnote extensionality. Direct name and equality-by-identical-membership statement. The page then discusses naive comprehension and Russell; do not import unrestricted comprehension as a sound axiom.
- FA-OL-CANON-0003:P0023, PDF 23, printed 22: Ordering definitions with quantified irreflexivity. Direct irreflexive condition forall x not xRx, distinct from negation of reflexivity. Page introduces well-ordering as equivalent to Choice. Its strict-order convention is not silently substituted for the discrete textbook’s non-strict convention.
- FA-OL-CANON-0003:P0051, PDF 51, printed 50: Equinumerosity/cardinal comparison and empty exception. Direct cardinal comparison/inverse constructions and explicit empty alternative. General reverse preimage selection invokes Choice, but a unique inverse and least occurrence in Nat do not. Visible unrelated notation slips are not copied.
- FA-OL-CANON-0003:P0053, PDF 53, printed 52: Definition10 and Cantor theorem13. Direct infinite enumeration and general Cantor diagonal argument. This page reserves شمارا for cardinality omega; retain the already disclosed OLP inclusive finite/empty convention.
- FA-OL-CANON-0005:P0114, PDF 114, printed 114: Cardinal comparison and finite/countably-infinite distinction. Direct cardinal comparison through injections, with well-ordering/Choice background. The source convention governs inclusive enumerable; a general infinite-set comparison must not be passed off as a Choice-free definition.
- FA-OL-CANON-0005:P0115, PDF 115, printed 115: Cantor theorem263 and diagonal contradiction. Direct singleton injection, diagonal nonmembership and the missing-power-set-image argument. Applies to arbitrary A; Choice is not needed for this theorem.
- FA-REL-P050, PDF 50, printed 40: Composition, inverse, identity. Direct inverse of a bijection and composition conventions. Retain source macro argument order, which its own displayed equation fixes.
- FA-REL-P055, PDF 55, printed 45: Properties of binary relations. Direct property names and quantified definitions. Retain تراگذری in this edition rather than mechanically replacing it with the other canon’s متعدی. Non-symmetry is not asymmetry.
- FA-REL-P056, PDF 56, printed 46: Equivalence relation definition. Direct three-property equivalence definition; equality and congruence examples do not identify equinumerosity with literal set equality.

## FA-0035-C01: Equinumerosity heading

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0005:P0114.

Source:
```latex
\olsection{Equinumerosity}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{هم‌توانی}
```

هم‌توانی follows directly from the canon’s هم‌توان and هم‌اندازه. It means same cardinality, not literal equality or being related by any map.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C02: Intuitive size to arbitrary-set comparison

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0005:P0114.

Source:
```latex
We have an intuitive notion of ``size'' of sets, which works fine for
finite sets. But what about infinite sets? If we want to come up with
a formal way of comparing the sizes of two sets of \emph{any} size, it
is a good idea to start by defining when sets are the same size. Here
is Frege:
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
تصوری شهودی از «اندازه» مجموعه‌ها داریم که برای مجموعه‌های متناهی به‌خوبی
کار می‌کند. اما مجموعه‌های نامتناهی چه؟ اگر بخواهیم روشی صوری برای
مقایسهٔ اندازهٔ دو مجموعه، با \emph{هر} اندازه‌ای که داشته باشند، به
دست دهیم، بهتر
است کار را با تعریف اینکه چه هنگام دو مجموعه هم‌اندازه‌اند آغاز کنیم.
فرگه چنین می‌گوید:
```

Retain finite/infinite contrast and arbitrary sizes. The following historical illustration already belongs to the source; no new analogy companion is inserted.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C03: Frege quotation

Action: correct; confidence 2/3: Editorial0–3, not a calibrated probability. Source meaning checked; the stated convention or historical-evidence limit remains.
Canon: FA-REL-P050, FA-OL-CANON-0003:P0051.

Source:
```latex
\begin{quote}
  If a waiter wants to be sure that he has laid exactly as many knives
  as plates on the table, he does not need to count either of them, if
  he simply lays a knife to the right of each plate, so that every
  knife on the table lies to the right of some plate. The plates and
  knives are thus uniquely correlated to each other, and indeed
  through that same spatial relationship. \citep[\S70]{Frege1884}
\end{quote}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{quote}
  اگر پیشخدمتی بخواهد مطمئن شود که روی میز دقیقاً به تعداد بشقاب‌ها
  چاقو چیده است، لازم نیست هیچ‌یک را بشمارد؛ کافی است در سمت راست هر
  بشقاب یک چاقو بگذارد، به‌گونه‌ای که هر چاقوی روی میز در سمت راست
  یکی از بشقاب‌ها قرار گیرد. به این ترتیب، بشقاب‌ها و چاقوها از هر دو طرف به‌طور
  یکتا با یکدیگر متناظر می‌شوند، آن هم به‌واسطهٔ همان رابطهٔ مکانی.
  \citep[\S70]{Frege1884}
\end{quote}
```

Compared the cited German §70 transcription as ORIGINAL_QUOTATION_PROVENANCE.json. Make uniquely correlated explicitly two-sided, as beiderseits eindeutig states. Preserve waiter, knives, plates, right-side relation and citation key/section. Persian mathematical register uses the canon’s bijective correspondence, not new attribution.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Primary text was checked through a German transcription, not a scanned facsimile. The Persian wording is an editorial translation of the embedded quotation, not an established published Persian translation.

## FA-0035-C04: From illustration to definition

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0005:P0114.

Source:
```latex
The insight of this passage can be brought out through a formal
definition:
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
نکتهٔ این عبارت را می‌توان در قالب تعریفی صوری بیان کرد:
```

Use direct Persian نکتهٔ این عبارت rather than the literal بینش این قطعه. Preserve the function of the sentence: introduce the formal definition.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C05: Definition of equinumerosity

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0005:P0114, FA-REL-P050.

Source:
```latex
\begin{defn}\ollabel{comparisondef}
  $A$ is \emph{equinumerous} with $B$, written $\cardeq{A}{B}$, iff
  there is !!a{bijection} $f \colon A \to B$. 
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}\ollabel{comparisondef}
  مجموعهٔ $A$ با $B$ \emph{هم‌توان} است، که آن را با $\cardeq{A}{B}$
  می‌نویسیم، اگر و تنها اگر تناظر دوسویی به‌صورت
  $f \colon A \to B$ وجود داشته باشد.
\end{defn}
```

Bijection A→B is equivalent to cardeq, with if and only if. Preserve the label and formula; existence of one bijection is sufficient, no canonical bijection required.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C06: Equivalence proposition

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-REL-P056, FA-OL-CANON-0003:P0051.

Source:
```latex
\begin{prop}\ollabel{equinumerosityisequi}
Equinumerosity is an equivalence relation.
\end{prop}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prop}\ollabel{equinumerosityisequi}
هم‌توانی یک رابطهٔ هم‌ارزی است.
\end{prop}
```

Same three-property equivalence relation as in the actual discrete-mathematics definition; no antisymmetry or literal equality condition.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C07: Three proof obligations

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-REL-P055, FA-REL-P056.

Source:
```latex
\begin{proof} 
We must show that equinumerosity is reflexive, symmetric, and
transitive. Let $A, B$, and $C$ be sets.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
باید نشان دهیم که هم‌توانی بازتابی، متقارن و تراگذری است. فرض کنید
$A, B$ و $C$ مجموعه باشند.
```

Retain reflexive, symmetric and transitive as three distinct requirements. تراگذری is directly attested; do not replace it merely because another canon uses متعدی.

Alternatives: متعدی is another consulted canon’s term, but retaining the directly attested تراگذری maintains the existing register.

## FA-0035-C08: Reflexivity by identity

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-REL-P050, FA-REL-P055.

Source:
```latex
\emph{Reflexivity.} The identity map $\Id{A} \colon A \to A$, where
$\Id{A} (x) = x$ for all $x \in A$, is !!a{bijection}. So
$\cardeq{A}{A}$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\emph{بازتابی‌بودن.} نگاشت همانیِ $\Id{A} \colon A \to A$، که در آن
$\Id{A} (x) = x$ برای هر $x \in A$، تناظر دوسویی است. پس
$\cardeq{A}{A}$.
```

Identity map is a bijection even on empty A. Preserve universal x and both occurrences of A.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C09: Symmetry by inverse

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-REL-P050, FA-REL-P055.

Source:
```latex
\emph{Symmetry.} Suppose $\cardeq{A}{B}$, i.e., there is
!!a{bijection} $f\colon A \to B$. Since $f$ is !!{bijective}, its
inverse $f^{-1}$ exists and is also !!{bijective}. Hence,
$f^{-1}\colon B \to A$ is !!a{bijection}, so $\cardeq{B}{A}$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\emph{تقارن.} فرض کنید $\cardeq{A}{B}$؛ یعنی تناظر دوسویی به‌صورت
$f\colon A \to B$ وجود دارد. چون $f$ دوسویی است، معکوس آن
$f^{-1}$ وجود دارد و آن نیز دوسویی است. بنابراین
$f^{-1}\colon B \to A$ تناظر دوسویی است؛ پس $\cardeq{B}{A}$.
```

Use معکوس consistently with the read function canon. Inverse of bijection is total on B and bijective onto A; no inversion of a merely injective map is assumed.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C10: Transitivity by composition

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-REL-P050, FA-REL-P055.

Source:
```latex
\emph{Transitivity.} Suppose that $\cardeq{A}{B}$ and $\cardeq{B}{C}$,
i.e., there are !!{bijection}s $f\colon A \to B$ and $g\colon B \to
C$. Then the composition $\comp{f}{g}\colon A \to C$ is !!{bijective},
so that $\cardeq{A}{C}$.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\emph{تراگذری.} فرض کنید $\cardeq{A}{B}$ و $\cardeq{B}{C}$؛ یعنی
تناظرهای دوسویی زیر وجود دارند: $f\colon A \to B$ و $g\colon B \to
C$. آنگاه ترکیب $\comp{f}{g}\colon A \to C$ دوسویی
است؛ پس $\cardeq{A}{C}$.
\end{proof}
```

Keep f:A→B,g:B→C and source comp(f,g) macro order, consistent with comp(g,f)(n)=f(g(n)) later. Composition of bijections is bijective; empty cases included.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C11: Enumeration invariant proposition

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{prop}
If $\cardeq{A}{B}$, then $A$ is !!{enumerable} if
and only if $B$ is.
\end{prop}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prop}
اگر $\cardeq{A}{B}$، آنگاه $A$ شمارا است اگر
و تنها اگر $B$ چنین باشد.
\end{prop}
```

Enumerable iff the equinumerous set is enumerable. Inclusive finite/empty OLP meaning retained, not only countably infinite.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C12: Conditional definition selection

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{editorial}
The following proof uses \olref[enm]{defn:enumerable} if
\olref[enm]{sec} is included and \olref[enm-alt]{defn:enumerable}
otherwise.
\end{editorial}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{editorial}
برهان زیر از \olref[enm]{defn:enumerable} استفاده می‌کند، اگر
\olref[enm]{sec} گنجانده شده باشد، و در غیر این صورت از
\olref[enm-alt]{defn:enumerable}.
\end{editorial}
```

Retain both definition references and the exact section-availability conditional. Reader selection is not permission to omit alternative source content.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C13: Fixed bijection and repair disclosure

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0051, FA-REL-P050.

Source:
```latex
\begin{proof}
Suppose $\cardeq{A}{B}$, so there is some !!{bijection} $f \colon A
\to B$, and suppose that $A$ is !!{enumerable}.
\oliflabeldef{sfr:siz:enm:defn:enumerable}{
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
فرض کنید $\cardeq{A}{B}$؛ پس یک تناظر دوسویی به‌صورت $f \colon A
\to B$ وجود دارد، و فرض کنید $A$ شمارا است.
\emph{یادداشت ویراستاری:} در حالت تهی، هر دو نسخهٔ برهان در متن مبدأ به‌اشتباه
به تابع برشماری اشاره می‌کردند که در آن حالت معرفی نشده است. نام تابع در
هر دو مورد اصلاح شده تا به تناظر دوسوییِ همین جمله اشاره کند.
\oliflabeldef{sfr:siz:enm:defn:enumerable}{
```

f is fixed before either empty/enumeration case. Explain the two wrong g references as source slips, not a flaw in the proposition; preserve all formal assumptions.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C14: Surjective enumeration branch

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053, FA-REL-P050.

Source:
```latex
Then either $A = \emptyset$ or there is !!a{surjective} function
  $g\colon \PosInt \to A$. If $A = \emptyset$, then $B = \emptyset$
  also (otherwise there would be !!a{element}~$y \in B$ but no $x \in
  A$ with $g(x) = y$). If, on the other hand, $g\colon \PosInt \to A$
  is !!{surjective}, then $\comp{g}{f} \colon \PosInt \to B$ is
  !!{surjective}. To see this, let $y \in B$. Since $f$ is
  !!{surjective}, there is an $x \in A$ such that $f(x) = y$. Since
  $g$ is !!{surjective}, there is an $n \in \PosInt$ such that $g(n) =
  x$. Hence,
\[
(\comp{g}{f})(n) = f(g(n)) = f(x) = y
\]
and thus $\comp{g}{f}$ is !!{surjective}. We have that $\comp{g}{f}$
is an enumeration of~$B$, and so $B$~is !!{enumerable}.}
{
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
آنگاه یا $A = \emptyset$، یا تابعی پوشا به‌صورت
  $g\colon \PosInt \to A$ وجود دارد. اگر $A = \emptyset$، آنگاه $B = \emptyset$
  است (زیرا در غیر این صورت عضو~$y \in B$ وجود می‌داشت،
  اما هیچ عضوی مانند $x \in
  A$ با $f(x) = y$ وجود نداشت). از سوی دیگر، اگر $g\colon \PosInt \to A$
  پوشا باشد، آنگاه $\comp{g}{f} \colon \PosInt \to B$
  پوشا است. برای دیدن این مطلب، $y \in B$ را در نظر بگیرید.
  چون $f$ پوشا است، عضوی مانند $x \in A$ وجود دارد که $f(x) = y$.
  چون $g$ پوشا است، عددی مانند $n \in \PosInt$ وجود دارد که $g(n) =
  x$. بنابراین
\[
(\comp{g}{f})(n) = f(g(n)) = f(x) = y
\]
و در نتیجه $\comp{g}{f}$ پوشا است. پس $\comp{g}{f}$
برشماری‌ای از~$B$ است و بنابراین $B$~شمارا است.}
{
```

Fix only premature g(x)=y to f(x)=y; add missing Persian copula. Empty maps to empty. In nonempty branch retain g:PosInt→A, output witness chain and exact composition equation; no Choice required.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C15: Alternative finite-or-Nat bijection branch

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053, FA-REL-P050.

Source:
```latex
Then either $A  = \emptyset$ or there is !!a{bijection}~$g$ whose
  range is $A$ and whose domain is either $\Nat$ or an initial
  sequence of natural numbers. If $A = \emptyset$, then $B =
  \emptyset$ also (otherwise there would be some~$y \in B$ with no $x
  \in A$ such that $g(x) = y$). So suppose we have our
  !!{bijection}~$g$. Then $\comp{g}{f}$ is !!a{bijection} with
  range~$B$ and domain the same as that of~$g$ (i.e., either $\Nat$ or
  an initial segment of it), so that $B$ is !!{enumerable}.}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
آنگاه یا $A  = \emptyset$، یا یک تناظر دوسویی~$g$ وجود دارد که
  بردش $A$ و دامنه‌اش یا $\Nat$ یا قطعه‌ای آغازین از اعداد طبیعی
  است. اگر $A = \emptyset$، آنگاه $B =
  \emptyset$ است (زیرا در غیر این صورت عضوی مانند~$y \in B$ وجود می‌داشت، اما
  هیچ عضوی مانند $x
  \in A$ نبود که $f(x) = y$). پس فرض کنید تناظر دوسویی~$g$ را
  داریم. آنگاه $\comp{g}{f}$ تناظر دوسویی است که بردش~$B$ و دامنه‌اش
  همان دامنهٔ~$g$ است (یعنی یا $\Nat$ یا قطعه‌ای آغازین از آن)؛ پس
  $B$ شمارا است.}
```

Fix the second premature g(x)=y to f(x)=y. Preserve the finite initial segment/Nat alternatives and the identical domain of the composed bijection; empty branch remains explicit.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C16: Reverse implication

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-REL-P050, FA-OL-CANON-0003:P0051.

Source:
```latex
If $B$ is !!{enumerable}, we obtain that $A$ is !!{enumerable} by
repeating the argument with the !!{bijection} $f^{-1}\colon B \to A$
instead of~$f$. 
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
اگر $B$ شمارا باشد، نتیجه می‌گیریم که $A$ شمارا است؛
کافی است استدلال را با تناظر دوسویی $f^{-1}\colon B \to A$ به‌جای~$f$
تکرار کنیم.
\end{proof}
```

Apply exactly the same argument to f inverse:B→A. Preserve if direction and no additional nonempty hypothesis.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C17: Disjoint union exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0051, FA-REL-P050.

Source:
```latex
\begin{prob}
Show that if $\cardeq{A}{C}$ and $\cardeq{B}{D}$, and $A \cap B =
C \cap D = \emptyset$, then $\cardeq{A \cup B}{C \cup D}$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
نشان دهید اگر $\cardeq{A}{C}$ و $\cardeq{B}{D}$ و $A \cap B =
C \cap D = \emptyset$، آنگاه $\cardeq{A \cup B}{C \cup D}$.
\end{prob}
```

Preserve both disjointness assumptions A∩B=empty and C∩D=empty and both given bijections. The combined bijection is well-defined, injective and onto; no solution inserted.

Alternatives: No material alternative recorded; none invented.

## FA-0035-C18: Infinite enumerable means equinumerous with Nat

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0114.

Source:
```latex
\begin{prob}
Show that if $A$ is infinite and !!{enumerable}, then
$\cardeq{A}{\Nat}$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
نشان دهید اگر $A$ نامتناهی و شمارا باشد، آنگاه
$\cardeq{A}{\Nat}$.
\end{prob}
```

Retain infinite qualifier. Least first-occurrence indices give a bijection without an effective-enumeration assumption or Choice family. Exercise remains unsolved.

Alternatives: No material alternative recorded; none invented.

## FA-0036-C01: Different sizes and Cantor heading

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0005:P0114, FA-OL-CANON-0005:P0115.

Source:
```latex
\olsection{Sets of Different Sizes, and Cantor's Theorem}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{مجموعه‌هایی با اندازه‌های متفاوت و قضیهٔ کانتور}
```

Preserve distinct sizes and named theorem; not just inequivalent notation.

Alternatives: No material alternative recorded; none invented.

## FA-0036-C02: Injection comparison intuition

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0005:P0114.

Source:
```latex
\begin{explain}
We have offered a precise statement of the idea that two sets have the
same size. We can also offer a precise statement of the idea that one
set is smaller than another. Our definition of ``is smaller than (or
equinumerous)'' will require, instead of !!a{bijection} between the
sets, !!a{injection} from the first set to the second. If such a
function exists, the size of the first set is less than or equal to
the size of the second. Intuitively, !!a{injection} from one set to
another guarantees that the range of the function has at least as many
!!{element}s as the domain, since no two !!{element}s of the domain
map to the same !!{element} of the range.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
بیان دقیقی از این اندیشه به دست دادیم که دو مجموعه اندازه‌ای یکسان
دارند. همچنین می‌توانیم این اندیشه را که یک مجموعه از دیگری کوچک‌تر
است به‌دقت بیان کنیم. تعریف ما از «کوچک‌تر از (یا هم‌توان با)» به‌جای
تناظر دوسویی میان مجموعه‌ها، به نگاشت یک‌به‌یک از مجموعهٔ نخست به
مجموعهٔ دوم نیاز دارد. اگر چنین تابعی وجود داشته باشد، اندازهٔ مجموعهٔ
نخست کوچک‌تر یا مساوی اندازهٔ مجموعهٔ دوم است. به‌طور شهودی، وجود
نگاشت یک‌به‌یک از یک مجموعه به مجموعه‌ای دیگر تضمین می‌کند که تعدادِ
اعضا در برد تابع دست‌کم برابر با تعداد آن‌ها در دامنه است، زیرا
هیچ دو عضو متمایز در دامنه به یک عضو در برد
نگاشته نمی‌شوند.
\end{explain}
```

Injection compares source to target and distinct source elements cannot collide. Replace clumsy “two cases of elements” with “two distinct elements”. Domain and actual image are equinumerous; weaker source at-least wording is true, not a defect.

Alternatives: No material alternative recorded; none invented.

## FA-0036-C03: No larger than definition

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0005:P0114.

Source:
```latex
\begin{defn}
$A$ is \emph{no larger than}~$B$, written $\cardle{A}{B}$, iff there
is !!a{injection} $f \colon A \to B$.
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}
مجموعهٔ $A$ از~$B$ \emph{بزرگ‌تر نیست}، که آن را با $\cardle{A}{B}$
می‌نویسیم، اگر و تنها اگر نگاشت یک‌به‌یک به‌صورت $f \colon A \to B$
وجود داشته باشد.
\end{defn}
```

Preserve A≤B by injection A→B and iff; no subset or total order assertion.

Alternatives: No material alternative recorded; none invented.

## FA-0036-C04: Preorder properties

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-REL-P055, FA-REL-P056.

Source:
```latex
It is clear that this is a reflexive and transitive relation, but that
it is not symmetric (this is left as an exercise). We can also
introduce a notion, which states that one set is (strictly) smaller
than another.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
آشکار است که این رابطه بازتابی و تراگذری است، اما متقارن نیست (اثبات
این مطلب به‌عنوان تمرین واگذار می‌شود). همچنین می‌توانیم مفهومی معرفی
کنیم که می‌گوید یک مجموعه به‌طور اکید از دیگری کوچک‌تر است.
```

Reflexive and transitive but not symmetric. Do not translate not symmetric as asymmetric; paired equal-size distinct sets remain related both ways.

Alternatives: No material alternative recorded; none invented.

## FA-0036-C05: Strict comparison definition

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0005:P0114.

Source:
```latex
\begin{defn}
$A$ is \emph{smaller than}~$B$, written $\cardless{A}{B}$, iff there
is !!a{injection}~$f\colon A \to B$ but no !!{bijection}~$g\colon A
\to B$, i.e., $\cardle{A}{B}$ and $\cardneq{A}{B}$.
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}
مجموعهٔ $A$ از~$B$ \emph{کوچک‌تر است}، که آن را با $\cardless{A}{B}$
می‌نویسیم، اگر و تنها اگر نگاشت یک‌به‌یک~$f\colon A \to B$ وجود داشته
باشد، اما هیچ تناظر دوسویی~$g\colon A
\to B$ وجود نداشته باشد؛ یعنی $\cardle{A}{B}$ و $\cardneq{A}{B}$.
\end{defn}
```

Injection exists and no bijection exists. Preserve conjunction and non-equivalence notation, not absence of every reverse injection asserted without justification.

Alternatives: No material alternative recorded; none invented.

## FA-0036-C06: Irreflexivity and comparison convention

Action: correct; confidence 2/3: Editorial0–3, not a calibrated probability. Source meaning checked; the stated convention or historical-evidence limit remains.
Canon: FA-OL-CANON-0003:P0023, FA-REL-P055, FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0114.

Source:
```latex
It is clear that this relation is irreflexive
and transitive. (This is left as an exercise.) Using this notation, we
can say that a set $A$ is !!{enumerable} iff $\cardle{A}{\Nat}$, and
that $A$ is !!{nonenumerable} iff $\cardless{\Nat}{A}$. This allows us
to restate
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
آشکار است که این رابطه پادبازتابی و تراگذری است. پادبازتابی یعنی هیچ مجموعه‌ای به‌طور اکید از خودش کوچک‌تر نیست. (اثبات این مطلب
به‌عنوان تمرین واگذار می‌شود.) با این نمادگذاری می‌توانیم بگوییم
مجموعهٔ $A$ شمارا است اگر و تنها اگر $\cardle{A}{\Nat}$، و
$A$ ناشمارا است اگر و تنها اگر $\cardless{\Nat}{A}$.
\emph{یادداشت دربارهٔ فرض‌ها:} هم‌ارزیِ دوم، دربارهٔ ناشمارایی، در اینجا با
فرض اصل انتخاب بیان می‌شود: تحت این فرض، هر مجموعهٔ نامتناهی زیرمجموعه‌ای
شمارای نامتناهی دارد. هم‌ارزیِ نخست، دربارهٔ شمارابودن، و قضیهٔ کانتور در
ادامه به این فرض نیاز ندارند.
این نمادگذاری به ما اجازه می‌دهد
```

Replace ambiguous غیربازتابی by directly attested پادبازتابی, explaining no set is strictly smaller than itself. This explanation defines irreflexivity only, not transitivity. Keep transitivity and exercises. Enumerable iff injection into Nat is Choice-free; attach the explicit Choice background only to the subsequent nonenumerability iff Nat<A statement.

Alternatives: No material alternative recorded; none invented.

Expert-review question: The source leaves its Choice background implicit. The candidate discloses a sufficient standard assumption; it does not claim full Choice is the weakest necessary principle. Review this editorial convention without weakening either original equivalence or Cantor’s theorem.

## FA-0036-C07: Alternative restatements and Cantor attribution

Action: retain_after_fresh_review; confidence 2/3: Editorial0–3, not a calibrated probability. Source meaning checked; the stated convention or historical-evidence limit remains.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\oliflabeldef{sfr:siz:nen-alt:thm:nonenum-pownat}{%
\olref[sfr][siz][nen-alt]{thm:nonenum-pownat}
as the observation that
$\cardless{\Nat}{\Pow{\Nat}}$}{%
\olref[sfr][siz][nen]{thm:nonenum-pownat}
as the observation that $\cardless{\PosInt}{\Pow{\PosInt}}$}. In fact,
\citet{Cantor1892} proved that this last point is \emph{perfectly
general}:
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\oliflabeldef{sfr:siz:nen-alt:thm:nonenum-pownat}{%
\olref[sfr][siz][nen-alt]{thm:nonenum-pownat}
را به‌صورت مشاهدهٔ
$\cardless{\Nat}{\Pow{\Nat}}$ بازگو کنیم}{%
\olref[sfr][siz][nen]{thm:nonenum-pownat}
را به‌صورت مشاهدهٔ $\cardless{\PosInt}{\Pow{\PosInt}}$ بازگو کنیم}. در واقع،
\citet{Cantor1892} ثابت کرد که این نکته \emph{کاملاً کلی} است:
```

Preserve both conditional Nat/PosInt theorem restatements and Cantor1892 citation. Generality is checked mathematically for arbitrary A.

Alternatives: No material alternative recorded; none invented.

Expert-review question: The mathematical theorem is checked against both Persian canon and source proof; the precise Cantor1892 bibliographic date is retained from source, not newly verified from its original journal printing.

## FA-0036-C08: Cantor theorem includes every set

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{thm}[Cantor]\ollabel{thm:cantor}
$\cardless{A}{\Pow{A}}$, for any set $A$.
\end{thm}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{thm}[کانتور]\ollabel{thm:cantor}
$\cardless{A}{\Pow{A}}$ برای هر مجموعهٔ $A$ برقرار است.
\end{thm}
```

Strict inequality A<Pow(A) for all sets including empty. The preceding Choice note must not narrow this theorem.

Alternatives: No material alternative recorded; none invented.

## FA-0036-C09: Singleton injection and extensionality

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0008, FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{proof}
The map $f(x) = \{x\}$ is !!a{injection} $f \colon A \to \Pow{A}$,
since if $x \neq y$, then also $\{x\} \neq \{y\}$ by extensionality,
and so $f(x) \neq f(y)$. So we have that $\cardle{A}{\Pow{A}}$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
نگاشت $f(x) = \{x\}$، نگاشت یک‌به‌یک به‌صورت $f \colon A \to \Pow{A}$
است، زیرا اگر $x \neq y$، آنگاه بنا بر اصل گسترش،
$\{x\} \neq \{y\}$ نیز برقرار است و بنابراین $f(x) \neq f(y)$.
پس $\cardle{A}{\Pow{A}}$.
```

Correct اصل امتداد to directly attested اصل گسترش with English extensionality footnote in canon. Distinct singleton sets and injection formula unchanged.

Alternatives: No material alternative recorded; none invented.

## FA-0036-C10: Proof variant editorial

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{editorial}
We present the slow proof if \olref[nen]{sec} is
present, otherwise a faster proof matching \olref[nen-alt]{sec}.
\end{editorial}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{editorial}
اگر \olref[nen]{sec} موجود باشد برهان تفصیلی را می‌آوریم، وگرنه برهان
سریع‌تری را که با \olref[nen-alt]{sec} مطابقت دارد ارائه می‌کنیم.
\end{editorial}
```

Preserve availability-controlled detailed/short proof alternatives and both section links.

Alternatives: No material alternative recorded; none invented.

## FA-0036-C11: Detailed diagonal proof

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0008, FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\oliflabeldef{sfr:siz:nen:sec}{% 
  We will now show that there cannot be !!a{surjective} function~$g\colon A \to
  \Pow{A}$, let alone !!a{bijective} one, and hence that
  $\cardneq{A}{\Pow{A}}$. For suppose that $g\colon A \to \Pow{A}$.
  Since $g$ is total, every $x \in A$ is mapped to a subset $g(x)
  \subseteq A$. We can show that $g$ cannot be surjective. To do this, we
  define a subset~$\overline{A} \subseteq A$ which by definition cannot be in the
  range of~$g$. Let
  \[
  \overline{A} = \Setabs{x \in A}{x \notin g(x)}.
  \]
  Since $g(x)$ is defined for all $x \in A$, $\overline{A}$ is clearly
  a well-defined subset of~$A$.  But, it cannot be in the range
  of~$g$. Let $x \in A$ be arbitrary, we will show that $\overline{A} \neq
  g(x)$.  If $x \in g(x)$, then it does not satisfy $x \notin g(x)$,
  and so by the definition of~$\overline{A}$, we have $x \notin
  \overline{A}$.  If $x \in \overline{A}$, it must satisfy the
  defining property of~$\overline{A}$, i.e., $x \in A$ and $x \notin
  g(x)$. Since $x$ was arbitrary, this shows that for each $x \in
  \overline{A}$, $x \in g(x)$ iff $x \notin \overline{A}$, and so
  $g(x) \neq \overline{A}$.  In other words, $\overline{A}$ cannot be
  in the range of~$g$, contradicting the assumption that~$g$ is
  surjective.}{
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\oliflabeldef{sfr:siz:nen:sec}{%
  اکنون نشان می‌دهیم که هیچ تابع پوشا به‌صورت~$g\colon A \to
  \Pow{A}$ نمی‌تواند وجود داشته باشد، چه رسد به تابعی دوسویی؛
  و ازاین‌رو $\cardneq{A}{\Pow{A}}$. فرض کنید $g\colon A \to \Pow{A}$.
  چون $g$ در همهٔ دامنه‌اش تعریف شده است، هر $x \in A$ به زیرمجموعه‌ای مانند $g(x)
  \subseteq A$ نگاشته می‌شود. می‌توانیم نشان دهیم که $g$ نمی‌تواند
  پوشا باشد. برای این کار، زیرمجموعه‌ای مانند~$\overline{A} \subseteq A$
  تعریف می‌کنیم که بنا بر تعریف نمی‌تواند در بردِ~$g$ باشد. بگذارید
  \[
  \overline{A} = \Setabs{x \in A}{x \notin g(x)}.
  \]
  چون $g(x)$ برای همهٔ $x \in A$ تعریف شده است، $\overline{A}$ به‌روشنی
  زیرمجموعه‌ای خوش‌تعریف از~$A$ است. اما نمی‌تواند در بردِ~$g$ باشد.
  $x \in A$ را دلخواه بگیرید؛ نشان می‌دهیم $\overline{A} \neq
  g(x)$. اگر $x \in g(x)$، آنگاه شرط $x \notin g(x)$ را برآورده
  نمی‌کند؛ پس بنا بر تعریفِ~$\overline{A}$، داریم $x \notin
  \overline{A}$. اگر $x \in \overline{A}$، باید ویژگی معرفِ
  $\overline{A}$ را برآورده کند؛ یعنی $x \in A$ و $x \notin
  g(x)$. با توجه به تعریفِ مجموعه و دلخواه‌بودنِ $x$، برای هر $x \in
  A$، $x \in g(x)$ اگر و تنها اگر $x \notin \overline{A}$؛
  پس $g(x) \neq \overline{A}$. به‌عبارت دیگر، $\overline{A}$ نمی‌تواند
  در بردِ~$g$ باشد و این با فرض پوشابودنِ~$g$ تناقض دارد.
  \emph{یادداشت ویراستاری:} در نتیجه‌گیریِ متن مبدأ، متغیر به‌اشتباه فقط بر
  مجموعهٔ قطری کمیت‌گذاری شده بود. نتیجه باید برای همهٔ ورودی‌های تابع
  برقرار باشد؛ دامنهٔ کمیت‌گذاری در اینجا اصلاح شده است.}{
```

Unpack total as defined at every input. Keep diagonal definition and all membership directions. Repair the conclusion from x in diagonal subset to arbitrary x in A; explicitly invoke the definition for the iff rather than pretend the preceding two incompatibility statements alone prove it. Source finding OLSIZ-007 is disclosed; theorem unchanged.

Alternatives: No material alternative recorded; none invented.

## FA-0036-C12: Short contradiction proof

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0008, FA-OL-CANON-0005:P0115.

Source:
```latex
It remains to show that $\cardneq{A}{\Pow{A}}$. For
  reductio, suppose $\cardeq{A}{\Pow{A}}$, i.e., there is some
  !!{bijection} $g \colon A \to \Pow{A}$. Now consider:
  \[
    D = \Setabs{x \in A}{x \notin g(x)}
  \]
  Note that $D \subseteq A$, so that $D \in \Pow{A}$. Since $g$ is
  !!a{bijection}, there is some $y \in A$ such that $g(y) = D$. But
  now we have:
  \[
    y \in g(y) \text{ iff } y \in D \text{ iff } y \notin g(y).
  \]
  This is a contradiction; so $\cardneq{A}{\Pow{A}}$.}{}
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
هنوز باید
  نشان دهیم $\cardneq{A}{\Pow{A}}$. برای برهان خلف، فرض کنید
  $\cardeq{A}{\Pow{A}}$؛ یعنی یک تناظر دوسویی به‌صورت
  $g \colon A \to \Pow{A}$ وجود دارد. اکنون در نظر بگیرید:
  \[
    D = \Setabs{x \in A}{x \notin g(x)}
  \]
  توجه کنید که $D \subseteq A$؛ پس $D \in \Pow{A}$. چون $g$
  تناظر دوسویی است، عضوی مانند $y \in A$ وجود دارد که $g(y) = D$. اما اکنون
  داریم:
  \[
    y \in g(y) \text{ اگر و تنها اگر } y \in D \text{ اگر و تنها اگر } y \notin g(y).
  \]
  این تناقض است؛ پس $\cardneq{A}{\Pow{A}}$.}{}
\end{proof}
```

Retain D subset A, hence D in Pow(A), surjectivity witness y and both iff links. Use natural برهان خلف; no additional Choice needed.

Alternatives: No material alternative recorded; none invented.

## FA-0036-C13: Detailed comparison to countable diagonal

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{explain}
\oliflabeldef{sfr:siz:nen:thm:nonenum-pownat}{It's instructive to
  compare the proof of \olref{thm:cantor} to that of
  \olref[nen]{thm:nonenum-pownat}. There we showed that for any list
  $Z_1$, $Z_2$, \dots, of subsets of~$\PosInt$ one can construct a
  set~$\overline{Z}$ of numbers guaranteed not to be on the list. It
  was guaranteed not to be on the list because, for every $n \in
  \PosInt$, $n \in Z_n$ iff $n \notin \overline{Z}$. This way, there
  is always some number that is !!a{element} of one of $Z_n$ or
  $\overline{Z}$ but not the other. We follow the same idea here,
  except the indices~$n$ are now !!{element}s of~$A$ instead
  of~$\PosInt$. The set $\overline{A}$ is defined so that it is
  different from~$g(x)$ for each $x \in A$, because $x \in g(x)$ iff
  $x \notin \overline{A}$. Again, there is always !!a{element} of~$A$
  which is !!a{element} of one of $g(x)$ and $\overline{A}$ but not
  the other. And just as $\overline{Z}$ therefore cannot be on the
  list $Z_1$, $Z_2$, \dots, $\overline{A}$ cannot be in the range
  of~$g$.}{}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
\oliflabeldef{sfr:siz:nen:thm:nonenum-pownat}{مقایسهٔ برهان
  \olref{thm:cantor} با برهانِ
  \olref[nen]{thm:nonenum-pownat} آموزنده است. آنجا نشان دادیم که برای
  هر فهرستِ $Z_1$، $Z_2$، \dots از زیرمجموعه‌های~$\PosInt$ می‌توان
  مجموعه‌ای از اعداد به‌صورت~$\overline{Z}$ ساخت که تضمین شده است در
  فهرست نباشد. این مجموعه از آن رو در فهرست نبود که برای هر $n \in
  \PosInt$، $n \in Z_n$ اگر و تنها اگر $n \notin \overline{Z}$. به
  این ترتیب، همیشه عددی وجود دارد که عضو یکی از $Z_n$ یا
  $\overline{Z}$ است، اما عضو آن دیگری نیست. در اینجا نیز از همان اندیشه
  پیروی می‌کنیم، جز اینکه شاخص‌های~$n$ اکنون از جملهٔ اعضا در~$A$ هستند،
  نه عضوهای~$\PosInt$. مجموعهٔ $\overline{A}$ چنان تعریف می‌شود که
  با~$g(x)$ برای هر $x \in A$ متفاوت باشد، زیرا $x \in g(x)$ اگر و تنها
  اگر $x \notin \overline{A}$. باز به ازای هر ورودی، خودِ همان عضوِ~$A$
  عضو یکی از $g(x)$ و $\overline{A}$ است، اما عضو آن دیگری
  نیست. همان‌گونه که $\overline{Z}$ ازاین‌رو نمی‌تواند در فهرستِ
  $Z_1$، $Z_2$، \dots باشد، $\overline{A}$ نیز نمی‌تواند در بردِ~$g$
  باشد.}{}
```

The arbitrary index generalizes from positive integers to elements of A. Clarify that the differing element is the chosen input, not an unconditional assertion A nonempty. Preserve every source label and equation.

Alternatives: No material alternative recorded; none invented.

## FA-0036-C14: Alternative zero-based comparison

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\oliflabeldef{sfr:siz:nen-alt:thm:nonenum-pownat}{It's instructive to
  compare the proof of \olref{thm:cantor} to that of
  \olref[nen-alt]{thm:nonenum-pownat}. There we showed that for any
  list $N_0$, $N_1$, $N_2$, \dots, of subsets of~$\Nat$ we can construct a
  set~$D$ of numbers guaranteed not to be on the list. It was
  guaranteed not to be on the list because $n \in N_n$ iff $n \notin
  D$, for every $n \in \Nat$. We follow the same idea here, except the
  indices~$n$ are now !!{element}s of~$A$ rather than of~$\Nat$. The
  set $D$ is defined so that it is different from~$g(x)$ for each $x
  \in A$, because $x \in g(x)$ iff $x \notin D$.}{}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\oliflabeldef{sfr:siz:nen-alt:thm:nonenum-pownat}{مقایسهٔ برهان
  \olref{thm:cantor} با برهانِ
  \olref[nen-alt]{thm:nonenum-pownat} آموزنده است. آنجا نشان دادیم که
  برای هر فهرستِ $N_0$، $N_1$، $N_2$، \dots از زیرمجموعه‌های~$\Nat$
  می‌توان مجموعه‌ای از اعداد به‌صورت~$D$ ساخت که تضمین شده است در
  فهرست نباشد. این مجموعه از آن رو در فهرست نبود که
  $n \in N_n$ اگر و تنها اگر $n \notin
  D$، و این برای هر $n \in \Nat$ برقرار است. در اینجا نیز از همان اندیشه پیروی می‌کنیم،
  جز اینکه شاخص‌های~$n$ اکنون از جملهٔ اعضا در~$A$ هستند، نه عضوهای~$\Nat$.
  مجموعهٔ $D$ چنان تعریف می‌شود که با~$g(x)$ برای هر $x
  \in A$ متفاوت باشد، زیرا $x \in g(x)$ اگر و تنها اگر $x \notin D$.}{}
```

Preserve N_0,N_1 list and n in Nat, distinct from the prior one-based list. Same diagonal membership equivalence, no reindexing error.

Alternatives: No material alternative recorded; none invented.

## FA-0036-C15: Russell comparison and historical statement

Action: retain_after_fresh_review; confidence 2/3: Editorial0–3, not a calibrated probability. Source meaning checked; the stated convention or historical-evidence limit remains.
Canon: FA-OL-CANON-0003:P0008, FA-OL-CANON-0005:P0115.

Source:
```latex
The proof is also worth comparing with the proof of Russell's Paradox,
\olref[sfr][set][rus]{thm:russells-paradox}. Indeed, Cantor's Theorem was
the inspiration for Russell's own paradox.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
این برهان را همچنین می‌توان با برهان پارادوکس راسل مقایسه کرد:
\olref[sfr][set][rus]{thm:russells-paradox}. در واقع قضیهٔ کانتور الهام‌بخش
پارادوکس خود راسل بود.
\end{explain}
```

Retain comparison with Russell’s paradox and exact source reference. K8 displays the analogous membership contradiction, not an attestation of the historical causal claim.

Alternatives: No material alternative recorded; none invented.

Expert-review question: The statement about historical inspiration is retained as a source historical claim; this pass does not claim original archival confirmation. The mathematical comparison is directly checked.

## FA-0036-C16: No injection from powerset to set exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and directly relevant scholarly construction checked.
Canon: FA-OL-CANON-0003:P0008, FA-OL-CANON-0003:P0051, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{prob}
  Show that there cannot be !!a{injection} $g\colon \Pow{A} \to
  A$, for any set~$A$. Hint: Suppose $g\colon \Pow{A} \to A$ is
  !!{injective}. Consider $D = \Setabs{g(B)}{B \subseteq A \text{ and
  } g(B) \notin B}$. Let $x = g(D)$. Use the fact that $g$ is
  !!{injective} to derive a contradiction. 
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
  نشان دهید هیچ نگاشت یک‌به‌یک به‌صورت $g\colon \Pow{A} \to
  A$ برای هیچ مجموعهٔ~$A$ نمی‌تواند وجود داشته باشد. راهنمایی: فرض کنید
  $g\colon \Pow{A} \to A$
  یک‌به‌یک است. $D = \Setabs{g(B)}{B \subseteq A \text{ و
  } g(B) \notin B}$ را در نظر بگیرید. بگذارید $x = g(D)$. با استفاده
  از این واقعیت که $g$ یک‌به‌یک است، تناقضی به دست آورید.
\end{prob}
```

Preserve reversed arrow Pow(A)→A, all A, injectivity assumption, the image-set D and x=g(D). Check both x∈D and x∉D yield contradictions using injectivity. The inline math-text and is preserved; no hidden solution added.

Alternatives: No material alternative recorded; none invented.

## Validation boundary

Every substantive source and target character lies in an ordered non-overlapping reviewed span. Formal tokens are checked across inline, bracketed, multline and align mathematics. Text arguments in mathematics are separately aligned and manually reviewed for exact connective, quantifier and number-family meaning.
Finite tests support the written reasoning; they are not universal formal proofs. No new PDF was built or visually certified. Frozen owner inputs and reader releases are unchanged; corrections enter the owner’s normal next-batch build and visual QA.
Attribution: Open Logic Project and contributors, under existing CC BY 4.0 notices. https://github.com/OpenLogicProject/OpenLogic . Existing edition: https://github.com/KokunoYumeto/OpenLogic-fa-ir . Canon sources retain separate rights.
