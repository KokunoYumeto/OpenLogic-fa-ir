# Persian OpenLogic: operations on relations and function basics

Complete aligned review of OLP-0019 and OLP-0021, plus the title/import wrapper OLP-0020. Seven Persian scholarly page images were actually read. Consultation is retrospective and does not establish consultation during original translation. This package supplies reader-integration candidates and an expert-review ledger, not a rebuilt reader or whole-corpus certification.

## Review priorities

- Preserve the source convention for relation restriction: both coordinates, not the domain-only restriction used in the canon. Preserve relative-product order: first R, then S.
- Distinguish domain, codomain and range, and preserve function extensionality with its shared-domain/shared-codomain qualification.
- Correct the source square-root boundary at zero and the n/x input-symbol inconsistency, with explicit Persian editorial disclosures. Retain frozen originals.
- Improve actual Persian constructions without abridging examples, changing proof obligations, or treating literal word substitution as idiomatic translation.
- OLP-0020 is only a chapter title and import structure; it must not be counted as another translated prose chapter.
- Confidence is editorial 0-3, not calibrated probability. Human review is a later opportunity, not a gate.

## Scholarly pages actually consulted

- نظریهٔ مجموعه‌ها; محسن خانی, افشین زارعی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/jozve-kamel.pdf). PDF SHA-256: dbd518c80232921264ab5d79b79be01fe42efe8c01a766327db248b2d261de04. Canon PDFs are privately retained, not redistributed.
- ریاضیات گسسته و کاربردها; علیرضا غفاری حدیقه, مگردیچ تومانیان; مؤسسه چاپ و انتشارات دانشگاه جامع امام حسین (ع). [Source](https://hadigheha.github.io/books/teaching/Textbooks/Tarkibiyat.pdf). PDF SHA-256: 8f79c45a926c1cea819c4fefa86383f2a65ae23b1d526baaf99cf2506bb9f317. Canon PDFs are privately retained, not redistributed.
- FA-OL-CANON-0003:P0008, PDF 8, printed 7: Naive set theory: first axiom and footnote2. Directly pairs اصل گسترش with extensionality. Its set-theoretic equality-by-membership is a lexical and structural witness, not a theorem about arbitrary codomain-sensitive functions. Preserve the OpenLogic function statement and its hypotheses.
- FA-OL-CANON-0003:P0014, PDF 14, printed 13: Definition19: products, relations, restriction and domain. Direct relation-as-ordered-pair-set and restriction terminology. IMPORTANT CONVENTION CONFLICT: the canon restricts the first coordinate only, R intersect (A times V); OpenLogic here uses R intersect A squared. Use the vocabulary, not the differing definition.
- FA-OL-CANON-0003:P0015, PDF 15, printed 14: Image class; functional relation; composition; inverse. Direct image, composition and converse definitions. Q composed with R means first R then Q; this matches OLP R|S as S composed with R. The canon distinguishes functional classes from set functions; do not transfer class-theoretic scope to OLP. وارون and حاصل‌ضرب نسبی are not verbatim labels here.
- FA-REL-P044, PDF 44, printed 34: Section2.2: definition, domain/codomain/range and square-root correspondence. Direct function vocabulary, uniqueness and assignment syntax; square-root correspondence includes zero. Its box labelled بسط prints only equality implies equal values: do NOT substitute that direction for OLP extensionality. The source square-root example has real codomain, unlike the canon integer correspondence.
- FA-REL-P045, PDF 45, printed 35: Examples of numerical functions, graph and restriction. Supports mathematical example register and function graph/restriction terminology. The restriction again acts on inputs only. Do not import the page’s floor/ceiling prose (which lacks the greatest/least qualifier), its modulus-at-zero ambiguity, or its different natural-number convention.
- FA-REL-P052, PDF 52, printed 42: Exercises9-13 and relations introduction. Direct piecewise formulas and composition exercises support case-based presentation and ordinary mathematical instructions. The relationships example supplies contextual relational prose, not evidence about actual student grades or family structure. Its literal marriage-example variables are not copied.
- FA-REL-P055, PDF 55, printed 45: Properties of binary relations and composition continuation. Direct definitions and Persian logical connective register for reflexivity and transitivity. The compounds بستار تراگذری and بستار بازتابی و تراگذری are not directly attested on these pages and remain explicitly provisional descriptive labels.

## FA-0019-C01: Operations heading and earlier constructions

Action: retain_after_fresh_review; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0003:P0015, FA-REL-P055.

Source:
```latex
\olsection{Operations on Relations}

It is often useful to modify or combine relations. In
\olref[sfr][rel][ord]{prop:stricttopartial}, we considered the \emph{union}
of relations, which is just the union of two relations considered as
sets of pairs. Similarly, in \olref[sfr][rel][ord]{prop:partialtostrict},
we considered the relative difference of relations. Here are some
other operations we can perform on relations.
```

Reviewed Persian:
```latex
\olsection{عملیات روی روابط}

اغلب مفید است که روابط را تغییر دهیم یا با هم ترکیب کنیم. در
\olref[sfr][rel][ord]{prop:stricttopartial}، \emph{اجتماعِ}
روابط را بررسی کردیم، که صرفاً اجتماع دو رابطه است وقتی آن دو را
به‌منزلهٔ مجموعه‌هایی از زوج‌ها در نظر بگیریم. به همین ترتیب، در
\olref[sfr][rel][ord]{prop:partialtostrict}، تفاضل نسبی روابط را
بررسی کردیم. در اینجا چند عمل دیگر آمده است که می‌توانیم روی روابط انجام دهیم.
```

Retain عملیات روی روابط and the distinction between ordinary union and relative difference of sets of pairs. The two cross-references retain their exact order-conversion labels; relations are not treated as pointwise numerical functions.

Alternatives: No material alternative recorded; none invented.

## FA-0019-C02: Ambient data for the four operations

Action: retain_after_fresh_review; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0003:P0015.

Source:
```latex
\begin{defn}\ollabel{relationoperations} 
Let $R$, $S$ be relations, and $A$ be any set.
```

Reviewed Persian:
```latex
\begin{defn}\ollabel{relationoperations}
فرض کنید $R$ و $S$ رابطه باشند و $A$ مجموعه‌ای دلخواه باشد.
```

Preserve two arbitrary relations and any set A. No common-carrier or function hypothesis is inserted merely because the later example has one.

Alternatives: No material alternative recorded; none invented.

## FA-0019-C03: Inverse relation

Action: retain_after_fresh_review; confidence 2/3: Exact operation is attested; the chosen synonymous label is not printed on the consulted page.
Canon: FA-OL-CANON-0003:P0015.

Source:
```latex
The \emph{inverse} of $R$ is $R^{-1} = \Setabs{\tuple{y, x}}{\tuple{x,
    y} \in R}$.
```

Reviewed Persian:
```latex
\emph{وارون} $R$ برابر است با $R^{-1} = \Setabs{\tuple{y, x}}{\tuple{x,
    y} \in R}$.
```

The coordinates are reversed and every original pair contributes a converse pair. This is inverse relation, not reciprocal arithmetic and not an assertion of function invertibility.

Alternatives: رابطهٔ معکوس is directly attested in the canon; وارون remains the existing transparent label with its exact defining formula.

Expert-review question: Review lane-wide وارون versus معکوس terminology; keep converse available for nonfunctional relations.

## FA-0019-C04: Relative product and order

Action: retain_after_fresh_review; confidence 2/3: Composition is directly attested; the relative-product compound is provisional.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0003:P0015, FA-REL-P055.

Source:
```latex
The \emph{relative product} of $R$ and $S$ is $(R \mid S) =
\{\tuple{x, z} : \exists y(Rxy \land Syz)\}$.
```

Reviewed Persian:
```latex
\emph{حاصل‌ضرب نسبی} $R$ و $S$ برابر است با $(R \mid S) =
\{\tuple{x, z} : \exists y(Rxy \land Syz)\}$.
```

Keep the existential intermediate y and the order Rxy then Syz. The canon composition Q after R has the same order. Do not reverse it by visually matching R|S to R composed with S.

Alternatives: ترکیب is canon-attested; retain حاصل‌ضرب نسبی to preserve the source naming and expose its definition.

Expert-review question: Is a parenthetic ترکیب in this lane desirable? The present exact formula removes orientation ambiguity without renaming the operation.

## FA-0019-C05: Restriction: both coordinates

Action: correct; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-OL-CANON-0003:P0014, FA-REL-P045.

Source:
```latex
The \emph{restriction} of $R$ to $A$ is $\funrestrictionto{R}{A}= R
\cap A^2$.
```

Reviewed Persian:
```latex
\emph{تحدید} $R$ به $A$ برابر است با $\funrestrictionto{R}{A}= R
\cap A^2$؛ در این تعریف، هر دو مؤلفهٔ زوج مرتب باید در مجموعهٔ داده‌شده باشند.
```

Retain the directly attested تحدید, but explicitly unpack the source A-squared condition into both coordinates lying in A. Canon R intersect(A times V) and function restriction are different conventions; the explanation adds no hypothesis and changes no formula.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Keep this convention distinction visible when later function restriction is introduced; never normalize both operations to one formula.

## FA-0019-C06: Application as relation image

Action: correct; confidence 2/3: Image concept and syntax are direct; اعمال is a descriptive label retained from the edition.
Canon: FA-OL-CANON-0003:P0015, FA-REL-P044.

Source:
```latex
The \emph{application} of $R$ to $A$ is $\funimage{R}{A} = \{y :
(\exists x \in A)Rxy\}$
\end{defn}
```

Reviewed Persian:
```latex
\emph{اعمال} $R$ بر $A$، یعنی گرفتن تصویر مجموعه تحت رابطه، برابر است با $\funimage{R}{A} = \{y :
(\exists x \in A)Rxy\}$
\end{defn}
```

Add the explanatory image wording from the canon while retaining the source operation label اعمال. Existentially selected outputs, not pairs, form R[A]; y need not belong to A.

Alternatives: تصویر is directly attested. A complete replacement of the source-named application label is unnecessary.

## FA-0019-C07: Integer successor example

Action: retain_after_fresh_review; confidence 2/3: Definition is exact; successor wording is contextual rather than directly attested.
Canon: FA-REL-P044, FA-OL-CANON-0003:P0015.

Source:
```latex
\begin{ex}
Let $S \subseteq \Int^2$ be the successor relation on~$\Int$, i.e.,
$S = \Setabs{\tuple{x, y} \in \Int^2}{x + 1 = y}$, so that $Sxy$ iff $x + 1 = y$.
```

Reviewed Persian:
```latex
\begin{ex}
فرض کنید $S \subseteq \Int^2$ رابطهٔ جانشینی روی~$\Int$ باشد؛ یعنی
$S = \Setabs{\tuple{x, y} \in \Int^2}{x + 1 = y}$، به‌طوری‌که $Sxy$ اگر و تنها اگر $x + 1 = y$.
```

Keep Int-squared, x+1=y and iff. جانشینی denotes the explicitly defined immediate integer successor, not set-theoretic replacement; canon numerical-function presentation supports the exposition.

Alternatives: No material alternative recorded; none invented.

Expert-review question: جانشینی is contextual here; its relation-label compound is not directly attested on the selected pages.

## FA-0019-C08: Integer predecessor

Action: retain_after_fresh_review; confidence 2/3: Inverse operation direct; پیشینی label contextual.
Canon: FA-OL-CANON-0003:P0015, FA-REL-P044.

Source:
```latex
$S^{-1}$ is the predecessor relation on $\Int$, i.e.,
$\Setabs{\tuple{x,y}\in\Int^2}{x -1 =y}$.
```

Reviewed Persian:
```latex
$S^{-1}$ رابطهٔ پیشینی روی $\Int$ است؛ یعنی
$\Setabs{\tuple{x,y}\in\Int^2}{x -1 =y}$.
```

Reverse the successor relation: x-1=y. Keep the integer carrier, which avoids a missing predecessor at the natural-number boundary.

Alternatives: پیشین versus سلف remains a register preference; no alternate attestation is invented.

## FA-0019-C09: Two successor steps

Action: retain_after_fresh_review; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-OL-CANON-0003:P0015, FA-REL-P044.

Source:
```latex
$S\mid S$ is 
$ \Setabs{\tuple{x,y}\in\Int^2}{x + 2 =y}$
```

Reviewed Persian:
```latex
$S\mid S$ برابر است با
$ \Setabs{\tuple{x,y}\in\Int^2}{x + 2 =y}$
```

Two consecutive successor steps produce x+2=y. Preserve the relative-product symbol and ordered pairs.

Alternatives: No material alternative recorded; none invented.

## FA-0019-C10: Natural-number restriction

Action: retain_after_fresh_review; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-OL-CANON-0003:P0014, FA-REL-P045.

Source:
```latex
$\funrestrictionto{S}{\Nat}$ is the successor relation on~$\Nat$.
```

Reviewed Persian:
```latex
$\funrestrictionto{S}{\Nat}$ رابطهٔ جانشینی روی~$\Nat$ است.
```

Restrict both coordinates to Nat under the local OLP definition. The result is still natural successor; do not use this example to erase the general distinction from domain-only restriction.

Alternatives: No material alternative recorded; none invented.

## FA-0019-C11: Finite image example

Action: retain_after_fresh_review; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-OL-CANON-0003:P0015, FA-REL-P044.

Source:
```latex
$\funimage{S}{\{1,2,3\}}$ is $\{2, 3, 4\}$.
\end{ex}
```

Reviewed Persian:
```latex
$\funimage{S}{\{1,2,3\}}$ برابر است با $\{2, 3, 4\}$.
\end{ex}
```

The image consists of2,3,4. Preserve braces, order and the external output4, which also prevents confusing R[A] with restriction.

Alternatives: No material alternative recorded; none invented.

## FA-0019-C12: Positive-power transitive closure

Action: retain_after_fresh_review; confidence 2/3: Transitivity and composition directly attested; closure compound and recursion wording contextual.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0015.

Source:
```latex
\begin{defn}[Transitive closure]Let $R \subseteq A^2$ be a binary relation. 
	
The \emph{transitive closure} of~$R$ is $R^+ = \bigcup_{0 < n \in
\Nat} R^n$, where we recursively define $R^1 = R$ and $R^{n+1} = R^n
\mid R$.
```

Reviewed Persian:
```latex
\begin{defn}[بستار تراگذری]فرض کنید $R \subseteq A^2$ یک رابطهٔ دوتایی باشد.

\emph{بستار تراگذریِ}~$R$ برابر است با $R^+ = \bigcup_{0 < n \in
\Nat} R^n$، که در آن به‌صورت بازگشتی $R^1 = R$ و $R^{n+1} = R^n
\mid R$ را تعریف می‌کنیم.
```

Keep positive powers only, R1=R and recursion R(n+1)=Rn|R. The source reuses R+ locally; its earlier reflexive-closure use must not override this explicit definition. بستار تراگذری is retained as a transparent compound with its exact full construction.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Further direct attestation of بستار تراگذری is desirable. Do not falsely claim these pages contain that compound or a closure theorem.

## FA-0019-C13: Reflexive transitive closure

Action: retain_after_fresh_review; confidence 2/3: Properties attested, compound provisional.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0015.

Source:
```latex
The \emph{reflexive transitive closure} of $R$ is $R^* = R^+ \cup
\Id{A}$.
\end{defn}
```

Reviewed Persian:
```latex
\emph{بستار بازتابی و تراگذریِ} $R$ برابر است با $R^* = R^+ \cup
\Id{A}$.
\end{defn}
```

Union with the identity on A includes every diagonal pair, even for isolated elements. Keep R-star distinct from R-plus. Conjoined Persian adjectives do not mean two alternative closures.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Review preferred spelling of the combined closure compound; the definition and two required properties are fixed.

## FA-0019-C14: Reachability for integer successor

Action: retain_after_fresh_review; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0015, FA-REL-P044.

Source:
```latex
\begin{ex}
Take the successor relation $S \subseteq \Int^2$. $S^2xy$ iff $x + 2 =
y$, $S^3xy$ iff $x + 3 = y$, etc. So $S^+xy$ iff $x + n = y$ for some
$n \geq 1$. In other words, $S^+xy$ iff $x < y$, and $S^*xy$ iff $x \le
y$.
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}
رابطهٔ جانشینی $S \subseteq \Int^2$ را در نظر بگیرید. $S^2xy$ اگر و تنها اگر $x + 2 =
y$، و $S^3xy$ اگر و تنها اگر $x + 3 = y$، و به همین ترتیب. پس $S^+xy$ اگر و تنها اگر $x + n = y$ برای یک
$n \geq 1$ برقرار باشد. به عبارت دیگر، $S^+xy$ اگر و تنها اگر $x < y$، و $S^*xy$ اگر و تنها اگر $x \le
y$.
\end{ex}
```

Retain powers two and three, some n at least one, strict less-than for R-plus and less-or-equal for R-star. The quantifier must not become all n; no bounded-integer truncation is asserted in the mathematics.

Alternatives: No material alternative recorded; none invented.

## FA-0019-C15: Unsolved closure exercise

Action: retain_after_fresh_review; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-REL-P055, FA-REL-P052.

Source:
```latex
\begin{prob}
Show that the transitive closure of $R$ is in fact transitive.
\end{prob}
```

Reviewed Persian:
```latex
\begin{prob}
نشان دهید که بستار تراگذریِ $R$ در واقع تراگذری است.
\end{prob}
```

Keep the imperative نشان دهید and transitivity obligation. Do not insert the validation proof into the exercise or change it into a mere numerical example.

Alternatives: No material alternative recorded; none invented.

## FA-0020-C01: Functions title and chapter imports only

Action: retain_after_fresh_review; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-REL-P044, FA-OL-CANON-0003:P0015.

Source:
```latex
\olchapter{sfr}{fun}{Functions}

\olimport{function-basics}

\olimport{function-kinds}

\olimport{functions-relations}

\olimport{inverses}

\olimport{composition}

%\olimport{isomorphic-functions}

\olimport{partial-functions}

\OLEndChapterHook
```

Reviewed Persian:
```latex
\olchapter{sfr}{fun}{توابع}

\olimport{function-basics}

\olimport{function-kinds}

\olimport{functions-relations}

\olimport{inverses}

\olimport{composition}

%\olimport{isomorphic-functions}

\olimport{partial-functions}

\OLEndChapterHook
```

توابع is the ordinary scholarly plural of تابع. Preserve all six active imports, the inactive isomorphic-functions comment and the chapter hook. This is a title/structure-only source unit, not the content of the imported sections.

Alternatives: No material alternative recorded; none invented.

## FA-0021-C01: Basics heading and mapping intuition

Action: retain_after_fresh_review; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-REL-P044.

Source:
```latex
\olsection{Basics}

\begin{explain}
A \emph{function} is a map which sends each !!{element} of a given set
to a specific !!{element} in some (other) given set. For instance, the
operation of adding~$1$ defines a function: each number~$n$ is mapped
to a unique number~$n+1$.
```

Reviewed Persian:
```latex
\olsection{مبانی}

\begin{explain}
یک \emph{تابع} نگاشتی است که هر !!{element} از یک مجموعهٔ معین را
به یک !!{element} معین در یک مجموعهٔ معینِ (دیگر) می‌فرستد. برای نمونه،
عمل افزودن~$1$ تابعی را تعریف می‌کند: هر عدد~$n$ به
عدد یکتای~$n+1$ نگاشته می‌شود.
```

Retain مبانی and نگاشت, with each given input assigned a specific output. The successor illustration remains n to n+1. A source parenthesis allows the two sets to coincide; do not require distinct sets.

Alternatives: No material alternative recorded; none invented.

## FA-0021-C02: Pairs and higher-arity inputs

Action: retain_after_fresh_review; confidence 2/3: Numerical function register attested; precise input/output wording contextual.
Canon: FA-REL-P044, FA-REL-P045.

Source:
```latex
More generally, functions may take pairs, triples, etc., as inputs and
return some kind of output. Many functions are familiar to us from
basic arithmetic. For instance, addition and multiplication are
functions. They take in two numbers and return a third.
```

Reviewed Persian:
```latex
به‌طور کلی‌تر، توابع ممکن است زوج‌ها، سه‌تایی‌ها و مانند آن‌ها را ورودی بگیرند و
نوعی خروجی بازگردانند. بسیاری از توابع را از
حساب مقدماتی می‌شناسیم. برای نمونه، جمع و ضرب
تابع‌اند. آن‌ها دو عدد را ورودی می‌گیرند و عدد سومی بازمی‌گردانند.
```

Preserve pairs, triples and the arithmetic examples: addition and multiplication take two inputs and return one output. ورودی and خروجی are explanatory register choices, not claims of algorithmic computability.

Alternatives: No material alternative recorded; none invented.

Expert-review question: ورودی/خروجی are contextual explanatory labels, not verbatim labels on the selected pages.

## FA-0021-C03: Black-box abstraction

Action: retain_after_fresh_review; confidence 2/3: Extensional interpretation source-grounded; metaphor label provisional.
Canon: FA-REL-P044, FA-OL-CANON-0003:P0008.

Source:
```latex
In this mathematical, abstract sense, a function is a \emph{black
box}: what matters is only what output is paired with what input, not
the method for calculating the output.
\end{explain}
```

Reviewed Persian:
```latex
در این معنای ریاضی و انتزاعی، تابع یک \emph{جعبهٔ
سیاه} است: تنها این مهم است که کدام خروجی با کدام ورودی جفت می‌شود، نه
روش محاسبهٔ خروجی.
\end{explain}
```

Retain the source black-box metaphor and its immediately explicit meaning: output/input association matters, calculation method does not. This is source content, not a newly inserted analogy or a computability promise.

Alternatives: No material alternative recorded; none invented.

Expert-review question: جعبهٔ سیاه is a transparent source metaphor; the consulted mathematical pages do not attest the phrase itself.

## FA-0021-C04: Function definition: assignment and uniqueness

Action: correct; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-REL-P044, FA-OL-CANON-0003:P0015.

Source:
```latex
\begin{defn}[Function]
A \emph{function} $f \colon A \to B$ is a mapping of each !!{element}
of~$A$ to an !!{element} of~$B$.
```

Reviewed Persian:
```latex
\begin{defn}[تابع]
یک \emph{تابع} $f \colon A \to B$ به هر !!{element}
از~$A$ دقیقاً یک !!{element} از~$B$ نسبت می‌دهد.
```

Replace the calqued نگاشتی از هر عضو ... به یک عضو with the directly attested Persian assignment construction به هر ... دقیقاً یک ... نسبت می‌دهد. It preserves the source’s unique-value meaning, also stated in the introduction and later definition instructions.

Alternatives: No material alternative recorded; none invented.

## FA-0021-C05: Domain, codomain, arguments and value

Action: correct; confidence 2/3: Core domain/codomain/value distinction directly attested; آرگومان/ورودی register contextual.
Canon: FA-REL-P044, FA-OL-CANON-0003:P0015.

Source:
```latex
We call $A$ the \emph{domain} of~$f$ and $B$ the \emph{codomain}
of~$f$.  The !!{element}s of~$A$ are called inputs or \emph{arguments}
of~$f$, and the !!{element} of~$B$ that is paired with an argument~$x$
by~$f$ is called the \emph{value of~$f$} for argument~$x$,
written~$f(x)$.
```

Reviewed Persian:
```latex
$A$ را \emph{دامنهٔ}~$f$ و $B$ را \emph{هم‌دامنهٔ}
~$f$ می‌نامیم. اعضای~$A$، ورودی‌ها یا \emph{آرگومان‌های}
~$f$ نامیده می‌شوند، و آن !!{element} از~$B$ که با آرگومان~$x$
به‌وسیلهٔ~$f$ جفت می‌شود، \emph{مقدار~$f$} برای آرگومان~$x$ نام دارد و
به‌صورت~$f(x)$ نوشته می‌شود.
```

Keep دامنه, هم‌دامنه and مقدار distinct. Repair اعضا از to اعضای and insert آن before the unique selected member of B. آرگومان remains explained by ورودی rather than being mistaken for a proof argument. Preserve f(x).

Alternatives: شناسه can collide with identifiers; no canon evidence here supports replacing آرگومان by it.

Expert-review question: The chosen argument synonym is contextual; confirm preferred lane terminology without changing argument/value direction.

## FA-0021-C06: Range is the attained subset

Action: correct; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-REL-P044, FA-OL-CANON-0003:P0015.

Source:
```latex
The \emph{range} $\ran{f}$ of~$f$ is the subset of the codomain
consisting of the values of~$f$ for some argument; $\ran{f} =
\Setabs{f(x)}{x \in A}$.
\end{defn}
```

Reviewed Persian:
```latex
\emph{برد} $\ran{f}$ تابع~$f$ زیرمجموعه‌ای از هم‌دامنه است
که از همهٔ مقادیر~$f$ برای آرگومان‌های دامنه تشکیل می‌شود؛ $\ran{f} =
\Setabs{f(x)}{x \in A}$.
\end{defn}
```

Retain برد and subset of codomain. Replace the potentially subset-suggesting برخی آرگومان‌ها with all values for arguments in the domain, as in the canon’s تمامی تصاویر. This is the same image set, not all members of the codomain; no surjectivity is implied.

Alternatives: No material alternative recorded; none invented.

## FA-0021-C07: Arrow-diagram explanation

Action: retain_after_fresh_review; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-REL-P044, FA-REL-P045.

Source:
```latex
The diagram in \olref{fig:function} may help to think about functions. The ellipse
on the left represents the function's \emph{domain}; the ellipse on
the right represents the function's \emph{codomain}; and an arrow
points from an \emph{argument} in the domain to the corresponding
\emph{value} in the codomain.
```

Reviewed Persian:
```latex
نمودارِ \olref{fig:function} می‌تواند به فهم توابع کمک کند. بیضی
سمت چپ \emph{دامنهٔ} تابع را بازنمایی می‌کند؛ بیضی سمت
راست \emph{هم‌دامنهٔ} تابع را بازنمایی می‌کند؛ و پیکانی
از یک \emph{آرگومان} در دامنه به
\emph{مقدار} متناظر در هم‌دامنه اشاره می‌کند.
```

Keep left domain, right codomain and arrows from argument to value exactly as the source asset. RTL prose is not permission to mirror the mathematical diagram. The graphic asset itself is separately checked unchanged.

Alternatives: No material alternative recorded; none invented.

## FA-0021-C08: Figure caption and indefinite member

Action: correct; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-REL-P044, FA-REL-P045.

Source:
```latex
\begin{figure}
  \olasset{assets/diagrams/function.tikz}
  \caption{A function is a mapping of each !!{element} of one set to
    !!a{element} of another. An arrow points from an argument in the
    domain to the corresponding value in the codomain.}
  \ollabel{fig:function}
\end{figure}
```

Reviewed Persian:
```latex
\begin{figure}
  \olasset{assets/diagrams/function.tikz}
  \caption{یک تابع هر !!{element} از یک مجموعه را به
    یک !!{element} از مجموعه‌ای دیگر می‌فرستد. پیکانی از یک آرگومان در
    دامنه به مقدار متناظر در هم‌دامنه اشاره می‌کند.}
  \ollabel{fig:function}
\end{figure}
```

Use the active assignment construction هر عضو را ... می‌فرستد in place of the calqued نگاشتی از هر عضو از. The locale indefinite token expands to nothing, so also restore یک before the target member. Retain figure identity, the diagram asset and input-to-output direction; no new mathematical caption content.

Alternatives: No material alternative recorded; none invented.

## FA-0021-C09: Multiplication domain, codomain and range

Action: retain_after_fresh_review; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-REL-P044, FA-REL-P045.

Source:
```latex
\begin{ex}
Multiplication takes pairs of natural numbers as inputs and maps them
to natural numbers as outputs, so goes from $\Nat \times \Nat$ (the
domain) to $\Nat$ (the codomain). As it turns out, the range is also
$\Nat$, since every $n \in \Nat$ is $n \times 1$.
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}
ضرب، زوج‌های اعداد طبیعی را ورودی می‌گیرد و آن‌ها را
به اعداد طبیعی به‌عنوان خروجی نگاشت می‌کند؛ پس از $\Nat \times \Nat$ (
دامنه) به $\Nat$ (هم‌دامنه) می‌رود. چنان‌که معلوم می‌شود، برد نیز
$\Nat$ است، زیرا هر $n \in \Nat$ برابر $n \times 1$ است.
\end{ex}
```

Keep Nat times Nat as domain and Nat as codomain/range. The n times1 example works for zero too. Preserve the distinction between an ordered pair as one input and a natural number as output.

Alternatives: No material alternative recorded; none invented.

## FA-0021-C10: Single-valuedness and the square-root boundary

Action: correct; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-REL-P044, FA-OL-CANON-0003:P0015.

Source:
```latex
\begin{ex}
Multiplication is a function because it pairs each input---each pair
of natural numbers---with a single output: $\times \colon \Nat^2 \to
\Nat$. By contrast, mapping a natural number~$n$ to a real~$x$ such
that $x^2 = n$ is not functional, since each positive integer~$n$ has two
square roots: $\sqrt{n}$ and~$-\sqrt{n}$. We can make it functional by
only returning the positive square root: $\sqrt{\phantom{X}} \colon
\Nat \to \Real$. 
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}
ضرب یک تابع است، زیرا هر ورودی---هر زوج
از اعداد طبیعی---را با یک خروجی یگانه جفت می‌کند: $\times \colon \Nat^2 \to
\Nat$. در مقابل، نگاشت‌کردن عدد طبیعی~$n$ به عدد حقیقی~$x$ چنان‌که
$x^2 = n$، تابع تعریف نمی‌کند، زیرا هر عدد صحیح مثبت~$n$ دو
ریشهٔ دوم دارد: $\sqrt{n}$ و~$-\sqrt{n}$. می‌توانیم با
بازگرداندن تنها ریشهٔ دوم نامنفی، یک تابع تعریف کنیم: $\sqrt{\phantom{X}} \colon
\Nat \to \Real$.
\emph{یادداشت ویراستاری:} در متن مبدأ «مثبت» آمده است؛ چون دامنه صفر را هم دربر می‌گیرد، در اینجا «نامنفی» لازم است.
\end{ex}
```

Use تابع تعریف نمی‌کند instead of the awkward تابع‌وار نیست, while retaining two real square roots for positive inputs. Correct positive to nonnegative in the chosen-root function because OLP includes zero in Nat. The Persian editorial note explicitly identifies this source repair. Do not change the codomain to integers as in the canon example.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Source repair is high-confidence: at zero the positive-root rule supplies no output. The entire real-square-root existence statement remains source mathematics, not a finite-test theorem.

## FA-0021-C11: Student grades and parents example

Action: retain_after_fresh_review; confidence 2/3: Mathematical interpretation clear; source assumptions and everyday example boundaries are explicit.
Canon: FA-REL-P044, FA-REL-P052.

Source:
```latex
\begin{ex}
The relation that pairs each student in a class with their final grade
is a function---no student can get two different final grades in the
same class. The relation that pairs each student in a class with their
parents is not a function: students can have zero, or two, or more
parents.
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}
رابطه‌ای که هر دانش‌آموز یک کلاس را با نمرهٔ نهایی او جفت می‌کند،
تابع است---هیچ دانش‌آموزی نمی‌تواند در همان
کلاس دو نمرهٔ نهایی متفاوت بگیرد. رابطه‌ای که هر دانش‌آموز یک کلاس را با
والدین او جفت می‌کند تابع نیست: دانش‌آموزان می‌توانند صفر، دو، یا بیش از
دو والد داشته باشند.
\end{ex}
```

Retain the complete original social example, including zero/two/more parents, without imposing a biological-parent-only interpretation. The grade example assumes every student receives a final grade; uniqueness alone would not establish a total function. No new empirical claim about students is inferred from the canon.

Alternatives: No material alternative recorded; none invented.

Expert-review question: The source leaves universal grade assignment implicit. A future editorial clarification could state it, but the existing example is not rewritten into a different social claim.

## FA-0021-C12: Ways to specify a function

Action: retain_after_fresh_review; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-REL-P044, FA-REL-P045, FA-REL-P052.

Source:
```latex
\begin{explain}
We can define functions by specifying in some precise way what the
value of the function is for every possible argument. Different ways of
doing this are by giving a formula, describing a method for computing
the value, or listing the values for each argument. However functions
are defined, we must make sure that for each argument we specify one,
and only one, value.
\end{explain}
```

Reviewed Persian:
```latex
\begin{explain}
می‌توانیم توابع را با تعیین دقیق مقدار تابع برای
هر آرگومان ممکن تعریف کنیم. روش‌های گوناگون این کار عبارت‌اند از
ارائهٔ یک فرمول، توصیف روشی برای محاسبهٔ
مقدار، یا فهرست‌کردن مقادیر برای هر آرگومان. توابع را به هر شیوه‌ای که
تعریف کنیم، باید اطمینان یابیم که برای هر آرگومان یک،
و تنها یک، مقدار تعیین می‌کنیم.
\end{explain}
```

Retain formula, computation description and table of values as alternative ways of specifying an association. Each possible argument must have exactly one value. Do not add a requirement that every function have an effective algorithm.

Alternatives: No material alternative recorded; none invented.

## FA-0021-C13: Successor range excludes zero

Action: retain_after_fresh_review; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-REL-P044, FA-OL-CANON-0003:P0015.

Source:
```latex
\begin{ex}
Let $f \colon \Nat \to \Nat$ be defined such that $f(x) = x+1$. This
is a definition that specifies $f$ as a function which takes in
natural numbers and outputs natural numbers. It tells us that, given a
natural number~$x$, $f$ will output its successor~$x+1$.
In this case, the codomain $\Nat$ is not the range of~$f$, since the
natural number~$0$ is not the successor of any natural number. The
range of~$f$ is the set of all positive integers, $\Int^{+}$.
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}
فرض کنید $f \colon \Nat \to \Nat$ چنان تعریف شود که $f(x) = x+1$. این
تعریف، $f$ را به‌صورت تابعی مشخص می‌کند که
اعداد طبیعی را ورودی می‌گیرد و اعداد طبیعی خروجی می‌دهد. این تعریف می‌گوید که با داشتن یک
عدد طبیعی~$x$، تابع $f$ جانشین آن، یعنی~$x+1$، را خروجی خواهد داد.
در این مورد، هم‌دامنهٔ $\Nat$ بردِ~$f$ نیست، زیرا
عدد طبیعی~$0$ جانشین هیچ عدد طبیعی‌ای نیست.
بردِ~$f$ مجموعهٔ همهٔ اعداد صحیح مثبت، یعنی $\Int^{+}$، است.
\end{ex}
```

Keep f from Nat to Nat, x+1, zero not attained and positive integers as range. This paragraph independently fixes OLP’s inclusion of zero in Nat and establishes the square-root correction boundary.

Alternatives: No material alternative recorded; none invented.

## FA-0021-C14: Equivalent definition and input-variable correction

Action: correct; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-REL-P044, FA-OL-CANON-0003:P0008.

Source:
```latex
\begin{ex}\ollabel{examplefunext}
Let $g \colon \Nat \to \Nat$ be defined such that $g(x) = x+2-1$. This
tells us that $g$ is a function which takes in natural numbers and
outputs natural numbers. Given a natural number~$n$, $g$ will output
the predecessor of the successor of the successor of~$x$, i.e.,
$x+1$.
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}\ollabel{examplefunext}
فرض کنید $g \colon \Nat \to \Nat$ چنان تعریف شود که $g(x) = x+2-1$. این
تعریف به ما می‌گوید که $g$ تابعی است که اعداد طبیعی را ورودی می‌گیرد و
اعداد طبیعی خروجی می‌دهد. با داشتن یک عدد طبیعی~$x$، تابع $g$
پیشینِ جانشینِ جانشینِ~$x$، یعنی
$x+1$، را خروجی خواهد داد.
\emph{یادداشت ویراستاری:} نماد ورودی در این جمله با نماد به‌کاررفته در تعریف تابع یکسان شد.
\end{ex}
```

Correct the source input name n to x in this one sentence, so g(x)=x+2-1 and the predecessor-of-successor-of-successor narrative refer to the same input. Preserve every other symbol and disclose the change in a Persian editorial note.

Alternatives: No material alternative recorded; none invented.

## FA-0021-C15: Function extensionality with qualifications

Action: retain_after_fresh_review; confidence 3/3: Meaning and the stated formula were checked against the source and the cited Persian usage; attestation does not imply a reader study or calibrated probability.
Canon: FA-OL-CANON-0003:P0008, FA-REL-P044, FA-OL-CANON-0003:P0015.

Source:
```latex
\begin{explain}
We just considered two functions, $f$ and $g$, with different
\emph{definitions}. However, these are the \emph{same function}. After
all, for any natural number~$n$, we have that $f(n) = n+1 = n+2-1 =
g(n)$. Otherwise put: our  definitions for $f$ and~$g$ specify the
same mapping by means of different equations. Implicitly, then, we are
relying upon a principle of extensionality for functions, 
\[
  \text{if }\forall x\, f(x) = g(x)\text{, then }f = g
\]
provided that $f$ and~$g$ share the same domain and codomain.
\end{explain}
```

Reviewed Persian:
```latex
\begin{explain}
اکنون دو تابع $f$ و $g$ را با \emph{تعریف‌های} متفاوت بررسی کردیم.
بااین‌حال، این‌ها \emph{همان تابع} هستند. چراکه
برای هر عدد طبیعی~$n$ داریم $f(n) = n+1 = n+2-1 =
g(n)$. به بیان دیگر، تعریف‌های ما برای $f$ و~$g$ یک
نگاشت واحد را به‌وسیلهٔ معادلات متفاوت مشخص می‌کنند. پس به‌طور ضمنی
بر اصل گسترش برای توابع تکیه می‌کنیم،
\[
  \text{اگر }\forall x\, f(x) = g(x)\text{، آنگاه }f = g
\]
مشروط بر اینکه $f$ و~$g$ دامنه و هم‌دامنهٔ یکسانی داشته باشند.
\end{explain}
```

Retain اصل گسترش, directly paired with extensionality in Khani. Preserve the equality chain, forall then implication direction, and same domain AND codomain qualification. The discrete-text box prints the reverse implication under بسط; that does not authorize reversing OLP. Keep f/g definitions distinct from their shared function.

Alternatives: اصل بسط is printed in the second canon but with a differently directed statement. اصل گسترش is already supported and avoids an unnecessary terminology switch.

## FA-0021-C16: Definition by exhaustive exclusive cases

Action: retain_after_fresh_review; confidence 2/3: Piecewise mathematical presentation directly attested; paired explanatory labels contextual.
Canon: FA-REL-P052, FA-REL-P044.

Source:
```latex
\begin{ex}
We can also define functions by cases. For instance, we could define
$h \colon \Nat \to \Nat$  by
\[
h(x) =
\begin{cases}
  \frac{x}{2} & \text{if $x$ is even} \\
  \frac{x+1}{2} & \text{if $x$ is odd.}
\end{cases}
\]
Since every natural number is either even or odd, the output of this
function will always be a natural number. Just remember that if you
define a function by cases, every possible input must fall into
exactly one case.  In some cases, this will require a proof that the
cases are exhaustive and exclusive.
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}
توابع را می‌توانیم به‌صورت موردی نیز تعریف کنیم. برای نمونه، می‌توانیم
$h \colon \Nat \to \Nat$ را چنین تعریف کنیم:
\[
h(x) =
\begin{cases}
  \frac{x}{2} & \text{اگر $x$ زوج باشد} \\
  \frac{x+1}{2} & \text{اگر $x$ فرد باشد.}
\end{cases}
\]
چون هر عدد طبیعی یا زوج است یا فرد، خروجی این
تابع همواره عددی طبیعی خواهد بود. فقط به یاد داشته باشید که اگر
تابعی را به‌صورت موردی تعریف می‌کنید، هر ورودی ممکن باید در
دقیقاً یک حالت قرار گیرد. در برخی موارد، این امر مستلزم اثبات آن است که
حالت‌ها جامع و دوبه‌دو ناسازگارند.
\end{ex}
```

Preserve both branches, even/odd tests, denominator2 and natural codomain. جامع and دوبه‌دو ناسازگار unpack exhaustive and exclusive without dropping either requirement. The source uses a sufficient disjoint-case rule; we do not replace it by the more general compatible-overlap criterion.

Alternatives: No material alternative recorded; none invented.

Expert-review question: جامع و دوبه‌دو ناسازگار is a semantically precise rendering; those exact paired words are not printed in the consulted example.

## Validation boundary

Every substantive source and target character lies in an ordered non-overlapping reviewed span. Formal tokens are checked across inline, bracketed, multline and align mathematics. Text arguments in mathematics are separately aligned and manually reviewed for exact connective, quantifier and number-family meaning.
Finite tests support the written reasoning; they are not universal formal proofs. No new PDF was built or visually certified. Frozen owner inputs and reader releases are unchanged; corrections enter the owner’s normal next-batch build and visual QA.
Attribution: Open Logic Project and contributors, under existing CC BY 4.0 notices. https://github.com/OpenLogicProject/OpenLogic . Existing edition: https://github.com/KokunoYumeto/OpenLogic-fa-ir . Canon sources retain separate rights.
