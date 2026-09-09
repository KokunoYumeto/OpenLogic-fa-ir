# Persian OpenLogic: philosophical reflections and relation properties

Corrected retrospective source/canon review of OLP-0013 through OLP-0015. Supersedes the defective manager review at 1f2ed7ef4bf4fa18836aac0e96a2e3b8bbdc650a, not an owner reader. In particular, the old PASS did not establish linguistic correctness: its irreflexivity change was inconsistent, the connectivity attestation was false, and one test was vacuous. These are additive integration candidates; all original-translation consultation and whole-edition certification remain unclaimed. Exact attestations, contextual inferences and provisional choices are distinguished below.

## Review priorities

- Preserve relation-as-set semantics while separating representational convenience from metaphysical identity.
- Use directly attested Persian relation-property terminology and distinguish asymmetric from merely non-symmetric and irreflexive from merely non-reflexive.
- Preserve every proof step, quantifier, formula, citation, label, hierarchy and token; correct only evidenced wording or scope defects.
- Treat the Persian canon as evidence for register and terminology, not as authority overriding the frozen OpenLogic mathematics.
- Confidence is editorial 0-3, not calibrated probability. Human review is a later opportunity, not a gate.

## Scholarly pages actually consulted

- نظریهٔ مجموعه‌ها; محسن خانی, افشین زارعی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/jozve-kamel.pdf). PDF SHA-256: dbd518c80232921264ab5d79b79be01fe42efe8c01a766327db248b2d261de04. Canon PDFs are privately retained, not redistributed.
- ریاضیات گسسته و کاربردها; علیرضا غفاری حدیقه, مگردیچ تومانیان; مؤسسه چاپ و انتشارات دانشگاه جامع امام حسین (ع). [Source](https://hadigheha.github.io/books/teaching/Textbooks/Tarkibiyat.pdf). PDF SHA-256: 8f79c45a926c1cea819c4fefa86383f2a65ae23b1d526baaf99cf2506bb9f317. Canon PDFs are privately retained, not redistributed.
- تفسیر هستی‌شناختی از عینیت اندیشه نزد فرگه; محمدرضا قربانی, موسی اکرمی; University of Qom, Philosophical-Theological Research 14(1). [Source](https://pfk.qom.ac.ir/article_83_cd0efb6a18ff24d85acdc8842cba1f3d.pdf). PDF SHA-256: 9c5648cbdee48e823469dea0320d0da5422284c78cac9eb506c43b5222e2bcf4. Canon PDFs are privately retained, not redistributed.
- FA-OL-CANON-0003:P0023, PDF 23, printed 22: Chapter 2 definition 1, strict orders and comparability. The explicit universal not-xrx formula attests irreflexivity. Strict-order terminology here must not replace the nonstrict partial-order convention in the other canon.
- FA-OL-CANON-0003:P0024, PDF 24, printed 23: Definition 5, isomorphism. Counted noun after two is singular; element labels x and y do not imply distinctness without a separate distinctness condition.
- FA-OL-CANON-0003:P0062, PDF 62, printed 61: Ramsey chapter introduction. Cardinality constructions use a singular noun stem. This supports contextual singular عضو after n, not deleting genuine uncounted plurals.
- FA-PH-QOM-P006, PDF 6, printed 78: Section 2, object/function and sentence-value discussion. The page contrasts naming an object with making a judgment and uses محمول near the bottom. It supports name/judgment/predicate distinctions; a function/object contrast belongs to page 7, not this passage.
- FA-PH-QOM-P007, PDF 7, printed 79: Section 3 opening, proper names and concepts. The page explicitly calls Socrates a proper name and discusses removing a proper name to obtain a function/concept; it supports the target’s predicate/singular-term discussion without proving that every target phrase is a fixed technical term.
- FA-PH-QOM-P009, PDF 9, printed 81: Object, sense and reference discussion. The page distinguishes sentence meaning/content and reference in Persian philosophical prose. It supports the target’s careful separation of relation representation from identity claims; it is not a general metaphysical identity theory.
- FA-PH-QOM-P020, PDF 20, printed 92: Section 3, mathematical objects and objectivity. The page discusses mathematical objects (عین‌های ریاضی) and objectivity in a research register. It supports the conceptual framing of the target’s final discussion; it does not attest Benacerraf’s specific set-theoretic reduction argument.
- FA-REL-P054, PDF 54, printed 44: Inverse relations and composition. Direct visual attestation of relation-operation exposition. It supports register and notation around relations, not the later property labels.
- FA-REL-P055, PDF 55, printed 45: Binary relation properties and partial orders. Direct visual definitions give Rxx for reflexivity, Rxy and Ryz imply Rxz for transitivity, Rxy implies Ryx for symmetry, and both directions imply x=y for antisymmetry. The page uses تراگذری and پادمتقارن; it distinguishes partial order and comparability.
- FA-REL-P056, PDF 56, printed 46: Equivalence relation definition and congruence example. Direct visual definition and modular-congruence example. It supports the exact equivalence terminology and the distinction among the three properties.
- FA-REL-P057, PDF 57, printed 47: Equivalence classes, quotient set and partitions. Direct visual usage of quotient set, equivalence classes and partition language. The surrounding explanation distinguishes the partition as a whole from its classes; preserve that distinction in OLP-0015.
- FA-REL-P058, PDF 58, printed 48: Congruence, equivalence classes and relation exercises. Direct visual usage of congruence modulo m, equivalence classes, transitivity and partial-order exercises. The pages do not attest asymmetric or irreflexive labels.

## FA-0013-C01: Section title and relation representation

Action: retain_after_fresh_review; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-PH-QOM-P006, FA-PH-QOM-P009.

Source:
```latex
\olsection{Philosophical Reflections}

In \olref[set]{sec}, we defined relations as certain sets. We should
pause and ask a quick philosophical question: what is such a
definition \emph{doing}? It is extremely doubtful that we should want
to say that we have \emph{discovered} some metaphysical identity
facts; that, for example, the order relation on $\Nat$ \emph{turned
out} to be the set $R=  \Setabs{\tuple{n,m}}{n, m \in \Nat\text{ and }
n < m}$ that we defined in \olref[set]{sec}.
```

Reviewed Persian:
```latex
\olsection{تأملات فلسفی}

در \olref[set]{sec}، روابط را مجموعه‌هایی معین تعریف کردیم. شایسته است
درنگ کنیم و پرسشی فلسفی و کوتاه بپرسیم: چنین تعریفی چه
\emph{می‌کند}؟ بسیار بعید است بخواهیم بگوییم برخی واقعیت‌های متافیزیکیِ
این‌همانی را \emph{کشف کرده‌ایم}؛ مثلاً اینکه رابطهٔ ترتیب روی $\Nat$،
چنان‌که \emph{معلوم شده است}، همان مجموعهٔ
$R=  \Setabs{\tuple{n,m}}{n, m \in \Nat\text{ و }
n < m}$ است که در \olref[set]{sec} تعریف کردیم.
```

تأملات فلسفی is a faithful section title. The opening defines relations extensionally as sets but immediately asks what this representation does; preserve the philosophical question rather than turning it into a theorem.

Alternatives: No material alternative recorded; none invented.

## FA-0013-C02: Three-reason transition

Action: retain_after_fresh_review; confidence 2/3: Direct source meaning and ordinary Persian explanatory syntax; contextual register evidence only.
Canon: FA-PH-QOM-P009.

Source:
```latex
Here are three
reasons why.
```

Reviewed Persian:
```latex
در ادامه سه دلیل
برای این تردید می‌آوریم.
```

The transition announces the same three reasons for the preceding doubt. Page 9 supplies examples of connected scholarly argument; it does not directly attest this exact transition. The preceding identity discussion belongs to the previous segment, not this one.

Alternatives: No material alternative recorded; none invented.

## FA-0013-C03: Kuratowski and reverse ordered-pair coding

Action: retain_after_fresh_review; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-REL-P054, FA-PH-QOM-P007.

Source:
```latex
First: in \olref[set][pai]{wienerkuratowski}, we defined $\tuple{a, b} =
\{\{a\}, \{a, b\}\}$. Consider instead the definition $\lVert a,
b\rVert = \{\{b\}, \{a, b\}\} = \tuple{b,a}$. When $a \neq b$, we have
that $\tuple{a, b} \neq \lVert a,b\rVert$. But we could equally have
regarded $\lVert a,b\rVert$ as our definition of an ordered pair,
rather than $\tuple{a,b}$. Both definitions would have worked equally
well. So now we have two equally good candidates to ``be'' the order
relation on the natural numbers, namely:
\begin{align*}
		R &= \Setabs{\tuple{n,m}}{n, m \in \Nat \text{ and }n < m}\\
		S &= \Setabs{\lVert n,m\rVert}{n, m \in \Nat \text{ and }n < m}.
\end{align*}
```

Reviewed Persian:
```latex
نخست: در \olref[set][pai]{wienerkuratowski}، تعریف کردیم $\tuple{a, b} =
\{\{a\}, \{a, b\}\}$. در عوض، تعریف $\lVert a,
b\rVert = \{\{b\}, \{a, b\}\} = \tuple{b,a}$ را در نظر بگیرید. وقتی
$a \neq b$، داریم $\tuple{a, b} \neq \lVert a,b\rVert$. اما به همان
اندازه می‌توانستیم $\lVert a,b\rVert$ را تعریف خود از زوج مرتب قرار
دهیم، نه $\tuple{a,b}$ را. هر دو تعریف به یک اندازه کار می‌کردند. پس
اکنون دو نامزدِ به یک اندازه شایسته داریم که هر یک می‌تواند «خودِ»
رابطهٔ ترتیب روی اعداد طبیعی باشد، یعنی:
\begin{align*}
		R &= \Setabs{\tuple{n,m}}{n, m \in \Nat \text{ و }n < m}\\
		S &= \Setabs{\lVert n,m\rVert}{n, m \in \Nat \text{ و }n < m}.
\end{align*}
```

Both pair codings, inequality under a neq b, and the two candidate relation sets remain explicit. The relation canon supports ordered-pair/composition register; the philosophy canon supports the conceptual function/object contrast.

Alternatives: No material alternative recorded; none invented.

## FA-0013-C04: Benacerraf attribution and alternatives

Action: retain_after_fresh_review; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-PH-QOM-P009, FA-PH-QOM-P020.

Source:
```latex
Since $R \neq S$, by extensionality, it is clear that they cannot
\emph{both} be identical to the order relation on~$\Nat$. But it would
just be arbitrary, and hence a bit embarrassing, to claim that $R$
rather than $S$ (or vice versa) \emph{is} the ordering relation, as a
matter of fact. (This is a very simple instance of an argument against
set-theoretic reductionism which Benacerraf made famous in
\citeyear{Benacerraf1965}. We will revisit it several times.)
```

Reviewed Persian:
```latex
از آنجا که بنا بر اصل گسترش $R \neq S$، روشن است که نمی‌توانند
\emph{هر دو} با رابطهٔ ترتیب روی~$\Nat$ این‌همان باشند. اما ادعای اینکه
بنا بر واقعیت امر، $R$، و نه $S$ (یا برعکس)، \emph{همان} رابطهٔ ترتیب
است، صرفاً دل‌بخواهی و ازاین‌رو اندکی شرم‌آور خواهد بود. (این نمونه‌ای بسیار ساده
از استدلالی علیه تقلیل‌گرایی مجموعه‌شناختی است که بناسراف در
\citeyear{Benacerraf1965} مشهور ساخت. چند بار دیگر به آن بازخواهیم گشت.)
```

The target retains extensionality, R neq S, arbitrariness of choosing R or S, and the Benacerraf1965 citation. The cited Persian article is not used as evidence for Benacerraf’s argument; it only supports native scholarly prose and identity/meaning distinctions.

Alternatives: No material alternative recorded; none invented.

## FA-0013-C05: Membership relation and universal-set contradiction

Action: retain_after_fresh_review; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-REL-P054, FA-PH-QOM-P020.

Source:
```latex
Second: if we think that \emph{every} relation should be identified
with a set, then the relation of set-membership itself, $\in$, should
be a particular set. Indeed, it would have to be the set
$\Setabs{\tuple{x,y}}{x \in y}$. But does this set exist? Given
Russell's Paradox, it is a non-trivial claim that such a set exists.
In fact, \oliflabeldef{cumul:::part}{the theory of sets which we develop in
\olref[cumul][][]{part} will \emph{deny} the existence of this
set.\footnote{Skipping ahead, here is why. For reductio, suppose $I =
\Setabs{\tuple{x,y}}{x \in y}$ exists. Then $\bigcup \bigcup I$ is the
universal set, contradicting
\olref[sfr][z][sep]{thm:NoUniversalSet}.}}{it is possible to
develop set theory in a rigorous way as an axiomatic theory, and that 
theory will indeed deny the existence of this set.}
So, even if some relations can be treated as sets, the relation of
set-membership will have to be a special case.
```

Reviewed Persian:
```latex
دوم: اگر گمان کنیم \emph{هر} رابطه‌ای باید با مجموعه‌ای یکی انگاشته
شود، آنگاه خودِ رابطهٔ عضویت در مجموعه، یعنی $\in$، نیز باید مجموعه‌ای
معین باشد. در واقع، باید مجموعهٔ $\Setabs{\tuple{x,y}}{x \in y}$ باشد.
اما آیا این مجموعه وجود دارد؟ با توجه به پارادوکس راسل، وجود چنین
مجموعه‌ای ادعایی نابدیهی است. در حقیقت،
\oliflabeldef{cumul:::part}{نظریهٔ مجموعه‌ها که آن را در
\olref[cumul][][]{part} بسط می‌دهیم، وجود این مجموعه را \emph{انکار}
خواهد کرد.\footnote{اگر قدری جلوتر برویم، دلیل چنین است. برای برهان
خلف، فرض کنید $I =
\Setabs{\tuple{x,y}}{x \in y}$ وجود دارد. آنگاه $\bigcup \bigcup I$
مجموعهٔ جهان‌شمول است، و این با
\olref[sfr][z][sep]{thm:NoUniversalSet} تناقض دارد.}}{می‌توان نظریهٔ
مجموعه‌ها را به شیوه‌ای دقیق و در قالب نظریه‌ای اصل‌موضوعی بسط داد، و
آن نظریه واقعاً وجود این مجموعه را انکار خواهد کرد.}
پس حتی اگر بتوان برخی روابط را همچون مجموعه‌ها در نظر گرفت، رابطهٔ
عضویت در مجموعه باید حالتی ویژه باشد.
```

The target preserves the conditional membership relation, its set-builder, the nontrivial existence question, both label-definition branches and the footnote deriving a universal set contradiction. No metaphysical identity is asserted.

Alternatives: No material alternative recorded; none invented.

## FA-0013-C06: Predicates versus three singular terms

Action: retain_after_fresh_review; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-PH-QOM-P006, FA-PH-QOM-P007.

Source:
```latex
Third: when we ``identify'' relations with sets, we said that we would
allow ourselves to write $Rxy$ for $\tuple{x,y} \in R$. This is fine,
provided that the membership relation, ``$\in$'', is treated \emph{as}
a predicate. But if we think that ``$\in$'' stands for a certain kind
of set, then the expression ``$\tuple{x,y} \in R$'' just consists of
three singular terms which stand for sets: ``$\tuple{x,y}$'',
``$\in$'', and ``$R$''. And such a list of names is no more capable of
expressing a proposition than the nonsense string: ``the cup penholder
the table''. Again, even if some relations can be treated as sets, the
relation of set-membership must be a special case. (This rolls
together a simple version of Frege's concept \emph{horse} paradox, and
a famous objection that Wittgenstein once raised against Russell.)
```

Reviewed Persian:
```latex
سوم: وقتی روابط را با مجموعه‌ها «یکی می‌انگاریم»، گفتیم به خود اجازه
می‌دهیم $Rxy$ را به جای $\tuple{x,y} \in R$ بنویسیم. این کار بی‌اشکال
است، به شرط آنکه رابطهٔ عضویت، یعنی «$\in$»، \emph{به‌منزلهٔ} یک محمول
در نظر گرفته شود. اما اگر گمان کنیم «$\in$» بر نوع معینی از مجموعه
دلالت دارد، آنگاه عبارت «$\tuple{x,y} \in R$» فقط از سه حد مفرد تشکیل
شده است که بر مجموعه‌ها دلالت می‌کنند: «$\tuple{x,y}$»، «$\in$» و
«$R$». چنین فهرستی از نام‌ها، درست مانند رشتهٔ بی‌معنای «فنجان جاقلمی
میز»، توان بیان یک گزاره را ندارد. باز هم، حتی اگر بتوان برخی روابط را همچون
مجموعه‌ها در نظر گرفت، رابطهٔ عضویت در مجموعه باید حالتی ویژه باشد.
(این استدلال صورت ساده‌ای از پارادوکس «مفهوم \emph{اسب}» فرگه را با
اعتراض مشهوری درهم می‌آمیزد که ویتگنشتاین زمانی علیه راسل مطرح کرد.)
```

The target keeps the predicate/singular-term contrast, the three terms, the deliberately nonsentential cup-penholder-table string, and the Frege/Wittgenstein attributions. The article directly supports proper-name/function/object vocabulary but not a universal term for every singular term; that limit is retained.

Alternatives: No material alternative recorded; none invented.

## FA-0013-C07: Conceptual conclusion

Action: retain_after_fresh_review; confidence 2/3: Mathematical and conceptual meaning is explicit; the exact idiomatic phrase is not directly attested in the selected article pages.
Canon: FA-PH-QOM-P009, FA-PH-QOM-P020.

Source:
```latex
So where does this leave us? Well, there is nothing \emph{wrong} with
our saying that the relations on the numbers are sets. We just have to
understand the spirit in which that remark is made. We are not stating
a metaphysical identity fact. We are simply noting that, in certain
contexts, we can (and will) \emph{treat} (certain) relations as
certain sets.
```

Reviewed Persian:
```latex
پس این بحث ما را به کجا می‌رساند؟ خب، اینکه بگوییم روابط روی اعداد
مجموعه‌اند هیچ \emph{اشکالی} ندارد. فقط باید روح حاکم بر این سخن را
دریابیم. ما واقعیتی متافیزیکی دربارهٔ این‌همانی بیان نمی‌کنیم؛ صرفاً
خاطرنشان می‌کنیم که در برخی زمینه‌ها می‌توانیم (و چنین خواهیم کرد)
روابطی (معین) را \emph{همچون} مجموعه‌هایی معین در نظر بگیریم.
```

The ending says relations may be treated as sets in contexts without claiming metaphysical identity. This is the source’s conceptual conclusion; the canon supplies objectivity/register context, not an attestation of each metaphor. The transparent phrase روح حاکم بر این سخن remains a register choice, not a source-attested technical term.

Alternatives: No material alternative recorded; none invented.

## FA-0014-C01: Title and motivating relation examples

Action: retain_after_fresh_review; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-REL-P055, FA-REL-P056.

Source:
```latex
\olsection{Special Properties of Relations}

\begin{intro}
Some kinds of relations turn out to be so common that they have been
given special names.  For instance, $\le$ and~$\subseteq$ both relate
their respective domains (say, $\Nat$ in the case of~$\le$ and
$\Pow{A}$ in the case of~$\subseteq$) in similar ways.  To get at
exactly how these relations are similar, and how they differ, we
categorize them according to some special properties that relations
can have.  It turns out that (combinations of) some of these special
properties are especially important: orders and equivalence relations.
\end{intro}
```

Reviewed Persian:
```latex
\olsection{ویژگی‌های خاص روابط}

\begin{intro}
برخی گونه‌های روابط چنان رایج‌اند که نام‌هایی خاص به آنها داده‌اند.
برای نمونه، $\le$ و~$\subseteq$ هر دو اعضای دامنه‌های مربوط به خود را
(مثلاً $\Nat$ در مورد~$\le$ و $\Pow{A}$ در مورد~$\subseteq$) به
شیوه‌هایی مشابه به هم مرتبط می‌کنند. برای آنکه دقیقاً دریابیم این روابط
از چه جهت مشابه و از چه جهت متفاوت‌اند، آنها را بر پایهٔ برخی ویژگی‌های
خاصی که روابط می‌توانند داشته باشند دسته‌بندی می‌کنیم. معلوم می‌شود که
(ترکیب‌هایی از) بعضی از این ویژگی‌های خاص اهمیت ویژه‌ای دارند: ترتیب‌ها
و روابط هم‌ارزی.
\end{intro}
```

The title and introduction preserve the Nat/Pow(A) examples and the reason for classifying properties; the directly read book uses the same relation-property exposition and equivalence/partial-order framing.

Alternatives: No material alternative recorded; none invented.

## FA-0014-C02: Reflexivity

Action: retain_after_fresh_review; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-REL-P055.

Source:
```latex
\begin{defn}[Reflexivity]
A relation $R \subseteq A^2$ is \emph{reflexive} iff, for every $x \in
A$, $Rxx$.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[بازتابی‌بودن]
رابطهٔ $R \subseteq A^2$ \emph{بازتابی} است اگر و تنها اگر برای هر $x \in
A$، $Rxx$.
\end{defn}
```

بازتابی is directly printed beside the universal Rxx condition. The target’s بازتابی‌بودن heading and prose preserve that definition.

Alternatives: No material alternative recorded; none invented.

## FA-0014-C03: Transitivity

Action: retain_after_fresh_review; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-REL-P055, FA-REL-P056.

Source:
```latex
\begin{defn}[Transitivity]
A relation $R \subseteq A^2$ is \emph{transitive} iff, whenever $Rxy$
and $Ryz$, then also $Rxz$.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[تراگذری]
رابطهٔ $R \subseteq A^2$ \emph{تراگذری} است اگر و تنها اگر هرگاه $Rxy$
و $Ryz$، آنگاه $Rxz$ نیز.
\end{defn}
```

تراگذری is directly printed with the Rxy,Ryz to Rxz condition. Preserve the source’s implication and the target’s formula; the label is not replaced by an unattested synonym.

Alternatives: No material alternative recorded; none invented.

## FA-0014-C04: Symmetry

Action: retain_after_fresh_review; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-REL-P055, FA-REL-P056.

Source:
```latex
\begin{defn}[Symmetry]
A relation~$R \subseteq A^2$ is \emph{symmetric} iff, whenever
$Rxy$, then also~$Ryx$.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[تقارن]
رابطهٔ~$R \subseteq A^2$ \emph{متقارن} است اگر و تنها اگر هرگاه
$Rxy$، آنگاه~$Ryx$ نیز.
\end{defn}
```

متقارن is directly printed with Rxy implying Ryx. The target heading تقارن and prose preserve the source definition.

Alternatives: No material alternative recorded; none invented.

## FA-0014-C05: Antisymmetry and hyphenation repair

Action: correct; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-REL-P055.

Source:
```latex
\begin{defn}[Anti-symmetry]
A relation~$R \subseteq A^2$ is \emph{anti-sym\-met\-ric} iff, whenever both
$Rxy$ and $Ryx$, then $x=y$ (or, in other words: if $x\neq y$ then
either $\lnot Rxy$ or $\lnot Ryx$).
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[پادتقارنی]
رابطهٔ~$R \subseteq A^2$ \emph{پادمتقارن} است اگر و تنها اگر هرگاه هر دو
$Rxy$ و $Ryx$ برقرار باشند، آنگاه $x=y$ (یا به بیان دیگر: اگر $x\neq y$،
آنگاه دست‌کم یکی از $\lnot Rxy$ یا $\lnot Ryx$ برقرار است).
\end{defn}
```

پادمتقارن is directly printed in the canon. The target’s discretionary TeX hyphenation is removed as a presentation artifact while the meaning and formula remain unchanged.

Alternatives: No material alternative recorded; none invented.

## FA-0014-C06: Antisymmetry is not non-symmetry

Action: retain_after_fresh_review; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-REL-P055.

Source:
```latex
\begin{explain}
In a symmetric relation, $Rxy$ and $Ryx$ always hold together, or
neither holds.  In an anti-symmetric relation, the only way for $Rxy$
and $Ryx$ to hold together is if $x = y$.  Note that this does not
\emph{require} that $Rxy$ and $Ryx$ holds when $x = y$, only that it
isn't ruled out.  So an anti-symmetric relation can be reflexive, but
it is not the case that every anti-symmetric relation is
reflexive.  Also note that being anti-symmetric and merely not being
symmetric are different conditions.  In fact, a relation can be both
symmetric and anti-symmetric at the same time (e.g., the identity
relation is).
\end{explain}
```

Reviewed Persian:
```latex
\begin{explain}
در رابطه‌ای متقارن، $Rxy$ و $Ryx$ همیشه با هم برقرارند یا هیچ‌یک برقرار
نیست. در رابطه‌ای پادمتقارن، تنها در صورتی ممکن است $Rxy$ و $Ryx$ با هم
برقرار باشند که $x = y$. توجه کنید که این امر \emph{ایجاب نمی‌کند} که
$Rxy$ و $Ryx$ وقتی $x = y$ است برقرار باشند؛ فقط برقرار بودنشان را منتفی
نمی‌کند. پس یک رابطهٔ پادمتقارن می‌تواند بازتابی باشد، اما هر رابطهٔ
پادمتقارنی بازتابی نیست. همچنین توجه کنید که پادمتقارن‌بودن با صرفاً
متقارن‌نبودن دو شرط متفاوت‌اند. در واقع، یک رابطه می‌تواند هم‌زمان هم
متقارن و هم پادمتقارن باشد (برای نمونه، رابطهٔ همانی چنین است).
\end{explain}
```

The target preserves the crucial distinction: antisymmetry permits both directions when x=y, does not require diagonal pairs, and differs from merely not symmetric. The identity relation remains the example.

Alternatives: No material alternative recorded; none invented.

## FA-0014-C07: Connectivity/comparability

Action: correct; confidence 2/3: The defining condition is exact; the selected canon supports the explanation, not the existing heading.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0023.

Source:
```latex
\begin{defn}[Connectivity]
A relation $R \subseteq A^2$ is \emph{connected} if for all $x,y\in
A$, if $x \neq y$, then either $Rxy$ or~$Ryx$.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[همبندی]
رابطهٔ $R \subseteq A^2$ \emph{همبند} است اگر برای همهٔ $x,y\in
A$، اگر $x \neq y$، آنگاه دست‌کم یکی از $Rxy$ و~$Ryx$ برقرار است.
به بیان دیگر، هر دو عضو متمایز در دامنه با این رابطه مقایسه‌پذیرند.
\end{defn}
```

Neither cited page attests همبند as the exact relation label. Page 55 uses مقایسه‌پذیر and page 23 قابل مقایسه in order contexts. Retain the existing label provisionally and add an explicit explanation: every two distinct elements are comparable in at least one direction. The condition is pairwise comparability, not a graph-path condition; do not import reflexivity or transitivity from the canon examples.

Alternatives: مقایسه‌پذیری is directly supported for the property; replacing the heading globally requires the later whole-lane terminology decision, not an unlogged substitution here.

Expert-review question: Is همبندی with an explicit pairwise-comparability explanation appropriate as a local label, or should all occurrences adopt مقایسه‌پذیری?

## FA-0014-C08: Exercise domain restriction

Action: retain_after_fresh_review; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-REL-P055.

Source:
```latex
\begin{prob}
Give examples of relations that are (a) reflexive and symmetric but
not transitive, (b) reflexive and anti-symmetric, (c) anti-symmetric,
transitive, but not reflexive, and (d) reflexive, symmetric, and
transitive.  Do not use relations on numbers or sets.
\end{prob}
```

Reviewed Persian:
```latex
\begin{prob}
نمونه‌هایی از روابطی به دست دهید که (a) بازتابی و متقارن ولی
تراگذری نیستند، (b) بازتابی و پادمتقارن‌اند، (c) پادمتقارن و تراگذری‌اند
ولی بازتابی نیستند، و (d) بازتابی، متقارن و تراگذری‌اند. از روابط روی اعداد
یا مجموعه‌ها استفاده نکنید.
\end{prob}
```

Preserve all four property combinations and the explicit prohibition on relations over numbers or sets. The canon provides labels, not exercise solutions.

Alternatives: No material alternative recorded; none invented.

## FA-0014-C09: Irreflexivity distinction

Action: correct; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-OL-CANON-0003:P0023, FA-REL-P055.

Source:
```latex
\begin{defn}[Irreflexivity]
A relation $R \subseteq A^2$ is called \emph{irreflexive} if, for all $x \in
A$, not $Rxx$. 
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[پادبازتابی‌بودن]
رابطهٔ $R \subseteq A^2$ \emph{پادبازتابی} نامیده می‌شود اگر برای هر $x \in
A$، نه $Rxx$.
\end{defn}
```

Khani/Zarei PDF 23 explicitly pairs پادبازتابی with universal not-xrx. Apply that term in the heading, definition and final paragraph. Its universal condition differs from merely failing reflexivity. Page 55 provides surrounding nonstrict relation labels, not this term.

Alternatives: غیربازتابی can be read as not reflexive; reject that ambiguity here. پادبازتابی is directly attested with the required universal formula.

## FA-0014-C10: Asymmetry

Action: retain_after_fresh_review; confidence 2/3: The formal distinction is exact, but the selected pages do not directly attest the exact نامتقارن compound.
Canon: FA-REL-P055, FA-REL-P056.

Source:
```latex
\begin{defn}[Asymmetry]
A relation $R \subseteq A^2$ is called \emph{asymmetric} if for no pair $x,y\in
A$ we have both $Rxy$ and~$Ryx$. 
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[نامتقارنی]
رابطهٔ $R \subseteq A^2$ \emph{نامتقارن} نامیده می‌شود اگر هیچ زوج $x,y\in
A$ وجود نداشته باشد که هر دو $Rxy$ و~$Ryx$ برقرار باشند.
\end{defn}
```

The source requires no pair with both directions. The selected pages do not attest نامتقارن directly, so retain it as a transparent provisional form and explicitly disclose that gap rather than conflating it with not-symmetric or antisymmetric.

Alternatives: No material alternative recorded; none invented.

## FA-0014-C11: Final existence scope

Action: correct; confidence 3/3: Definitions and the singleton counterexample establish the distinction; exhaustive finite checks test all relations on domains of size 0 through 3.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0023.

Source:
```latex
Note that if $A \neq \emptyset$, then no irreflexive relation on~$A$
is reflexive and every asymmetric relation on~$A$ is also
anti-symmetric. However, there are $R \subseteq A^2$ that are not
reflexive and also not irreflexive, and there are anti-symmetric
relations that are not asymmetric.
```

Reviewed Persian:
```latex
توجه کنید که اگر $A \neq \emptyset$، آنگاه هیچ رابطهٔ پادبازتابی
روی~$A$ بازتابی نیست و هر رابطهٔ نامتقارن روی~$A$ پادمتقارن نیز هست.
بااین‌حال، اگر دامنه دست‌کم دو عضو داشته باشد، روابطی $R \subseteq A^2$
وجود دارند که نه بازتابی‌اند و نه پادبازتابی. همچنین، روی هر دامنهٔ
ناتهی رابطه‌ای پادمتقارن وجود دارد که نامتقارن نیست.
\emph{یادداشت ویراستاری:} قید اندازهٔ دامنه برای روشن‌کردن ادعای متن مبدأ
افزوده شده است؛ روی دامنهٔ تک‌عضوی هر رابطه یا بازتابی است یا پادبازتابی.
```

For a fixed singleton domain every relation is either reflexive or irreflexive. A mixed diagonal requires at least two elements, and choosing one diagonal pair supplies a witness on any such domain. Antisymmetric-but-not-asymmetric relations already exist on every nonempty domain (identity). Separate these two existence conditions and label the first qualification as an editorial addition; do not silently strengthen both claims.

Alternatives: A single common at-least-two-elements qualifier is mathematically sufficient but unnecessarily restricts the second claim. Bare text-mode A was introduced merely to satisfy a span test; replace it with the unambiguous phrase دامنه while retaining the original mathematical spans.

Expert-review question: The editorial note is an explicit source-scope clarification, not a transcription correction; retain it when integrating.

## FA-0015-C01: Opening identity relation

Action: retain_after_fresh_review; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-REL-P055, FA-REL-P056.

Source:
```latex
\olsection{Equivalence Relations}

The identity relation on a set is reflexive, symmetric, and
transitive. Relations~$R$ that have all three of these properties are very
common.
```

Reviewed Persian:
```latex
\olsection{روابط هم‌ارزی}

رابطهٔ همانی روی هر مجموعه، رابطه‌ای بازتابی، متقارن و تراگذری است. روابط~$R$
که هر سهٔ این ویژگی‌ها را دارند بسیار رایج‌اند.
```

The target states the identity relation is reflexive, symmetric and transitive and introduces the equivalence section without changing the three properties.

Alternatives: No material alternative recorded; none invented.

## FA-0015-C02: Definition and singular element token

Action: correct; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-REL-P056, FA-OL-CANON-0003:P0024.

Source:
```latex
\begin{defn}[Equivalence relation] 
A relation $R \subseteq A^2$ that is reflexive, symmetric, and
transitive is called an \emph{equivalence relation}. !!^{element}s $x$
and $y$ of~$A$ are said to be \emph{$R$-equivalent} if~$Rxy$.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[رابطهٔ هم‌ارزی]
رابطهٔ $R \subseteq A^2$ که بازتابی، متقارن و تراگذری باشد
\emph{رابطهٔ هم‌ارزی} نامیده می‌شود. گفته می‌شود دو !!{element} $x$
و $y$ از~$A$ \emph{نسبت به $R$ هم‌ارزند} اگر~$Rxy$.
\end{defn}
```

The canon directly attests رابطه هم‌ارزی and دو عنصر. Write دو عضو for the two element variables and preserve the shared element token; the first review incorrectly removed the plural suffix without supplying دو. No claim that x and y are distinct is added.

Alternatives: An uncounted plural with correct Persian ezafe is possible, but the explicit دو عضو construction follows the directly read mathematical usage.

## FA-0015-C03: Classes and partition

Action: retain_after_fresh_review; confidence 2/3: Class/partition meaning is directly supported; the exact retained Persian class label is not attested on this selected page.
Canon: FA-REL-P057.

Source:
```latex
Equivalence relations give rise to the notion of an \emph{equivalence
class}. An equivalence relation ``chunks up'' the domain into
different partitions. Within each partition, all the objects are
related to one another; and no objects from different partitions
relate to one another. Sometimes, it's helpful just to talk about
these partitions \emph{directly}. To that end, we introduce a
definition:
```

Reviewed Persian:
```latex
روابط هم‌ارزی مفهوم \emph{ردهٔ هم‌ارزی} را پدید می‌آورند. یک رابطهٔ
هم‌ارزی دامنه را به رده‌های متفاوتِ یک افراز «تکه‌تکه می‌کند». درون هر
رده، همهٔ اشیا با یکدیگر در رابطه‌اند؛ و هیچ دو شیئی از رده‌های متفاوت
با یکدیگر در رابطه نیستند. گاهی سودمند است که دربارهٔ خودِ این رده‌ها
\emph{مستقیماً} سخن بگوییم. برای این منظور، تعریف زیر را معرفی می‌کنیم:
```

The inherited target distinguishes each class from the partition of the domain. The English informally calls individual blocks partitions; the next definition and the canon support the target’s contextual disambiguation. The page directly prints کلاس‌های هم‌ارزی, مجموعه خارج قسمت and افرازها, not the target’s exact ردهٔ هم‌ارزی wording. Retain that existing class label as a provisional lexical choice with the same explicit definition, without claiming direct attestation.

Alternatives: کلاس هم‌ارزی is directly attested on this page. Do not silently change the established lane-wide رده label from this local review.

Expert-review question: Check the lane-wide evidence for ردهٔ هم‌ارزی; the present page directly attests کلاس هم‌ارزی instead.

## FA-0015-C04: Equivalence-class definition

Action: retain_after_fresh_review; confidence 2/3: The formula and conceptual equivalence are exact; no direct attestation of the target’s رده compound is claimed.
Canon: FA-REL-P057.

Source:
```latex
\begin{defn}\ollabel{def:equivalenceclass}
Let $R \subseteq A^2$ be an equivalence relation. For each $x \in A$,
the \emph{equivalence class} of $x$ in~$A$ is the set $\equivrep{x}{R}
= \Setabs{y \in A}{Rxy}$. The \emph{quotient} of $A$ under~$R$ is
$\equivclass{A}{R} = \Setabs{\equivrep{x}{R}}{x \in A}$, i.e., the set
of these equivalence classes. 
\end{defn}

The next result vindicates the definition of an equivalence class, in
proving that the equivalence classes are indeed the partitions of~$A$:
```

Reviewed Persian:
```latex
\begin{defn}\ollabel{def:equivalenceclass}
فرض کنید $R \subseteq A^2$ رابطه‌ای هم‌ارزی باشد. برای هر $x \in A$،
\emph{ردهٔ هم‌ارزیِ} $x$ در~$A$ مجموعهٔ $\equivrep{x}{R}
= \Setabs{y \in A}{Rxy}$ است. \emph{مجموعهٔ خارج‌قسمتِ} $A$ نسبت
به~$R$ عبارت است از
$\equivclass{A}{R} = \Setabs{\equivrep{x}{R}}{x \in A}$، یعنی مجموعهٔ
این رده‌های هم‌ارزی.
\end{defn}

نتیجهٔ بعدی با اثبات اینکه رده‌های هم‌ارزی به‌راستی بخش‌های یک افراز از~$A$
هستند، تعریف ردهٔ هم‌ارزی را موجه می‌سازد:
```

The class representative, quotient set and exact set-builder formulas remain intact. The canon directly supports the quotient terminology and class concept, using کلاس rather than رده; that lexical limit is recorded in the preceding choice. Frozen mathematical definitions govern.

Alternatives: No material alternative recorded; none invented.

## FA-0015-C05: Class equality proposition and proof

Action: retain_after_fresh_review; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-REL-P055, FA-REL-P056, FA-REL-P057.

Source:
```latex
\begin{prop}
If $R \subseteq A^2$ is an equivalence relation, then $Rxy$ iff
$\equivrep{x}{R} = \equivrep{y}{R}$.
\end{prop}

\begin{proof}
For the left-to-right direction, suppose $Rxy$, and let $z \in
\equivrep{x}{R}$. By definition, then, $Rxz$. Since $R$ is an
equivalence relation, $Ryz$. (Spelling this out: as $Rxy$ and~$R$ is
symmetric we have $Ryx$, and as $Rxz$ and~$R$ is transitive we
have~$Ryz$.) So $z \in \equivrep{y}{R}$. Generalising,
$\equivrep{x}{R} \subseteq \equivrep{y}{R}$. But exactly similarly,
$\equivrep{y}{R} \subseteq \equivrep{x}{R}$. So $\equivrep{x}{R} =
\equivrep{y}{R}$, by extensionality.

For the right-to-left direction, suppose $\equivrep{x}{R} =
\equivrep{y}{R}$. Since $R$ is reflexive, $Ryy$, so $y \in
\equivrep{y}{R}$. Thus also $y \in \equivrep{x}{R}$ by the assumption
that $\equivrep{x}{R} = \equivrep{y}{R}$. So $Rxy$.
\end{proof}
```

Reviewed Persian:
```latex
\begin{prop}
اگر $R \subseteq A^2$ رابطه‌ای هم‌ارزی باشد، آنگاه $Rxy$ اگر و تنها اگر
$\equivrep{x}{R} = \equivrep{y}{R}$.
\end{prop}

\begin{proof}
برای جهت چپ به راست، فرض کنید $Rxy$ و بگذارید $z \in
\equivrep{x}{R}$. بنا بر تعریف، آنگاه $Rxz$. چون $R$ رابطه‌ای هم‌ارزی
است، $Ryz$. (با شرح جزئیات: چون $Rxy$ برقرار است و~$R$ متقارن است، $Ryx$؛
و چون $Rxz$ برقرار است و~$R$ تراگذری است، داریم~$Ryz$.) پس
$z \in \equivrep{y}{R}$. با تعمیم
این استدلال، $\equivrep{x}{R} \subseteq \equivrep{y}{R}$. اما درست به
همین ترتیب، $\equivrep{y}{R} \subseteq \equivrep{x}{R}$. بنابراین بنا
بر اصل گسترش، $\equivrep{x}{R} =
\equivrep{y}{R}$.

برای جهت راست به چپ، فرض کنید $\equivrep{x}{R} =
\equivrep{y}{R}$. چون $R$ بازتابی است، $Ryy$، پس $y \in
\equivrep{y}{R}$. پس $y \in \equivrep{x}{R}$ نیز، بنا بر این فرض که
$\equivrep{x}{R} = \equivrep{y}{R}$. بنابراین $Rxy$.
\end{proof}
```

Every proof direction remains: symmetry plus transitivity for the left-to-right inclusion, extensionality for equality, and reflexivity for the right-to-left direction. No proof step is omitted.

Alternatives: No material alternative recorded; none invented.

## FA-0015-C06: Modular congruence scope

Action: correct; confidence 2/3: The mathematical extension is exact; the intended scope of the source wording remains an editorial interpretation.
Canon: FA-REL-P056, FA-REL-P058.

Source:
```latex
\begin{ex}
A nice example of equivalence relations comes from modular arithmetic.
For any $a$, $b$, and $n \in \PosInt$, say that $a \equiv_n b$ iff
dividing $a$ by~$n$ gives the same remainder as dividing $b$ by~$n$.
(Somewhat more symbolically: $a \equiv_n b$ iff, for some $k \in
\Int$, $a - b = kn$.) Now, $\equiv_n$ is an equivalence relation, for
any~$n$. And there are exactly $n$ distinct equivalence classes
generated by~$\equiv_n$; that is, $\equivclass{\Nat}{\equiv_n}$ has
```

Reviewed Persian:
```latex
\begin{ex}
نمونه‌ای خوب از روابط هم‌ارزی از حساب پیمانه‌ای به دست می‌آید. برای هر دو عدد طبیعی $a$، $b$ و هر $n \in \PosInt$، می‌گوییم $a \equiv_n b$ اگر و تنها اگر
تقسیم $a$ بر~$n$ همان باقی‌مانده‌ای را بدهد که تقسیم $b$ بر~$n$ می‌دهد.
(به‌صورتی نمادین‌تر: $a \equiv_n b$ اگر و تنها اگر یک $k \in
\Int$ وجود داشته باشد که $a - b = kn$.) اکنون، $\equiv_n$ برای
هر~$n$ رابطه‌ای هم‌ارزی است. و دقیقاً $n$ ردهٔ هم‌ارزیِ متمایز
به‌وسیلهٔ~$\equiv_n$ پدید می‌آیند؛ یعنی $\equivclass{\Nat}{\equiv_n}$
```

The source phrase a, b, and n in PosInt is ambiguous against its later quotient of Nat and zero representative. Retain the natural-number a,b clarification with positive n, but visibly disclose the extension to zero in an editorial note. The canon uses congruence on integers, so it supports arithmetic and vocabulary, not the exact source-domain choice.

Alternatives: Keeping all three variables strictly positive conflicts with the subsequent zero representative. Extending to all integers is mathematically possible but broader than the Nat quotient needed here.

Expert-review question: Source-scope clarification: zero is included for a and b to agree with the quotient and its listed representatives.

## FA-0015-C07: Residue classes and counted element

Action: correct; confidence 3/3: The frozen source, existing Persian target and directly read Persian canon passage were compared; limits are stated explicitly.
Canon: FA-REL-P057, FA-REL-P058, FA-OL-CANON-0003:P0062.

Source:
```latex
$n$ !!{element}s. These are: the set of numbers divisible by $n$
without remainder, i.e., $\equivrep{0}{\equiv_n}$; the set of numbers
divisible by $n$ with remainder~$1$, i.e., $\equivrep{1}{\equiv_n}$;
\ldots; and the set of numbers divisible by~$n$ with remainder~$n-1$,
i.e.,~$\equivrep{n-1}{\equiv_n}$.
\end{ex}

\begin{prob}
Show that $\equiv_n$ is an equivalence relation, for any $n \in
\PosInt$, and that $\equivclass{\Nat}{\equiv_n}$ has exactly $n$ members.
\end{prob}
```

Reviewed Persian:
```latex
دارای $n$ !!{element} است. این رده‌ها عبارت‌اند از: مجموعهٔ اعدادی که
بر $n$ بدون باقی‌مانده بخش‌پذیرند، یعنی $\equivrep{0}{\equiv_n}$؛
مجموعهٔ اعدادی که تقسیمشان بر $n$ باقی‌ماندهٔ~$1$ می‌دهد، یعنی
$\equivrep{1}{\equiv_n}$؛ \ldots؛ و مجموعهٔ اعدادی که تقسیمشان بر~$n$
باقی‌ماندهٔ~$n-1$ می‌دهد، یعنی~$\equivrep{n-1}{\equiv_n}$.
\emph{یادداشت ویراستاری:} در این مثال، صفر نیز برای دو عدد نخست مجاز دانسته شده است تا دامنه با خارج‌قسمت اعداد طبیعی و نمایندهٔ صفر در ادامه سازگار باشد؛ پیمانه همچنان مثبت است.
\end{ex}

\begin{prob}
نشان دهید که $\equiv_n$ برای هر $n \in
\PosInt$ رابطه‌ای هم‌ارزی است و
$\equivclass{\Nat}{\equiv_n}$ دقیقاً $n$ عضو دارد.
\end{prob}
```

Change the counted noun after n to singular عضو, consistent with n عضوی in Khani/Zarei and with the final exercise already saying دقیقاً n عضو دارد. The previous review wrongly retained English plural morphology here. Preserve every residue representative and all n distinct classes.

Alternatives: Retaining اعضا after a numerical cardinality is rejected in this construction; uncounted اعضا elsewhere is unaffected.

## Validation boundary

Every substantive source and target character lies in an ordered non-overlapping reviewed span. Formal tokens are checked across inline, bracketed, multline and align mathematics. Text arguments in mathematics are separately aligned and manually reviewed for exact connective, quantifier and number-family meaning.
Finite tests support the written reasoning; they are not universal formal proofs. No new PDF was built or visually certified. Frozen owner inputs and reader releases are unchanged; corrections enter the owner’s normal next-batch build and visual QA.
Attribution: Open Logic Project and contributors, under existing CC BY 4.0 notices. https://github.com/OpenLogicProject/OpenLogic . Existing edition: https://github.com/KokunoYumeto/OpenLogic-fa-ir . Canon sources retain separate rights.
