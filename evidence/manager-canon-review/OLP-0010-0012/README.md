# Persian OpenLogic: Russell’s paradox and relations as sets

Complete source/canon review of OLP-0010 and OLP-0012 plus the OLP-0011 chapter driver. These are two substantive sections and one driver, not three completed chapters. Candidates and evidence only; not a newly built reader. Every canon consultation here is retrospective current review, not a claim about original generation.

## Review priorities

- Retain the genuinely attested naive-set terminology and both branches of Russell’s contradiction.
- Distinguish irreflexivity from the negation of reflexivity using the canon’s exact formula and term.
- Identify the frozen English example’s unintroduced I explicitly as the diagonal identity relation, in a visible editorial footnote.
- Record lexical variants and attestation gaps honestly; no global replacement or invented consultation.
- Confidence is editorial 0-3, not calibrated probability. Human review is a later opportunity, not a gate.

## Scholarly pages actually consulted

- نظریهٔ مجموعه‌ها; محسن خانی, افشین زارعی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/jozve-kamel.pdf). PDF SHA-256: dbd518c80232921264ab5d79b79be01fe42efe8c01a766327db248b2d261de04. Canon PDFs are privately retained, not redistributed.
- مبانی منطق و نظریهٔ مجموعه‌ها; محسن خانی; دانشگاه صنعتی اصفهان. [Source](https://mohsen-khani.github.io/logic97-1/jozve/logic-full.pdf). PDF SHA-256: 565558b76701858236844f19663de27ee10a8d72fd8b007e69b85159ac49f86d. Canon PDFs are privately retained, not redistributed.
- FA-OL-CANON-0003:P0007, PDF 7, printed 6: Section 1.2 and definition 3, with naive footnote. Exact disciplinary naive label and گردایه are visible. Retain the source register; do not replace the attested term with an imagined synonym. Bounded-quantifier notation on this page also clarifies all/only scope.
- FA-OL-CANON-0003:P0008, PDF 8, printed 7: Section 1.2.1, extensionality/comprehension and Russell argument. Extensionality is conditional equality; unrestricted comprehension yields self-membership contradiction. The author explicitly discusses repairing axioms. Canon term اصل ادراک is not the only Persian designation; compare F85.
- FA-OL-CANON-0003:P0010, PDF 10, printed 9: Theorem 7 and its proof; inclusion and binary union definitions. Corroborates the diagonal contradiction and universal membership criterion. The class-theory conclusion is proper class, not a replacement for the OLP theorem denying a set.
- FA-OL-CANON-0003:P0014, PDF 14, printed 13: Definitions 17/19 and lemma 18. Coordinates determine ordered-pair equality; relation represented by pairs and aRb by membership. This canon allows proper-class relations; OLP’s definition stays restricted to a set square.
- FA-OL-CANON-0003:P0023, PDF 23, printed 22: Definition 1, first two bullets. پادبازتابی occurs beside forall x not xrx. This is stronger than merely not reflexive. This canon starts with strict orders; OLP also calls weak orders orders, so retain OLP’s classification.
- FA-OL-CANON-0005:P0085, PDF 85, printed 85: Axioms 1/2 and lemma 201. Second native witness for naive label; comprehension called اصل شمول rather than اصل ادراک. The lemma begins the explicit inconsistent instance. No claim of one exclusive translation for comprehension.
- FA-OL-CANON-0005:P0086, PDF 86, printed 86: Continuation of lemma 201 and transition to ZFC. Explicit z in z iff z notin z, then model-based alternative and motivation for restricted axioms. OLP’s elementary proof does not acquire a completeness-theorem prerequisite.
- FA-OL-CANON-0005:P0090, PDF 90, printed 90: Definition 211 and binary relation paragraph. Set product membership and exact binary-relation term. Canon defines relations from a to b; specializing a=b yields the source’s on-A definition. Function uniqueness conditions later on this page are not imposed on arbitrary relations.

## FA-0010-C01: Title: Russell’s paradox

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0008, FA-OL-CANON-0005:P0086.

Source:
```latex
\olsection{Russell's Paradox}
```

Reviewed Persian:
```latex
\olsection{پارادوکس راسل}
```

پارادوکس راسل is directly attested, including the same diagonal argument. Retain the title and file identity. The canon also uses تناقض راسل or قضیه‌ی راسل in different contexts, not a reason to rename this section.

Alternatives: تناقض راسل is a witnessed variant; قضیه‌ی راسل belongs to the proper-class formulation, not this heading.

## FA-0010-C02: Extensionality: uniqueness only if existence is granted

Action: correct; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0008, FA-OL-CANON-0005:P0085.

Source:
```latex
Extensionality licenses the notation $\Setabs{x}{\phi(x)}$, for
\emph{the} set of $x$'s such that~$\phi(x)$. However, all that
extensionality \emph{really} licenses is the following thought.
\emph{If} there is a set whose members are all and only the $\phi$'s,
\emph{then} there is only one such set. Otherwise put: having fixed
some~$\phi$, the set $\Setabs{x}{\phi(x)}$ is unique, \emph{if it
exists}.
```

Reviewed Persian:
```latex
اصل گسترش به ما اجازه می‌دهد نماد $\Setabs{x}{\phi(x)}$ را برای
\emph{آن} مجموعه از $x$ها به کار ببریم که~$\phi(x)$ درباره‌شان صادق
است. بااین‌حال، اصل گسترش \emph{در واقع} فقط گزارهٔ زیر را
تضمین می‌کند. \emph{اگر} مجموعه‌ای وجود داشته باشد که اعضایش دقیقاً
همان اشیایی باشند که ویژگیِ $\phi$ را دارند، \emph{آنگاه} تنها یک چنین
مجموعه‌ای وجود دارد. به بیان دیگر: پس از تثبیت یک~$\phi$، مجموعهٔ
$\Setabs{x}{\phi(x)}$ یکتا است، \emph{اگر وجود داشته باشد}.
```

The definite-description emphasis, all-and-only membership, fixed property and both explicit existence conditionals remain. C8 gives equality from equal extensions and discusses uniqueness after comprehension. Replace the English-shaped phrase licensing a thought with تضمین می‌کند applied only to the following conditional proposition; do not claim extensionality proves existence.

Alternatives: The original مجاز می‌سازد ... اندیشه is understandable but an unnecessary syntactic calque. Unconditional وجود دارد would be mathematically wrong.

## FA-0010-C03: Comprehension is not available for every property

Action: retain_after_fresh_review; confidence 2/3: Meaning is fully explained by source and canon; the exact descriptive noun has not been found on the consulted pages.
Canon: FA-OL-CANON-0003:P0008, FA-OL-CANON-0005:P0085.

Source:
```latex
But this conditional is important!{} Crucially, not every property
lends itself to \emph{comprehension}. That is, some  properties do
\emph{not} define sets. If they all did, then we would run into
outright contradictions. The most famous example of this is Russell's
Paradox.
```

Reviewed Persian:
```latex
اما این گزارهٔ شرطی مهم است!{} نکتهٔ اساسی آن است که هر ویژگی‌ای امکان
\emph{مجموعه‌سازی} را به دست نمی‌دهد. یعنی برخی ویژگی‌ها مجموعه‌ای را
\emph{تعریف نمی‌کنند}. اگر همهٔ ویژگی‌ها مجموعه تعریف می‌کردند، با
ناسازگاری‌های آشکار روبه‌رو می‌شدیم. مشهورترین نمونهٔ این امر پارادوکس
راسل است.
```

Retain the descriptive مجموعه‌سازی in this introductory paragraph: the very next sentence explains that not every property defines a set. The exact noun is not attested in these pages; C8 uses اصل ادراک and F85 اصل شمول for the schema. We do not label this descriptive wording the exclusive scholarly term or replace it with an unexplained axiom name.

Alternatives: اصل ادراک and اصل شمول are genuinely attested but name the schema; either needs context if substituted for the present process description.

Expert-review question: Should a later corpus glossary add a parenthetical attested schema name here? The current explanatory wording is mathematically faithful but not directly term-attested.

## FA-0010-C04: Self-membership as a question under naive assumptions

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0007, FA-OL-CANON-0003:P0008, FA-OL-CANON-0005:P0090.

Source:
```latex
Sets may be !!{element}s of other sets---for instance, the power set
of a set~$A$ is made up of sets. And so it makes sense to ask or
investigate whether a set is !!a{element} of another set. Can a set be
a member of itself?  Nothing about the idea of a set seems to rule
this out. For instance, if \emph{all} sets form a collection of
objects, one might think that they can be collected into a single
set---the set of all sets. And it, being a set, would be !!a{element}
of the set of all sets.
```

Reviewed Persian:
```latex
مجموعه‌ها می‌توانند !!{element}s مجموعه‌های دیگر باشند---برای نمونه،
مجموعهٔ توانیِ مجموعهٔ~$A$ از مجموعه‌ها تشکیل شده است. بنابراین
پرسیدن یا بررسی اینکه آیا مجموعه‌ای !!a{element} مجموعه‌ای دیگر است،
معنا دارد. آیا یک مجموعه می‌تواند عضو خودش باشد؟ ظاهراً هیچ‌چیز در
مفهوم مجموعه این امکان را منتفی نمی‌کند. برای نمونه، اگر \emph{همهٔ}
مجموعه‌ها گردایه‌ای از اشیا را تشکیل دهند، ممکن است گمان کنیم که
می‌توان آنها را در یک مجموعه گرد آورد---مجموعهٔ همهٔ مجموعه‌ها. و این
مجموعه، چون خود یک مجموعه است، !!a{element} مجموعهٔ همهٔ مجموعه‌ها
خواهد بود.
```

Retain actual plural member macros for sets that are members of other sets, the power-set example, and the hypothetical all-sets collection. گردایه is attested in C7. The source says self-membership seems not ruled out by the informal idea, not that Foundation permits it. Preserve ظاهراً and the conditional; do not import a later axiom.

Alternatives: Replacing the hypothetical with a categorical ban on self-membership would change the exposition and its assumptions. The exact adjective توانی is a transparent retained locale variant; F90 names اصل توان.

## FA-0010-C05: Non-self-membered sets and the proposed Russell set

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0008, FA-OL-CANON-0005:P0086.

Source:
```latex
Russell's Paradox arises when we consider the property of not having
itself as !!a{element}, of being \emph{non-self-membered}. What if we
suppose that there is a set of all sets that do not have themselves as
!!a{element}? Does
\[
R = \Setabs{x}{x \notin x}
\]
exist? It turns out that we can prove that it does not.
```

Reviewed Persian:
```latex
پارادوکس راسل هنگامی پدید می‌آید که ویژگیِ !!a{element} خود نبودن، یعنی
\emph{عضو خود نبودن}، را در نظر بگیریم. اگر فرض کنیم مجموعه‌ای از همهٔ
مجموعه‌هایی وجود دارد که !!a{element} خودشان نیستند، چه؟ آیا
\[
R = \Setabs{x}{x \notin x}
\]
وجود دارد؟ معلوم می‌شود که می‌توانیم ثابت کنیم چنین مجموعه‌ای وجود ندارد.
```

Both the property and the existential question are retained, with the display unchanged. عضو خود نبودن directly unpacks non-self-membered without implying ordinary disjointness or absence of all members. The brief repetition maps the source’s descriptive clause and emphasized name.

Alternatives: تهی or a set having no members would describe a different property.

## FA-0010-C06: The theorem denies existence, not emptiness

Action: correct; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0008, FA-OL-CANON-0003:P0010.

Source:
```latex
\begin{thm}[Russell's Paradox]\ollabel{thm:russells-paradox}
	There is no set $R = \Setabs{x}{x \notin x}$.
\end{thm}
```

Reviewed Persian:
```latex
\begin{thm}[پارادوکس راسل]\ollabel{thm:russells-paradox}
	هیچ مجموعه‌ای به صورت $R = \Setabs{x}{x \notin x}$ وجود ندارد.
\end{thm}
```

Add به صورت to make the Persian noun phrase grammatical; the exact R equation and theorem label are unchanged. The conclusion is that no set with that specification exists, not that R is empty. C10 calls the analogous class proper; it is not imported as the OLP theorem statement.

Alternatives: R is empty is false as a replacement for nonexistence.

## FA-0010-C07: Short proof: contradictory biconditional

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0008, FA-OL-CANON-0005:P0086.

Source:
```latex
\begin{proof}
If $R = \Setabs{x}{x \notin x}$ exists, then
$R \in R$ iff $R \notin R$, which is a contradiction.
\end{proof}
```

Reviewed Persian:
```latex
\begin{proof}
اگر $R = \Setabs{x}{x \notin x}$ وجود داشته باشد، آنگاه
$R \in R$ اگر و تنها اگر $R \notin R$؛ و این یک تناقض است.
\end{proof}
```

Preserve the existence assumption, R in R iff R notin R, and contradiction. اگر و تنها اگر directly matches the canon’s biconditional use. No appeal to Foundation, Cantor’s theorem or completeness is added.

Alternatives: No material alternative recorded; none invented.

## FA-0010-C08: Expanded proof: first membership branch

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0008, FA-OL-CANON-0005:P0086.

Source:
```latex
\begin{tagblock}{novice}
\begin{explain}
Let's run through this proof more slowly. If $R$ exists, it makes sense to ask whether $R \in
R$ or not. Suppose that indeed $R \in R$. Now, $R$~was defined as the set of all
sets that are not !!{element}s of themselves. So, if $R \in R$,
then $R$ does not itself have $R$'s defining property. But only sets
that have this property are in~$R$, hence, $R$ cannot be !!a{element}
of~$R$, i.e., $R \notin R$. But $R$ can't both be and not be
!!a{element} of~$R$, so we have a contradiction.
```

Reviewed Persian:
```latex
\begin{tagblock}{novice}
\begin{explain}
بیایید این برهان را آهسته‌تر مرور کنیم. اگر $R$ وجود داشته باشد، پرسیدن
اینکه آیا $R \in
R$ است یا نه معنا دارد. فرض کنید واقعاً $R \in R$. اکنون، $R$ به‌صورت
مجموعهٔ همهٔ مجموعه‌هایی تعریف شده بود که !!{element}s خودشان نیستند. پس
اگر $R \in R$، خودِ $R$ ویژگیِ تعریف‌کنندهٔ $R$ را ندارد. اما فقط
مجموعه‌هایی که این ویژگی را دارند در~$R$ هستند؛ ازاین‌رو $R$ نمی‌تواند
!!a{element}~$R$ باشد، یعنی $R \notin R$. ولی $R$ نمی‌تواند نسبت
به~$R$، هم !!a{element} باشد و هم نباشد؛ پس به تناقض رسیده‌ایم.
```

The novice wrapper is inherited source structure, not newly simplified content. Under the existence assumption, supposing membership forces failure of the defining property and hence nonmembership. All occurrences of R and membership statements in this span were read in order; actual plural themselves is distributive and is not a counted-noun suffix defect.

Alternatives: Turning همهٔ مجموعه‌هایی ... اعضای خودشان نیستند into a claim of no members would be wrong.

## FA-0010-C09: Expanded proof: nonmembership branch

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0008, FA-OL-CANON-0005:P0086.

Source:
```latex
Since the assumption that $R \in R$ leads to a contradiction, we have
$R \notin R$. But this also leads to a contradiction!{} For if $R
\notin R$, then $R$ itself does have $R$'s defining property, and so $R$ would be
!!a{element} of $R$ just like all the other non-self-membered sets.
And again, it can't both not be and be !!a{element} of~$R$.
\end{explain}
\end{tagblock}
```

Reviewed Persian:
```latex
چون فرضِ $R \in R$ به تناقض می‌انجامد، داریم $R \notin R$. اما این نیز
به تناقض می‌انجامد!{} زیرا اگر $R
\notin R$، آنگاه خودِ $R$ ویژگیِ تعریف‌کنندهٔ $R$ را دارد، و بنابراین
$R$ نیز درست مانند همهٔ مجموعه‌های دیگری که عضو خود نیستند، !!a{element}
$R$ خواهد بود. و باز هم نمی‌تواند نسبت به~$R$، هم !!a{element} نباشد و
هم باشد.
\end{explain}
\end{tagblock}
```

The preceding contradiction gives nonmembership only within the assumed existence context. Then the defining property forces membership again. Retain the second contradiction and both closure environments. The final conclusion remains rejection of existence, not selection of one truth value.

Alternatives: No material alternative recorded; none invented.

## FA-0010-C10: Precise existence axioms avoid the paradox

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0008, FA-OL-CANON-0005:P0086.

Source:
```latex
\begin{digress}
How do we set up a set theory which avoids falling into
Russell's Paradox, i.e., which avoids making the \emph{inconsistent}
claim that $R = \Setabs{x}{x \notin x}$ exists? Well, we would need to
lay down axioms which give us very precise conditions for stating when
sets exist (and when they don't).
```

Reviewed Persian:
```latex
\begin{digress}
چگونه نظریه‌ای برای مجموعه‌ها بنا کنیم که به پارادوکس راسل گرفتار نشود؛
یعنی ادعای \emph{ناسازگارِ} وجود مجموعهٔ
$R = \Setabs{x}{x \notin x}$ را مطرح نکند؟ باید اصول موضوعی‌ای وضع کنیم
که شرایط بسیار دقیقی برای بیان اینکه مجموعه‌ها چه هنگام وجود دارند (و چه
هنگام وجود ندارند) به دست دهند.
```

The digression asks for precise conditions on existence and nonexistence. اصول موضوعی and ناسازگار preserve the mathematical register of the canon. Do not claim arbitrary additional axioms automatically give a consistency proof.

Alternatives: No material alternative recorded; none invented.

## FA-0010-C11: Naive theory and conditional continuation

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0007, FA-OL-CANON-0003:P0008, FA-OL-CANON-0005:P0085.

Source:
```latex
The set theory sketched in this chapter doesn't do this. It's
\emph{genuinely na\"ive}. It tells you only that sets obey
extensionality and that, if you have some sets, you can form their
union, intersection, etc. It is possible to develop set theory more
rigorously than this. \oliflabeldef{cumul:::part}{That rigour will be
reserved for Part \olref[cumul][][]{part}. For now, we will proceed
na\"ively, and carefully try to sidestep contradictions.}{}
\end{digress}
```

Reviewed Persian:
```latex
نظریهٔ مجموعه‌هایی که در این فصل طرح شده چنین کاری نمی‌کند. این نظریه
\emph{به‌راستی ساده‌انگارانه} است. فقط می‌گوید مجموعه‌ها از اصل گسترش
پیروی می‌کنند و اگر چند مجموعه
داشته باشیم، می‌توانیم اجتماع، اشتراک و مانند آن را تشکیل دهیم. می‌توان
نظریهٔ مجموعه‌ها را به‌صورتی دقیق‌تر از این بسط داد.
\oliflabeldef{cumul:::part}{آن دقت را برای بخش
\olref[cumul][][]{part} نگه می‌داریم. فعلاً ساده‌انگارانه، اما با احتیاط،
پیش می‌رویم و می‌کوشیم از ناسازگاری‌ها دوری کنیم.}{}
\end{digress}
```

Retain both ساده‌انگارانه occurrences: C7’s naive footnote, C8’s heading and F85’s alternative name are direct disciplinary witnesses. A preliminary concern about pejorative calquing is resolved by actual canon reading. The same paragraph retains extensionality, conditional operations, future rigor and the complete cumul conditional link; no new prerequisite is added.

Alternatives: شهودی was considered as a possible informal equivalent but is not the directly attested name on these pages; do not replace witnessed terminology on intuition alone.

## FA-0011-C01: Relations chapter title and all eight imports

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0090.

Source:
```latex
\olchapter{sfr}{rel}{Relations}

\olimport{relations-as-sets}

\olimport{reflections}

\olimport{special-properties}

\olimport{equivalence-relations}

\olimport{orders}

\olimport{graphs}

\olimport{trees}

\olimport{operations}

\OLEndChapterHook
```

Reviewed Persian:
```latex
\olchapter{sfr}{rel}{روابط}

\olimport{relations-as-sets}

\olimport{reflections}

\olimport{special-properties}

\olimport{equivalence-relations}

\olimport{orders}

\olimport{graphs}

\olimport{trees}

\olimport{operations}

\OLEndChapterHook
```

روابط is the plural of the attested mathematical رابطه. Retain it. All eight ordered imports and OLEndChapterHook are unchanged. This record reviews the driver’s title and assembly instructions only; it does not certify the imported sections not reviewed in this batch.

Alternatives: No alternative chapter architecture or independent translated-book claim is introduced.

## FA-0012-C01: Relations represented as sets

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0090.

Source:
```latex
\olsection{Relations as Sets}
```

Reviewed Persian:
```latex
\olsection{روابط به‌مثابه مجموعه‌ها}
```

The title روابط به‌مثابه مجموعه‌ها accurately announces representation of relations as sets. The exact connective به‌مثابه is an editorial syntax choice, not claimed as a quotation. F90 provides the set-level construction and C14 the broader class analogue.

Alternatives: No material alternative recorded; none invented.

## FA-0012-C02: Familiar orders and identity

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0003:P0023.

Source:
```latex
\begin{explain}
In \olref[sfr][set][imp]{sec}, we mentioned some important sets:
$\Nat$, $\Int$, $\Rat$, $\Real$. You will no doubt remember some
interesting relations between the !!{element}s of some of these sets.
For instance, each of these sets has a completely standard \emph{order
relation} on it.  There is also the relation \emph{is identical with}
that every object bears to itself and to no other thing. There are
many more interesting relations that we'll encounter, and even more
possible relations. Before we review them, though, we will start by
pointing out that we can look at relations as a special sort of set.
```

Reviewed Persian:
```latex
\begin{explain}
در \olref[sfr][set][imp]{sec}، از چند مجموعهٔ مهم یاد کردیم:
$\Nat$، $\Int$، $\Rat$ و $\Real$. بی‌گمان برخی روابط جالب میان
!!{element}s بعضی از این مجموعه‌ها را به خاطر دارید. برای نمونه، بر
هر یک از این مجموعه‌ها یک \emph{رابطهٔ ترتیب} کاملاً استاندارد وجود
دارد. رابطه‌ای نیز هست با معنای \emph{با یکدیگر یکسان‌بودن}؛ هر شیء
این رابطه را با خودش، و با هیچ چیز دیگری، دارد. روابط جالب دیگری نیز
هستند که با آنها روبه‌رو خواهیم شد، و روابط ممکن از این هم بیشترند.
اما پیش از مرور آنها، نخست نشان می‌دهیم که می‌توان روابط را نوع خاصی
از مجموعه دانست.
```

Retain the references and four number systems, ordinary order relations and self-only identity. C14 explicitly defines equality relation by equal coordinates; C23 uses the familiar less-than analogy for order. با یکدیگر یکسان‌بودن means identity here, not merely similarity, as the next clause restricts it to the same object.

Alternatives: رابطه‌ی تساوی is the exact canon variant; رابطهٔ همانی later names the diagonal. Keep the descriptive opening and expose the lexical relation rather than inventing a difference of mathematical objects.

## FA-0012-C03: Ordered-pair coordinates and Cartesian product

Action: correct; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0090.

Source:
```latex
For this, recall two things from \olref[sfr][set][pai]{sec}. First,
recall the notion of an \emph{ordered pair}: given $a$ and $b$, we can
form~$\tuple{a, b}$. Importantly, the order of elements \emph{does}
matter here. So if $a \neq b$ then $\tuple{a, b} \neq \tuple{b, a}$.
(Contrast this with unordered pairs, i.e., $2$-element sets, where
$\{a, b\}=\{b, a\}$.) Second, recall the notion of a \emph{Cartesian
product}: if $A$ and $B$ are sets, then we can form~$A \times B$, the
set of all pairs $\tuple{x, y}$ with $x \in A$ and $y \in B$. In
particular, $A^{2}= A \times A$ is the set of all ordered pairs
from~$A$.
```

Reviewed Persian:
```latex
برای این منظور، دو مطلب را از \olref[sfr][set][pai]{sec} به یاد آورید.
نخست، مفهوم \emph{زوج مرتب} را یادآوری کنید: با داشتن $a$ و $b$،
می‌توانیم~$\tuple{a, b}$ را تشکیل دهیم. نکتهٔ مهم این است که ترتیب
مؤلفه‌ها در اینجا \emph{واقعاً} اهمیت دارد. پس اگر $a \neq b$، آنگاه
$\tuple{a, b} \neq \tuple{b, a}$. (این را با زوج‌های نامرتب، یعنی
مجموعه‌های $2$-عضوی، مقایسه کنید که در آنها
$\{a, b\}=\{b, a\}$.) دوم، مفهوم \emph{ضرب دکارتی} را به یاد آورید:
اگر $A$ و $B$ مجموعه باشند، می‌توانیم~$A \times B$، یعنی مجموعهٔ همهٔ
زوج‌های $\tuple{x, y}$ را تشکیل دهیم که در آنها $x \in A$ و $y \in B$.
به‌ویژه، $A^{2}= A \times A$ مجموعهٔ همهٔ زوج‌های مرتب از~$A$ است.
```

Replace اعضا with مؤلفه‌ها for the ordered positions, directly witnessed in C14. This prevents confusing order of coordinates with ordering members of a set representation. Preserve the unequal-coordinate antecedent, reverse-pair inequality, unordered-pair contrast, both product factors and A squared. The local preceding a != b condition supplies the two-element contrast; no claim that every unordered pair has size two is added.

Alternatives: اعضا mirrors the English loosely; مؤلفه‌ها is more precise for pair positions. ضرب دکارتی is retained from the prior section; these pages attest the product construction and حاصلضرب, not an exclusive compound spelling.

## FA-0012-C04: Less-than graph and biconditional

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0090, FA-OL-CANON-0003:P0023.

Source:
```latex
Now we will consider a particular relation on a set: the $<$-relation
on the set~$\Nat$ of natural numbers. Consider the set of all pairs of
numbers $\tuple{n, m}$ where $n<m$, i.e.,
\[
  R=\Setabs{\tuple{n, m}}{n, m \in \Nat \text{ and } n<m}.
\]
There is a close connection between $n$ being less than $m$, and the
pair $\tuple{n, m}$ being a member of $R$, namely:
\[
      n<m\text{ iff }\tuple{n, m} \in R.
\]
Indeed, without any loss of information, we can consider the set $R$
to \emph{be} the $<$-relation on $\Nat$.
```

Reviewed Persian:
```latex
اکنون رابطه‌ای خاص روی یک مجموعه را در نظر می‌گیریم: رابطهٔ $<$ روی
مجموعهٔ~$\Nat$ از اعداد طبیعی. مجموعهٔ همهٔ زوج‌های عددی
$\tuple{n, m}$ را در نظر بگیرید که در آنها $n<m$، یعنی
\[
  R=\Setabs{\tuple{n, m}}{n, m \in \Nat \text{ و } n<m}.
\]
میان کوچک‌تر بودن $n$ از $m$ و عضو بودن زوج $\tuple{n, m}$ در $R$
پیوند نزدیکی وجود دارد؛ دقیقاً:
\[
      n<m\text{ اگر و تنها اگر }\tuple{n, m} \in R.
\]
در واقع، بی‌آنکه هیچ اطلاعاتی از دست برود، می‌توانیم مجموعهٔ $R$ را
\emph{همان} رابطهٔ $<$ روی $\Nat$ در نظر بگیریم.
```

The set-builder conjunction و is and, not or. اگر و تنها اگر is iff, not implication. Both formulas, n/m order and Nat domain remain exact; representing a binary predicate by its extension loses no information once that domain is fixed.

Alternatives: Reading ordered pairs in reverse would represent greater-than instead.

## FA-0012-C05: Conversely, every subset gives a relation

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0090.

Source:
```latex
In the same way we can construct a subset of $\Nat^{2}$ for any
relation between numbers. Conversely, given any set of pairs of
numbers $S \subseteq \Nat^{2}$, there is a corresponding relation
between numbers, namely, the relationship $n$ bears to $m$ if and only
if $\tuple{n, m} \in S$. This justifies the following definition:
\end{explain}
```

Reviewed Persian:
```latex
به همین شیوه می‌توانیم برای هر رابطه‌ای میان اعداد، زیرمجموعه‌ای از
$\Nat^{2}$ بسازیم. برعکس، با داشتن هر مجموعهٔ $S \subseteq \Nat^{2}$
از زوج‌های عددی، رابطه‌ای متناظر میان اعداد وجود دارد: رابطه‌ای که
میان $n$ و $m$ برقرار است اگر و تنها اگر $\tuple{n, m} \in S$. این نکته تعریف
زیر را توجیه می‌کند:
\end{explain}
```

Both directions of the graph correspondence remain, with S subset Nat squared and pair membership iff the relation. No definability restriction is added: the source explicitly quantifies over any subset.

Alternatives: No material alternative recorded; none invented.

## FA-0012-C06: Binary relation terminology and notation

Action: correct; confidence 3/3: Exact native binary-relation term and its set-product definition agree with the source specialization.
Canon: FA-OL-CANON-0005:P0090, FA-OL-CANON-0003:P0014.

Source:
```latex
\begin{defn}[Binary relation] 
A \emph{binary relation} on a set $A$ is a subset of~$A^{2}$. If $R
\subseteq A^{2}$ is a binary relation on~$A$ and $x, y \in A$, we
sometimes write $Rxy$ (or $xRy$) for $\tuple{x, y} \in R$.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[رابطهٔ دوموضعی]
یک \emph{رابطهٔ دوموضعی} روی مجموعهٔ $A$، زیرمجموعه‌ای از~$A^{2}$ است.
اگر $R \subseteq A^{2}$ رابطه‌ای دوموضعی روی~$A$ باشد و $x, y \in A$،
گاه $Rxy$ (یا $xRy$) را به جای $\tuple{x, y} \in R$ می‌نویسیم.
\end{defn}
```

Replace all three دوتایی occurrences within this definition by the exactly attested دوموضعی. F90 defines a binary relation from a to b as a subset of a product; here both domains are A. Preserve Rxy, xRy and ordered-pair membership, and do not add the function uniqueness condition from F90.

Alternatives: دوتایی is a transparent prior variant, not a proved mathematical error. دوموضعی is chosen for direct disciplinary attestation. دوگانی risks confusion with duality.

Expert-review question: This is a bounded definition-level terminology update; future occurrences of binary relation must be checked in context against this rule, not mass-replaced.

## FA-0012-C07: Natural-number matrix

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0090.

Source:
```latex
\begin{ex}
  \ollabel{relations}
The set $\Nat^{2}$ of pairs of natural numbers can be listed in a
2-dimensional matrix like this:
\[
  \begin{array}{ccccc}
  \mathbf{\tuple{ 0,0 }} & \tuple{ 0,1 } &
    \tuple{ 0,2 } & \tuple{ 0,3 } & \ldots\\
  \tuple{ 1,0 } & \mathbf{\tuple{ 1,1 }} &
    \tuple{ 1,2 } & \tuple{ 1,3 } & \ldots\\
  \tuple{ 2,0 } & \tuple{ 2,1 } &
    \mathbf{\tuple{ 2,2 }} & \tuple{ 2,3 } & \ldots\\
  \tuple{ 3,0 } & \tuple{ 3,1 } & \tuple{ 3,2 } &
    \mathbf{\tuple{ 3,3 }} & \ldots\\
  \vdots & \vdots & \vdots & \vdots & \mathbf{\ddots}
  \end{array}
\]
```

Reviewed Persian:
```latex
\begin{ex}
  \ollabel{relations}
مجموعهٔ $\Nat^{2}$ از زوج‌های اعداد طبیعی را می‌توان در یک ماتریس
دوبعدی چنین فهرست کرد:
\[
  \begin{array}{ccccc}
  \mathbf{\tuple{ 0,0 }} & \tuple{ 0,1 } &
    \tuple{ 0,2 } & \tuple{ 0,3 } & \ldots\\
  \tuple{ 1,0 } & \mathbf{\tuple{ 1,1 }} &
    \tuple{ 1,2 } & \tuple{ 1,3 } & \ldots\\
  \tuple{ 2,0 } & \tuple{ 2,1 } &
    \mathbf{\tuple{ 2,2 }} & \tuple{ 2,3 } & \ldots\\
  \tuple{ 3,0 } & \tuple{ 3,1 } & \tuple{ 3,2 } &
    \mathbf{\tuple{ 3,3 }} & \ldots\\
  \vdots & \vdots & \vdots & \vdots & \mathbf{\ddots}
  \end{array}
\]
```

Read the complete array: first coordinate is row, second is column; diagonal entries are bold, all ellipses preserved and zero included. The formula checker protects all array tokens. This checks the mathematical layout specification, not a new RTL PDF rendering.

Alternatives: No material alternative recorded; none invented.

## FA-0012-C08: Diagonal identity and general identity notation

Action: retain_after_fresh_review; confidence 2/3: The mathematical object is exact; the selected pages attest the equality-relation variant rather than the precise noun همانی.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0090.

Source:
```latex
We have put the diagonal, here, in bold, since the subset of $\Nat^2$
consisting of the pairs lying on the diagonal, i.e.,
\[
  \{\tuple{0,0 }, \tuple{ 1,1 }, \tuple{ 2,2 }, \dots\},
  \]
is the \emph{identity relation on}~$\Nat$. (Since the identity
relation is popular, let's define $\Id{A}=\Setabs{\tuple{ x,x }}{x \in
A}$ for any set $A$.)
```

Reviewed Persian:
```latex
در اینجا درایه‌های روی قطر را پررنگ نوشته‌ایم، زیرا زیرمجموعهٔ
$\Nat^2$ متشکل از زوج‌های روی قطر، یعنی
\[
  \{\tuple{0,0 }, \tuple{ 1,1 }, \tuple{ 2,2 }, \dots\},
  \]
\emph{رابطهٔ همانی روی}~$\Nat$ است. (از آنجا که رابطهٔ همانی
پرکاربرد است، تعریف می‌کنیم $\Id{A}=\Setabs{\tuple{ x,x }}{x \in A}$
برای هر مجموعهٔ $A$.)
```

The diagonal is exactly equality of the two coordinates; the listed pairs and general Id(A) formula remain unchanged. رابطهٔ همانی is retained as a descriptive established-edition variant, while the consulted C14 page explicitly says رابطه‌ی تساوی. No identity function with a separate codomain structure is imposed.

Alternatives: رابطه‌ی تساوی is directly witnessed; the exact compound همانی is not attested on the selected pages.

Expert-review question: Keep the glossary distinction between a diagonal relation and an identity function clear when later function sections are reviewed.

## FA-0012-C09: Above-diagonal strict less-than

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0023, FA-OL-CANON-0005:P0090.

Source:
```latex
The subset of all pairs lying above the
diagonal, i.e.,
\[
  L = \{\tuple{ 0,1 },\tuple{ 0,2 },\ldots,\tuple{ 1,2 },
  \tuple{ 1,3 }, \dots, \tuple{ 2,3 }, \tuple{ 2,4 },\ldots\},
\]
is the \emph{less than} relation, i.e., $Lnm$ iff $n<m$.
```

Reviewed Persian:
```latex
زیرمجموعهٔ همهٔ زوج‌های
بالای قطر، یعنی
\[
  L = \{\tuple{ 0,1 },\tuple{ 0,2 },\ldots,\tuple{ 1,2 },
  \tuple{ 1,3 }, \dots, \tuple{ 2,3 }, \tuple{ 2,4 },\ldots\},
\]
رابطهٔ \emph{کوچک‌تر از} است؛ یعنی $Lnm$ اگر و تنها اگر $n<m$.
```

For the printed matrix, above-diagonal positions have row n less than column m. Every explicit L pair satisfies that criterion. کوچک‌تر از preserves the direction and strict inequality. No RTL mirroring of the mathematical array is authorized.

Alternatives: No material alternative recorded; none invented.

## FA-0012-C10: Below-diagonal strict greater-than

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0023, FA-OL-CANON-0005:P0090.

Source:
```latex
The subset of
pairs below the diagonal, i.e.,
\[
  G=\{ \tuple{ 1,0 },\tuple{ 2,0 },\tuple{
    2,1 }, \tuple{ 3,0 },\tuple{ 3,1 },\tuple{ 3,2 }, \dots\},
\]
is the \emph{greater than} relation, i.e., $Gnm$ iff $n>m$.
```

Reviewed Persian:
```latex
زیرمجموعهٔ زوج‌های پایین قطر، یعنی
\[
  G=\{ \tuple{ 1,0 },\tuple{ 2,0 },\tuple{
    2,1 }, \tuple{ 3,0 },\tuple{ 3,1 },\tuple{ 3,2 }, \dots\},
\]
رابطهٔ \emph{بزرگ‌تر از} است؛ یعنی $Gnm$ اگر و تنها اگر $n>m$.
```

Every explicit G pair has first coordinate greater than second. The Persian بزرگ‌تر از and the Gnm iff n>m clause match. Above and below refer to the unchanged array, not text flow.

Alternatives: No material alternative recorded; none invented.

## FA-0012-C11: Weak orders: disclose what I denotes

Action: correct; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0003:P0023, FA-OL-CANON-0005:P0090.

Source:
```latex
The union
of $L$ with $I$, which we might call $K=L\cup I$, is the \emph{less
than or equal to} relation: $Knm$ iff $n \le m$. Similarly, $H=G \cup
I$ is the \emph{greater than or equal to relation.}
```

Reviewed Persian:
```latex
اجتماع $L$ با $I$\footnote{یادداشت ویراستاری: منظور از این نماد، همان رابطهٔ همانی روی اعداد طبیعی است که از زوج‌های روی قطر تشکیل می‌شود؛ متن مبدأ در این مثال این نام‌گذاری را صریح نکرده است.} را که می‌توانیم آن را $K=L\cup I$ بنامیم، رابطهٔ
\emph{کوچک‌تر یا مساوی} می‌نامیم: $Knm$ اگر و تنها اگر $n \le m$.
به همین ترتیب، $H=G \cup I$ \emph{رابطهٔ بزرگ‌تر یا مساوی} است.
```

The frozen source defines the diagonal and Id(A) but then uses bare I in two unions without explicitly assigning that name. Add a visibly labelled editorial footnote at its first occurrence: I is that same natural-number diagonal identity relation. Keep all original formulas, including K=L union I and H=G union I, in the same order. This is notation clarification, not a claimed transcription error or a source silently rewritten.

Alternatives: Leaving I wholly implicit obscures the example. Replacing every I by Id(Nat) would alter the frozen formulas; the annotation preserves them.

## FA-0012-C12: Irreflexive versus not reflexive; strict orders

Action: correct; confidence 3/3: The native term and its explicit universal formula exactly match the source; the retained strict-order compound has a separately disclosed lexical limit.
Canon: FA-OL-CANON-0003:P0023.

Source:
```latex
These relations
$L$, $G$, $K$, and $H$ are special kinds of relations called
\emph{orders}. $L$ and $G$ have the property that no number bears $L$
or $G$ to itself (i.e., for all $n$, neither $Lnn$ nor $Gnn$).
Relations with this property are called \emph{irreflexive}, and, if
they also happen to be orders, they are called \emph{strict orders.}
\end{ex}
```

Reviewed Persian:
```latex
این
روابط $L$، $G$، $K$ و $H$ انواع خاصی از روابط‌اند که \emph{ترتیب}
نامیده می‌شوند. $L$ و $G$ این ویژگی را دارند که هیچ عددی با خودش در
رابطهٔ $L$ یا $G$ نیست (یعنی برای هر $n$، نه $Lnn$ برقرار است و نه
$Gnn$). روابط دارای این ویژگی \emph{پادبازتابی} نامیده می‌شوند و اگر
درعین‌حال ترتیب نیز باشند، \emph{ترتیب اکید} نام دارند.
\end{ex}
```

Keep the broader OLP orders category for L,G,K,H even though C23 initially defines orders strictly. Change غیربازتابی to پادبازتابی, attested beside forall x not xrx. The source says no number bears the relation to itself, not merely that at least one number lacks a loop. ترتیب اکید is a transparent retained edition term for the strict case; the exact compound is not on this canon page.

Alternatives: Merely not reflexive means existence of a missing diagonal pair; a relation with one present and one absent loop is not reflexive but is not irreflexive.

Expert-review question: Future property definitions should use the same پادبازتابی distinction; verify exact اکید usage in the later order canon rather than inventing an attestation.

## FA-0012-C13: Arbitrary, empty and universal relations

Action: retain_after_fresh_review; confidence 2/3: Definitions and domain scope are exact; the selected scholarly passages do not directly witness all three compound labels.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0090, FA-OL-CANON-0003:P0023.

Source:
```latex
\begin{explain}
Although orders and identity are important and natural relations, it
should be emphasized that according to our definition \emph{any}
subset of $A^{2}$ is a relation on~$A$, regardless of how unnatural or
contrived it seems. In particular, $\emptyset$ is a relation on any
set (the \emph{empty relation}, which no pair of elements bears), and
$A^{2}$~itself is a relation on~$A$ as well (one which every pair
bears), called the \emph{universal relation}. But also something like
$E=\Setabs{\tuple{n, m}}{n>5 \text{ or } m \times n \ge 34}$ counts as
a relation.
\end{explain}
```

Reviewed Persian:
```latex
\begin{explain}
گرچه ترتیب‌ها و رابطهٔ همانی روابطی مهم و طبیعی‌اند، باید تأکید کرد
که بنا بر تعریف ما، \emph{هر} زیرمجموعهٔ $A^{2}$ رابطه‌ای روی~$A$ است،
هرقدر هم غیرطبیعی یا ساختگی به نظر برسد. به‌ویژه، $\emptyset$ روی هر
مجموعه‌ای یک رابطه است (\emph{رابطهٔ تهی} که هیچ زوجی آن را ندارد)،
و خودِ~$A^{2}$ نیز رابطه‌ای روی~$A$ است (رابطه‌ای که هر زوجی آن را
دارد) و \emph{رابطهٔ جهان‌شمول} نامیده می‌شود. حتی چیزی مانند
$E=\Setabs{\tuple{n, m}}{n>5 \text{ یا } m \times n \ge 34}$ نیز یک
رابطه به شمار می‌آید.
\end{explain}
```

The definition permits every subset, not just natural-looking or definable relations. Empty relation contains no ordered pairs; universal relation contains every pair of A elements. Preserve the final contrived number-relation formula and its disjunction یا. Its n,m inherit the number-example context; no new all-sets domain is asserted. The exact compounds رابطهٔ تهی and رابطهٔ جهان‌شمول are descriptive retained variants not attested on these selected pages.

Alternatives: Conflating the universal relation with an all-sets membership relation would be wrong.

Expert-review question: A fuller relation-specific terminology canon may supply exact empty/universal compounds. Keep these semantic matches provisional without claiming exact lexical attestation.

## FA-0012-C14: Power-set inclusion exercise

Action: retain_after_fresh_review; confidence 3/3: The exact source content and relevant native mathematical passage were compared; remaining limitations are stated in the rationale.
Canon: FA-OL-CANON-0003:P0010, FA-OL-CANON-0005:P0090.

Source:
```latex
\begin{prob}
  List the !!{element}s of the relation $\subseteq$ on the set
  $\Pow{\{a, b, c\}}$.
\end{prob}
```

Reviewed Persian:
```latex
\begin{prob}
  !!{element}s رابطهٔ $\subseteq$ روی مجموعهٔ
  $\Pow{\{a, b, c\}}$ را فهرست کنید.
\end{prob}
```

Retain the exercise, inclusive subset relation and full power-set argument. Its elements are ordered pairs of subsets, not simply the three alphabet objects. C10 supplies subset direction and F90 supplies products/power sets. The private deterministic check obtains 27 qualifying pairs for three distinct symbols; this does not insert a solution into the reader.

Alternatives: No material alternative recorded; none invented.

## Validation boundary

Every substantive source and target character lies in an ordered non-overlapping reviewed span. Formal tokens are checked across inline, bracketed, multline and align mathematics. Text arguments in mathematics are separately aligned and manually reviewed for exact connective, quantifier and number-family meaning.
Finite tests support the written reasoning; they are not universal formal proofs. No new PDF was built or visually certified. Frozen owner inputs and reader releases are unchanged; corrections enter the owner’s normal next-batch build and visual QA.
Attribution: Open Logic Project and contributors, under existing CC BY 4.0 notices. https://github.com/OpenLogicProject/OpenLogic . Existing edition: https://github.com/KokunoYumeto/OpenLogic-fa-ir . Canon sources retain separate rights.
