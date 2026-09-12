# Persian OpenLogic: pairing functions and numerical codes

Complete retrospective source/canon review of OLP-0031 and0032. Six complete scholarly pages were consulted; every substantive source/target span is mapped below. Corrected candidates are source-production inputs, not a rebuilt reader or full-corpus certification. All review in this packet is by the main agent; no independent or human certification is claimed.

## Review priorities

- Preserve injection, surjection, inverse-on-image and enumeration as different notions.
- Repair the triangular-sum inequality and two explicitly identified coordinate typos; preserve the pairing formulas and numeric tables.
- Disclose the positive-column boundary, corrected inverse exercise, and choice convention for the countable-union exercise.
- Keep ordinary countability distinct from computability and valuations distinct from finite-arity truth functions.
- Exact pairing/cofinite/partial-function labels have explicit attestation limits; no invented dictionary evidence.
- Confidence is editorial 0-3, not calibrated probability. Human review is a later opportunity, not a gate.

## Scholarly pages actually consulted

- منطق ریاضی; محسن خانی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/chapter2_0.pdf). PDF SHA-256: 0f3fb75ed1fcb0cbc669c04493acf520888e1ebfd62795bb28fc510bc41c7e79. Canon PDFs are privately retained, not redistributed.
- مبانی منطق و نظریهٔ مجموعه‌ها; محسن خانی; دانشگاه صنعتی اصفهان. [Source](https://mohsen-khani.github.io/logic97-1/jozve/logic-full.pdf). PDF SHA-256: 565558b76701858236844f19663de27ee10a8d72fd8b007e69b85159ac49f86d. Canon PDFs are privately retained, not redistributed.
- نظریهٔ مجموعه‌ها; محسن خانی, افشین زارعی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/jozve-kamel.pdf). PDF SHA-256: dbd518c80232921264ab5d79b79be01fe42efe8c01a766327db248b2d261de04. Canon PDFs are privately retained, not redistributed.
- ریاضیات گسسته و کاربردها; علیرضا غفاری حدیقه, مگردیچ تومانیان; مؤسسه چاپ و انتشارات دانشگاه جامع امام حسین (ع). [Source](https://hadigheha.github.io/books/teaching/Textbooks/Tarkibiyat.pdf). PDF SHA-256: 8f79c45a926c1cea819c4fefa86383f2a65ae23b1d526baaf99cf2506bb9f317. Canon PDFs are privately retained, not redistributed.
- FA-OL-CANON-0001:P0093, PDF 93, printed 92: Numerical coding of formulas/proofs; recursive enumerability distinction. Direct coding register and explicit computability qualification. The symbol table uses pair-shaped codes; it does not attest the exact term جفت‌سازی or imply every injection is computable.
- FA-OL-CANON-0005:P0013, PDF 13, printed 13: Truth tables and lemma23 for arbitrary Boolean n-ary functions. Direct distinction between F on Boolean tuples and a valuation mu of propositions; lemma23 realizes every such F by a formula. تابع ارزشِ صدق is an explicitly contextual label, not a verbatim quotation of that lemma.
- FA-OL-CANON-0003:P0051, PDF 51, printed 50: Cardinal comparison; inverse on image; choice selection. Inverse-on-image and fixed-default construction; general reverse selection explicitly invokes Choice. Do not import visible proof notation slips or require Choice for least preimages in natural indices.
- FA-OL-CANON-0003:P0053, PDF 53, printed 52: Definition10 and ordinal enumerations. This canon reserves شمارا for cardinality omega, whereas OpenLogic includes finite and empty sets. Preserve the convention already disclosed in the reviewed0029; ordinal enumeration is not automatically a finite-position or computable list.
- FA-REL-P046, PDF 46, printed 36: Injection/surjection definitions and diagrams. At most one preimage is not at least one. Code uniqueness requires injection, not all numbers being used.
- FA-REL-P050, PDF 50, printed 40: Inverse of a bijection and function composition. Direct معکوس terminology and the inverse domain/codomain distinction. Restricting an injection to its image supplies a bijection. The exact label تابع جزئی is not attested on this selected page.

## FA-0031-C01: Pairing and codes heading

Action: retain_after_fresh_review; confidence 2/3: Editorial0–3, not a calibrated probability. Source meaning checked; exact label or register convention has the stated attestation limit.
Canon: FA-OL-CANON-0001:P0093, FA-REL-P046.

Source:
```latex
\olsection{Pairing Functions and Codes}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{توابع جفت‌سازی و کدها}
```

جفت‌سازی labels the explicitly defined injective pair-to-number function; کد follows actual numerical coding on L93. No computational requirement is added.

Alternatives: No material alternative recorded; none invented.

Expert-review question: The exact label جفت‌سازی is not directly attested on these pages. It remains a source-defined contextual term, not a claimed quotation.

## FA-0031-C02: Computing the inverse position map

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-REL-P050, FA-OL-CANON-0001:P0093.

Source:
```latex
\begin{explain}
Cantor's zig-zag method makes the enumerability of $\Nat^n$ visually
evident. But let us focus on our array depicting $\Nat^2$. Following
the zig-zag line in the array and counting the places, we can check
that $\tuple{1,2}$ is associated with the number~$7$. However, it would
be nice if we could compute this more directly. That is, it would be
nice to have to hand the \emph{inverse} of the zig-zag enumeration,
$g\colon \Nat^2 \to \Nat$, such that
\[
g(\tuple{0,0}) = 0, \;
g(\tuple{0,1}) = 1, \;
g(\tuple{1,0}) = 2, \; \dots,  
g(\tuple{1,2}) = 7, \; \dots
\]
This would enable us to calculate exactly where $\tuple{n, m}$ will occur
in our enumeration.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
روش زیگزاگ کانتور شماراییِ $\Nat^n$ را به‌صورت دیداری آشکار می‌کند. اما
بیایید بر آرایه‌ای متمرکز شویم که $\Nat^2$ را نمایش می‌دهد. با دنبال‌کردن
خط زیگزاگ در آرایه و شمردن جایگاه‌ها، می‌توانیم بررسی کنیم که
$\tuple{1,2}$ با عدد~$7$ متناظر است. بااین‌حال، اگر بتوانیم
این مقدار را مستقیماً محاسبه کنیم، کار ساده‌تر می‌شود. به بیان دیگر، می‌خواهیم
\emph{معکوسِ} برشماری زیگزاگ، یعنی $g\colon \Nat^2 \to \Nat$، را به‌صورت صریح
داشته باشیم؛ به‌گونه‌ای که
\[
g(\tuple{0,0}) = 0, \;
g(\tuple{0,1}) = 1, \;
g(\tuple{1,0}) = 2, \; \dots,
g(\tuple{1,2}) = 7, \; \dots
\]
این تابع به ما امکان می‌دهد دقیقاً محاسبه کنیم که $\tuple{n, m}$ در کجای
برشماری ظاهر خواهد شد.
```

Use معکوس consistently with the actually read inverse page rather than alternating unexplained وارون/معکوس. Recast counterfactual wording as an explicit desired position calculation, retaining Nat^n, Nat^2, every listed pair/code and direction g:Nat²→Nat. The source already provides the construction later; no new necessity theorem is implied.

Alternatives: وارون is mathematically intelligible; معکوس matches D50 and the reviewed neighbouring sections. No claim that وارون is intrinsically incorrect.

## FA-0031-C03: Diagonal successor and triangular formula

Action: correct; confidence 2/3: Editorial0–3, not a calibrated probability. Source meaning checked; exact label or register convention has the stated attestation limit.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0003:P0053.

Source:
```latex
In fact, we can define $g$ directly by making two observations. First:
if the $n$th row and $m$th column contains value~$v$, then the
$(n+1)$st row and $(m-1)$st column contains value $v + 1$. Second: the
first row of our enumeration consists of the triangular numbers,
starting with $0$, $1$, $3$, $6$, etc. The $k$th triangular number is
the sum of the natural numbers $< k$, which can be computed as
$k(k+1)/2$. Putting these two observations together, consider this
function:
\[
  g(n,m) = \frac{(n+m+1)(n+m)}{2} + n
\]
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
در واقع، می‌توانیم با دو مشاهده $g$ را مستقیماً تعریف کنیم. نخست: اگر
خانهٔ واقع در سطر $n$اُم و ستون $m$اُم حاوی مقدار~$v$ باشد و شمارهٔ ستون مثبت باشد،
آنگاه خانهٔ واقع در سطر $(n+1)$اُم و ستون $(m-1)$اُم حاوی مقدار $v + 1$ است. دوم: سطر نخست
برشماری ما از اعداد مثلثی تشکیل می‌شود که با $0$، $1$، $3$، $6$ و
الی آخر آغاز می‌شوند. عدد مثلثیِ $k$اُم مجموع اعداد طبیعیِ $\leq k$ است
که می‌توان آن را به‌صورت $k(k+1)/2$ محاسبه کرد. \emph{یادداشت ویراستاری:} شرط مثبت‌بودن شمارهٔ ستون در مشاهدهٔ نخست،
و احتساب خودِ عدد در مجموع اعداد مثلثی، دو اصلاح در توضیح متن مبدأ هستند.
با کنار هم گذاشتن این
دو مشاهده، تابع زیر را در نظر بگیرید:
\[
  g(n,m) = \frac{(n+m+1)(n+m)}{2} + n
\]
```

Source successor step is valid only when m>0. Add that condition in prose and specify the cell at the stated row/column intersection, not a whole row holding one value. Correct sum of naturals<k to≤k so it equals k(k+1)/2, retaining the zero-based triangular convention and exact pairing formula. Both source corrections are visibly disclosed. Numeric triangular values unchanged.

Alternatives: No material alternative recorded; none invented.

Expert-review question: اعداد مثلثی is a source-defined contextual label here; these selected pages do not attest that exact phrase. The formula supplies exact meaning.

## FA-0031-C04: Notation abbreviation and computed example

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0001:P0093, FA-REL-P050.

Source:
```latex
We often just write $g(n, m)$ rather that $g(\tuple{n, m})$, since it
is easier on the eyes. This tells you first to determine the
$(n+m)^\text{th}$ triangle number, and then add $n$ to it. And
it populates the array in exactly the way we would like. So in
particular, the pair $\tuple{1, 2}$ is sent to $\frac{4 \times 3}{2} +
1 = 7$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
اغلب صرفاً $g(n, m)$ را به‌جای $g(\tuple{n, m})$ می‌نویسیم، زیرا خواندنش
آسان‌تر است. این فرمول می‌گوید نخست عدد مثلثیِ $(n+m)^\text{اُم}$ را
به دست آورید و سپس $n$ را به آن بیفزایید. این کار آرایه را دقیقاً به
شیوهٔ مطلوب ما پر می‌کند. پس به‌ویژه، زوج $\tuple{1, 2}$ به
$\frac{4 \times 3}{2} +
1 = 7$ فرستاده می‌شود.
```

Retain tuple versus two-argument abbreviation, ordinal text in math, and g(1,2)=7. No changed pairing direction or RTL coordinate reversal.

Alternatives: No material alternative recorded; none invented.

## FA-0031-C05: Specific inverse versus general pairing

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-REL-P046, FA-REL-P050.

Source:
```latex
This function $g$ is the \emph{inverse} of an enumeration of a set of
pairs. Such functions are called \emph{pairing functions}.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
این تابع $g$ \emph{معکوسِ} برشماریِ مجموعه‌ای از زوج‌هاست. چنین توابعی
\emph{توابع جفت‌سازی} نامیده می‌شوند.
\end{explain}
```

The particular g is a bijection and inverse of the diagonal enumeration. The following general definition only requires injection; this sentence does not override it.

Alternatives: No material alternative recorded; none invented.

## FA-0031-C06: Arithmetical pairing definition

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-REL-P046, FA-OL-CANON-0001:P0093.

Source:
```latex
\begin{defn}[Pairing function] 
  A function $f\colon A \times B \to \Nat$ is an arithmetical
  \emph{pairing function} if $f$ is injective. We also say that $f$
  \emph{encodes} $A \times B$, and that $f(x,y)$ is the
  \emph{code} for $\tuple{x,y}$.
\end{defn}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{defn}[تابع جفت‌سازی]
  تابع $f\colon A \times B \to \Nat$ یک \emph{تابع جفت‌سازیِ} حسابی است
  اگر $f$ یک‌به‌یک باشد. همچنین می‌گوییم $f$ \emph{کدگذاریِ}
  $A \times B$ را انجام می‌دهد و $f(x,y)$ \emph{کدِ} $\tuple{x,y}$ است.
\end{defn}
```

Keep any injection A×B→Nat; neither onto, computable nor total inverse on Nat is added. Encoding/code are source-defined numerical representations. Empty factors are not excluded.

Alternatives: No material alternative recorded; none invented.

## FA-0031-C07: Decoding only valid codes

Action: correct; confidence 2/3: Editorial0–3, not a calibrated probability. Source meaning checked; exact label or register convention has the stated attestation limit.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0001:P0093.

Source:
```latex
\begin{explain}
We can use pairing functions to encode, e.g., pairs of natural numbers;
or, in other words, we can represent each \emph{pair} of elements
using a \emph{single} number. Using the inverse of the pairing
function, we can \emph{decode} the number, i.e., find out which
pair it represents.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
می‌توانیم، برای نمونه، زوج‌های اعداد طبیعی را با توابع جفت‌سازی
کدگذاری کنیم؛ یا به بیان دیگر، هر \emph{زوج} از عناصر را با
\emph{یک} عدد بازنمایی کنیم. با استفاده از معکوس تابع جفت‌سازی، که بر برد آن تعریف شده است، می‌توانیم
\emph{کدگشایی کنیم}؛ یعنی زوجی را که یک کدِ معتبر بازنمایی می‌کند به دست آوریم.
\emph{توضیح ویراستاری:} یک‌به‌یک‌بودن به‌تنهایی تضمین نمی‌کند که هر عددی کدِ یک زوج باشد.
\end{explain}
```

Explicitly restrict inverse decoding to the range, because injection guarantees uniqueness but not existence of a pair for every natural number. The source alternate section confirms partial inverse scope. کدگشایی is explained as recovering the represented pair, not cryptographic decryption.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Exact کدگشایی is not directly attested on the selected page; L93 attests coding and codes. Retain it with the explicit source-grounded meaning and inverse-domain condition.

## FA-0031-C08: Nonnegative rational exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0001:P0093.

Source:
```latex
\begin{prob}
Give an enumeration of the set of all non-negative rational numbers. 
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
برشماری‌ای از مجموعهٔ همهٔ اعداد گویای نامنفی ارائه کنید.
\end{prob}
```

Retain all nonnegative rationals, including zero. A repeated enumeration from numerator/positive denominator pairs is allowed; reduced fractions are not required. Exercise remains unsolved.

Alternatives: No material alternative recorded; none invented.

## FA-0031-C09: All rationals exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0001:P0093.

Source:
```latex
\begin{prob}
Show that $\Rat$ is !!{enumerable}. Recall that any rational number 
can be written as a fraction $z/m$ with $z \in \Int$, $m \in \Nat^+$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
نشان دهید $\Rat$ شمارا است. به یاد آورید که هر عدد گویا را
می‌توان به‌صورت کسر $z/m$ با $z \in \Int$ و $m \in \Nat^+$ نوشت.
\end{prob}
```

Preserve numerator z in integers, positive denominator m and Rat notation. Nonzero denominator is essential; negative rationals must not disappear.

Alternatives: No material alternative recorded; none invented.

## FA-0031-C10: Finite binary strings exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0001:P0093, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{prob}
Define an enumeration of $\Bin^*$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
برشماری‌ای از $\Bin^*$ تعریف کنید.
\end{prob}
```

Retain Bin star as all finite binary strings including empty, not infinite bit streams. Numerical formula/sequence coding on L93 supports register, not an identical chosen encoding.

Alternatives: No material alternative recorded; none invented.

## FA-0031-C11: Truth functions and valuation distinction

Action: correct; confidence 2/3: Editorial0–3, not a calibrated probability. Source meaning checked; exact label or register convention has the stated attestation limit.
Canon: FA-OL-CANON-0005:P0013, FA-OL-CANON-0001:P0093.

Source:
```latex
\begin{prob}
Recall from your introductory logic course that each possible truth
table expresses a truth function. In other words, the truth functions
are all functions from $\Bin^k \to \Bin$ for some~$k$. Prove that the
set of all truth functions is enumerable.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
از درس مقدماتی منطق خود به یاد آورید که هر جدول ارزشِ ممکن یک تابعِ ارزشِ صدق
را تعیین می‌کند. به بیان دیگر، این‌ها همهٔ توابعی به‌صورت
$\Bin^k \to \Bin$ برای یک~$k$ هستند. ثابت کنید مجموعهٔ همهٔ توابعِ ارزشِ صدق
شماراست.
\end{prob}
```

F13 explicitly separates arbitrary F:{0,1}^n→{0,1} from valuation mu of propositions. Use تابع ارزشِ صدق for this finite-arity input/output role; preserve all arities, all functions and countability, not merely syntactically written formulas. No solution inserted.

Alternatives: No material alternative recorded; none invented.

Expert-review question: The expanded label تابع ارزشِ صدق is contextual, not a verbatim page attestation. It avoids conflating F with the canon’s نگاشت ارزیابی mu.

## FA-0031-C12: Finite subsets of an infinite countable set

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053, FA-OL-CANON-0001:P0093.

Source:
```latex
\begin{prob}
Show that the set of all finite subsets of an arbitrary infinite
!!{enumerable} set is !!{enumerable}.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
نشان دهید مجموعهٔ همهٔ زیرمجموعه‌های متناهیِ یک مجموعهٔ نامتناهی و
شمارا دلخواه، شمارا است.
\end{prob}
```

Preserve arbitrary infinite countable source set and all finite subsets, including empty. Choice of one enumeration of one set is not countably many independent selections.

Alternatives: No material alternative recorded; none invented.

## FA-0031-C13: Cofinite sets and union of two collections

Action: correct; confidence 2/3: Editorial0–3, not a calibrated probability. Source meaning checked; exact label or register convention has the stated attestation limit.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{prob}
A subset of $\Nat$ is said to be \emph{cofinite} iff it is the
complement of a finite set $\Nat$; that is, $A \subseteq \Nat$ is
cofinite iff $\Nat\setminus A$ is finite. Let $I$ be the set whose
!!{element}s are exactly the finite and cofinite subsets of $\Nat$.
Show that $I$ is !!{enumerable}.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
زیرمجموعه‌ای از $\Nat$ را \emph{هم‌متناهی} می‌نامیم اگر و تنها اگر
متممِ یک زیرمجموعهٔ متناهی از~$\Nat$ باشد؛ یعنی $A \subseteq \Nat$
هم‌متناهی است اگر و تنها اگر $\Nat\setminus A$ متناهی باشد. فرض کنید
$I$ مجموعه‌ای باشد که اعضا آن دقیقاً زیرمجموعه‌های متناهی و
هم‌متناهیِ $\Nat$ هستند. نشان دهید $I$ شمارا است.
\emph{یادداشت ویراستاری:} عبارت ناقصِ متن مبدأ دربارهٔ مجموعهٔ متناهی، مطابق
تعریف فرمولیِ بلافاصله پس از آن، «زیرمجموعهٔ متناهیِ اعداد طبیعی» خوانده شده است.
\end{prob}
```

The already correct Persian definition reads complement in Nat of a finite subset of Nat, as forced by Nat minus A finite. Record that retrospective correction of the malformed English; retain its formula and I consisting of both finite and cofinite subsets.

Alternatives: No material alternative recorded; none invented.

Expert-review question: هم‌متناهی is retained as a locally defined term; exact usage is not directly attested in the six pages. The defining complement condition is unambiguous. Existing source finding OLSIZ-002 already covers the malformed phrase.

## FA-0031-C14: Countable union and supplied enumerations

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{prob}
Show that the !!{enumerable} union of !!{enumerable} sets is
!!{enumerable}. That is, whenever $A_1$, $A_2$, \dots{} are sets, and
each $A_i$ is !!{enumerable}, then the union $\bigcup_{i=1}^\infty
A_i$ of all of them is also !!{enumerable}. [NB: this is hard!]
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
نشان دهید اجتماعِ خانواده‌ای شمارا از مجموعه‌های شمارا،
شمارا است. یعنی هرگاه $A_1$، $A_2$، \dots{} مجموعه باشند و هر
$A_i$ شمارا باشد، آنگاه اجتماع $\bigcup_{i=1}^\infty
A_i$ همهٔ آن‌ها نیز شمارا است. [توجه: این مسئله دشوار است!]
\emph{یادداشت دربارهٔ فرض‌ها:} در برهان معمولِ این گزاره، برای انتخاب هم‌زمانِ
یک برشماری برای هر مجموعهٔ ناتهیِ خانواده از اصل انتخاب استفاده می‌شود.
اگر این برشماری‌ها از ابتدا جزو داده‌های مسئله باشند، می‌توان همان داده‌ها را
در ساخت قطری به کار برد؛ در آن صورت این مرحلهٔ انتخاب لازم نیست.
\end{prob}
```

Retain the source exercise and its infinite-family scope. Label the choice selection used by the standard proof; when a family of enumerations is supplied, diagonal construction uses those data. Do not call this false in ZFC or claim full Choice is the weakest necessary axiom. No solution or human-review gate inserted.

Alternatives: No material alternative recorded; none invented.

## FA-0031-C15: Corrected arbitrary inverse exercise

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0003:P0051, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{prob}
Let $f \colon A \times B \to \Nat$ be an arbitrary pairing function.
Show that the inverse of $f$ is an enumeration of $A \times B$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
فرض کنید $f \colon A \times B \to \Nat$ یک تابع جفت‌سازی دلخواه باشد.
\emph{صورت اصلاح‌شدهٔ تمرین:} در حالت ناتهی، با استفاده از معکوسِ $f$
که بر برد آن تعریف شده است، برشماری‌ای برای $A \times B$ بسازید.
حالت تهی را نیز جداگانه بررسی کنید.
\emph{یادداشت ویراستاری:} صورت اولیهٔ تمرین، معکوس را بی‌قید برشماری می‌نامید؛
اما معکوسِ یک تابع یک‌به‌یک لزوماً بر همهٔ اعداد طبیعی تعریف نشده است.
\end{prob}
```

Correct rather than translate the false claim verbatim: an arbitrary injection has inverse only on its image. In nonempty case require constructing an enumeration from that inverse; handle empty separately. The source0032 explicitly calls nonsurjective inverse partial. Preserve f, A×B, codomain and exercise character; disclose the old claim instead of silently redefining pairing functions.

Alternatives: No material alternative recorded; none invented.

## FA-0031-C16: Triple encoding exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0001:P0093, FA-REL-P046.

Source:
```latex
\begin{prob}
Specify a function that encodes $\Nat^3$.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
تابعی مشخص کنید که $\Nat^3$ را کدگذاری کند.
\end{prob}
```

Keep source request to specify an encoding of Nat cubed; composition of a specified pairing works. No need to insert an exercise solution or choose a different corpus definition.

Alternatives: No material alternative recorded; none invented.

## FA-0032-C01: Alternative pairing title

Action: retain_after_fresh_review; confidence 2/3: Editorial0–3, not a calibrated probability. Source meaning checked; exact label or register convention has the stated attestation limit.
Canon: FA-OL-CANON-0001:P0093, FA-REL-P046.

Source:
```latex
\olsection{An Alternative Pairing Function}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{یک تابع جفت‌سازی جایگزین}
```

Retain alternative rather than a supposedly canonical replacement of the prior function. Same source-defined pairing label and explicit injectivity meaning.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Same contextual جفت‌سازی term as0031; no new direct attestation asserted.

## FA-0032-C02: First row and odd vacant positions

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P050.

Source:
```latex
\begin{explain}
There are other enumerations of $\Nat^2$ that make it easier to
figure out what their inverses are. Here is one. Instead of
visualizing the enumeration in an array, start with the list of
positive integers associated with (initially) empty spaces. Imagine
filling these spaces successively with pairs $\tuple{n,m}$ as follows.
Starting with the pairs that have~$0$ in  the first place (i.e., pairs
$\tuple{0,m}$), put the first (i.e., $\tuple{0,0}$) in the first empty
place, then skip an empty space, put the second (i.e., $\tuple{0,2}$)
in the next empty place, skip one again, and so forth. The
(incomplete) beginning of our enumeration now looks like this
\[\small
\begin{array}{@{}c c c c c c c c c c c@{}}
\mathbf 1 & \mathbf 2 & \mathbf 3 & \mathbf 4 & \mathbf 5 & \mathbf 6 & \mathbf 7 & \mathbf 8 & \mathbf 9 & \mathbf{10} & \dots \\ \\
\tuple{0,0} &  & \tuple{0,1} &  & \tuple{0,2} &  & \tuple{0,3} & & \tuple{0,4} &  & \dots \\
\end{array}
\]
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
برشماری‌های دیگری از $\Nat^2$ وجود دارند که یافتن معکوسشان را آسان‌تر
می‌کنند. یکی از آن‌ها را در اینجا می‌بینیم. به‌جای آنکه برشماری را در
یک آرایه مجسم کنید، با فهرستی از اعداد صحیح مثبت آغاز کنید که با
جایگاه‌هایی (در ابتدا) تهی متناظرند. تصور کنید این جایگاه‌ها را به‌ترتیب
و به‌شکل زیر با زوج‌های $\tuple{n,m}$ پر می‌کنیم. از زوج‌هایی آغاز کنید
که در مؤلفهٔ نخستشان~$0$ دارند (یعنی زوج‌های $\tuple{0,m}$): نخستین زوج
(یعنی $\tuple{0,0}$) را در نخستین جایگاه تهی بگذارید، سپس یک جایگاه تهی
را رد کنید، دومین زوج (یعنی $\tuple{0,1}$) را در جایگاه تهی بعدی بگذارید،
دوباره یکی را رد کنید، و به همین ترتیب ادامه دهید. آغازِ (ناکاملِ)
برشماری ما اکنون به‌شکل زیر است:
\[\small
\begin{array}{@{}c c c c c c c c c c c@{}}
\mathbf 1 & \mathbf 2 & \mathbf 3 & \mathbf 4 & \mathbf 5 & \mathbf 6 & \mathbf 7 & \mathbf 8 & \mathbf 9 & \mathbf{10} & \dots \\ \\
\tuple{0,0} &  & \tuple{0,1} &  & \tuple{0,2} &  & \tuple{0,3} & & \tuple{0,4} &  & \dots \\
\end{array}
\]
```

Retain positive-index positions, skip one empty position and first row all(0,m). Correct second pair from(0,2) to(0,1), matching the immediately following table. Table bytes and all other coordinates are unchanged.

Alternatives: No material alternative recorded; none invented.

## FA-0032-C03: Second row and remaining empty positions

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P046.

Source:
```latex
Repeat this with pairs $\tuple{1,m}$ for the place that still remain
empty, again skipping every other empty place:
\[\small
\begin{array}{@{}c c c c c c c c c c c@{}}
\mathbf 1 & \mathbf 2 & \mathbf 3 & \mathbf 4 & \mathbf 5 & \mathbf 6 & \mathbf 7 & \mathbf 8 & \mathbf 9 & \mathbf{10} & \dots \\ \\
\tuple{0,0} & \tuple{1,0} & \tuple{0,1} &  & \tuple{0,2} & \tuple{1,1} & 
\tuple{0,3} & & \tuple{0,4} &  \tuple{1,2} & \dots \\
\end{array}
\]
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
این کار را برای جایگاه‌هایی که هنوز خالی مانده‌اند، با
```

Every other still-empty position means positions2,6,10,..., not every other position in the whole list. Keep the partial second table and its intentional blanks.

Alternatives: No material alternative recorded; none invented.

## FA-0032-C04: Successive rows and completed prefix

Action: correct; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-REL-P046.

Source:
```latex
Enter pairs $\tuple{2,m}$, $\tuple{2,m}$, etc., in the same way. Our
completed enumeration thus starts like this:
\[\small
\begin{array}{@{}cc c c c c c c c c c@{}}
\mathbf 1 & \mathbf 2 & \mathbf 3 & \mathbf 4 & \mathbf 5 & \mathbf 6 & \mathbf 7 & \mathbf 8 & \mathbf 9 & \mathbf{10} & \dots \\ \\
\tuple{0,0} & \tuple{1,0} & \tuple{0,1} & \tuple{2,0}  & \tuple{0,2} & 
\tuple{1,1} & \tuple{0,3} & \tuple{3,0}  & \tuple{0,4} &  \tuple{1,2} & \dots \\
\end{array}
\]
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
زوج‌های
$\tuple{1,m}$ تکرار کنید و باز هم یک جایگاه خالی در میان را رد کنید:
\[\small
\begin{array}{@{}c c c c c c c c c c c@{}}
\mathbf 1 & \mathbf 2 & \mathbf 3 & \mathbf 4 & \mathbf 5 & \mathbf 6 & \mathbf 7 & \mathbf 8 & \mathbf 9 & \mathbf{10} & \dots \\ \\
\tuple{0,0} & \tuple{1,0} & \tuple{0,1} &  & \tuple{0,2} & \tuple{1,1} &
\tuple{0,3} & & \tuple{0,4} &  \tuple{1,2} & \dots \\
\end{array}
\]
زوج‌های $\tuple{2,m}$، $\tuple{3,m}$ و جز آن را نیز به همین شیوه وارد
کنید. \emph{یادداشت ویراستاری:} دو لغزش در مؤلفه‌های زوج‌ها در توضیح متن مبدأ
اصلاح شده‌اند تا توضیح با جدول‌ها سازگار باشد.
بنابراین برشماری کامل‌شدهٔ ما چنین آغاز می‌شود:
\[\small
\begin{array}{@{}cc c c c c c c c c c@{}}
\mathbf 1 & \mathbf 2 & \mathbf 3 & \mathbf 4 & \mathbf 5 & \mathbf 6 & \mathbf 7 & \mathbf 8 & \mathbf 9 & \mathbf{10} & \dots \\ \\
\tuple{0,0} & \tuple{1,0} & \tuple{0,1} & \tuple{2,0}  & \tuple{0,2} &
\tuple{1,1} & \tuple{0,3} & \tuple{3,0}  & \tuple{0,4} &  \tuple{1,2} & \dots \\
\end{array}
\]
```

Correct repeated(2,m) to next family(3,m). Retain source prefix indices1..10; explicit note discloses both prose-coordinate slips. This repeated-row defect matches existing OLSIZ-003, not a newly discovered source issue.

Alternatives: No material alternative recorded; none invented.

## FA-0032-C05: Array of positive codes

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-REL-P046, FA-OL-CANON-0001:P0093.

Source:
```latex
If we number the cells in the array above according to this
enumeration, we will not find a neat zig-zag line, but this
arrangement:
\[
\begin{array}{ c | c | c | c | c | c | c | c }
& \mathbf 0 & \mathbf 1 & \mathbf 2 & \mathbf 3 & \mathbf 4 & \mathbf 5 & \dots \\
\hline
\mathbf 0 & 1 & 3 & 5 & 7 & 9 & 11 & \dots \\
\hline
\mathbf 1 & 2 & 6 & 10 & 14 & 18 & \dots & \dots \\
\hline
\mathbf 2 & 4 & 12 & 20 & 28 & \dots & \dots & \dots \\
\hline
\mathbf 3 & 8 & 24 & 40 & \dots & \dots & \dots & \dots \\
\hline
\mathbf 4 & 16 & 48 & \dots & \dots & \dots & \dots & \dots \\
\hline
\mathbf 5 & 32 & \dots & \dots & \dots & \dots & \dots & \dots \\
\hline
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots\\
\end{array}
\]
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
اگر خانه‌های آرایهٔ بالا را مطابق این برشماری شماره‌گذاری کنیم، خط
زیگزاگ مرتبی نخواهیم یافت، بلکه آرایش زیر را خواهیم داشت:
\[
\begin{array}{ c | c | c | c | c | c | c | c }
& \mathbf 0 & \mathbf 1 & \mathbf 2 & \mathbf 3 & \mathbf 4 & \mathbf 5 & \dots \\
\hline
\mathbf 0 & 1 & 3 & 5 & 7 & 9 & 11 & \dots \\
\hline
\mathbf 1 & 2 & 6 & 10 & 14 & 18 & \dots & \dots \\
\hline
\mathbf 2 & 4 & 12 & 20 & 28 & \dots & \dots & \dots \\
\hline
\mathbf 3 & 8 & 24 & 40 & \dots & \dots & \dots & \dots \\
\hline
\mathbf 4 & 16 & 48 & \dots & \dots & \dots & \dots & \dots \\
\hline
\mathbf 5 & 32 & \dots & \dots & \dots & \dots & \dots & \dots \\
\hline
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots\\
\end{array}
\]
```

Retain all21 explicitly numeric code cells, row/column orientation and headers. These are positive position numbers, before subtracting1, not the final h codes.

Alternatives: No material alternative recorded; none invented.

## FA-0032-C06: Powers-of-two factors and index shift

Action: correct; confidence 2/3: Editorial0–3, not a calibrated probability. Source meaning checked; exact label or register convention has the stated attestation limit.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0001:P0093.

Source:
```latex
We can see that the pairs in row~$0$ are in the odd numbered places of
our enumeration, i.e., pair $\tuple{0,m}$ is in place $2m+1$; pairs in
the second row, $\tuple{1,m}$, are in places whose number is the
double of an odd number, specifically,  $2 \cdot (2m+1)$; pairs in the
third row, $\tuple{2,m}$, are in places whose number is four times an
odd number, $4 \cdot (2m+1)$; and so on. The factors of $(2m+1)$ for
each row, $1$, $2$, $4$, $8$, \dots, are exactly the powers of~$2$:
$1= 2^0$, $2 = 2^1$, $4 = 2^2$, $8 = 2^3$, \dots\@ In fact, the
relevant exponent is always the first member of the pair in
question. Thus, for pair $\tuple{n,m}$ the factor is $2^n$.  This
gives us the general formula: $2^n \cdot (2m+1)$. However, this is a
mapping of pairs to \emph{positive} integers, i.e., $\tuple{0,0}$ has
position~$1$. If we want to begin at position~$0$ we must subtract~$1$
from the result. This gives us:
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
می‌بینیم که زوج‌های سطر~$0$ در جایگاه‌هایی از برشماری ما قرار دارند
که شمارهٔ آن‌ها فرد است؛ یعنی زوج $\tuple{0,m}$ در جایگاه $2m+1$ است. زوج‌های سطر
دوم، یعنی $\tuple{1,m}$، در جایگاه‌هایی قرار دارند که شمارهٔ آن‌ها دو
برابر یک عدد فرد، و به‌طور مشخص $2 \cdot (2m+1)$ است. زوج‌های سطر سوم،
یعنی $\tuple{2,m}$، در جایگاه‌هایی قرار دارند که شمارهٔ آن‌ها چهار برابر
یک عدد فرد، یعنی $4 \cdot (2m+1)$ است؛ و به همین ترتیب. ضریب‌های
$(2m+1)$ در سطرهای مختلف، یعنی $1$، $2$، $4$، $8$، \dots، دقیقاً توان‌های~$2$
هستند: $1= 2^0$، $2 = 2^1$، $4 = 2^2$، $8 = 2^3$، \dots\@ در واقع،
این نما همواره مؤلفهٔ نخستِ زوج مورد نظر است. پس برای زوج
$\tuple{n,m}$، ضریب برابر $2^n$ است. این امر فرمول کلی
$2^n \cdot (2m+1)$ را به ما می‌دهد. بااین‌حال، این نگاشتی از زوج‌ها به
اعداد صحیح \emph{مثبت} است؛ یعنی $\tuple{0,0}$ در جایگاه~$1$ قرار دارد.
اگر بخواهیم از جایگاه~$0$ آغاز کنیم، باید~$1$ را از حاصل کم کنیم. پس داریم:
\end{explain}
```

Replace compressed فردشماره with positions whose numbers are odd. Use ضریب for the multiplier of the odd term, and clear reference for the exponent. Preserve every numeric factor, power, coordinate and the positive-to-zero-based subtraction. No altered arithmetic or computability assumption.

Alternatives: No material alternative recorded; none invented.

Expert-review question: The specific exponent/multiplier syntax is contextual mathematical prose, not a claim of exact attestation on the coding page. Source formulas determine each role.

## FA-0032-C07: Total alternative pairing h

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-REL-P046, FA-OL-CANON-0001:P0093.

Source:
```latex
\begin{ex}
The function $h\colon \Nat^2 \to \Nat$ given by
\[
h(n,m) = 2^n (2m+1) - 1
\]
is a pairing function for the set of pairs of natural numbers~$\Nat^2$.
\end{ex}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{ex}
تابع $h\colon \Nat^2 \to \Nat$ که به‌صورت زیر داده می‌شود
\[
h(n,m) = 2^n (2m+1) - 1
\]
یک تابع جفت‌سازی برای مجموعهٔ زوج‌های اعداد طبیعی~$\Nat^2$ است.
\end{ex}
```

Retain h(n,m)=2^n(2m+1)-1 and Nat²→Nat. Unique decomposition of k+1 as a power of2 times an odd factor proves bijectivity. General proof is in source-mathematics review, not falsely inferred from bounded tests.

Alternatives: No material alternative recorded; none invented.

## FA-0032-C08: Three explicit h computations

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0001:P0093, FA-REL-P046.

Source:
```latex
\begin{explain}
Accordingly, in our second enumeration of $\Nat^2$, the pair
$\tuple{0,0}$ has code $h(0,0) = 2^0(2\cdot 0+1) - 1 = 0$;
$\tuple{1,2}$ has code $2^{1} \cdot (2 \cdot 2 + 1) - 1 = 2
\cdot 5 - 1 = 9$; $\tuple{2,6}$ has code $2^{2} \cdot (2
\cdot 6 + 1) - 1 = 51$.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
بر این اساس، در دومین برشماریِ $\Nat^2$، زوج $\tuple{0,0}$ دارای کد
$h(0,0) = 2^0(2\cdot 0+1) - 1 = 0$ است؛ زوج $\tuple{1,2}$ دارای کد
$2^{1} \cdot (2 \cdot 2 + 1) - 1 = 2
\cdot 5 - 1 = 9$ است؛ زوج $\tuple{2,6}$ دارای کد $2^{2} \cdot (2
\cdot 6 + 1) - 1 = 51$ است.
\end{explain}
```

Preserve h(0,0)=0, h(1,2)=9 and h(2,6)=51 and every intermediate step. These codes differ from the preceding Cantor code; do not globally normalize them to one pairing.

Alternatives: No material alternative recorded; none invented.

## FA-0032-C09: Non-surjectivity and partial inverses

Action: correct; confidence 2/3: Editorial0–3, not a calibrated probability. Source meaning checked; exact label or register convention has the stated attestation limit.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0001:P0093.

Source:
```latex
Sometimes it is enough to encode pairs of natural numbers~$\Nat^2$
without requiring that the encoding is surjective. Such encodings have
inverses that are only partial functions.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
گاهی کافی است زوج‌های اعداد طبیعی~$\Nat^2$ را کدگذاری کنیم، بی‌آنکه
لازم باشد کدگذاری پوشا باشد. اگر کدگذاری پوشا نباشد، معکوس آن فقط در بردش
تعریف می‌شود؛ بنابراین با در نظر گرفتن همهٔ اعدادِ مجموعهٔ مقصد به‌عنوان
ورودی‌های ممکن، معکوس یک تابع جزئی است.
```

Clarify conditional: if the code is not onto its numerical codomain, inverse only on the range is partial relative to the entire codomain. Merely not requiring onto does not make every admitted encoding nonsurjective. Keep plain cardinality versus effective enumeration separate.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Selected D50 establishes the inverse on a bijection’s codomain, not the exact partial-function label. Source0032 supplies the partial-function concept; تابع جزئی is retained contextually.

## FA-0032-C10: Prime-power injection j

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not a calibrated probability. Source semantics and relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-REL-P046, FA-OL-CANON-0001:P0093.

Source:
```latex
\begin{ex}
The function $j\colon \Nat^2 \to \Nat^+$ given by
\[
j(n,m) = 2^n3^m
\]
is !!a{injective} function $\Nat^2 \to \Nat$.
\end{ex}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{ex}
تابع $j\colon \Nat^2 \to \Nat^+$ که به‌صورت زیر داده می‌شود
\[
j(n,m) = 2^n3^m
\]
تابعی یک‌به‌یک به‌صورت $\Nat^2 \to \Nat$ است.
\end{ex}
```

Preserve j(n,m)=2^n3^m, positive output declaration and its view as a map into Nat. Codomain inclusion is valid, not a defect. Unique prime factorization gives injection;5 is not in its range. The map is not the onto pairing h, and its inverse is partial on all naturals.

Alternatives: No material alternative recorded; none invented.

## Validation boundary

Every substantive source and target character lies in an ordered non-overlapping reviewed span. Formal tokens are checked across inline, bracketed, multline and align mathematics. Text arguments in mathematics are separately aligned and manually reviewed for exact connective, quantifier and number-family meaning.
Finite tests support the written reasoning; they are not universal formal proofs. No new PDF was built or visually certified. Frozen owner inputs and reader releases are unchanged; corrections enter the owner’s normal next-batch build and visual QA.
Attribution: Open Logic Project and contributors, under existing CC BY 4.0 notices. https://github.com/OpenLogicProject/OpenLogic . Existing edition: https://github.com/KokunoYumeto/OpenLogic-fa-ir . Canon sources retain separate rights.
