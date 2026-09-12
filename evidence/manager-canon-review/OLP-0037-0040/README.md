# Persian OpenLogic: the closing size-of-sets sections

Complete retrospective source/canon review of OLP-0037–0040, including disabled explanatory source text. Ten complete scholarly pages were consulted. Every substantive source/target span is mapped; exact locale expansion, not raw token spelling, controls inflection judgments. Source-correction package, not a new compiled reader or full-corpus certification.

## Review priorities

- Retain genuine Persian plural ezafe: element+s+ی realizes اعضای and is not an error.
- Preserve finite/empty enumeration conventions, bijective versus surjective lists, and both index origins.
- Correct reversed coordinate prose and the duplicated bit-flip direction, with source disclosures.
- Repair the malformed three-argument conditional around the optional footnote.
- Translate retained disabled explanatory blocks without activating them; disclose their source defects.
- Preserve the already localized Potter page locator and already disambiguated reduction exercise label through explicit audited mappings.
- Confidence is editorial 0-3, not calibrated probability. Human review is a later opportunity, not a gate.

## Scholarly pages actually consulted

- نظریهٔ مجموعه‌ها; محسن خانی, افشین زارعی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/jozve-kamel.pdf). PDF SHA-256: dbd518c80232921264ab5d79b79be01fe42efe8c01a766327db248b2d261de04. Canon PDFs are privately retained, not redistributed.
- مبانی منطق و نظریهٔ مجموعه‌ها; محسن خانی; دانشگاه صنعتی اصفهان. [Source](https://mohsen-khani.github.io/logic97-1/jozve/logic-full.pdf). PDF SHA-256: 565558b76701858236844f19663de27ee10a8d72fd8b007e69b85159ac49f86d. Canon PDFs are privately retained, not redistributed.
- منطق ریاضی; محسن خانی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/chapter2_0.pdf). PDF SHA-256: 0f3fb75ed1fcb0cbc669c04493acf520888e1ebfd62795bb28fc510bc41c7e79. Canon PDFs are privately retained, not redistributed.
- ریاضیات گسسته و کاربردها; علیرضا غفاری حدیقه, مگردیچ تومانیان; مؤسسه چاپ و انتشارات دانشگاه جامع امام حسین (ع). [Source](https://hadigheha.github.io/books/teaching/Textbooks/Tarkibiyat.pdf). PDF SHA-256: 8f79c45a926c1cea819c4fefa86383f2a65ae23b1d526baaf99cf2506bb9f317. Canon PDFs are privately retained, not redistributed.
- FA-OL-CANON-0003:P0051, PDF 51, printed 50: Lemmas5–6 and Schroder–Bernstein statement. Direct injection/surjection and equal-cardinality terminology, empty exception, and the two-injection theorem statement. Cardinal comparison here has Choice background. Do not copy incidental notation slips.
- FA-OL-CANON-0003:P0052, PDF 52, printed 51: Choice-free theorem discussion and finite cardinalities. The page explicitly distinguishes the Choice-free theorem from a well-ordering-based proof. Its displayed orbit proof has notation/argument defects and is not adopted as a proof. OLP0037 itself defers its proof; none is inserted.
- FA-OL-CANON-0003:P0053, PDF 53, printed 52: Definition10 and Cantor theorem13. Direct countably-infinite enumeration and diagonal reasoning. OLP includes finite and empty sets; this convention must remain explicit.
- FA-OL-CANON-0005:P0114, PDF 114, printed 114: Cardinal comparisons and definition262. Distinguishes finite, countably infinite and nonenumerable in a Choice/well-ordering setting. It is not authority for dropping the finite/empty exception in OLP.
- FA-OL-CANON-0005:P0115, PDF 115, printed 115: Cantor proof and subset/binary-function correspondence. Direct membership diagonal and binary characteristic-function correspondence. It supports all-coordinate matching, not uniqueness of binary real expansions.
- FA-OL-CANON-0001:P0082, PDF 82, printed 81: Algorithms, inputs/outputs and possible nontermination. Read the distinction between arbitrary functions and algorithms that may not terminate. No effective-enumeration requirement is imported. Exact کاهش and پسین are not attested here; their lexical limits are recorded rather than fabricated.
- FA-REL-P044, PDF 44, printed 34: Function definition, image, domain and codomain. Direct function-language syntax and mathematical membership context. Preserve source function type; image is not automatically the whole codomain.
- FA-REL-P045, PDF 45, printed 35: Floor/ceiling definition, graph and negative examples. Direct ceiling term and integer examples, including negative values. Retain the least-integer-above meaning rather than ordinary nearest-integer rounding.
- FA-REL-P046, PDF 46, printed 36: Injective and surjective functions with diagrams. Distinct at-most-one and at-least-one preimage conditions. A surjective image list may repeat even if its original enumeration does not.
- FA-REL-P050, PDF 50, printed 40: Composition and inverse of a bijection. Direct composition/inverse idiom. An injection has a unique inverse on its image; do not extend that inverse to the whole target without a construction.

## FA-0037-C01: Heading and theorem name

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0005:P0114.

Source:
```latex
\olsection{The Notion of Size, and Schr\"oder-Bernstein}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{مفهوم اندازه و قضیهٔ شرودر–برنشتاین}
```

Retain size and the scholarly rendering شرودر–برنشتاین, directly corresponding to the canon’s theorem name.

Alternatives: No material alternative recorded; none invented.

## FA-0037-C02: Intuition does not replace proof

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0005:P0114.

Source:
```latex
\begin{explain}
Here is an intuitive thought: if $A$ is no larger than $B$ and $B$ is
no larger than $A$, then $A$ and $B$ are equinumerous. To be honest,
if this thought were \emph{wrong}, then we could scarcely justify the
thought that our defined notion of equinumerosity has anything to do
with comparisons of ``sizes'' between sets!{} Fortunately, though,
the intuitive thought is correct. This is justified by the
Schr\"oder-Bernstein Theorem.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
اندیشهٔ شهودیِ زیر را در نظر بگیرید: اگر $A$ از $B$ بزرگ‌تر نباشد و
$B$ از $A$ بزرگ‌تر نباشد، آنگاه $A$ و $B$ هم‌توان‌اند. انصافاً اگر این
اندیشه \emph{نادرست} بود، به‌دشواری می‌توانستیم این تصور را توجیه کنیم
که مفهوم تعریف‌شدهٔ ما از هم‌توانی ربطی به مقایسهٔ «اندازه»های
مجموعه‌ها دارد!{} اما خوشبختانه این اندیشهٔ شهودی درست است. قضیهٔ
شرودر–برنشتاین این امر را توجیه می‌کند.
\end{explain}
```

Both inequalities and equinumerosity are preserved. Source rhetorical explanation remains, without inserting a new analogy or claiming a proof here.

Alternatives: No material alternative recorded; none invented.

## FA-0037-C03: Schroder–Bernstein statement

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0052, FA-OL-CANON-0005:P0114.

Source:
```latex
\begin{thm}[Schr\"oder-Bernstein]
	\ollabel{thm:schroder-bernstein}
	If $\cardle{A}{B}$ and $\cardle{B}{A}$,
	then $\cardeq{A}{B}$.
\end{thm}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{thm}[شرودر–برنشتاین]
	\ollabel{thm:schroder-bernstein}
	اگر $\cardle{A}{B}$ و $\cardle{B}{A}$،
	آنگاه $\cardeq{A}{B}$.
\end{thm}
```

Two opposite injections suffice for a bijection, including empty cases. This is not literal equality of sets and needs no Choice.

Alternatives: No material alternative recorded; none invented.

## FA-0037-C04: Equivalent injection wording

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0003:P0051.

Source:
```latex
\begin{explain}
In other words, if there is !!a{injection} from $A$ to~$B$, and
!!a{injection} from $B$ to~$A$, then there is !!a{bijection} from $A$
to~$B$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
به عبارت دیگر، اگر نگاشت یک‌به‌یک از $A$ به~$B$ و نگاشت یک‌به‌یک از
$B$ به~$A$ وجود داشته باشد، آنگاه تناظر دوسویی از $A$ به~$B$ وجود
دارد.
```

Preserve both arrow directions and existential quantifiers. Bijection is the conclusion, not an assumption.

Alternatives: No material alternative recorded; none invented.

## FA-0037-C05: Difficulty and historical citation

Action: retain_after_fresh_review; confidence 2/3: Editorial0–3, not a calibrated probability. Meaning checked; the stated lexical, historical or editorial limit remains.
Canon: FA-OL-CANON-0003:P0052, FA-OL-CANON-0005:P0114.

Source:
```latex
This result, however, is really rather \emph{difficult} to prove.
Indeed, although Cantor stated the result, others proved
it.\footnote{For more on the history, see e.g.,
\citet[pp.~165--6]{Potter2004}.}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
بااین‌حال اثبات این نتیجه واقعاً نسبتاً \emph{دشوار} است. در واقع،
هرچند کانتور این نتیجه را بیان کرد، دیگران آن را اثبات
کردند.\footnote{برای آگاهی بیشتر از تاریخچه، برای نمونه بنگرید به
\citet[صص.~165--6]{Potter2004}.}
```

Retain the source’s attribution, existing Potter2004 key and pages165–166. Localized صص. is an existing equivalent page prefix, not a changed page number.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Historical attribution is inherited from the cited source; no independent reading of Potter’s pages is claimed.

## FA-0037-C06: Conditional deferred proof

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0052, FA-OL-CANON-0005:P0114.

Source:
```latex
\oliflabeldef{sfr:cardinals:card-sb:sec}{We will only be in
a position to \emph{prove} Schr\"oder-Bernstein in
\olref[sfr][cardinals][card-sb]{sec}.}{}% 
For now, you can (and must)
take it on trust.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\oliflabeldef{sfr:cardinals:card-sb:sec}{تنها زمانی می‌توانیم قضیهٔ
شرودر–برنشتاین را \emph{اثبات} کنیم که به
\olref[sfr][cardinals][card-sb]{sec} برسیم.}{}%
فعلاً می‌توانید (و باید) آن را بی‌اثبات بپذیرید.
```

Keep conditional later-section link and the instruction that the theorem is being accepted before proof. Do not import the canon’s defective displayed orbit proof.

Alternatives: No material alternative recorded; none invented.

## FA-0037-C07: Two directional tasks, not cases

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0005:P0114, FA-REL-P046.

Source:
```latex
Fortunately, Schr\"oder-Bernstein is \emph{correct}, and it
vindicates our thinking of the relations we defined, i.e.,
$\cardeq{A}{B}$ and $\cardle{A}{B}$, as having something to do with
``size''. Moreover, Schr\"oder-Bernstein is very \emph{useful}. It
can be difficult to think of !!a{bijection} between two equinumerous
sets. The Schr\"oder-Bernstein Theorem allows us to break the comparison
down into cases so we only have to think of !!a{injection} from the
first to the second, and vice-versa.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
خوشبختانه قضیهٔ شرودر–برنشتاین \emph{درست} است و تصور ما را تأیید
می‌کند که رابطه‌هایی که تعریف کردیم، یعنی $\cardeq{A}{B}$ و
$\cardle{A}{B}$، واقعاً به «اندازه» ارتباط دارند. افزون‌براین، قضیهٔ
شرودر–برنشتاین \emph{بسیار سودمند} است. یافتنِ تناظر دوسویی میان دو
مجموعهٔ هم‌توان می‌تواند دشوار باشد. قضیهٔ شرودر–برنشتاین به ما اجازه
می‌دهد مقایسه را در دو جهت جداگانه انجام دهیم، به‌گونه‌ای که فقط لازم باشد
نگاشت یک‌به‌یک از مجموعهٔ نخست به مجموعهٔ دوم و برعکس بیابیم.
\end{explain}
```

The source’s cases are the two directions of injection construction. Render as two separately checked directions, not an exhaustive case split on a set.

Alternatives: No material alternative recorded; none invented.

## FA-0038-C01: Alternative enumeration heading

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0114.

Source:
```latex
\olsection{Enumerations and \usetoken{S}{enumerable} Sets}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{برشماری‌ها و مجموعه‌های شمارا}
```

Preserve the title token’s actual realization شمارا; source convention remains inclusive.

Alternatives: No material alternative recorded; none invented.

## FA-0038-C02: Set-theoretic convention editorial

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P050.

Source:
```latex
\begin{editorial}
  This section defines enumerations as bijections with (initial
  segments) of $\Nat$, the way it's done in set theory. So it
  conflicts slightly with the definitions in \olref[enm]{sec}, and
  repeats all the examples there. It is also a bit more terse than
  that section.
\end{editorial}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{editorial}
  این بخش برشماری‌ها را، مطابق شیوهٔ رایج در نظریهٔ مجموعه‌ها، به‌صورت
  تناظرهای دوسویی با (قطعه‌های آغازینِ) $\Nat$ تعریف می‌کند. بنابراین
  اندکی با تعریف‌های \olref[enm]{sec} تعارض دارد و همهٔ مثال‌های آنجا
  را تکرار می‌کند. همچنین کمی موجزتر از آن بخش است.
\end{editorial}
```

Bijections rather than arbitrary surjective lists; preserve the explicit contrast, repeated examples and relative terseness.

Alternatives: No material alternative recorded; none invented.

## FA-0038-C03: Finite listing and empty case

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-REL-P044, FA-OL-CANON-0003:P0052, FA-OL-CANON-0003:P0053.

Source:
```latex
We can specify finite set is by simply enumerating its
!!{element}s. We do this when we define a set like so:
\[
  A = \{a_1, a_2, \ldots, a_n\}.
\]
Assuming that the !!{element}s $a_1$, \dots, $a_n$ are all distinct,
this gives us !!a{bijection} between $A$ and the first $n$ natural
numbers $0$, \dots, $n-1$. Conversely, since every finite set has only
finitely many !!{element}s, every finite set can be put into such a
correspondence. In other words, if $A$ is finite, there is
!!a{bijection} between $A$ and $\{0, \dots, n-1\}$, where $n$ is the
number of !!{element}s of~$A$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
می‌توانیم یک مجموعهٔ متناهی را صرفاً با برشمردن
اعضای آن مشخص کنیم. این کار را هنگامی انجام می‌دهیم که مجموعه‌ای را
به‌صورت زیر تعریف می‌کنیم:
\[
  A = \{a_1, a_2, \ldots, a_n\}.
\]
با فرض اینکه اعضای $a_1$، \dots، $a_n$ همگی متمایز باشند،
این تعریف تناظر دوسویی میان $A$ و نخستین $n$ عدد طبیعی، یعنی $0$،
\dots، $n-1$، به دست می‌دهد. برعکس، چون هر مجموعهٔ متناهی فقط تعداد
متناهی عضو دارد، هر مجموعهٔ متناهی را می‌توان در چنین تناظری
قرار داد. به عبارت دیگر، اگر $A$ متناهی باشد، میان $A$ و
$\{0, \dots, n-1\}$ تناظر دوسویی وجود دارد، که در آن $n$ شمار
اعضای~$A$ است.
\emph{یادداشت دربارهٔ حالت تهی:} در این جمله، قطعهٔ آغازینِ متناظر با
مجموعهٔ تهی نیز تهی در نظر گرفته می‌شود. تعریفِ بعدی، شمارابودنِ مجموعهٔ
تهی را جداگانه تصریح می‌کند.
```

Distinct listed members give a bijection with the first n naturals. All four اعضای forms are valid expanded plural-ezafe constructions and retained. The n=0 initial-segment convention is explicit; no spurious extra member is inserted.

Alternatives: No material alternative recorded; none invented.

## FA-0038-C04: Infinite enumeration

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0114.

Source:
```latex
If we allow for certain kinds of infinite sets, then we will also
allow some infinite sets to be enumerated. We can make this precise by
saying that an infinite set is enumerated by !!a{bijection} between it
and all of~$\Nat$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
اگر برخی گونه‌های مجموعهٔ نامتناهی را نیز مجاز بدانیم، آنگاه اجازه
خواهیم داد برخی مجموعه‌های نامتناهی هم برشمرده شوند. می‌توانیم این مطلب
را با گفتن اینکه یک مجموعهٔ نامتناهی به‌وسیلهٔ تناظر دوسویی میان آن
و کل~$\Nat$ برشمرده می‌شود، دقیق سازیم.
```

Keep bijection with all Nat, not merely injection and not a listing required to be computable.

Alternatives: No material alternative recorded; none invented.

## FA-0038-C05: Enumeration definition

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P050.

Source:
```latex
\begin{defn}[Enumeration, set-theoretic] 
An \emph{enumeration} of a set $A$ is !!a{bijection} whose range is
$A$ and whose domain is either an initial set of natural numbers $\{0,
1, \ldots, n\}$ {or} the entire set of natural numbers~$\Nat$. 
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}[برشماری، مجموعه‌شناختی]
یک \emph{برشماری} از مجموعهٔ $A$، یک تناظر دوسویی است که بردش $A$
و دامنه‌اش یا قطعه‌ای آغازین از اعداد طبیعی $\{0,
1, \ldots, n\}$ {یا} کل مجموعهٔ اعداد طبیعی~$\Nat$ است.
\end{defn}
```

Finite initial segment0 through n has n+1 elements; this bound is a new dummy variable, not the previous size n. Empty is separately allowed in enumerable definition.

Alternatives: No material alternative recorded; none invented.

## FA-0038-C06: Counting and index origin

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044.

Source:
```latex
\begin{explain}
There is an intuitive underpinning to this use of the word
\emph{enumeration}. For to say that we have enumerated a set $A$ is to
say that there is !!a{bijection} $f$ which allows us to count out the
elements of the set $A$. The $0$th element is $f(0)$, the 1st is
$f(1)$, \ldots the $n$th is $f(n)$\ldots.\footnote{Yes, we count
from $0$. Of course we could also start with~$1$. This would
make no big difference. We would just have to replace~$\Nat$
by~$\PosInt$.} The rationale for this may be made even clearer by
adding the following:
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
این کاربرد واژهٔ \emph{برشماری} مبنایی شهودی دارد. زیرا اینکه بگوییم
مجموعهٔ $A$ را برشمرده‌ایم، یعنی یک تناظر دوسویی مانند $f$ وجود دارد
که به ما اجازه می‌دهد عضوهای مجموعهٔ $A$ را یک‌به‌یک بشماریم. عضو
$0$اُم، $f(0)$ است؛ عضو 1اُم، $f(1)$ است؛ \ldots و عضو $n$اُم،
$f(n)$ است\ldots.\footnote{بله، از $0$ می‌شماریم. البته می‌توانستیم
از~$1$ نیز آغاز کنیم. این انتخاب تفاوت مهمی ایجاد نمی‌کرد. فقط لازم
بود~$\Nat$ را با~$\PosInt$ جایگزین کنیم.} مبنای این کاربرد را می‌توان
با افزودن تعریف زیر باز هم روشن‌تر کرد:
\end{explain}
```

Preserve f(0),f(1),f(n) and footnote0 versus1. Ordinal suffixes attach to mathematical indices; no indices are silently shifted.

Alternatives: No material alternative recorded; none invented.

## FA-0038-C07: Enumerable/nonenumerable definition

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0114.

Source:
```latex
\begin{defn}
  \ollabel{defn:enumerable}
  A set~$A$ is !!{enumerable} iff either $A = \emptyset$ or there is
  an enumeration of~$A$. We say that $A$ is !!{nonenumerable} iff $A$
  is not !!{enumerable}.
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}
  \ollabel{defn:enumerable}
  مجموعهٔ~$A$ شمارا است اگر و تنها اگر یا $A = \emptyset$
  باشد یا برشماری‌ای از~$A$ وجود داشته باشد. می‌گوییم $A$
  ناشمارا است اگر و تنها اگر $A$ شمارا نباشد.
\end{defn}
```

Explicit empty alternative, existence of a finite-or-Nat bijection, and negation are all retained. Do not substitute strict countably infinite.

Alternatives: No material alternative recorded; none invented.

## FA-0038-C08: Definition in words

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-REL-P044, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{explain}
So a set is !!{enumerable} iff it is empty or you can use an
enumeration to count out its !!{element}s.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
پس یک مجموعه شمارا است اگر و تنها اگر تهی باشد یا بتوان
به‌کمک یک برشماری اعضای آن را یک‌به‌یک شمرد.
\end{explain}
```

Retain empty or counting its members; the expanded اعضای آن is grammatical.

Alternatives: No material alternative recorded; none invented.

## FA-0038-C09: Identity and successor examples

Action: retain_after_fresh_review; confidence 2/3: Editorial0–3, not a calibrated probability. Meaning checked; the stated lexical, historical or editorial limit remains.
Canon: FA-REL-P044, FA-REL-P050, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{ex}
A function enumerating the natural numbers is simply the identity
function $\Id{\Nat} \colon \Nat \to \Nat$ given by $\Id{\Nat}(n) = n$. A
function enumerating the \emph{positive} natural numbers, $\Nat^+ =
\Nat \setminus \{0\}$, is the function $g(n) = n + 1$, i.e., the
successor function.
\end{ex}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{ex}
تابعی که اعداد طبیعی را برمی‌شمارد، صرفاً تابع همانی
$\Id{\Nat} \colon \Nat \to \Nat$ است که با $\Id{\Nat}(n) = n$ داده
می‌شود. تابعی که اعداد طبیعیِ \emph{مثبت}، یعنی $\Nat^+ =
\Nat \setminus \{0\}$، را برمی‌شمارد، تابع $g(n) = n + 1$، یعنی تابع
پسین، است.
\end{ex}
```

Identity enumerates Nat; n+1 enumerates positive naturals. Preserve the stated map and source domain. پسین is retained with its explicit n+1 meaning.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Exact lexical label تابع پسین was not found on the selected pages; its mathematical meaning is fixed by n+1. Later lexical review may replace the label without changing the map.

## FA-0038-C10: Surjection/injection equivalences exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0051, FA-REL-P046, FA-REL-P050.

Source:
```latex
\begin{prob}
Show that a set $A$ is !!{enumerable} iff either $A = \emptyset$ or
there is !!a{surjection} $f\colon \Nat \to A$. Show that $A$ is
!!{enumerable} iff there is !!a{injection} $g\colon A \to \Nat$. 
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
نشان دهید مجموعهٔ $A$ شمارا است اگر و تنها اگر یا
$A = \emptyset$ باشد یا نگاشت پوشا به‌صورت $f\colon \Nat \to A$
وجود داشته باشد. نشان دهید $A$ شمارا است اگر و تنها اگر
نگاشت یک‌به‌یک به‌صورت $g\colon A \to \Nat$ وجود داشته باشد.
\end{prob}
```

Both directions, the empty exception for surjections, and the unconditional injection characterization are retained. First-occurrence indexing requires no arbitrary choice family.

Alternatives: No material alternative recorded; none invented.

## FA-0038-C11: Even and odd examples

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-REL-P044, FA-REL-P046, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{ex}
The functions $f\colon \Nat \to \Nat$ and $g \colon \Nat \to \Nat$
given by
\begin{align*}
  f(n) & = 2n \text{ and}\\
  g(n) & = 2n+1
\end{align*}
respectively enumerate the even natural numbers and the odd natural
numbers. But neither is !!{surjective}, so neither is an enumeration
of $\Nat$.
\end{ex}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{ex}
توابع $f\colon \Nat \to \Nat$ و $g \colon \Nat \to \Nat$ که
به‌صورت زیر داده می‌شوند
\begin{align*}
  f(n) & = 2n \text{ و}\\
  g(n) & = 2n+1
\end{align*}
به‌ترتیب اعداد طبیعی زوج و اعداد طبیعی فرد را برمی‌شمارند. اما هیچ‌یک
پوشا نیست؛ پس هیچ‌یک برشماریِ $\Nat$ نیست.
\end{ex}
```

Correct images of2n and2n+1 from zero, neither onto Nat. The English and inside align is translated as و with all formulas preserved.

Alternatives: No material alternative recorded; none invented.

## FA-0038-C12: Positive square sequence exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P044.

Source:
```latex
\begin{prob}
Define an enumeration of the square numbers $1$, $4$, $9$, $16$, \dots
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
برشماری‌ای از اعداد مربعی $1$، $4$، $9$، $16$، \dots تعریف کنید.
\end{prob}
```

Source starts1,4,9,16, not0. Preserve that sequence and the unsolved request.

Alternatives: No material alternative recorded; none invented.

## FA-0038-C13: Ceiling and integer zigzag

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-REL-P045, FA-REL-P044, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{ex}
Let $\lceil x \rceil$ be the \emph{ceiling} function, which rounds $x$
up to the nearest integer. Then the function $f \colon \Nat \to \Int$
given by:
\[
  f(n) = (-1)^{n} \left\lceil\tfrac{n}{2}\right\rceil
\]
enumerates the set of
integers~$\Int$ as follows:
\[
\begin{array}{c c c c c c c c}
f(0) & f(1) & f(2) & f(3) & f(4) & f(5) & f(6) & \dots \\ \\
\big\lceil \tfrac{0}{2} \big\rceil & -\big\lceil \tfrac{1}{2}\big\rceil &  \big\lceil \tfrac{2}{2} \big\rceil & -\big\lceil \tfrac{3}{2} \big\rceil & \big\lceil \tfrac{4}{2} \big\rceil  & -\big\lceil \tfrac{5}{2}\big\rceil & \big\lceil \tfrac{6}{2} \big\rceil & \dots \\ \\
0 & -1 & 1 & -2 & 2 & -3 & 3& \dots
\end{array}
\]
Notice how $f$ generates the values of $\Int$ by ``hopping'' back and
forth between positive and negative integers. You can also think of
$f$ as defined by cases as follows:
\[
f(n) = \begin{cases}
  \frac{n}{2} & \text{if $n$ is even}\\
  -\frac{n+1}{2} & \text{if $n$ is odd}
  \end{cases}
\]
\end{ex}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{ex}
بگذارید $\lceil x \rceil$ تابع \emph{سقف} باشد که $x$ را به کوچک‌ترین عدد صحیحِ بزرگ‌تر یا مساویِ آن می‌برد. آنگاه تابع $f \colon \Nat \to \Int$
که به‌صورت زیر داده می‌شود:
\[
  f(n) = (-1)^{n} \left\lceil\tfrac{n}{2}\right\rceil
\]
مجموعهٔ اعداد صحیح~$\Int$ را به‌ترتیب زیر برمی‌شمارد:
\[
\begin{array}{c c c c c c c c}
f(0) & f(1) & f(2) & f(3) & f(4) & f(5) & f(6) & \dots \\ \\
\big\lceil \tfrac{0}{2} \big\rceil & -\big\lceil \tfrac{1}{2}\big\rceil &  \big\lceil \tfrac{2}{2} \big\rceil & -\big\lceil \tfrac{3}{2} \big\rceil & \big\lceil \tfrac{4}{2} \big\rceil  & -\big\lceil \tfrac{5}{2}\big\rceil & \big\lceil \tfrac{6}{2} \big\rceil & \dots \\ \\
0 & -1 & 1 & -2 & 2 & -3 & 3& \dots
\end{array}
\]
توجه کنید که $f$ چگونه مقادیر $\Int$ را با «جهیدن» رفت‌وبرگشتی
میان اعداد صحیح مثبت و منفی تولید می‌کند. همچنین می‌توانید $f$ را
به‌صورت موردیِ زیر در نظر بگیرید:
\[
f(n) = \begin{cases}
  \frac{n}{2} & \text{اگر $n$ زوج باشد}\\
  -\frac{n+1}{2} & \text{اگر $n$ فرد باشد}
  \end{cases}
\]
\end{ex}
```

Direct سقف attestation. Specify the least integer at least x; preserve0,-1,1,-2,2 and both parity branches with nested mathematical n unchanged.

Alternatives: No material alternative recorded; none invented.

## FA-0038-C14: Binary union exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053, FA-REL-P050.

Source:
```latex
\begin{prob}
Show that if $A$ and $B$ are !!{enumerable}, so is $A \cup B$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
نشان دهید اگر $A$ و $B$ شمارا باشند، $A \cup B$ نیز چنین است.
\end{prob}
```

Finite or infinite enumerations can be interleaved, then first occurrences kept. Empty sets and overlap do not invalidate the statement; exercise remains unsolved.

Alternatives: No material alternative recorded; none invented.

## FA-0038-C15: Finite union induction exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{prob}
Show by induction on $n$ that if $A_1$, $A_2$, \dots, $A_n$ are all
!!{enumerable}, so is $A_1 \cup \dots \cup A_n$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
با استقرا بر $n$ نشان دهید که اگر $A_1$، $A_2$، \dots، $A_n$ همگی
شمارا باشند، $A_1 \cup \dots \cup A_n$ نیز چنین است.
\end{prob}
```

Preserve finite n-family and induction. No claim about an arbitrary countable family without selected enumerations is added.

Alternatives: No material alternative recorded; none invented.

## FA-0039-C01: Nonenumerability heading

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0114, FA-OL-CANON-0003:P0053.

Source:
```latex
\olsection{\printtoken{S}{nonenumerable} Sets}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{مجموعه‌های ناشمارا}
```

Actual heading token is ناشمارا. It negates the inclusive enumerable definition.

Alternatives: No material alternative recorded; none invented.

## FA-0039-C02: Alternative-definition editorial

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P046, FA-REL-P050.

Source:
```latex
\begin{editorial}
  This section proves the non-enumerability of $\Bin^\omega$ and
  $\Pow{\Nat}$ using the definitions in \olref[enm-alt]{sec}, i.e.,
  requiring a bijection with~$\Nat$ instead of a surjection from
  $\PosInt$.
\end{editorial}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{editorial}
  این بخش ناشمارابودنِ $\Bin^\omega$ و $\Pow{\Nat}$ را با استفاده از
  تعریف‌های \olref[enm-alt]{sec} ثابت می‌کند؛ یعنی وجود تناظری دوسویی
  با~$\Nat$ را به‌جای یک تابع پوشا از $\PosInt$ لازم می‌گیرد.
\end{editorial}
```

Preserve Bin omega and Pow Nat and the distinction from the PosInt-surjection route.

Alternatives: No material alternative recorded; none invented.

## FA-0039-C03: Infinite enumerable naturals and other sets

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0114.

Source:
```latex
\begin{explain}
The set $\Nat$ of natural numbers is infinite. It is also trivially
!!{enumerable}. But the remarkable fact is that there are
\emph{!!{nonenumerable}} sets, i.e., sets which are not !!{enumerable}
(see \olref[sfr][siz][enm-alt]{defn:enumerable}).
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
مجموعهٔ $\Nat$ از اعداد طبیعی نامتناهی است. همچنین به‌وضوح
شمارا است. اما واقعیت شگفت‌انگیز این است که مجموعه‌های
\emph{ناشمارا} وجود دارند؛ یعنی مجموعه‌هایی که شمارا
نیستند (نگاه کنید به \olref[sfr][siz][enm-alt]{defn:enumerable}).
```

Nat is infinite and enumerable; source definition reference and existence of nonenumerable sets are retained.

Alternatives: No material alternative recorded; none invented.

## FA-0039-C04: Finite exception and cardinal comparison

Action: correct; confidence 2/3: Editorial0–3, not a calibrated probability. Meaning checked; the stated lexical, historical or editorial limit remains.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0114.

Source:
```latex
This might be surprising. After all, to say that $A$ is
!!{nonenumerable} is to say that there is \emph{no} !!{bijection} $f
\colon \Nat \to A$; that is, no function mapping the infinitely many
!!{element}s of~$\Nat$ to~$A$ exhausts all of~$A$.  So if $A$ is
!!{nonenumerable}, there are ``more'' !!{element}s of~$A$ than there
are natural numbers.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
این مطلب شاید شگفت‌آور باشد. برای یک مجموعهٔ نامتناهی، گفتن اینکه $A$
ناشمارا است یعنی گفتن اینکه \emph{هیچ} تناظر دوسویی‌ای مانند $f
\colon \Nat \to A$ وجود ندارد؛ یعنی هیچ تابعی که اعضای~$\Nat$
را، که شمارشان نامتناهی است، به~$A$ نگاشت کند، همهٔ~$A$ را فرا نمی‌گیرد. پس اگر
$A$ ناشمارا باشد، شمار اعضای~$A$ از شمار اعداد طبیعی
«بیشتر» است.
\emph{یادداشت ویراستاری:} نبودنِ تناظر دوسویی با کل اعداد طبیعی،
مجموعه‌های متناهی را نیز شامل می‌شود؛ قید نامتناهی در این توضیح ضروری است.
در مورد مجموعه‌های دلخواه، تعبیرِ مقایسهٔ اندازه‌ها در اینجا با فرض اصل
انتخاب خوانده می‌شود. برهان‌های قطریِ زیر به این فرض نیاز ندارند.
```

The no-bijection-with-Nat equivalence is restricted to infinite A: finite A is a counterexample to the unrestricted phrase. A separate editorial note identifies the sufficient Choice background of the general more-than comparison, not of either following diagonal proof.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Review the explicit assumption disclosure as editorial wording, not a new claim that full Choice is a weakest necessary principle.

## FA-0039-C05: Diagonal strategy and scope

Action: correct; confidence 2/3: Editorial0–3, not a calibrated probability. Meaning checked; the stated lexical, historical or editorial limit remains.
Canon: FA-OL-CANON-0005:P0115, FA-OL-CANON-0003:P0053, FA-OL-CANON-0001:P0082.

Source:
```latex
To prove that a set is !!{nonenumerable}, you have to show that no
appropriate !!{bijection} can exist. The best way to do this is to
show that every attempt to enumerate !!{element}s of~$A$ must leave at
least one !!{element} out; this shows that no function $f\colon \Nat
\to A$ is !!{surjective}. And a general strategy for establishing this
is to use Cantor's \emph{diagonal method}. Given a list of
!!{element}s of $A$, say, $x_1$, $x_2$, \dots, we construct another
!!{element} of~$A$ which, by its construction, cannot possibly be on
that list.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
برای اثبات اینکه مجموعه‌ای نامتناهی ناشمارا است، باید نشان دهید که هیچ
تناظر دوسویی مناسبی نمی‌تواند وجود داشته باشد. بهترین راه برای این کار
آن است که نشان دهید هر کوششی برای برشمردن اعضای~$A$ ناگزیر
دست‌کم یک عضو را از قلم می‌اندازد؛ این نشان می‌دهد که هیچ تابع
$f\colon \Nat \to A$ پوشا نیست. راهبردی کلی برای اثبات این
مطلب، استفاده از \emph{روش قطری} کانتور است. با داشتن فهرستی از
اعضای $A$، مثلاً $x_1$، $x_2$، \dots، عضو دیگری از~$A$
می‌سازیم که بنا بر نحوهٔ ساختش، به‌هیچ‌وجه نمی‌تواند در آن فهرست باشد.
```

For infinite A, ruling out all infinite lists suffices. Do not confuse arbitrary lists with effective/algorithmic enumeration. The exact قطری label is source-driven, with the canon attesting the construction.

Alternatives: No material alternative recorded; none invented.

Expert-review question: The consulted canon demonstrates the diagonal argument, but does not supply a direct exact-label attestation for قطری‌سازی.

## FA-0039-C06: Binary sequences and conditional footnote

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P044.

Source:
```latex
But all of this is best understood by example. So, our first example
is the set~$\Bin^\omega$ of all infinite strings of $0$'s and $1$'s.
(The `$\Bin$' stands for binary, and we can just think of it as the
two-element set
$\{0,1\}$.)\oliflabeldef{sfr:card-arithmetic:card-opps:sec}{\footnote{More
accurately, we should stipulate that $\Bin^\omega$ is the set of all
$\omega$-sequences of $0$'s and $1$s, i.e., the set
$\funfromto{\omega}{\{0,1\}}$. But the meaning of this will only
become clear in \olref[sfr][card-arithmetic][card-opps]{sec}.}{} This
slightly loose formulation should not cause any confusions
for now, however.}
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
اما همهٔ این مطالب با یک مثال بهتر فهمیده می‌شوند. بنابراین نخستین مثال
ما مجموعهٔ~$\Bin^\omega$ از همهٔ رشته‌های نامتناهیِ $0$ها و $1$هاست.
(نماد $\Bin$ نمایندهٔ «دودویی» است و می‌توانیم آن را صرفاً مجموعهٔ دوعضویِ
$\{0,1\}$ بدانیم.)\oliflabeldef{sfr:card-arithmetic:card-opps:sec}{\footnote{دقیق‌تر
آن است که مقرر کنیم $\Bin^\omega$ مجموعهٔ همهٔ دنباله‌های $\omega$تایی
از $0$ها و $1$ها، یعنی مجموعهٔ
$\funfromto{\omega}{\{0,1\}}$، است. اما معنای این مطلب تنها در
\olref[sfr][card-arithmetic][card-opps]{sec} روشن خواهد شد.}}{}
بااین‌حال، این صورت‌بندیِ اندکی مسامحه‌آمیز فعلاً نباید موجب هیچ ابهامی شود.
\end{explain}
```

Keep infinite zero-one strings, set{0,1} and omega-function precision. Repair three-argument oliflabeldef grouping so its true branch is the optional footnote and its false branch is empty; no end-environment token is consumed.

Alternatives: No material alternative recorded; none invented.

## FA-0039-C07: Binary theorem

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{thm}
\ollabel{thm:nonenum-bin-omega}
$\Bin^\omega$~is !!{nonenumerable}.
\end{thm}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{thm}
\ollabel{thm:nonenum-bin-omega}
$\Bin^\omega$~ناشمارا است.
\end{thm}
```

Preserve nonenumerability of all infinite binary strings, not finite words or only computable sequences.

Alternatives: No material alternative recorded; none invented.

## FA-0039-C08: List and coordinate array

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P044.

Source:
```latex
\begin{proof}
Consider any enumeration of a subset of $\Bin^\omega$. So we have some
list $s_{0}$, $s_{1}$, $s_{2}$, \dots{} where every $s_n$ is an
infinite string of $0$'s and~$1$'s. Let $s_n(m)$ be the $n$th digit of
the $m$th string in this list. So we can now think of our list as an
array, where $s_n(m)$ is placed at the $n$th row and $m$th column:
\[
\begin{array}{c|c|c|c|c|c}
& 0 & 1 & 2 & 3 & \dots \\\hline
0 & \mathbf{s_{0}(0)} & s_{0}(1) & s_{0}(2) & s_0(3) & \dots \\\hline
1 & s_{1}(0)& \mathbf{s_{1}(1)} & s_1(2) & s_1(3) & \dots \\\hline
2 & s_{2}(0)& s_{2}(1) & \mathbf{s_2(2)} & s_2(3) & \dots \\\hline
3 & s_{3}(0)& s_{3}(1) & s_3(2) & \mathbf{s_3(3)} & \dots \\\hline
\vdots & \vdots & \vdots & \vdots & \vdots & \mathbf{\ddots}
\end{array}
\]
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
هر فهرستِ نامتناهی از اعضای $\Bin^\omega$ را در نظر بگیرید. پس فهرستی
مانند $s_{0}$، $s_{1}$، $s_{2}$، \dots{} داریم که در آن هر $s_n$ رشته‌ای
نامتناهی از $0$ها و~$1$هاست. بگذارید $s_n(m)$ رقم $m$اُمِ رشتهٔ $n$اُمِ
این فهرست باشد. اکنون می‌توانیم فهرست خود را آرایه‌ای در نظر بگیریم که
در آن $s_n(m)$ در سطر $n$اُم و ستون $m$اُم قرار گرفته است.
\emph{یادداشت ویراستاری:} ترتیب شاخص‌های رقم و رشته در جملهٔ متن مبدأ
جابه‌جا شده بود؛ اینجا با آرایه هماهنگ شده است:
\[
\begin{array}{c|c|c|c|c|c}
& 0 & 1 & 2 & 3 & \dots \\\hline
0 & \mathbf{s_{0}(0)} & s_{0}(1) & s_{0}(2) & s_0(3) & \dots \\\hline
1 & s_{1}(0)& \mathbf{s_{1}(1)} & s_1(2) & s_1(3) & \dots \\\hline
2 & s_{2}(0)& s_{2}(1) & \mathbf{s_2(2)} & s_2(3) & \dots \\\hline
3 & s_{3}(0)& s_{3}(1) & s_3(2) & \mathbf{s_3(3)} & \dots \\\hline
\vdots & \vdots & \vdots & \vdots & \vdots & \mathbf{\ddots}
\end{array}
\]
```

Use arbitrary infinite list; s_n(m) is digit m of string n, matching row n and column m. Two coordinate tokens are corrected and disclosed; array and diagonal entries unchanged.

Alternatives: No material alternative recorded; none invented.

## FA-0039-C09: Complement both bits

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-OL-CANON-0003:P0053.

Source:
```latex
We will now construct an infinite string, $d$, of $0$'s and $1$'s
which is not on this list.  We will do this by specifying each of its
entries, i.e., we specify $d(n)$ for all $n \in \Nat$.  Intuitively,
we do this by reading down the diagonal of the array above (hence the
name ``diagonal method'') and then changing every $1$ to a $0$ and
every $1$ to a~$0$. More abstractly, we define $d(n)$ to be $0$ or $1$
according to whether the $n$-th !!{element} of the diagonal, $s_n(n)$,
is $1$ or $0$, that is:
\[
d(n) =
\begin{cases}
1 & \text{if $s_{n}(n) = 0$}\\
0 & \text{if $s_{n}(n) = 1$}
\end{cases}
\]
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
اکنون رشته‌ای نامتناهی، یعنی $d$، از $0$ها و $1$ها می‌سازیم که در این
فهرست نیست. این کار را با مشخص‌کردن هریک از درایه‌های آن انجام می‌دهیم؛
یعنی $d(n)$ را برای همهٔ $n \in \Nat$ مشخص می‌کنیم. به‌طور شهودی، قطر
آرایهٔ بالا را رو به پایین می‌خوانیم (ازاین‌رو نام «روش قطری») و سپس هر
$1$ را به $0$ و هر $0$ را به~$1$ تغییر می‌دهیم.
\emph{یادداشت ویراستاری:} جهتِ دومِ تبدیل در جملهٔ متن مبدأ به‌اشتباه
تکرار شده بود؛ عبارت با تعریفِ زیر هماهنگ شده است. به‌بیان انتزاعی‌تر،
$d(n)$ را برابر $0$ یا $1$ تعریف می‌کنیم، بسته به اینکه عضو
$n$اُمِ قطر، یعنی $s_n(n)$، برابر $1$ یا $0$ باشد؛ یعنی:
\[
d(n) =
\begin{cases}
1 & \text{اگر $s_{n}(n) = 0$}\\
0 & \text{اگر $s_{n}(n) = 1$}
\end{cases}
\]
```

Every1 becomes0 and every0 becomes1. Source duplicated1-to0; repair precisely the second input/output pair. Piecewise definition and every diagonal coordinate remain unchanged.

Alternatives: No material alternative recorded; none invented.

## FA-0039-C10: Each listed string differs

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115.

Source:
```latex
Clearly $d \in \Bin^\omega$, since it is an infinite string of $0$'s
and $1$'s. But we have constructed $d$ so that $d(n) \neq s_n(n)$ for
any $n \in \Nat$. That is, $d$ differs from $s_n$ in its $n$th entry.
So $d \neq s_n$ for any $n\in \Nat$. So $d$ cannot be on the list
$s_0$, $s_1$, $s_2$,
\dots
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
آشکارا $d \in \Bin^\omega$ است، زیرا رشته‌ای نامتناهی از $0$ها و $1$هاست.
اما $d$ را چنان ساخته‌ایم که $d(n) \neq s_n(n)$ برای هر $n \in \Nat$.
یعنی $d$ با $s_n$ در درایهٔ $n$اُم تفاوت دارد. پس $d \neq s_n$
برای هر $n\in \Nat$. بنابراین $d$ نمی‌تواند در فهرست
$s_0$، $s_1$، $s_2$،
\dots باشد.
```

d differs from s_n at n for every n. Retain all universal quantifiers, function values and negations.

Alternatives: No material alternative recorded; none invented.

## FA-0039-C11: Why all relevant enumerations are excluded

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
We have shown, given an arbitrary enumeration of some subset of
$\Bin^\omega$, that it will omit some !!{element} of $\Bin^\omega$. So
there is no enumeration of the set $\Bin^\omega$, i.e., $\Bin^\omega$
is !!{nonenumerable}.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
نشان داده‌ایم که هر فهرستِ نامتناهیِ دلخواه از اعضای $\Bin^\omega$،
یک عضو از $\Bin^\omega$ را از قلم می‌اندازد. پس هیچ برشماری‌ای
از مجموعهٔ $\Bin^\omega$ وجود ندارد؛ یعنی $\Bin^\omega$
ناشمارا است.
\emph{توضیح:} خودِ مجموعهٔ رشته‌های دودوییِ نامتناهی، نامتناهی است؛ پس
برشماریِ فرضیِ کل آن نمی‌تواند دامنه‌ای متناهی داشته باشد. به همین دلیل
بررسیِ فهرست‌های نامتناهی در این برهان کافی است.
\end{proof}
```

An infinite binary-string set cannot have a finite enumeration. State why the infinite-list argument excludes every candidate full enumeration, not just some subset listing.

Alternatives: No material alternative recorded; none invented.

## FA-0039-C12: Diagonalization without an array

Action: retain_after_fresh_review; confidence 2/3: Editorial0–3, not a calibrated probability. Meaning checked; the stated lexical, historical or editorial limit remains.
Canon: FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{explain}
This proof method is called ``diagonalization'' because it uses the
diagonal of the array to define~$d$. However, diagonalization need
not involve the presence of an array. Indeed, we can show that some set is 
!!{nonenumerable} by using a similar idea, even when no array and no
actual diagonal is involved. The following result illustrates how.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
این روش اثبات را «قطری‌سازی» می‌نامند، زیرا برای تعریف~$d$ از قطر آرایه
استفاده می‌کند. بااین‌حال، قطری‌سازی لزوماً مستلزم وجود آرایه نیست. در
واقع، می‌توانیم با اندیشه‌ای مشابه نشان دهیم که مجموعه‌ای
ناشمارا است، حتی هنگامی که هیچ آرایه و هیچ قطر واقعی‌ای در
میان نیست. نتیجهٔ زیر چگونگی این کار را نشان می‌دهد.
\end{explain}
```

Retain conceptual generality; an actual drawn diagonal is unnecessary. Mathematical construction attested; exact lexical label remains provisional.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Same diagonalization lexical limitation as the strategy paragraph; do not mistake repeated use for an independent attestation.

## FA-0039-C13: Powerset theorem

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{thm}
\ollabel{thm:nonenum-pownat}
$\Pow{\Nat}$ is not !!{enumerable}.
\end{thm}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{thm}
\ollabel{thm:nonenum-pownat}
$\Pow{\Nat}$ شمارا نیست.
\end{thm}
```

Pow Nat is not enumerable; preserve exact theorem label used in later reduction.

Alternatives: No material alternative recorded; none invented.

## FA-0039-C14: Set-membership diagonal proof

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{proof}
We proceed in the same way, by showing that every list of subsets
of~$\Nat$ omits some subset of $\Nat$. So, suppose that we have some
list $N_0, N_1, N_2, \ldots$ of subsets of $\Nat$. We define a set $D$
as follows: $n \in D$ iff $n \notin N_{n}$:
\[
D = \Setabs{n \in \Nat}{n \notin N_n}
\]
Clearly $D\subseteq \Nat$. But $D$ cannot be on the list. After all,
by construction $n \in D$ iff $n\notin N_n$, so that $D \neq N_n$ for
any $n \in \Nat$. 
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
به همان شیوه پیش می‌رویم و نشان می‌دهیم که هر فهرستی از زیرمجموعه‌های
~$\Nat$، زیرمجموعه‌ای از $\Nat$ را از قلم می‌اندازد. پس فرض کنید فهرستی
مانند $N_0, N_1, N_2, \ldots$ از زیرمجموعه‌های $\Nat$ داریم. مجموعهٔ
$D$ را چنین تعریف می‌کنیم: $n \in D$ اگر و تنها اگر $n \notin N_{n}$:
\[
D = \Setabs{n \in \Nat}{n \notin N_n}
\]
آشکارا $D\subseteq \Nat$ است. اما $D$ نمی‌تواند در فهرست باشد. زیرا بنا بر
ساخت، $n \in D$ اگر و تنها اگر $n\notin N_n$؛ ازاین‌رو $D \neq N_n$
برای هر $n \in \Nat$.
\end{proof}
```

D contains n iff N_n does not; D is a subset of Nat and differs from each listed set at its own index. Zero-based list maintained.

Alternatives: No material alternative recorded; none invented.

## FA-0039-C15: Set array and first four diagonal choices

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P044.

Source:
```latex
\begin{explain}
The preceding proof did not mention a diagonal. Still, you can think
of it as involving a diagonal if you picture it this way: Imagine the
sets $N_0$, $N_1$, \dots, written in an array, where we write $N_n$ on
the $n$th row by writing $m$ in the $m$th column iff if $m \in N_n$.
For example, say the first four sets on that list are
$\{0,1,2,\dots\}$, $\{1, 3, 5, \dots\}$, $\{0,1,4\}$, and
$\{2,3,4,\dots\}$; then our array would begin with
\[
\begin{array}{r@{}rrrrrrr}
  N_0 = \{ & \mathbf{0}, & 1, & 2, & & & & \dots\}\\
  N_1 = \{ &  & \mathbf{1}, &  & 3, &  & 5, & \dots\}\\
  N_2 = \{ & 0, & 1, &  &  & 4\phantom{,} &  & \}\\
  N_3 = \{ &  &  & 2, & \mathbf{3}, & 4, & & \dots\}\\
  &\vdots & & & & & & \ddots\phantom{\}}
  \end{array}
\]
Then $D$ is the set obtained by going down the diagonal, placing $n
\in D$ iff $n$ is \emph{not} on the diagonal. So in the above case, we
would leave out $0$ and $1$, we would include~$2$, we would leave
out~$3$, etc.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
برهان پیشین از قطر نام نبرد. بااین‌حال، اگر آن را چنین تصویر کنید،
می‌توانید آن را مشتمل بر یک قطر بدانید: فرض کنید مجموعه‌های $N_0$،
$N_1$، \dots، در آرایه‌ای نوشته شده‌اند که در آن $N_n$ را در سطر $n$اُم
با نوشتن $m$ در ستون $m$اُم، اگر و تنها اگر $m \in N_n$، نمایش می‌دهیم.
برای نمونه، فرض کنید چهار مجموعهٔ نخستِ آن فهرست
$\{0,1,2,\dots\}$، $\{1, 3, 5, \dots\}$، $\{0,1,4\}$ و
$\{2,3,4,\dots\}$ باشند؛ آنگاه آرایهٔ ما چنین آغاز می‌شود.
\emph{یادداشت ویراستاری:} در آرایهٔ متن مبدأ، سه عضوِ سطر نخست و یک
عضوِ سطر چهارم از قلم افتاده بود. در اینجا همهٔ خانه‌ها مطابق عضویت در
مجموعه‌های داده‌شده تکمیل شده‌اند:
\[
\begin{array}{r@{}rrrrrrr}
  N_0 = \{ & \mathbf{0}, & 1, & 2, & 3, & 4, & 5, & \dots\}\\
  N_1 = \{ &  & \mathbf{1}, &  & 3, &  & 5, & \dots\}\\
  N_2 = \{ & 0, & 1, &  &  & 4\phantom{,} &  & \}\\
  N_3 = \{ &  &  & 2, & \mathbf{3}, & 4, & 5, & \dots\}\\
  &\vdots & & & & & & \ddots\phantom{\}}
  \end{array}
\]
آنگاه $D$ مجموعه‌ای است که با پایین‌رفتن روی قطر به دست می‌آید و $n
\in D$ را دقیقاً هنگامی برقرار می‌گیریم که $n$ روی قطر \emph{نباشد}.
پس در حالت بالا، $0$ و $1$ را کنار می‌گذاریم، $2$ را در مجموعه قرار
می‌دهیم، $3$ را کنار می‌گذاریم و الی آخر.
\end{explain}
```

Row N_n and column m refer to membership of m. Insert the omitted3,4,5 in row0 and5 in row3, forced by the displayed sets; disclose these four source omissions. Every explicit membership cell is checked against its stated set. Diagonal decisions remain exclude0,exclude1,include2,exclude3. Preserve the examples and all other matrix tokens.

Alternatives: No material alternative recorded; none invented.

## FA-0039-C16: Functions diagonal exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-OL-CANON-0001:P0082.

Source:
```latex
\begin{prob}
Show that the set of all functions $f \colon \Nat \to \Nat$ is
!!{nonenumerable} by an explicit diagonal argument. That is, show that
if $f_1$, $f_2$, \dots, is a list of functions and each $f_i\colon
\Nat \to \Nat$, then there is some $g \colon \Nat \to
\Nat$ not on this list.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
با یک استدلال قطریِ صریح نشان دهید که مجموعهٔ همهٔ توابع
$f \colon \Nat \to \Nat$ ناشمارا است. یعنی نشان دهید که اگر
$f_1$، $f_2$، \dots، فهرستی از توابع باشد و هر $f_i\colon
\Nat \to \Nat$ باشد، آنگاه تابعی مانند $g \colon \Nat \to
\Nat$ وجود دارد که در این فهرست نیست.
\end{prob}
```

Retain all Nat→Nat functions, not algorithms. One-based list names f1,f2 do not change the zero-based function domain; diagonalization uses positive indices and a separately assigned zero value. No solution inserted.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C01: Reduction heading

Action: retain_after_fresh_review; confidence 2/3: Editorial0–3, not a calibrated probability. Meaning checked; the stated lexical, historical or editorial limit remains.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0005:P0115.

Source:
```latex
\olsection{Reduction}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{کاهش}
```

Retain کاهش as the existing provisional term, governed by the explicitly described direction of enumeration conversion; it does not mean lowering rigor or changing the theorem.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Exact کاهش attestation was not established in the selected scholarly pages. A bounded primary-site search produced no usable mathematical witness; none is cited. The construction and direction, not model memory, justify the provisional contextual choice.

## FA-0040-C02: Alternative route editorial

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{editorial}
  This section proves non-enumerability by reduction, matching the
  results in \olref[nen-alt]{sec}. An alternative, slightly more
  elaborate version matching the results in \olref[nen]{sec} is
  provided in \olref[red]{sec}.
\end{editorial}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{editorial}
  این بخش ناشمارابودن را از راه کاهش ثابت می‌کند و با نتایجِ
  \olref[nen-alt]{sec} مطابقت دارد. روایتی جایگزین و اندکی مشروح‌تر که
  با نتایجِ \olref[nen]{sec} مطابقت دارد، در \olref[red]{sec} آمده است.
\end{editorial}
```

Keep both alternative-section references and their relative detail.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C03: Contrapositive setup

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P046.

Source:
```latex
We proved that $\Bin^\omega$ is !!{nonenumerable} by a diagonalization
argument. We used a similar diagonalization argument to show that
$\Pow{\Nat}$ is !!{nonenumerable}. But here's another way we can prove
that $\Pow{\Nat}$ is !!{nonenumerable}: show that \emph{if
$\Pow{\Nat}$ is !!{enumerable} then $\Bin^\omega$ is also
!!{enumerable}}.  Since we know $\Bin^\omega$ is !!{nonenumerable}, it
will follow that $\Pow{\Nat}$ is too.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
با استدلالی قطری ثابت کردیم که $\Bin^\omega$ ناشمارا است.
با استدلال قطریِ مشابهی نشان دادیم که $\Pow{\Nat}$ ناشمارا
است. اما راه دیگری نیز برای اثبات اینکه $\Pow{\Nat}$
ناشمارا است وجود دارد: نشان دهید که \emph{اگر
$\Pow{\Nat}$ شمارا باشد، آنگاه $\Bin^\omega$ نیز
شمارا است}. چون می‌دانیم $\Bin^\omega$ ناشمارا است،
نتیجه می‌شود که $\Pow{\Nat}$ نیز چنین است.
```

If Pow Nat enumerable then Bin omega enumerable; known nonenumerability of the latter yields nonenumerability of the former. No reversal.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C04: Problem versus function direction

Action: retain_after_fresh_review; confidence 2/3: Editorial0–3, not a calibrated probability. Meaning checked; the stated lexical, historical or editorial limit remains.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0005:P0115.

Source:
```latex
This is called \emph{reducing} one problem to another. In this case,
we reduce the problem of enumerating $\Bin^\omega$ to the problem of
enumerating $\Pow{\Nat}$.  A solution to the latter---an enumeration
of $\Pow{\Nat}$---would yield a solution to the former---an
enumeration of $\Bin^\omega$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
این کار را \emph{کاهش‌دادن} یک مسئله به مسئله‌ای دیگر می‌نامند. در این
مورد، مسئلهٔ برشمردن $\Bin^\omega$ را به مسئلهٔ برشمردن
$\Pow{\Nat}$ کاهش می‌دهیم. راه‌حلی برای مسئلهٔ دوم---یعنی برشماریِ
$\Pow{\Nat}$---راه‌حلی برای مسئلهٔ نخست---یعنی برشماریِ
$\Bin^\omega$---به دست می‌دهد.
```

Problem B reduces to problem A because a solution/enumeration of A gives one of B. The mapping runs A→B. Keep both directions explicit; the label itself has the stated lexical limit.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C05: Surjective image list is not necessarily bijective

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0003:P0053.

Source:
```latex
To reduce the problem of enumerating a set~$B$ to that of enumerating
a set~$A$, we provide a way of turning an enumeration of~$A$ into an
enumeration of~$B$.  The easiest way to do that is to define
!!a{surjection} $f\colon A \to B$.  If $x_1$, $x_2$, \dots{}
enumerates~$A$, then $f(x_1)$, $f(x_2)$, \dots{} would enumerate~$B$.
In our case, we are looking for !!a{surjection} $f\colon \Pow{\Nat}
\to \Bin^\omega$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
برای کاهش مسئلهٔ برشمردن مجموعهٔ~$B$ به مسئلهٔ برشمردن مجموعهٔ~$A$،
روشی ارائه می‌کنیم که برشماریِ~$A$ را به برشماریِ~$B$ تبدیل کند.
آسان‌ترین راه برای این کار تعریف یک نگاشت پوشا مانند
$f\colon A \to B$ است. اگر $x_1$، $x_2$، \dots{} مجموعهٔ~$A$ را
برشمارد، آنگاه $f(x_1)$، $f(x_2)$، \dots{} هر عضوِ مجموعهٔ~$B$ را
دست‌کم یک بار در بر خواهد داشت.
\emph{یادداشت دربارهٔ تعریف:} این فهرست ممکن است تکرار داشته باشد و
بنابراین هنوز لزوماً برشماری به معنای تناظر دوسویی نیست. با نگه‌داشتن
نخستین رخدادِ هر مقدار و شماره‌گذاریِ دوباره، برشماریِ دوسوییِ لازم به
دست می‌آید؛ حالتِ تهی جداگانه طبق تعریف پوشش داده می‌شود.
در مورد ما، در پی یک نگاشت پوشا مانند $f\colon \Pow{\Nat}
\to \Bin^\omega$ هستیم.
```

A surjection maps an enumeration to an exhaustive list, which can repeat. Retain the list formulas, then explicitly keep first occurrences and reindex to obtain the required bijective enumeration. Empty B is separately enumerable. This is a definition repair, not a computable de-duplication claim.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C06: Injective transfer exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0003:P0051.

Source:
```latex
\begin{prob}
Show that if there is an !!{injective} function $g\colon B \to A$, and
$B$~is !!{nonenumerable}, then so is~$A$. Do this by showing how you
can use~$g$ to turn an enumeration of~$A$ into one of~$B$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
نشان دهید اگر یک تابعِ یک‌به‌یک مانند $g\colon B \to A$ وجود داشته
باشد و $B$~ناشمارا باشد، آنگاه $A$ نیز چنین است. برای این کار
نشان دهید چگونه می‌توان با استفاده از~$g$، برشماریِ~$A$ را به برشماریِ~$B$
تبدیل کرد.
\end{prob}
```

Preserve g:B→A and nonenumerability of B. Inverse only on g[B] plus first-appearance indices derives an enumeration; no inverse on all A and no Choice family.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C07: Hypothetical powerset enumeration

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{proof}[Proof of {\olref[nen-alt]{thm:nonenum-pownat}} by reduction]
For a reduction, suppose that $\Pow{\Nat}$ is !!{enumerable}, and thus that
there is an enumeration of it, $N_{1}$, $N_{2}$, $N_{3}$, \dots
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}[برهانِ {\olref[nen-alt]{thm:nonenum-pownat}} از راه کاهش]
برای انجام کاهش، فرض کنید $\Pow{\Nat}$ شمارا است و بنابراین
برشماری‌ای از آن به‌صورت $N_{1}$، $N_{2}$، $N_{3}$، \dots وجود دارد.
```

Retain the theorem reference and the one-based list labels N1,N2,N3. These labels are not the zero-based coordinates inside each binary string.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C08: Characteristic string without an unbound index

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P044.

Source:
```latex
Define the function $f \colon \Pow{\Nat} \to \Bin^\omega$ by letting
$f(N)$ be the string $s_{k}$ such that $s_{k}(n) = 1$ iff $n \in N$,
and $s_k(n) = 0$ otherwise.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
تابع $f \colon \Pow{\Nat} \to \Bin^\omega$ را با این قرارداد تعریف
کنید که $f(N)$ رشتهٔ $s$ باشد، به‌گونه‌ای که $s(n) = 1$ اگر و تنها
اگر $n \in N$، و در غیر این صورت $s(n) = 0$.
\emph{یادداشت ویراستاری:} زیرنویسِ تعریف‌نشدهٔ متن مبدأ حذف شده است؛
نماد رشته در این تعریف به همان مجموعهٔ ورودی وابسته است.
```

Remove the three unbound k subscripts. For each input N, f(N) is its characteristic string s, with bits fixed by membership. This is known source-notation repair; no quotient or extra parameter.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C09: Even, empty and whole-set examples

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P044.

Source:
```latex
This clearly defines a function, since whenever $N \subseteq \Nat$,
any $n \in \Nat$ either is !!a{element} of $N$ or isn't.  For
instance, the set $2\Nat = \Setabs{2n}{n \in \Nat} = \{0,2, 4, 6,
\dots\}$ of even naturals gets mapped to the string $1010101\dots$;
$\emptyset$ gets mapped to $0000\dots$; $\Nat$ gets mapped to
$1111\dots$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
این امر به‌روشنی تابعی را تعریف می‌کند، زیرا هرگاه $N \subseteq \Nat$،
هر $n \in \Nat$ یا یک عضو از $N$ است یا نیست. برای نمونه،
مجموعهٔ $2\Nat = \Setabs{2n}{n \in \Nat} = \{0,2, 4, 6,
\dots\}$ از اعداد طبیعی زوج به رشتهٔ $1010101\dots$ نگاشته می‌شود؛
$\emptyset$ به $0000\dots$ نگاشته می‌شود و $\Nat$ به
$1111\dots$.
```

Check zero-based parity1010..., empty000..., full111.... All are infinite strings; no finite approximation is substituted.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C10: Surjectivity by support

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P046.

Source:
```latex
It is also !!{surjective}: every string of $0$s and $1$s corresponds
to some set of natural numbers, namely the one which has as its
members those natural numbers corresponding to the places where the string
contains a~$1$s. More precisely, if $s \in \Bin^\omega$, then define $N
\subseteq \Nat$ by:
\[
N = \Setabs{n \in \Nat}{s(n) = 1}
\]
Then $f(N) = s$, as can be verified by consulting the definition
of~$f$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
این نگاشت همچنین پوشا است: هر رشته از $0$ها و $1$ها با
مجموعه‌ای از اعداد طبیعی متناظر است؛ یعنی مجموعه‌ای که اعضایش آن اعداد
طبیعی‌اند که با جایگاه‌هایی متناظرند که رشته در آن‌ها $1$ دارد. دقیق‌تر
بگوییم، اگر $s \in \Bin^\omega$، آنگاه $N
\subseteq \Nat$ را چنین تعریف کنید:
\[
N = \Setabs{n \in \Nat}{s(n) = 1}
\]
آنگاه $f(N) = s$؛ این را می‌توان با مراجعه به تعریفِ~$f$ بررسی کرد.
```

For arbitrary binary string s take its support N={n:s(n)=1}; then f(N)=s. Preserve iff and all-coordinate equality.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C11: Specific characteristic map gives no repetitions

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P046, FA-REL-P050.

Source:
```latex
Now consider the list
\[
f(N_1), f(N_2), f(N_3), \dots
\]
Since $f$ is !!{surjective}, every member of $\Bin^\omega$ must
appear as a value of~$f$ for some argument, and so must appear on the
list. This list must therefore enumerate all of~$\Bin^\omega$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
اکنون فهرست زیر را در نظر بگیرید:
\[
f(N_1), f(N_2), f(N_3), \dots
\]
چون $f$ پوشا است، هر عضوِ $\Bin^\omega$ باید برای ورودی‌ای
به‌عنوان مقدارِ~$f$ ظاهر شود و بنابراین باید در فهرست بیاید. پس این
فهرست باید همهٔ~$\Bin^\omega$ را برشمارد.
این نگاشت یک‌به‌یک نیز هست، زیرا رشتهٔ حاصل، عضویتِ هر عدد طبیعی در
مجموعهٔ ورودی را تعیین می‌کند. پس در این مثال، فهرستِ حاصل از یک
برشماریِ دوسویی، خود نیز بدون تکرار است.
```

Surjectivity covers every binary string. Explicitly explain injectivity of this particular characteristic map; thus an assumed bijective input enumeration yields a bijective output enumeration without repetition.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C12: Contradiction conclusion

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-OL-CANON-0003:P0053.

Source:
```latex
So if $\Pow{\Nat}$ were !!{enumerable}, $\Bin^\omega$ would be
!!{enumerable}.  But $\Bin^\omega$ is !!{nonenumerable}
(\olref[nen-alt]{thm:nonenum-bin-omega}). Hence $\Pow{\Nat}$ is
!!{nonenumerable}.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
بنابراین اگر $\Pow{\Nat}$ شمارا بود، $\Bin^\omega$ نیز
شمارا می‌بود. اما $\Bin^\omega$ ناشمارا است
(\olref[nen-alt]{thm:nonenum-bin-omega}). پس $\Pow{\Nat}$
ناشمارا است.
\end{proof}
```

Retain the implication, known nonenumerability reference and conclusion.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C13: Disabled direction warning and examples

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0005:P0115.

Source:
```latex
%\begin{explain}
%It is easy to be confused about the direction the reduction goes in.
%For instance, !!a{surjective} function $g \colon \Bin^\omega \to X$
%does \emph{not} establish that $X$ is !!{nonenumerable}.  (Consider $g
%\colon \Bin^\omega \to \Bin$ defined by $g(s) = s(1)$, the function
%that maps a sequence of $0$'s and $1$'s to its first !!{element}.  It
%is surjective, because some sequences start with $0$ and some start
%with $1$. But $\Bin$ is finite.)  Note also that the function $f$ must
%be surjective, or otherwise the argument does not go through:
%$f(x_1)$, $f(x_2)$, \dots{} would then not be guaranteed to include
%all the !!{element}s of~$Y$. For instance, $h\colon \Nat \to
%\Bin^\omega$ defined by
%\[
%h(n) = \underbrace{000\dots0}_{\text{$n$ $0$'s}}
%\]
%is a function, but $\Nat$ is !!{enumerable}.
%\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
%\begin{explain}
%ممکن است جهتِ کاهش اشتباه گرفته شود.
%برای نمونه، وجود تابعی پوشا مانند $g \colon \Bin^\omega \to X$
%ناشمارابودنِ $X$ را \emph{ثابت نمی‌کند}. تابعِ $g
%\colon \Bin^\omega \to \Bin$ با ضابطهٔ $g(s) = s(1)$ را در نظر بگیرید؛ این تابع
%هر دنباله از $0$ها و $1$ها را به عضوِ با اندیس یک می‌فرستد.
%این تابع پوشاست، زیرا بعضی دنباله‌ها در این جایگاه $0$ و بعضی
%دیگر $1$ دارند. اما $\Bin$ متناهی است. همچنین تابعِ $f$ باید
%پوشا باشد؛ در غیر این صورت استدلال برقرار نیست:
%$f(x_1)$، $f(x_2)$، \dots{} لزوماً همهٔ
%اعضای~$B$ را در بر نمی‌گیرند. برای نمونه، $h\colon \Nat \to
%\Bin^\omega$ را با ضابطهٔ زیر تعریف کنید:
%\[
%h(n) = \underbrace{000\dots0}_{\text{$n$ بار $0$}}0\ldots
%\]
%این یک تابع است، اما $\Nat$ شمارا است.
%یادداشت ویراستاری: متنِ غیرفعالِ مبدأ «نخستین» را برای اندیس یک به کار
%برده بود؛ اینجا اندیس صریح بیان شده است. نامِ مجموعهٔ مقصد با زمینه
%هماهنگ و دنبالهٔ خروجی واقعاً نامتناهی شده است. این توضیح همچنان غیرفعال است.
%\end{explain}
```

Translate the entire previously English commented explanation without activating it. Keep the wrong-direction counterexample onto a finite binary set; name its chosen index1 rather than falsely first under zero-based indexing. Repair unbound target Y to B and finite n-zero output to an actual infinite zero string; disclose all three issues. English mathematical-text plural is translated with n and0 unchanged.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C14: Functions reduction exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-REL-P046, FA-OL-CANON-0005:P0115, FA-OL-CANON-0001:P0082.

Source:
```latex
\begin{prob}\label{sfr:siz:red:prob:nat-nat}
  Show that the set~$X$ of all functions $f\colon \Nat \to \Nat$ is
  !!{nonenumerable} by a reduction argument (Hint: give a surjective
  function from $X$ to~$\Bin^\omega$.)
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}\label{sfr:siz:red-alt:prob:nat-nat}
  با استدلالی کاهشی نشان دهید مجموعهٔ~$X$ از همهٔ توابع
  $f\colon \Nat \to \Nat$ ناشمارا است. (راهنمایی: یک نگاشت
  پوشا از $X$ به~$\Bin^\omega$ بدهید.)
\end{prob}
```

All functions X=Nat→Nat; a surjection X→Bin omega gives the needed reduction. Preserve the existing red-alt label disambiguation, since the frozen source duplicates the red label in two files. No new renaming is made.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C15: Sets of pairs exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-REL-P044, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{prob}
Show that the set of all \emph{sets of} pairs of natural numbers,
i.e., $\Pow{\Nat \times \Nat}$, is !!{nonenumerable} by a reduction
argument.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
با استدلالی کاهشی نشان دهید که مجموعهٔ همهٔ \emph{مجموعه‌های} زوج‌های
اعداد طبیعی، یعنی $\Pow{\Nat \times \Nat}$، ناشمارا است.
\end{prob}
```

Pow(Nat×Nat), not just Nat×Nat; keep the emphasis on sets of pairs and the reduction request.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C16: Natural-sequence exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-OL-CANON-0001:P0082.

Source:
```latex
\begin{prob}
Show that $\Nat^\omega$, the set of infinite sequences of natural
numbers, is !!{nonenumerable} by a reduction argument.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
با استدلالی کاهشی نشان دهید که $\Nat^\omega$، یعنی مجموعهٔ دنباله‌های
نامتناهیِ اعداد طبیعی، ناشمارا است.
\end{prob}
```

Infinite sequences of naturals, equivalent to all functions Nat→Nat; no computability restriction.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C17: Disabled partial-function exercise

Action: correct; confidence 2/3: Editorial0–3, not a calibrated probability. Meaning checked; the stated lexical, historical or editorial limit remains.
Canon: FA-REL-P044, FA-REL-P050, FA-OL-CANON-0001:P0082.

Source:
```latex
%\begin{prob}
%Let $P$ be the set of functions from $\Nat$ to the set $\{0\}$, and let $Q$ be the set of \emph{partial}
%functions from the set of positive integers to the set $\{0\}$. Show
%that $P$~is !!{enumerable} and $Q$~is not. (Hint: reduce the problem
%of enumerating $\Bin^\omega$ to enumerating~$Q$).
%\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
%\begin{prob}
%فرض کنید $P$ مجموعهٔ توابع از $\Nat$ به مجموعهٔ $\{0\}$ باشد و $Q$ مجموعهٔ توابعِ \emph{جزئی}
%از اعداد صحیح مثبت به مجموعهٔ $\{0\}$ باشد؛ یعنی این توابع ممکن است برای بعضی
%ورودی‌ها تعریف نشده باشند. نشان دهید $P$~شمارا است و $Q$ چنین نیست.
%(راهنمایی: مسئلهٔ برشمردن $\Bin^\omega$ را به برشمردنِ~$Q$ کاهش دهید.)
%\end{prob}
```

Translate the whole dormant problem and preserve its inactive state. Partial means some inputs may be undefined, not an algorithm failing to halt. Total singleton-valued functions form a singleton; partial functions correspond to subsets of their input domain. Exact تابع جزئی label is supplemented by its definition.

Alternatives: No material alternative recorded; none invented.

Expert-review question: The explicit definition fixes partial-function meaning; exact جزئی is not attested on these selected pages. Preserve the distinction from partial computability.

## FA-0040-C18: All binary surjections exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-REL-P046, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{prob}
Let $S$ be the set of all !!{surjection}s from $\Nat$ to the set
$\{0,1\}$, i.e., $S$ consists of all !!{surjection}s~$f \colon \Nat
\to \Bin$.  Show that $S$ is !!{nonenumerable}.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
فرض کنید $S$ مجموعهٔ همهٔ نگاشت‌های پوشا از $\Nat$ به مجموعهٔ
$\{0,1\}$ باشد؛ یعنی $S$ از همهٔ نگاشت‌های پوشا~$f \colon \Nat
\to \Bin$ تشکیل می‌شود. نشان دهید $S$ ناشمارا است.
\end{prob}
```

All surjections Nat→{0,1}, not every binary-valued function. Surjectivity requires both values somewhere; padding a binary string with both values provides the relevant injection. No solution inserted.

Alternatives: No material alternative recorded; none invented.

## FA-0040-C19: Real-number exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source meaning, relevant scholarly usage and local context checked.
Canon: FA-OL-CANON-0005:P0115, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{prob}
Show that the set~$\Real$ of all real numbers is !!{nonenumerable}.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
نشان دهید مجموعهٔ~$\Real$ از همهٔ اعداد حقیقی ناشمارا است.
\end{prob}
```

Retain nonenumerability of all reals. Do not justify it by an unchecked one-to-one binary-expansion claim: endpoint ambiguities must be handled, e.g. using ternary0/2 embedding in the review reasoning.

Alternatives: No material alternative recorded; none invented.

## Validation boundary

Every substantive source and target character lies in an ordered non-overlapping reviewed span. Formal tokens are checked across inline, bracketed, multline and align mathematics. Text arguments in mathematics are separately aligned and manually reviewed for exact connective, quantifier and number-family meaning.
Finite tests support the written reasoning; they are not universal formal proofs. No new PDF was built or visually certified. Frozen owner inputs and reader releases are unchanged; corrections enter the owner’s normal next-batch build and visual QA.
Attribution: Open Logic Project and contributors, under existing CC BY 4.0 notices. https://github.com/OpenLogicProject/OpenLogic . Existing edition: https://github.com/KokunoYumeto/OpenLogic-fa-ir . Canon sources retain separate rights.
