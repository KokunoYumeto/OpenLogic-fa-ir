# Persian OpenLogic: sizes of sets and enumerations

Complete retrospective source/canon review of OLP-0027–0030, including the substantive chapter wrapper. Six full Persian scholarly pages were actually consulted. Corrected candidates and aligned choices are production inputs, not a rebuilt reader or full-corpus certification. The attempted independent reviewer failed before producing a report; mathematical review here is by the main agent, not an independent certification.

## Review priorities

- Preserve the historical book title Open Set Theory; it does not mean the theory of topologically open sets.
- Keep OpenLogic countability inclusive of finite and empty sets, explicitly distinguishing the narrower usage in the consulted Persian set-theory notes.
- Restore the missing seventh value, negative three, in the integer-enumeration table; preserve all other formal mathematics.
- State the finite-position requirement independently of the immediate-predecessor condition; make the finite-diagonal proof and zero-power case explicit.
- Keep arbitrary enumerability distinct from computable enumerability, and ordinal enumeration distinct from an ordinary finite-position list.
- Confidence is editorial 0-3, not calibrated probability. Human review is a later opportunity, not a gate.

## Scholarly pages actually consulted

- نظریهٔ مجموعه‌ها; محسن خانی, افشین زارعی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/jozve-kamel.pdf). PDF SHA-256: dbd518c80232921264ab5d79b79be01fe42efe8c01a766327db248b2d261de04. Canon PDFs are privately retained, not redistributed.
- ریاضیات گسسته و کاربردها; علیرضا غفاری حدیقه, مگردیچ تومانیان; مؤسسه چاپ و انتشارات دانشگاه جامع امام حسین (ع). [Source](https://hadigheha.github.io/books/teaching/Textbooks/Tarkibiyat.pdf). PDF SHA-256: 8f79c45a926c1cea819c4fefa86383f2a65ae23b1d526baaf99cf2506bb9f317. Canon PDFs are privately retained, not redistributed.
- FA-OL-CANON-0003:P0051, PDF 51, printed 50: Lemmas5–6: equinumerosity, size and injection/surjection. Direct size, initial-segment and injection/surjection register. The page uses Choice in the general reverse-selection implication and has proof-level notation slips; do not import those slips or impose Choice on natural-number least-preimage selection.
- FA-OL-CANON-0003:P0053, PDF 53, printed 52: Definition10, enumeration of ordinal classes, and Cantor theorem. Definition10 reserves شمارا for sets equinumerous with omega, unlike the inclusive OLP convention. A visible editorial convention note preserves OLP finite and empty cases. شمارش here can be transfinite; OLP برشماری is a finite-position list, not an ordinal-indexed generalization.
- FA-REL-P044, PDF 44, printed 34: Function assignment and domain/codomain/range. Exact unique-value assignment and domain/range language; no computational restriction is implied.
- FA-REL-P045, PDF 45, printed 35: Integer floor/ceiling and function graph. Direct ceiling definition as the least integer at least as large as the input, including negative inputs. Preserve OLP integer formula; do not copy unrelated numerical examples.
- FA-REL-P046, PDF 46, printed 36: Injective and surjective functions. At most one preimage versus at least one; terms explain the different functions used to enumerate sets. Onto the stated codomain is not the same as onto a restricted range.
- FA-REL-P050, PDF 50, printed 40: Function composition and inverse of a bijection. Direct bijection and inverse register. Supports index-shift inverses and distinct-input reasoning, not an infinite choice principle.

## FA-0027-C01: Chapter title

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051.

Source:
```latex
\olchapter{sfr}{siz}{The Size of Sets}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olchapter{sfr}{siz}{اندازهٔ مجموعه‌ها}
```

اندازه means set size/cardinality, not geometric area. Keep the exact chapter id and title role.

Alternatives: No material alternative recorded; none invented.

## FA-0027-C02: Two source routes and finite initial segments

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053, FA-REL-P046, FA-REL-P050.

Source:
```latex
\begin{editorial}
This chapter discusses enumerations, countability and uncountability.
Several sections come in two versions: a more elementary one, that
takes enumerations to be lists, or surjections from $\PosInt$; and a
more abstract one that defines enumerations as bijections with $\Nat$.
\end{editorial}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{editorial}
این فصل به برشماری‌ها، شمارایی و ناشمارایی می‌پردازد. چند بخش در دو
روایت آمده‌اند: روایتی مقدماتی‌تر که برشماری‌ها را فهرست‌ها، یا توابع
پوشا از $\PosInt$، در نظر می‌گیرد؛ و روایتی انتزاعی‌تر که برشماری‌ها را
تناظرهای دوسویی با $\Nat$ یا با بخشی ابتدایی از آن تعریف می‌کند.
\end{editorial}
```

Preserve elementary listing/surjection versus bijective alternative. Add the finite initial-segment qualification that the same source wrapper states later; the first overview must not appear to exclude all finite sets. This is reconciliation within the source, not a new definition.

Alternatives: No material alternative recorded; none invented.

## FA-0027-C03: Main chapter import sequence

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051.

Source:
```latex
\olimport{introduction}

\olimport{enumerability}

\olimport{zig-zag}

\olimport{pairing}

\olimport{pairing-alt}

\olimport{non-enumerability}

\olimport{reduction}

\olimport{equinumerous-sets}

\olimport{comparing-size}

\olimport{schroder-bernstein}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olimport{introduction}

\olimport{enumerability}

\olimport{zig-zag}

\olimport{pairing}

\olimport{pairing-alt}

\olimport{non-enumerability}

\olimport{reduction}

\olimport{equinumerous-sets}

\olimport{comparing-size}

\olimport{schroder-bernstein}
```

Preserve all ten main imports in order, including pairing-alt. These are build identifiers, not prose to translate or claims that this packet reviews the imported files.

Alternatives: No material alternative recorded; none invented.

## FA-0027-C04: Historical title and alternative register

Action: correct; confidence 2/3: Editorial0–3, not a calibrated probability. Mathematical scope checked; precise terminology or explanatory convention is contextual and its evidence limit is stated.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053, FA-REL-P050.

Source:
```latex
\begin{editorial}
The following \olref[sfr][siz][enm-alt]{sec},
\olref[sfr][siz][nen-alt]{sec}, \olref[sfr][siz][red-alt]{sec} are
alternative versions of \olref[sfr][siz][enm]{sec},
\olref[sfr][siz][nen]{sec}, \olref[sfr][siz][red]{sec} due to Tim
Button for use in his Open Set Theory text. They are slightly more
advanced and use a difference definition of enumerability more
suitable in a set theory context (i.e., bijection with $\Nat$ or an
initial segment, rather than being listable or being the range of a
surjective function from $\PosInt$).
\end{editorial}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{editorial}
بخش‌های زیر، یعنی \olref[sfr][siz][enm-alt]{sec}،
\olref[sfr][siz][nen-alt]{sec} و \olref[sfr][siz][red-alt]{sec}،
روایت‌های جایگزینی از \olref[sfr][siz][enm]{sec}،
\olref[sfr][siz][nen]{sec} و \olref[sfr][siz][red]{sec} هستند که تیم
باتن برای استفاده در کتاب خود با عنوان «Open Set Theory» نوشته
است. این روایت‌ها اندکی پیشرفته‌ترند و تعریفی متفاوت از
شمارایی را به کار می‌گیرند که برای بافت نظریهٔ مجموعه‌ها مناسب‌تر
است (یعنی تناظر دوسویی با $\Nat$ یا یک بخش ابتدایی، نه
فهرست‌پذیر بودن یا برد تابعی پوشا از $\PosInt$ بودن).
\end{editorial}
```

Restore original title Open Set Theory: the previous Persian meant theory of open sets, changing subject. Author UCL OER page explicitly identifies that historical title; it is separately referenced in TITLE_PROVENANCE.json. Keep author attribution, all six section references and both alternative definitions. Use attested بخش ابتدایی and consistent شمارایی. Correct source English difference to intended different, not to mathematical subtraction.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Retain the original English title for exact attribution; no established Persian published title was evidenced. برشماری is a contextually explained list label, not a claim that this canon uses it verbatim.

## FA-0027-C05: Alternative imports and chapter hook

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051.

Source:
```latex
\olimport{enumerability-alt}
\olimport{non-enumerability-alt}
\olimport{reduction-alt}

\OLEndChapterHook
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olimport{enumerability-alt}
\olimport{non-enumerability-alt}
\olimport{reduction-alt}

\OLEndChapterHook
```

Preserve all three alternative imports and the end hook. No content omitted as invisible editorial material.

Alternatives: No material alternative recorded; none invented.

## FA-0028-C01: Introduction heading

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051.

Source:
```latex
\olsection{Introduction}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{مقدمه}
```

Retain مقدمه and section identifier.

Alternatives: No material alternative recorded; none invented.

## FA-0028-C02: Cantor history and size comparison

Action: correct; confidence 2/3: Editorial0–3, not a calibrated probability. Mathematical scope checked; precise terminology or explanatory convention is contextual and its evidence limit is stated.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053.

Source:
```latex
When Georg Cantor developed set theory in the 1870s, one of his aims
was to make palatable the idea of an infinite collection---an actual
infinity, as the medievals would say.  A key part of this was his
treatment of the \emph{size} of different sets. If $a$, $b$ and $c$ are
all distinct, then the set $\{a, b, c\}$ is intuitively \emph{larger}
than $\{a, b\}$. But what about infinite sets? Are they all as large
as each other? It turns out that they are not.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
هنگامی که گئورگ کانتور در دههٔ ۱۸۷۰ نظریهٔ مجموعه‌ها را پروراند، یکی
از هدف‌هایش پذیرفتنی‌ساختن اندیشهٔ یک گردایهٔ نامتناهی بود---یک بی‌نهایتِ
بالفعل، به تعبیر اندیشمندان قرون وسطی. بخش کلیدی این کار، شیوهٔ پرداخت
او به \emph{اندازهٔ} مجموعه‌های گوناگون بود. اگر $a$، $b$ و $c$
همگی متمایز باشند، آنگاه مجموعهٔ $\{a, b, c\}$ به‌طور شهودی
\emph{بزرگ‌تر} از $\{a, b\}$ است. اما مجموعه‌های نامتناهی چطور؟ آیا
همهٔ آن‌ها هم‌اندازه‌اند؟ معلوم می‌شود که چنین نیست.
```

Preserve the1870s, actual-infinity versus potential-infinity context, all-distinct hypothesis and size comparison. بی‌نهایت is the Persian noun in the actual-infinity phrase; the selected math canon supports finite/infinite contrasts, not this specific philosophical history. Source authority supplies that claim.

Alternatives: No material alternative recorded; none invented.

Expert-review question: بالفعل is a contextual philosophical qualifier here; exact historical/philosophical phrasing is not attested in these mathematical pages. Do not represent the source historical assertion as independently historiographically audited.

## FA-0028-C03: Listing finite and infinite sets

Action: correct; confidence 2/3: Editorial0–3, not a calibrated probability. Mathematical scope checked; precise terminology or explanatory convention is contextual and its evidence limit is stated.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044.

Source:
```latex
The first important idea here is that of an enumeration.  We can
list every finite set by listing all its !!{element}s.  For some
infinite sets, we can also list all their !!{element}s if we allow the
list itself to be infinite. Such sets are called !!{enumerable}.
Cantor's surprising result, which we will fully understand by the end
of this chapter, was that some infinite sets are not !!{enumerable}.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
نخستین اندیشهٔ مهم در اینجا مفهوم برشماری، یعنی فهرست‌کردن اعضا، است. می‌توانیم هر مجموعهٔ
متناهی را با فهرست‌کردن همهٔ اعضا آن برشماریم. دربارهٔ برخی
مجموعه‌های نامتناهی نیز، اگر اجازه دهیم خود فهرست نامتناهی باشد،
می‌توانیم همهٔ اعضا آن‌ها را فهرست کنیم. چنین مجموعه‌هایی
شمارا نامیده می‌شوند. نتیجهٔ شگفت‌آور کانتور، که تا پایان این
فصل آن را به‌طور کامل خواهیم فهمید، این بود که برخی مجموعه‌های نامتناهی
شمارا نیستند.
```

Introduce برشماری with the explicit list-of-members gloss, maintain every finite set and only some infinite sets. شمارا uses OLP inclusive meaning disclosed in0029, not the strict infinite-only convention of K53. No algorithmic computability requirement is added.

Alternatives: No material alternative recorded; none invented.

Expert-review question: برشماری retains the established edition label with source-grounded gloss; the canon attests شمارش, including transfinite enumeration, so identity of scope cannot be inferred from the word alone.

## FA-0029-C01: Enumeration heading and token

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053.

Source:
```latex
\olsection{Enumerations and \usetoken{S}{enumerable} Sets}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{برشماری‌ها و مجموعه‌های شمارا}
```

Retain برشماری and locale شمارا; explicit heading usetoken is realized for expert reading. Scope note below distinguishes strict Persian cardinality convention.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C02: Editorial audiences and alternative definition

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051, FA-REL-P046, FA-REL-P050.

Source:
```latex
\begin{editorial}
  This section discusses enumerations of sets, defining them as
  surjections from $\PosInt$. It does things slowly, for readers with
  little mathematical background. An alternative, terser
  version is given in \olref[enm-alt]{sec}, which defines enumerations
  differently: as bijections with $\Nat$ (or an initial segment).
\end{editorial}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{editorial}
  این بخش برشماری‌های مجموعه‌ها را بررسی می‌کند و آن‌ها را توابع
  پوشا از $\PosInt$ تعریف می‌کند. مطالب را برای خوانندگانی که پیشینهٔ
  ریاضی اندکی دارند، آهسته و گام‌به‌گام پیش می‌برد. روایتی جایگزین و
  موجزتر در \olref[enm-alt]{sec} آمده است که برشماری‌ها را به‌گونه‌ای
  متفاوت تعریف می‌کند: به‌منزلهٔ تناظرهای دوسویی با $\Nat$ (یا یک بخش ابتدایی).
\end{editorial}
```

Translate the existing source account of slower exposition without adding condescending material. Retain PosInt-surjection and Nat/initial-segment-bijection alternatives; بخش ابتدایی follows K51.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C03: Listing exposition

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044.

Source:
```latex
\begin{explain}
We've already given examples of sets by listing their !!{element}s.
Let's discuss in more general terms how and when we can list the
!!{element}s of a set, even if that set is infinite.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
پیش‌تر نمونه‌هایی از مجموعه‌ها را با فهرست‌کردن اعضای آن‌ها
ارائه کرده‌ایم. بیایید به‌طور کلی‌تر بررسی کنیم که چگونه و چه هنگام
می‌توانیم اعضای یک مجموعه را فهرست کنیم، حتی اگر آن مجموعه
نامتناهی باشد.
\end{explain}
```

Retain lists of all members, including infinite sets. Locale اعضا plus connective ی correctly forms اعضای; do not remove the possessive linker mechanically.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C04: Informal list definition

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044.

Source:
```latex
\begin{defn}[Enumeration, informally]
Informally, an \emph{enumeration} of a set~$A$ is a list (possibly
infinite) of !!{element}s of~$A$ such that every !!{element} of $A$
appears on the list at some finite position. If $A$ has an
enumeration, then $A$ is said to be \emph{!!{enumerable}}.
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}[برشماری، به‌طور غیرصوری]
به‌طور غیرصوری، یک \emph{برشماری} مجموعهٔ~$A$ فهرستی (احتمالاً
نامتناهی) از اعضای~$A$ است، به‌گونه‌ای که هر عضو
از $A$ در جایگاهی متناهی از فهرست ظاهر شود. اگر $A$ برشماری‌ای داشته
باشد، می‌گوییم $A$ \emph{شمارا} است.
\end{defn}
```

Every member must occur at some finite position. Lists can be finite or infinite; membership is exhaustive but repetition is allowed. احتمالا here means possibly, not a probabilistic model.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C05: Finite-position requirement and predecessor caveat

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{explain}
A couple of points about enumerations:
\begin{enumerate}
\item We count as enumerations only lists which have a beginning and
  in which every !!{element} other than the first has a single
  !!{element} immediately preceding it.  In other words, there are
  only finitely many elements between the first !!{element} of the
  list and any other !!{element}. In particular, this means that every
  !!{element} of an enumeration has a finite position: the first
  !!{element} has position~$1$, the second position~$2$, etc.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
چند نکته دربارهٔ برشماری‌ها:
\begin{enumerate}
\item تنها فهرست‌هایی را برشماری به شمار می‌آوریم که آغازی داشته باشند و
  در آن‌ها هر عضو جز نخستین عضو، دقیقاً یک
  عضو داشته باشد که بی‌درنگ پیش از آن بیاید. همچنین لازم است میان
  نخستین عضو آن فهرست و هر عضو دیگر فقط شمار متناهی‌ای عضو
  قرار داشته باشد. \emph{توضیح ویراستاری:} شرط اخیر از داشتن آغاز و عضو پیشینِ
  بلافصل به‌تنهایی نتیجه نمی‌شود؛ همان شرط جایگاه متناهی در تعریف بالاست. به‌ویژه، این یعنی هر عضو در یک برشماری جایگاهی متناهی
  دارد: نخستین عضو در جایگاه~$1$، دومین در جایگاه~$2$ و الی آخر است.
```

Retain immediate predecessor plus finite-position conditions, but no longer state that the second follows from the first. A first element and predecessors alone allow omega followed by a Z block. The source definition already requires finite positions; labelled explanation repairs its purported equivalence, not the whole definition.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C06: Same set, different list orders

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053.

Source:
```latex
\item We can have different enumerations of the same set~$A$ which
  differ by the order in which the !!{element}s appear: $4$, $1$,
  $25$, $16$,~$9$ enumerates the (set of the) first five square
  numbers just as well as $1$, $4$, $9$, $16$,~$25$ does.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\item می‌توانیم برشماری‌های متفاوتی از همان مجموعهٔ~$A$ داشته باشیم که
  در ترتیب ظاهرشدن اعضا فرق کنند: $4$، $1$،
  $25$، $16$،~$9$ پنج مربعِ مثبتِ نخست را (به‌منزلهٔ یک مجموعه) درست
  به همان خوبیِ $1$، $4$، $9$، $16$،~$25$ برمی‌شمارد.
```

Preserve two orders of the five positive squares and distinction of sets from lists. All displayed numbers unchanged. The visible five-square example starts with1, not0; specify مثبت so the count does not depend on the convention for natural numbers.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C07: Repeated values allowed

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-REL-P046, FA-OL-CANON-0003:P0053.

Source:
```latex
\item Redundant enumerations are still enumerations: $1$, $1$, $2$,
  $2$, $3$, $3$,~\dots{} enumerates the same set as $1$, $2$,
  $3$,~\dots{} does.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\item برشماری‌های تکراردار همچنان برشماری‌اند: $1$، $1$، $2$،
  $2$، $3$، $3$،~\dots{} همان مجموعه‌ای را برمی‌شمارد که $1$، $2$،
  $3$،~\dots{} برمی‌شمارد.
```

Retain repeated-value list; enumerable does not imply its specified enumerating function injective.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C08: Order identifies a particular enumeration

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044.

Source:
```latex
\item Order and redundancy \emph{do} matter when we specify an
  enumeration: we can enumerate the positive integers beginning with
  $1$, $2$, $3$, $1$, \dots{}, but the pattern is easier to see when
  enumerated in the standard way as $1$, $2$, $3$, $4$,~\dots
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\item وقتی برشماری‌ای را مشخص می‌کنیم، ترتیب و تکرار \emph{اهمیت
  دارند}: می‌توانیم برشماریِ اعداد صحیح مثبت را با $1$، $2$، $3$، $1$،
  \dots{} آغاز کنیم، اما وقتی آن‌ها را به شیوهٔ متعارف، یعنی $1$، $2$،
  $3$، $4$،~\dots، برمی‌شماریم، الگو آسان‌تر دیده می‌شود.
```

Retain emphasis that order/redundancy matter for a specified list although not for its range. Prefix is only a possible start, not claimed a complete rule.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C09: No-first-element example

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053.

Source:
```latex
\item Enumerations must have a beginning: \dots, $3$, $2$, $1$ is not
  an enumeration of the positive integers because it has no first
  !!{element}. To see how this follows from the informal definition,
  ask yourself, ``at what position in the list does the number 76
  appear?''
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\item برشماری‌ها باید آغاز داشته باشند: \dots، $3$، $2$، $1$ برشماریِ
  اعداد صحیح مثبت نیست، زیرا نخستین عضو ندارد. برای اینکه ببینید
  این نکته چگونه از تعریف غیرصوری نتیجه می‌شود، از خود بپرسید: ``عدد 76
  در کدام جایگاه فهرست ظاهر می‌شود؟''
```

Retain reverse endless positive list and finite-position question76. It is the chosen list that fails, not the set of positive integers.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C10: Odds then evens is not a finite-position list

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053.

Source:
```latex
\item The following is not an enumeration of the positive integers:
  $1$, $3$, $5$, \dots, $2$, $4$, $6$, \dots\@ The problem is that the
  even numbers occur at places $\infty + 1$, $\infty + 2$, $\infty +
  3$, rather than at finite positions.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\item عبارت زیر برشماریِ اعداد صحیح مثبت نیست:
  $1$، $3$، $5$، \dots، $2$، $4$، $6$، \dots\@ مشکل این است که
  اعداد زوج به‌جای جایگاه‌های متناهی، در جایگاه‌های $\infty + 1$،
  $\infty + 2$، $\infty +
  3$ قرار می‌گیرند.
```

Retain source informal infinity-plus-position notation and explain that evens have no finite position. Do not interpret displayed infinity as a natural index.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C11: Empty list

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053.

Source:
```latex
\item The empty set is enumerable: it is enumerated by the empty list!{}
\end{enumerate}
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\item مجموعهٔ تهی شمارا است: فهرست تهی آن را برمی‌شمارد!{}
\end{enumerate}
\end{explain}
```

Retain empty list as enumeration in informal sense and empty set as countable. This differs from strict K53 usage, explicitly disclosed later.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C12: Removing repetitions: informal proposition

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P046.

Source:
```latex
\begin{prop}
  If $A$ has an enumeration, it has an enumeration without
  repetitions.
\end{prop}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prop}
  اگر $A$ برشماری‌ای داشته باشد، برشماری‌ای بی‌تکرار نیز دارد.
  در این گزاره، «برشماری» به معنای فهرست در تعریف غیرصوری بالاست.
\end{prop}
```

Clarify this is the earlier list definition; a finite nonempty set cannot have an injective enumeration with whole PosInt domain. This is definition staging, not a false proposition in context.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C13: Keep first occurrences proof

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044.

Source:
```latex
\begin{proof}
  Suppose $A$ has an enumeration $x_1$, $x_2$, \dots{} in which each
  $x_i$ is an !!{element} of~$A$.  We can remove repetitions from an
  enumeration by removing repeated !!{element}s. For instance, we can
  turn the enumeration into a new one in which we list $x_i$ if
  it is !!a{element} of~$A$ that is not among $x_1$, \dots,
  $x_{i-1}$ or remove $x_i$ from the list if it already appears among
  $x_1$, \dots,~$x_{i-1}$.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
  فرض کنید $A$ دارای برشماریِ $x_1$، $x_2$، \dots{} باشد که در آن هر
  $x_i$ یک عضو از~$A$ است. می‌توانیم با حذف اعضای تکراری،
  تکرارها را از یک برشماری برداریم. برای نمونه، می‌توانیم برشماری را به
  برشماری تازه‌ای تبدیل کنیم که در آن $x_i$ را، اگر یک عضو از~$A$
  باشد که در میان $x_1$، \dots، $x_{i-1}$ نیست، وارد فهرست کنیم؛ و اگر
  $x_i$ پیش‌تر در میان $x_1$، \dots،~$x_{i-1}$ ظاهر شده است، آن را از
  فهرست حذف کنیم.
\end{proof}
```

Preserve each x_i only at its first occurrence, remove later copies; equality of the range is maintained. No effective equality decision procedure or Choice assumption is asserted. Supply یک before عضو in the conditional: the configured indefinite-token prefix is empty, so the old phrase was grammatically incomplete. D44 shows the unique-member construction; this is contextual Persian syntax, not a new mathematical condition.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C14: Motivation for formal definition

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044.

Source:
```latex
The last argument shows that in order to get a good handle on
enumerations and !!{enumerable} sets and to prove things about them,
we need a more precise definition.  The following provides it.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
استدلال اخیر نشان می‌دهد که برای دستیابی به درکی دقیق از
برشماری‌ها و مجموعه‌های شمارا و اثبات مطالبی دربارهٔ آن‌ها،
به تعریفی دقیق‌تر نیاز داریم. تعریف زیر چنین تعریفی را فراهم می‌کند.
```

Keep the need for precise definitions and proofs, not merely efficient computational handling.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C15: Formal enumeration excludes empty codomain

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-REL-P044, FA-REL-P046, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{defn}[Enumeration, formally] 
An \emph{enumeration} of a set $A \neq \emptyset$ is any
!!{surjective} function $f \colon \PosInt \to A$.
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}[برشماری، به‌طور صوری]
منظور از یک \emph{برشماری} برای مجموعهٔ $A \neq \emptyset$، هر تابع
پوشا $f \colon \PosInt \to A$ است.
\end{defn}
```

An enumeration of nonempty A is an onto map from positive integers. Nonempty restriction is essential; retain exact type.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C16: Surjection gives finite-position list

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-REL-P044, FA-REL-P046, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{explain}
Let's convince ourselves that the formal definition and the informal
definition using a possibly infinite list are equivalent. First, any
!!{surjective} function from $\PosInt$ to a set~$A$ enumerates~$A$.
Such a function determines an enumeration as defined informally above:
the list $f(1)$, $f(2)$, $f(3)$, \dots. Since $f$ is !!{surjective},
every !!{element} of~$A$ is guaranteed to be the value of~$f(n)$ for
some~$n \in \PosInt$. Hence, every !!{element} of $A$ appears at some
finite position in the list. Since the function may not be
!!{injective}, the list may be redundant, but that is acceptable (as
noted above).
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
برای مجموعهٔ ناتهی، هم‌ارزی تعریف صوری با تعریف غیرصوری بر پایهٔ
فهرستی احتمالاً نامتناهی را در هر دو جهت بررسی می‌کنیم. نخست، هر تابع پوشا از
$\PosInt$ به مجموعهٔ~$A$، مجموعهٔ~$A$ را برمی‌شمارد. چنین تابعی
برشماری‌ای به معنای غیرصوری بالا تعیین می‌کند: فهرست $f(1)$، $f(2)$،
$f(3)$، \dots. چون $f$ پوشا است، تضمین می‌شود که هر
عضو از~$A$ مقدارِ~$f(n)$ برای یک~$n \in \PosInt$ باشد. ازاین‌رو،
هر عضو از $A$ در جایگاهی متناهی از فهرست ظاهر می‌شود. چون ممکن
است تابع یک‌به‌یک نباشد، فهرست می‌تواند تکراردار باشد، اما این
پذیرفتنی است (چنان‌که در بالا گفته شد).
```

Use natural proof exposition instead of a calqued invitation to convince oneself. Each output has some positive integer preimage; repetitions allowed and no injectivity required. State nonempty-set scope explicitly before comparing the formal and informal definitions; the source later handles the empty exception separately.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C17: List gives surjection, with last-value padding

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-REL-P044, FA-REL-P046, FA-OL-CANON-0003:P0053.

Source:
```latex
On the other hand, given a list that enumerates all !!{element}s
of~$A$, we can define !!a{surjective} function $f\colon \PosInt \to A$
by letting $f(n)$ be the $n$th !!{element} of the list, or the final
!!{element} of the list if there is no $n$th !!{element}. The only
case where this does not produce !!a{surjective} function is when $A$ is
empty, and hence the list is empty. So, every non-empty list
determines !!a{surjective} function $f\colon \PosInt \to A$.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
از سوی دیگر، با داشتن فهرستی که همهٔ اعضای~$A$ را
برمی‌شمارد، می‌توانیم تابعِ پوشا $f\colon \PosInt \to A$ را
چنان تعریف کنیم که $f(n)$ برابر $n$اُمین عضو در فهرست باشد، یا اگر
در جایگاه $n$ هیچ عضوی نیست، برابر آخرین عضو در فهرست باشد.
تنها حالتی که این کار تابعی پوشا تولید نمی‌کند زمانی است که
$A$ تهی و در نتیجه فهرست تهی باشد. پس هر فهرست ناتهی تابعی
پوشا به‌صورت $f\colon \PosInt \to A$ تعیین می‌کند.
\end{explain}
```

For finite nonempty lists repeat the final value for all remaining indices. For an infinite list use its nth value. Empty exception explicitly retained; nth ordinal syntax is reviewed contextually, not by token substitution.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C18: Countable definition and canon convention

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P046.

Source:
```latex
\begin{defn}
  \ollabel{defn:enumerable}
  A set~$A$ is !!{enumerable} iff it is empty or has an enumeration.
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}
  \ollabel{defn:enumerable}
  مجموعهٔ~$A$ شمارا است اگر و تنها اگر تهی باشد یا برشماری‌ای داشته باشد.

\emph{یادداشت اصطلاح‌شناختی:} در این متن «شمارا» مجموعه‌های متناهی، از جمله
مجموعهٔ تهی، و مجموعه‌های شمارای نامتناهی را در بر می‌گیرد. برخی منابع فارسی
این واژه را فقط برای حالت نامتناهی به کار می‌برند؛ در اینجا تعریف متن مبدأ ملاک است.
\end{defn}
```

Retain empty OR enumeration exactly. Add explicitly labelled terminology note: here شمارا includes finite and countably infinite, whereas K53 reserves it for cardinality omega. Source definition governs, and no computational meaning is imported.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C19: Positive and zero-based integer lists

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044, FA-REL-P050.

Source:
```latex
\begin{ex}
A function enumerating the positive integers ($\PosInt$) is simply the
identity function given by $f(n) = n$. A function enumerating the
natural numbers $\Nat$ is the function $g(n) = n - 1$.
\end{ex}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{ex}
تابعی که اعداد صحیح مثبت ($\PosInt$) را برمی‌شمارد، صرفاً تابع همانیِ
$f(n) = n$ است. تابعی که اعداد طبیعی $\Nat$ را برمی‌شمارد، تابع
$g(n) = n - 1$ است.
\end{ex}
```

Preserve f(n)=n for PosInt and g(n)=n-1 for Nat including0. Names/domain direction unchanged.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C20: Even/odd outputs and codomain distinction

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-REL-P046, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{ex}
The functions $f\colon \PosInt \to \PosInt$ and $g \colon \PosInt \to
\PosInt$ given by
\begin{align*}
f(n) & = 2n \text{ and}\\
g(n) & = 2n - 1
\end{align*}
enumerate the even positive integers and the odd positive integers,
respectively. However, neither function is an enumeration of
$\PosInt$, since neither is !!{surjective}.
\end{ex}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{ex}
توابع $f\colon \PosInt \to \PosInt$ و $g \colon \PosInt \to
\PosInt$ که به‌صورت زیر داده می‌شوند
\begin{align*}
f(n) & = 2n \text{ و}\\
g(n) & = 2n - 1
\end{align*}
به‌ترتیب اعداد صحیح مثبت زوج و اعداد صحیح مثبت فرد را برمی‌شمارند.
بااین‌حال، هیچ‌یک از این دو تابع برشماریِ $\PosInt$ نیست، زیرا هیچ‌یک
پوشا نیست.
\end{ex}
```

Keep codomain PosInt and the fact neither typed function is onto it. Saying it enumerates its even/odd range is informal corestriction usage; do not silently replace stated types.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C21: Positive-square exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044.

Source:
```latex
\begin{prob}
Define an enumeration of the positive squares $1$, $4$, $9$, $16$, \dots
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
برشماری‌ای از مربع‌های مثبت $1$، $4$، $9$، $16$، \dots تعریف کنید.
\end{prob}
```

Retain exercise and all displayed positive squares; do not insert a solution.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C22: Integer enumeration, ceiling and missing table entry

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-REL-P045, FA-REL-P044.

Source:
```latex
\begin{ex}
The function $f(n) = (-1)^{n} \lceil \frac{(n-1)}{2}\rceil$ (where
$\lceil x \rceil$ denotes the \emph{ceiling} function, which rounds
$x$ up to the nearest integer) enumerates the set of
integers~$\Int$. Notice how $f$ generates the values of $\Int$ by
``hopping'' back and forth between positive and negative integers:
\[
\begin{array}{c c c c c c c c}
f(1) & f(2) & f(3) & f(4) & f(5) & f(6) & f(7) & \dots \\ \\
- \lceil \tfrac{0}{2} \rceil & \lceil \tfrac{1}{2}\rceil & - \lceil \tfrac{2}{2} \rceil & \lceil \tfrac{3}{2} \rceil & - \lceil \tfrac{4}{2} \rceil  & \lceil \tfrac{5}{2}
\rceil & - \lceil \tfrac{6}{2} \rceil & \dots \\ \\
0 & 1 & -1 & 2 & -2 & 3 & \dots
\end{array}
\]
You can also think of $f$ as defined by cases as follows:
\[
f(n) = \begin{cases}
  0 & \text{if $n = 1$}\\
  n/2 & \text{if $n$ is even}\\
  -(n-1)/2 & \text{if $n$ is odd and $>1$}
  \end{cases}
\]
\end{ex}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{ex}
تابع $f(n) = (-1)^{n} \lceil \frac{(n-1)}{2}\rceil$ (که در آن
$\lceil x \rceil$ تابع \emph{سقف} را نشان می‌دهد که کوچک‌ترین عدد صحیحِ بزرگ‌تر یا مساویِ $x$ را
به دست می‌دهد) مجموعهٔ اعداد صحیح~$\Int$ را
برمی‌شمارد. توجه کنید که $f$ چگونه مقادیر $\Int$ را با ``جهیدن'' رفت‌وبرگشتی
میان اعداد صحیح مثبت و منفی تولید می‌کند:
\[
\begin{array}{c c c c c c c c}
f(1) & f(2) & f(3) & f(4) & f(5) & f(6) & f(7) & \dots \\ \\
- \lceil \tfrac{0}{2} \rceil & \lceil \tfrac{1}{2}\rceil & - \lceil \tfrac{2}{2} \rceil & \lceil \tfrac{3}{2} \rceil & - \lceil \tfrac{4}{2} \rceil  & \lceil \tfrac{5}{2}
\rceil & - \lceil \tfrac{6}{2} \rceil & \dots \\ \\
0 & 1 & -1 & 2 & -2 & 3 & -3 & \dots
\end{array}
\]
\emph{یادداشت ویراستاری:} در سطر آخر جدولِ متن مبدأ، مقدار هفتم، یعنی منفی سه،
جا افتاده بود؛ این مقدار در اینجا افزوده شده است.
همچنین می‌توانید $f$ را به‌صورت موردیِ زیر در نظر بگیرید:
\[
f(n) = \begin{cases}
  0 & \text{اگر $n = 1$}\\
  n/2 & \text{اگر $n$ زوج باشد}\\
  -(n-1)/2 & \text{اگر $n$ فرد و $>1$ باشد}
  \end{cases}
\]
\end{ex}
```

Use the direct canon ceiling definition (least integer at least x), correct missing seventh output to negative3, and disclose source omission. Verify explicit formula and all piecewise cases incl n=1. The only formal repair is that missing numeric table cell; formulas remain unchanged.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C23: Two-set union including empty cases

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-REL-P046, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{prob}
  Show that if $A$ and $B$ are !!{enumerable}, so is $A \cup B$. To do
  this, suppose there are !!{surjective} functions $f\colon \PosInt \to
  A$ and $g\colon \PosInt \to B$, and define !!a{surjective}
  function~$h\colon \PosInt \to A \cup B$ and prove that it is
  !!{surjective}. Also consider the cases where $A$ or~$B = \emptyset$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
  نشان دهید اگر $A$ و $B$ شمارا باشند، $A \cup B$ نیز چنین
  است. برای این کار، فرض کنید توابع پوشا $f\colon \PosInt \to
  A$ و $g\colon \PosInt \to B$ وجود دارند، و تابعی
  پوشا~$h\colon \PosInt \to A \cup B$ تعریف کنید و اثبات کنید که
  پوشا است. حالت تهی‌بودن $A$ و نیز حالت $B = \emptyset$ را بررسی کنید.
\end{prob}
```

Preserve onto functions, requested construction/proof and both empty cases. Repair malformed A-or-B-equals-empty prose while retaining source math. Two supplied enumerations suffice; arbitrary countable Choice is irrelevant.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C24: Subsets and empty subset

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051, FA-REL-P046, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{prob}
  Show that if $B \subseteq A$ and $A$ is !!{enumerable}, so is~$B$. To
  do this, suppose there is !!a{surjective} function $f\colon \PosInt \to
  A$. Define !!a{surjective} function~$g\colon \PosInt \to B$ and prove
  that it is !!{surjective}. What happens if $B = \emptyset$?
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
  نشان دهید اگر $B \subseteq A$ و $A$ شمارا باشد، $B$ نیز چنین
  است. برای این کار، فرض کنید تابعی پوشا به‌صورت $f\colon \PosInt \to
  A$ وجود دارد. تابعی پوشا به‌صورت $g\colon \PosInt \to B$
  تعریف کنید و اثبات کنید که پوشا است. اگر $B = \emptyset$ باشد چه رخ می‌دهد؟
\end{prob}
```

Preserve B subset A and separate empty case. For nonempty B a fixed default member or least-hit method defines the requested map without a new Choice axiom.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C25: Finite union induction

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P046.

Source:
```latex
\begin{prob}
  Show by induction on $n$ that if $A_1$, $A_2$, \dots, $A_n$ are all
  !!{enumerable}, so is $A_1 \cup \dots \cup A_n$. You may assume the
  fact that if two sets $A$ and~$B$ are !!{enumerable}, so is~$A \cup
  B$. 
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
  با استقرا بر $n$ نشان دهید که اگر $A_1$، $A_2$، \dots، $A_n$ همگی
  شمارا باشند، $A_1 \cup \dots \cup A_n$ نیز چنین است. می‌توانید
  این واقعیت را فرض کنید که اگر دو مجموعهٔ $A$ و~$B$ شمارا
  باشند، $A \cup
  B$ نیز چنین است.
\end{prob}
```

Retain induction on the finite number of sets and the binary-union assumption. Do not upgrade this to arbitrary countable unions without given enumerations.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C26: Zero-based indexing convention

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044.

Source:
```latex
Although it is perhaps more natural when listing the !!{element}s of a
set to start counting from the $1$st !!{element}, mathematicians like
to use the natural numbers~$\Nat$ for counting things. They
talk about the $0$th, $1$st, $2$nd, and so on, !!{element}s of a list.
Correspondingly, we can define an enumeration as !!a{surjective}
function from $\Nat$ to~$A$. Of course, the two definitions are
equivalent.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
هرچند هنگام فهرست‌کردن اعضای یک مجموعه شاید طبیعی‌تر باشد که
شمردن را از نخستین عضو، یعنی جایگاه $1$، آغاز کنیم، ریاضی‌دانان
دوست دارند برای شمردن چیزها از اعداد طبیعی~$\Nat$ استفاده کنند. آنان از
اعضای $0$اُم، $1$اُم، $2$اُم و الی آخرِ یک فهرست سخن
می‌گویند. بر همین اساس، می‌توانیم برشماری را تابعی پوشا از
$\Nat$ به~$A$ تعریف کنیم. البته این دو تعریف هم‌ارزند.
```

Retain0th/1st/2nd positions and equivalence of Nat versus PosInt domain, not identity of the same numerical indices. Plural اعضای and ordinal suffixes are grammatical connective constructions.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C27: Shift proposition

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-REL-P044, FA-REL-P046, FA-REL-P050.

Source:
```latex
\begin{prop}\ollabel{prop:enum-shift}
  There is !!a{surjection} $f\colon \PosInt \to A$ iff there is
  !!a{surjection} $g\colon \Nat \to A$.
\end{prop}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prop}\ollabel{prop:enum-shift}
  نگاشت پوشا $f\colon \PosInt \to A$ وجود دارد اگر و تنها اگر
  نگاشت پوشا $g\colon \Nat \to A$ وجود داشته باشد.
\end{prop}
```

Keep onto PosInt-to-A iff onto Nat-to-A, true also for empty A because both sides are false.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C28: Both directions of shift proof

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-REL-P044, FA-REL-P050.

Source:
```latex
\begin{proof}
  Given !!a{surjection} $f\colon \PosInt \to A$, we can define $g(n) =
  f(n+1)$ for all $n \in \Nat$. It is easy to see that $g\colon \Nat
  \to A$ is !!{surjective}. Conversely, given !!a{surjection} $g\colon
  \Nat \to A$, define $f(n) = g(n-1)$.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
  با داشتن نگاشت پوشا $f\colon \PosInt \to A$، می‌توانیم تعریف کنیم
  $g(n) =
  f(n+1)$ برای همهٔ $n \in \Nat$. به‌آسانی می‌توان دید که $g\colon \Nat
  \to A$ پوشا است. برعکس، با داشتن نگاشت پوشا $g\colon
  \Nat \to A$، تعریف کنید $f(n) = g(n-1)$.
\end{proof}
```

Preserve g(n)=f(n+1) for natural n and f(n)=g(n-1) for positive n. No zero-minus-one evaluation occurs.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C29: Natural-number surjection characterization

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P046.

Source:
```latex
This gives us the following result:

\begin{cor}\ollabel{cor:enum-nat}
A set $A$ is !!{enumerable} iff it is empty or there is
!!a{surjective} function $f\colon \Nat \to A$.
\end{cor}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
این امر نتیجهٔ زیر را به ما می‌دهد:

\begin{cor}\ollabel{cor:enum-nat}
مجموعهٔ $A$ شمارا است اگر و تنها اگر تهی باشد یا تابعی
پوشا به‌صورت $f\colon \Nat \to A$ وجود داشته باشد.
\end{cor}
```

Retain the empty OR surjection corollary, its label and preceding transition.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C30: Finite repetition-free lists require finite domains

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P046, FA-REL-P050.

Source:
```latex
We discussed above that a list of !!{element}s of a set~$A$ can be
turned into a list without repetitions. This is also true for
enumerations, but a bit harder to formulate and prove rigorously. Any
function $f\colon \PosInt \to A$ must be defined for all $n \in
\PosInt$. If there are only finitely many !!{element}s in~$A$ then we
clearly cannot have a function defined on the infinitely many
!!{element}s of~$\PosInt$ that takes as values all the !!{element}s
of~$A$ but never takes the same value twice. In that case, i.e., in
the case where the list without repetitions is finite, we must choose
a different domain for~$f$, one with only finitely many !!{element}s.
Not having repetitions means that $f$ must be !!{injective}. Since it
is also !!{surjective}, we are looking for !!a{bijection} between some
finite set $\{1, \dots, n\}$ or $\PosInt$ and~$A$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
در بالا گفتیم که می‌توان فهرستی از اعضای مجموعهٔ~$A$ را به
فهرستی بی‌تکرار تبدیل کرد. این مطلب دربارهٔ برشماری‌ها نیز درست است،
اما صورت‌بندی و اثبات دقیق آن کمی دشوارتر است. هر تابع $f\colon \PosInt \to A$
باید برای همهٔ $n \in
\PosInt$ تعریف شده باشد. اگر شمار اعضا در~$A$ متناهی باشد،
آشکار است که نمی‌توانیم تابعی داشته باشیم که بر همهٔ اعضای
مجموعهٔ نامتناهیِ~$\PosInt$ تعریف شده باشد و همهٔ
اعضای مجموعهٔ~$A$ را به‌عنوان مقدار بگیرد، اما هیچ‌گاه مقداری را
دوبار نگیرد. در این حالت، یعنی هنگامی که فهرست بی‌تکرار متناهی است، باید
دامنه‌ای متفاوت برای~$f$ برگزینیم که شمار اعضای آن متناهی باشد.
نداشتن تکرار یعنی $f$ باید یک‌به‌یک باشد. چون این تابع
پوشا نیز هست، در پی تناظر دوسویی میان یک مجموعهٔ متناهی
$\{1, \dots, n\}$ یا $\PosInt$ و~$A$ هستیم.
```

Preserve finite/infinite split, domain change and injection plus surjection = bijection. These sentences constrain the informal repetition-removal result, not contradict it. Replace the malformed quantified plural بی‌نهایت اعضای with all members of the infinite domain. This retains totality and infinite domain size without altering any formula.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C31: Bijection from positive integers or initial segment

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053, FA-REL-P050.

Source:
```latex
\begin{prop}\ollabel{prop:enum-bij}
If $f\colon \PosInt \to A$ is !!{surjective} (i.e., an enumeration
of~$A$), there is !!a{bijection} $g\colon Z \to A$ where $Z$ is
either~$\PosInt$ or $\{1, \dots, n\}$ for some~$n \in \PosInt$.
\end{prop}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prop}\ollabel{prop:enum-bij}
اگر $f\colon \PosInt \to A$ پوشا باشد (یعنی برشماریِ~$A$
باشد)، تناظر دوسویی $g\colon Z \to A$ وجود دارد که در آن $Z$ یا
~$\PosInt$ است یا $\{1, \dots, n\}$ برای یک~$n \in \PosInt$.
\end{prop}
```

Retain given surjection, nonempty codomain implicit in its existence, and alternative finite domain1..n for positive n.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C32: Recursive first-unused-value construction

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053, FA-REL-P044.

Source:
```latex
\begin{proof}
  We define the function $g$ recursively: Let $g(1) = f(1)$. If $g(i)$
  has already been defined, let $g(i+1)$ be the first value of $f(1)$,
  $f(2)$, \dots{} not already among $g(1)$, \dots, $g(i)$, if there is
  one. If $A$ has just $n$ !!{element}s, then $g(1)$, \dots, $g(n)$ are all
  defined, and so we have defined a function $g\colon \{1, \dots, n\}
  \to A$. If $A$ has infinitely many !!{element}s, then for any $i$
  there must be !!a{element} of~$A$ in the enumeration $f(1)$, $f(2)$,
  \dots, which is not already among $g(1)$, \dots, $g(i)$. In this
  case we have defined a function $g\colon \PosInt \to A$.
  
  The function $g$ is !!{surjective}, since any element of~$A$ is
  among $f(1)$, $f(2)$, \dots{} (since $f$ is !!{surjective}) and so
  will eventually be a value of~$g(i)$ for some~$i$. It is also
  !!{injective}, since if there were $j < i$ such that $g(j) = g(i)$,
  then $g(i)$ would already be among $g(1)$, \dots, $g(i-1)$, contrary
  to how we defined~$g$.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
  تابع $g$ را به‌صورت بازگشتی تعریف می‌کنیم: قرار دهید $g(1) = f(1)$.
  اگر $g(i)$ پیش‌تر تعریف شده باشد، $g(i+1)$ را نخستین مقدار از $f(1)$،
  $f(2)$، \dots{} قرار دهید که پیش‌تر در میان $g(1)$، \dots، $g(i)$
  نباشد، البته اگر چنین مقداری وجود داشته باشد. اگر شمار اعضای~$A$
  دقیقاً $n$ باشد، آنگاه $g(1)$، \dots، $g(n)$ همگی تعریف شده‌اند
  و بنابراین تابعی $g\colon \{1, \dots, n\}
  \to A$ تعریف کرده‌ایم. اگر شمار اعضای~$A$ نامتناهی باشد، آنگاه برای هر $i$ باید
  یک عضو از~$A$ در برشماریِ $f(1)$، $f(2)$، \dots وجود داشته باشد
  که پیش‌تر در میان $g(1)$، \dots، $g(i)$ نباشد. در این حالت، تابعی
  $g\colon \PosInt \to A$ تعریف کرده‌ایم.

  تابع $g$ پوشا است، زیرا هر عضو از~$A$ در میان $f(1)$،
  $f(2)$، \dots{} قرار دارد (چون $f$ پوشا است) و در نتیجه سرانجام
  مقدارِ~$g(i)$ برای یک~$i$ خواهد شد. این تابع همچنین یک‌به‌یک است،
  زیرا اگر برای $j < i$ داشتیم $g(j) = g(i)$، آنگاه $g(i)$ پیش‌تر
  در میان $g(1)$، \dots، $g(i-1)$ قرار می‌داشت، برخلاف شیوه‌ای که~$g$
  را تعریف کردیم.
\end{proof}
```

Preserve first unused value in source order, finite termination and infinite continuation. Make singular existential member explicit. Every member whose first occurrence is at k is selected after at most k new-value selections; hence onto. No arbitrary choice or effective procedure claim.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C33: Bijection with Nat or zero-based finite segment

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053, FA-REL-P050.

Source:
```latex
\begin{cor}\ollabel{cor:enum-nat-bij}
A set $A$ is !!{enumerable} iff it is empty or there is !!a{bijection}
$f\colon N \to A$ where either $N = \Nat$ or $N = \{0, \dots, n\}$ for
some $n \in \Nat$.
\end{cor}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{cor}\ollabel{cor:enum-nat-bij}
مجموعهٔ $A$ شمارا است اگر و تنها اگر تهی باشد یا تناظر دوسویی
$f\colon N \to A$ وجود داشته باشد که در آن یا $N = \Nat$ یا
$N = \{0, \dots, n\}$ برای یک $n \in \Nat$.
\end{cor}
```

Retain empty disjunct and0..n for n natural. This includes singleton when n=0; cannot drop empty separately.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C34: Reindex finite segment proof

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051, FA-REL-P050.

Source:
```latex
\begin{proof}
$A$ is !!{enumerable} iff $A$ is empty or there is !!a{surjective}
$f\colon \PosInt \to A$. By \olref{prop:enum-bij}, the latter holds
iff there is !!a{bijective} function~$f\colon Z \to A$ where $Z =
\PosInt$ or $Z = \{1, \dots, n\}$ for some $n \in \PosInt$. By the
same argument as in the proof of \olref{prop:enum-shift}, that in turn
is the case iff there is !!a{bijection} $g\colon N \to A$ where either
$N = \Nat$ or $N = \{0, \dots, n-1\}$.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
$A$ شمارا است اگر و تنها اگر $A$ تهی باشد یا تابعی
پوشا به‌صورت $f\colon \PosInt \to A$ وجود داشته باشد. بنا بر
\olref{prop:enum-bij}، مورد اخیر برقرار است اگر و تنها اگر تابعِ
دوسویی~$f\colon Z \to A$ وجود داشته باشد که در آن $Z =
\PosInt$ یا $Z = \{1, \dots, n\}$ برای یک $n \in \PosInt$. با همان
استدلالِ برهان \olref{prop:enum-shift}، این نیز به نوبهٔ خود برقرار است
اگر و تنها اگر تناظر دوسویی $g\colon N \to A$ وجود داشته باشد که در آن
یا $N = \Nat$ یا $N = \{0, \dots, n-1\}$.
\end{proof}
```

Preserve1..n to0..n-1; positive n in proof becomes natural endpoint n-1 in statement. This is reparametrization, not an off-by-one defect.

Alternatives: No material alternative recorded; none invented.

## FA-0029-C35: Injection characterization exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053, FA-REL-P046.

Source:
```latex
\begin{prob}
  According to \olref[sfr][siz][enm]{defn:enumerable}, a set $A$ is
  enumerable iff $A = \emptyset$ or there is !!a{surjective} $f\colon
  \PosInt \to A$.  It is also possible to define ``!!{enumerable} set''
  precisely by: a set is enumerable iff there is !!a{injective}
  function $g\colon A \to \PosInt$.  Show that the definitions are
  equivalent, i.e., show that there is !!a{injective} function
  $g\colon A \to \PosInt$ iff either $A = \emptyset$ or there is
  !!a{surjective} $f\colon \PosInt \to A$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
  بنا بر \olref[sfr][siz][enm]{defn:enumerable}، مجموعهٔ $A$ شمارا است
  اگر و تنها اگر $A = \emptyset$ یا تابعی پوشا به‌صورت $f\colon
  \PosInt \to A$ وجود داشته باشد. همچنین می‌توان اصطلاح
  ``مجموعهٔ شمارا'' را به‌طور دقیق چنین تعریف کرد: یک مجموعه شمارا
  است اگر و تنها اگر تابعی یک‌به‌یک به‌صورت
  $g\colon A \to \PosInt$ وجود داشته باشد. نشان دهید که این دو تعریف
  هم‌ارزند؛ یعنی نشان دهید که تابعی یک‌به‌یک به‌صورت
  $g\colon A \to \PosInt$ وجود دارد اگر و تنها اگر یا $A = \emptyset$
  یا تابعی پوشا~$f\colon \PosInt \to A$ وجود داشته باشد.
\end{prob}
```

Retain iff of injection A-to-PosInt and empty OR onto PosInt-to-A. The reverse uses least preimage in positive integers; the general canon Choice argument is not required here. Keep exercise unsolved.

Alternatives: No material alternative recorded; none invented.

## FA-0030-C01: Zig-zag heading and product array

Action: retain_after_fresh_review; confidence 2/3: Editorial0–3, not a calibrated probability. Mathematical scope checked; precise terminology or explanatory convention is contextual and its evidence limit is stated.
Canon: FA-REL-P044, FA-OL-CANON-0003:P0053.

Source:
```latex
\olsection{Cantor's Zig-Zag Method}

\begin{explain}
We've already considered some ``easy'' enumerations. Now we will
consider something a bit harder. Consider the set of pairs of natural
numbers\oliflabeldef{sfr:set:pai:sec}{, which we defined in
\olref[set][pai]{sec} thus:}{defined by:}
\[
\Nat \times \Nat = \Setabs{\tuple{n,m}}{n,m \in \Nat}
\]
We can organize these ordered pairs into an \emph{array}, like so:
\[
\begin{array}{ c | c | c | c | c | c}
& \mathbf 0 & \mathbf 1 & \mathbf 2 & \mathbf 3 & \dots \\
\hline
\mathbf 0 & \tuple{0,0} & \tuple{0,1} & \tuple{0,2} & \tuple{0,3} & \dots \\
\hline
\mathbf 1 & \tuple{1,0} & \tuple{1,1} & \tuple{1,2} & \tuple{1,3} & \dots \\
\hline
\mathbf 2 & \tuple{2,0} & \tuple{2,1} & \tuple{2,2} & \tuple{2,3} & \dots \\
\hline
\mathbf 3 & \tuple{3,0} & \tuple{3,1} & \tuple{3,2} & \tuple{3,3} & \dots \\
\hline
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots\\
\end{array}
\]
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{روش زیگزاگ کانتور}

\begin{explain}
پیش‌تر چند برشماریِ ``آسان'' را بررسی کرده‌ایم. اکنون موردی کمی
دشوارتر را بررسی می‌کنیم. مجموعهٔ زوج‌های مرتب اعداد طبیعی را در نظر
بگیرید\oliflabeldef{sfr:set:pai:sec}{، که آن را در
\olref[set][pai]{sec} چنین تعریف کردیم:}{، که چنین تعریف می‌شود:}
\[
\Nat \times \Nat = \Setabs{\tuple{n,m}}{n,m \in \Nat}
\]
می‌توانیم این زوج‌های مرتب را در یک \emph{آرایه} به‌شکل زیر سامان دهیم:
\[
\begin{array}{ c | c | c | c | c | c}
& \mathbf 0 & \mathbf 1 & \mathbf 2 & \mathbf 3 & \dots \\
\hline
\mathbf 0 & \tuple{0,0} & \tuple{0,1} & \tuple{0,2} & \tuple{0,3} & \dots \\
\hline
\mathbf 1 & \tuple{1,0} & \tuple{1,1} & \tuple{1,2} & \tuple{1,3} & \dots \\
\hline
\mathbf 2 & \tuple{2,0} & \tuple{2,1} & \tuple{2,2} & \tuple{2,3} & \dots \\
\hline
\mathbf 3 & \tuple{3,0} & \tuple{3,1} & \tuple{3,2} & \tuple{3,3} & \dots \\
\hline
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots\\
\end{array}
\]
```

Retain زیگزاگ as contextual name and آرایه as rectangular arrangement, all ordered-pair cells, indices and both conditional-reference branches. No change of row/column order for RTL.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Selected canon provides ordered-pair and enumeration context, not the exact phrase روش زیگزاگ کانتور or the array label. Preserve source-defined labels; do not fabricate a direct attestation.

## FA-0030-C02: One-dimensional order and diagonal index table

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044.

Source:
```latex
Clearly, every ordered pair in $\Nat \times \Nat$ will appear
exactly once in the array. In particular, $\tuple{n,m}$ will appear in
the $n$th row and $m$th column. But how do we organize the elements of
such an array into a ``one-dimensional'' list? The pattern in the array below
demonstrates one way to do this (although of course there are many other options):
\[
\begin{array}{ c | c | c | c | c | c | c}
& \mathbf 0 & \mathbf 1 & \mathbf 2 & \mathbf 3 & \mathbf 4 &\dots \\
\hline
\mathbf 0 & 0  & 1& 3 & 6& 10 &\ldots \\
\hline
\mathbf 1 &2 & 4& 7 & 11 & \dots &\ldots \\
\hline
\mathbf 2 & 5 & 8 & 12 & \ldots & \dots&\ldots \\
\hline
\mathbf 3 & 9 & 13 & \ldots & \ldots & \dots & \ldots \\
\hline
\mathbf 4 & 14 & \ldots & \ldots & \ldots & \dots & \ldots \\
\hline
\vdots & \vdots & \vdots & \vdots & \vdots&\ldots & \ddots\\
\end{array}
\]\noindent
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
آشکار است که هر زوج مرتب در $\Nat \times \Nat$ دقیقاً یک‌بار در آرایه
ظاهر می‌شود. به‌ویژه، $\tuple{n,m}$ در سطر $n$اُم و ستون $m$اُم ظاهر
خواهد شد. اما چگونه اعضای چنین آرایه‌ای را در فهرستی ``یک‌بعدی'' سامان
دهیم؟ الگوی آرایهٔ زیر یک شیوهٔ انجام این کار را نشان می‌دهد (هرچند
البته گزینه‌های بسیار دیگری نیز وجود دارند):
\[
\begin{array}{ c | c | c | c | c | c | c}
& \mathbf 0 & \mathbf 1 & \mathbf 2 & \mathbf 3 & \mathbf 4 &\dots \\
\hline
\mathbf 0 & 0  & 1& 3 & 6& 10 &\ldots \\
\hline
\mathbf 1 &2 & 4& 7 & 11 & \dots &\ldots \\
\hline
\mathbf 2 & 5 & 8 & 12 & \ldots & \dots&\ldots \\
\hline
\mathbf 3 & 9 & 13 & \ldots & \ldots & \dots & \ldots \\
\hline
\mathbf 4 & 14 & \ldots & \ldots & \ldots & \dots & \ldots \\
\hline
\vdots & \vdots & \vdots & \vdots & \vdots&\ldots & \ddots\\
\end{array}
\]\noindent
```

Keep row n, column m and the explicit diagonal order. Every numeric cell matches triangular(n+m)+n; this is not an alternating-direction traversal despite the informal zig-zag name.

Alternatives: No material alternative recorded; none invented.

## FA-0030-C03: Explicit pair sequence

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044.

Source:
```latex
This pattern is called \emph{Cantor's zig-zag method}. It  enumerates
$\Nat \times \Nat$ as follows:
\[
\tuple{0,0}, \tuple{0,1}, \tuple{1,0}, \tuple{0,2}, \tuple{1,1},
\tuple{2,0}, \tuple{0,3}, \tuple{1,2}, \tuple{2,1}, \tuple{3,0}, \dots
\]
And this establishes the following:
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
این الگو \emph{روش زیگزاگ کانتور} نامیده می‌شود. این روش
$\Nat \times \Nat$ را به‌صورت زیر برمی‌شمارد:
\[
\tuple{0,0}, \tuple{0,1}, \tuple{1,0}, \tuple{0,2}, \tuple{1,1},
\tuple{2,0}, \tuple{0,3}, \tuple{1,2}, \tuple{2,1}, \tuple{3,0}, \dots
\]
و این، گزارهٔ زیر را ثابت می‌کند:
\end{explain}
```

Retain all ten displayed pairs in exact source order; the array and sequence agree.

Alternatives: No material alternative recorded; none invented.

## FA-0030-C04: Natural square countability proposition

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P046.

Source:
```latex
\begin{prop}\ollabel{natsquaredenumerable}
$\Nat \times \Nat$ is !!{enumerable}.
\end{prop}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prop}\ollabel{natsquaredenumerable}
$\Nat \times \Nat$ شمارا است.
\end{prop}
```

Retain Nat square is countable, not a claim all Cartesian products are countable.

Alternatives: No material alternative recorded; none invented.

## FA-0030-C05: Complete finite-diagonal proof

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044, FA-REL-P046.

Source:
```latex
\begin{proof}
Let $f \colon \Nat \to \Nat\times\Nat$ take each $k \in \Nat$ to the
tuple $\tuple{n,m} \in \Nat \times \Nat$ such that $k$ is the value of
the $n$th row and $m$th column in Cantor's zig-zag array. 
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
تابع $f \colon \Nat \to \Nat\times\Nat$ را چنان تعریف می‌کنیم که هر
$k \in \Nat$ را به زوج $\tuple{n,m} \in \Nat \times \Nat$ بفرستد،
به‌گونه‌ای که $k$
مقدار خانهٔ واقع در سطر $n$اُم و ستون $m$اُمِ آرایهٔ زیگزاگ کانتور باشد.
\emph{تکمیل توضیح برهان:} خانه‌ها بر روی قطرهایی با مجموعِ ثابتِ دو مؤلفه
قرار دارند. قطرها به ترتیبِ این مجموع و خانه‌های هر قطر به ترتیبِ مؤلفهٔ اول
پیموده می‌شوند. هر قطر متناهی است و پیش از هر خانه فقط تعداد متناهی‌ای خانه
قرار می‌گیرد. این قطرها همهٔ زوج‌ها را دقیقاً یک‌بار در بر می‌گیرند؛ پس تابع
تعریف‌شده خوش‌تعریف و پوشاست.
\end{proof}
```

Retain original map from each index to its unique cell, then labelled proof explanation: increasing sum diagonals, finite length, increasing first coordinate, finite preceding cells, every pair exactly once. Supplies omitted justification of well-definedness and surjectivity without changing theorem.

Alternatives: No material alternative recorded; none invented.

## FA-0030-C06: Triples, finite powers and zero case

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044, FA-REL-P050.

Source:
```latex
\begin{explain}
This technique also generalises rather nicely. For example, we can use
it to enumerate the set of ordered triples of natural numbers, i.e.:
\[
\Nat \times \Nat \times \Nat = \Setabs{\tuple{n,m,k}}{n,m,k \in \Nat}
\]
We think of $\Nat \times \Nat \times \Nat$ as the Cartesian
product of $\Nat \times \Nat$ with $\Nat$, that is,
\[
\Nat^3 = (\Nat \times \Nat) \times \Nat =
\Setabs{\tuple{\tuple{n,m},k}}{n, m, k
  \in \Nat }
\]
and thus we can enumerate $\Nat^3$ with an array by labelling one
axis with the enumeration of $\Nat$, and the other axis with the
enumeration of $\Nat^2$:
\[
\begin{array}{ c | c | c | c | c | c}
& \mathbf 0 & \mathbf 1 & \mathbf 2 & \mathbf 3 & \dots \\
\hline
\mathbf{\tuple{0,0}} & \tuple{0,0,0} & \tuple{0,0,1} & \tuple{0,0,2} & \tuple{0,0,3} & \dots \\
\hline
\mathbf{\tuple{0,1}} & \tuple{0,1,0} & \tuple{0,1,1} & \tuple{0,1,2} & \tuple{0,1,3} & \dots \\
\hline
\mathbf{\tuple{1,0}} & \tuple{1,0,0} & \tuple{1,0,1} & \tuple{1,0,2} & \tuple{1,0,3} & \dots \\
\hline
\mathbf{\tuple{0,2}} & \tuple{0,2,0} & \tuple{0,2,1} & \tuple{0,2,2} & \tuple{0,2,3} & \dots\\
\hline
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots \\
\end{array}
\]
Thus, by using a method like Cantor's zig-zag method, we may similarly
obtain an enumeration of~$\Nat^3$. And we can keep going, obtaining
enumerations of $\Nat^n$ for any natural number $n$. So, we have:
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
این فن به‌خوبی قابل تعمیم نیز هست. برای نمونه، می‌توانیم از آن برای
برشمردن مجموعهٔ سه‌تایی‌های مرتب اعداد طبیعی استفاده کنیم؛ یعنی:
\[
\Nat \times \Nat \times \Nat = \Setabs{\tuple{n,m,k}}{n,m,k \in \Nat}
\]
$\Nat \times \Nat \times \Nat$ را ضرب دکارتیِ
$\Nat \times \Nat$ در $\Nat$ در نظر می‌گیریم؛ یعنی
\[
\Nat^3 = (\Nat \times \Nat) \times \Nat =
\Setabs{\tuple{\tuple{n,m},k}}{n, m, k
  \in \Nat }
\]
و ازاین‌رو می‌توانیم $\Nat^3$ را با آرایه‌ای برشماریم که یک محور آن
با برشماریِ $\Nat$ و محور دیگرش با برشماریِ $\Nat^2$ برچسب‌گذاری شده است:
\[
\begin{array}{ c | c | c | c | c | c}
& \mathbf 0 & \mathbf 1 & \mathbf 2 & \mathbf 3 & \dots \\
\hline
\mathbf{\tuple{0,0}} & \tuple{0,0,0} & \tuple{0,0,1} & \tuple{0,0,2} & \tuple{0,0,3} & \dots \\
\hline
\mathbf{\tuple{0,1}} & \tuple{0,1,0} & \tuple{0,1,1} & \tuple{0,1,2} & \tuple{0,1,3} & \dots \\
\hline
\mathbf{\tuple{1,0}} & \tuple{1,0,0} & \tuple{1,0,1} & \tuple{1,0,2} & \tuple{1,0,3} & \dots \\
\hline
\mathbf{\tuple{0,2}} & \tuple{0,2,0} & \tuple{0,2,1} & \tuple{0,2,2} & \tuple{0,2,3} & \dots\\
\hline
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots \\
\end{array}
\]
پس با استفاده از روشی مانند روش زیگزاگ کانتور، می‌توانیم به همین ترتیب
برشماری‌ای از~$\Nat^3$ به دست آوریم. همچنین می‌توانیم این روند را ادامه
دهیم و برشماری‌هایی از $\Nat^n$ برای هر عدد طبیعی $n$ به دست آوریم.
\emph{یادداشت ویراستاری:} حالت توان صفر نیز شامل گزارهٔ بعدی است:
طبق قرارداد معمول، مجموعهٔ صفر‌تایی‌ها تک‌عضوی است و تنها عضو آن دنبالهٔ تهی
است؛ بنابراین این حالت نیز شماراست. شناسایی سه‌تایی با زوجِ شامل یک زوج،
همان قرارداد گروه‌بندی مؤلفه‌ها در متن مبدأ است.
بنابراین داریم:
\end{explain}
```

Preserve nested-pair convention and all triple-array cells. Add explicit singleton empty-tuple case for exponent0 and describe grouping as source convention, not literal Cartesian associativity for arbitrary set encodings. General step composes specified enumerations and needs no countable Choice.

Alternatives: No material alternative recorded; none invented.

## FA-0030-C07: Every finite natural power

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{prop}
$\Nat^n$ is !!{enumerable}, for every $n \in \Nat$.
\end{prop}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prop}
$\Nat^n$ برای هر $n \in \Nat$ شمارا است.
\end{prop}
```

Preserve every natural exponent, including0 after the explicit note. Does not assert Nat-to-the-Nat countable.

Alternatives: No material alternative recorded; none invented.

## FA-0030-C08: Positive-integer finite powers exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P050.

Source:
```latex
\begin{prob}\label{sfr:siz:zigzag:prob:posint-n}
Show that $(\PosInt)^n$ is !!{enumerable}, for every $n \in \Nat$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}\label{sfr:siz:zigzag:prob:posint-n}
نشان دهید $(\PosInt)^n$ برای هر $n \in \Nat$ شمارا است.
\end{prob}
```

Retain exponent n natural, exercise label and source obligation. Shift each coordinate; emptytuple handles n=0.

Alternatives: No material alternative recorded; none invented.

## FA-0030-C09: All finite positive-integer sequences exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning and relevant canon construction checked; no unresolved material semantic alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044.

Source:
```latex
\begin{prob}\label{sfr:siz:zigzag:prob:posint-star}
  Show that $(\PosInt)^*$ is !!{enumerable}. You may assume \cref{sfr:siz:zigzag:prob:posint-n}.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}\label{sfr:siz:zigzag:prob:posint-star}
  نشان دهید $(\PosInt)^*$ شمارا است. می‌توانید
  \cref{sfr:siz:zigzag:prob:posint-n} را فرض کنید.
\end{prob}
```

Retain star for finite sequences of all lengths, not infinite streams. Keep cref dependency exact. Specified coordinate and diagonal encodings yield a uniform length-coded injection into Nat; no arbitrary enumerations selected by Choice.

Alternatives: No material alternative recorded; none invented.

## Validation boundary

Every substantive source and target character lies in an ordered non-overlapping reviewed span. Formal tokens are checked across inline, bracketed, multline and align mathematics. Text arguments in mathematics are separately aligned and manually reviewed for exact connective, quantifier and number-family meaning.
Finite tests support the written reasoning; they are not universal formal proofs. No new PDF was built or visually certified. Frozen owner inputs and reader releases are unchanged; corrections enter the owner’s normal next-batch build and visual QA.
Attribution: Open Logic Project and contributors, under existing CC BY 4.0 notices. https://github.com/OpenLogicProject/OpenLogic . Existing edition: https://github.com/KokunoYumeto/OpenLogic-fa-ir . Canon sources retain separate rights.
