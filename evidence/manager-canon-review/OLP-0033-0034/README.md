# Persian OpenLogic: nonenumerability and reduction

Complete retrospective source/canon review of OLP-0033 and0034, with seven complete Persian scholarly pages directly consulted. Every substantive source and target span is mapped. An independent source-only audit checks all three proofs and nine exercises; it is not independent Persian or human certification. Candidates are reader-production inputs, not a new reader release.

## Review priorities

- Add the missing nonempty-set restriction to the enumeration criterion, without changing the two valid theorems.
- Correct the finite-string example into an explicitly infinite constant-zero sequence; remove a stray characteristic-sequence subscript.
- Preserve every reduction arrow, diagonal index and quantifier; all functions means all functions, not only computable ones.
- Record unattested exact reduction/diagonalization labels honestly, while grounding syntax and meanings in the actually read mathematical canon.
- Confidence is editorial 0-3, not calibrated probability. Human review is a later opportunity, not a gate.

## Scholarly pages actually consulted

- نظریهٔ مجموعه‌ها; محسن خانی, افشین زارعی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/jozve-kamel.pdf). PDF SHA-256: dbd518c80232921264ab5d79b79be01fe42efe8c01a766327db248b2d261de04. Canon PDFs are privately retained, not redistributed.
- مبانی منطق و نظریهٔ مجموعه‌ها; محسن خانی; دانشگاه صنعتی اصفهان. [Source](https://mohsen-khani.github.io/logic97-1/jozve/logic-full.pdf). PDF SHA-256: 565558b76701858236844f19663de27ee10a8d72fd8b007e69b85159ac49f86d. Canon PDFs are privately retained, not redistributed.
- منطق ریاضی; محسن خانی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/chapter2_0.pdf). PDF SHA-256: 0f3fb75ed1fcb0cbc669c04493acf520888e1ebfd62795bb28fc510bc41c7e79. Canon PDFs are privately retained, not redistributed.
- ریاضیات گسسته و کاربردها; علیرضا غفاری حدیقه, مگردیچ تومانیان; مؤسسه چاپ و انتشارات دانشگاه جامع امام حسین (ع). [Source](https://hadigheha.github.io/books/teaching/Textbooks/Tarkibiyat.pdf). PDF SHA-256: 8f79c45a926c1cea819c4fefa86383f2a65ae23b1d526baaf99cf2506bb9f317. Canon PDFs are privately retained, not redistributed.
- FA-OL-CANON-0003:P0051, PDF 51, printed 50: Lemma6: injection, surjection and empty-domain exception. Direct cardinal comparison and inverse-on-image syntax, with an explicit empty-set alternative. The page also uses Choice for a general reverse selection; our enumerated-index construction needs no such family of choices. Do not import the visible notation slips.
- FA-OL-CANON-0003:P0053, PDF 53, printed 52: Definition10 and Cantor theorem13. Direct enumeration and Cantor diagonal membership argument. This source reserves شمارا for countably infinite; OpenLogic includes finite/empty. Retain the chapter’s disclosed inclusive convention. The exact label روش قطری is not printed here.
- FA-OL-CANON-0005:P0114, PDF 114, printed 114: Cardinals, definition262 and choice-sensitive comparison. Direct uncountable terminology and explicit distinction from finite/countably infinite, with cardinal comparison using injections. Exact OLP enumerable convention is governed by OLP, not silently replaced by a different convention.
- FA-OL-CANON-0005:P0115, PDF 115, printed 115: Cantor theorem263 and subset/binary-function correspondence. Direct diagonal nonmembership contradiction and correspondence between subsets and binary-valued functions. This supports set-versus-sequence and coordinate language, not a claim that binary real expansions are unique.
- FA-OL-CANON-0001:P0082, PDF 82, printed 81: Algorithm inputs, outputs, halting and possible undefined output. Direct contrast: an algorithm may not halt, and an effective presentation is an additional condition. OLP here quantifies over all set-theoretic functions; no algorithm or decidable-domain requirement is added. Exact تابع جزئی and reduction terminology are not attested on this page.
- FA-REL-P046, PDF 46, printed 36: Function-kind definitions and direction diagrams. Each target has at least one preimage versus at most one; apply contextually to each reduction arrow.
- FA-REL-P050, PDF 50, printed 40: Function composition and inverse of bijection. Direct composition and inverse syntax; an injection has a unique inverse only on its image. Reduction combines the actual enumeration with a function in the specified direction.

## FA-0033-C01: Uncountable sets heading

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0114, FA-OL-CANON-0003:P0053.

Source:
```latex
\olsection{\printtoken{S}{nonenumerable} Sets}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{مجموعه‌های ناشمارا}
```

ناشمارا is directly attested. The chapter’s شمارا includes finite and empty cases; no terminology-based restriction to infinite enumerable sets.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C02: Edition-level editorial comparison

Action: correct; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{editorial}
  This section proves the non-enumerability of $\Bin^\omega$ and
  $\Pow{\PosInt}$ using the definition in \olref[enm]{sec}. It is
  designed to be a little more elementary and a little more detailed
  than the version in \olref[enm-alt]{sec}
\end{editorial}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{editorial}
  این بخش ناشمارابودنِ $\Bin^\omega$ و $\Pow{\PosInt}$ را با استفاده
  از تعریفِ \olref[enm]{sec} ثابت می‌کند. این بخش طوری
  تنظیم شده است که اندکی مقدماتی‌تر و اندکی مشروح‌تر از روایتِ
  \olref[enm-alt]{sec} باشد.
\end{editorial}
```

Preserve all three source cross-reference roles: definitions in enm and the less elementary alternative enm-alt. Add the missing full stop; no omitted editorial metadata.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C03: Infinite sets and nonenumerability

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0114.

Source:
```latex
Some sets, such as the set $\PosInt$ of positive integers, are
infinite. So far we've seen examples of infinite sets which were all
!!{enumerable}. However, there are also infinite sets which do not
have this property. Such sets are called \emph{!!{nonenumerable}}.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
برخی مجموعه‌ها، مانند مجموعهٔ~$\PosInt$ از اعداد صحیح مثبت،
نامتناهی‌اند. تاکنون نمونه‌هایی از مجموعه‌های نامتناهی دیده‌ایم که همگی
شمارا بوده‌اند. بااین‌حال، مجموعه‌های نامتناهی‌ای نیز وجود دارند
که این ویژگی را ندارند. چنین مجموعه‌هایی را \emph{ناشمارا}
می‌نامند.
```

Retain the contrast between infinite enumerable examples and infinite nonenumerable sets. Infinite does not itself mean uncountable. Positive integers and Nat remain distinct.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C04: Enumeration criterion needs nonempty domain

Action: correct; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0051, FA-REL-P046, FA-OL-CANON-0005:P0114.

Source:
```latex
First of all, it is perhaps already surprising that there are
!!{nonenumerable} sets.  For any !!{enumerable} set~$A$ there is
!!a{surjective} function $f \colon \PosInt \to A$.  If a set is
!!{nonenumerable} there is no such function.  That is, no function
mapping the infinitely many !!{element}s of~$\PosInt$ to~$A$ can
exhaust all of~$A$.  So there are ``more'' !!{element}s of~$A$ than
the infinitely many positive integers.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
پیش از هر چیز، شاید همین وجود مجموعه‌های ناشمارا شگفت‌آور
باشد. برای هر مجموعهٔ ناتهی و شمارا مانند~$A$ تابعی پوشا
به‌صورت $f \colon \PosInt \to A$ وجود دارد. اگر مجموعه‌ای
ناشمارا باشد، چنین تابعی وجود ندارد. یعنی هیچ تابعی که
اعضا را از مجموعهٔ نامتناهیِ~$\PosInt$ به~$A$ نگاشت کند،
نمی‌تواند همهٔ~$A$ را فراگیرد. پس شمارِ اعضا در~$A$ از شمار
بی‌نهایت عدد صحیح مثبت نیز «بیشتر» است.
```

Repair the source’s unrestricted claim by adding nonempty to the enumerable target A. No map from positive integers to empty exists. Preserve the valid negative implication and the source’s explicitly informal “more” comparison.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C05: Diagonal method and empty-set disclosure

Action: correct; confidence 2/3: Editorial0–3, not calibrated probability. Source meaning checked; the stated exact-label or register attestation gap remains.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115, FA-REL-P046.

Source:
```latex
How would one prove that a set is !!{nonenumerable}? You have to show
that no such surjective function can exist. Equivalently, you have to
show that the elements of~$A$ cannot be enumerated in a one way
infinite list.  The best way to do this is to show that every list of
!!{element}s of~$A$ must leave at least one element out; or that no
function $f\colon \PosInt \to A$ can be !!{surjective}.  We can do this
using Cantor's \emph{diagonal method}.  Given a list of !!{element}s
of~$A$, say, $x_1$, $x_2$, \dots, we construct another element of~$A$
which, by its construction, cannot possibly be on that list.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
چگونه می‌توان ثابت کرد که مجموعه‌ای ناتهی ناشمارا است؟ باید نشان
دهید که هیچ تابع پوشایی از این نوع وجود ندارد.
\emph{یادداشت ویراستاری:} شرط ناتهی‌بودن در بیان اولیهٔ این معیار نیامده بود.
مجموعهٔ تهی طبق تعریف این فصل شماراست، با آنکه هیچ تابعی از اعداد صحیح مثبت
به آن وجود ندارد؛ پس این شرط در معیار بالا ضروری است.

 به‌طور
هم‌ارز، باید نشان دهید که نمی‌توان عناصر~$A$ را در فهرستی نامتناهی و
یک‌سویه برشمرد. بهترین راه برای این کار آن است که نشان دهید هر فهرستی
از اعضای~$A$ ناگزیر دست‌کم یک عضو را از قلم می‌اندازد؛ یا
اینکه هیچ تابع $f\colon \PosInt \to A$ نمی‌تواند پوشا باشد.
می‌توانیم این کار را با \emph{روش قطری} کانتور انجام دهیم. با داشتن
فهرستی از اعضای~$A$، مثلاً $x_1$، $x_2$، \dots، عضو دیگری
از~$A$ می‌سازیم که بنا بر نحوهٔ ساختش، به‌هیچ‌وجه نمی‌تواند در آن
فهرست باشد.
```

State the exclusion-of-surjections method for nonempty A and disclose the source correction. Empty is enumerable by the source definition, not a counterexample to either theorem. Smooth اعضایی از to اعضای while preserving all-list quantification and witness membership in A.

Alternatives: Argument by diagonal nonmembership is directly illustrated by the canon; no fabricated exact-label attestation is supplied.

Expert-review question: روش قطری is a contextual label for the exact source-defined construction; the consulted pages attest the construction, not that exact phrase.

## FA-0033-C06: Infinite binary sequences have every coordinate

Action: correct; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115.

Source:
```latex
Our first example is the set~$\Bin^\omega$ of all infinite, non-gappy
sequences of $0$'s and $1$'s.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
نخستین مثال ما مجموعهٔ~$\Bin^\omega$ از همهٔ دنباله‌های نامتناهیِ
$0$ها و $1$هاست که در هر جایگاه مقداری دارند.
```

Replace literal بدون شکاف with the precise readable meaning: every position has a value. No finite-string, finite-support or computability restriction.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C07: First theorem statement

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0114, FA-OL-CANON-0005:P0115.

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

Keep Bin^omega and nonenumerability, including theorem label. The constant-zero sequence witnesses the implicit nonemptiness needed by the criterion.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C08: Contradiction assumption and row/coordinate names

Action: correct; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115, FA-OL-CANON-0003:P0053.

Source:
```latex
\begin{proof}
Suppose, by way of contradiction, that $\Bin^\omega$ is
!!{enumerable}, i.e., suppose that there is a list $s_{1}$, $s_{2}$,
$s_{3}$, $s_{4}$, \dots{} of all !!{element}s of~$\Bin^\omega$.  Each
of these $s_i$ is itself an infinite sequence of $0$'s and~$1$'s.
Let's call the $j$-th element of the $i$-th sequence in this list
$s_i(j)$. Then the $i$-th sequence~$s_i$ is
\[
s_i(1), s_i(2), s_i(3), \dots
\]
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
برای برهان خلف، فرض کنید $\Bin^\omega$ شمارا است؛ یعنی فرض کنید
$s_{1}$، $s_{2}$، $s_{3}$، $s_{4}$، \dots{} فهرستی است که همهٔ
اعضا را از~$\Bin^\omega$ در بر می‌گیرد. هر $s_i$ خود دنباله‌ای
نامتناهی از $0$ها و~$1$هاست. عضو $j$اُمِ دنبالهٔ $i$اُم در این فهرست
را $s_i(j)$ می‌نامیم. پس دنبالهٔ $i$اُم، یعنی~$s_i$، چنین است:
\[
s_i(1), s_i(2), s_i(3), \dots
\]
```

Use natural برهان خلف. Preserve all-sequences assumption, repeated rows permitted, and i=row versus j=position. The displayed infinite sequence is not reversed for RTL.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C09: Binary matrix

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115.

Source:
```latex
We may arrange this list, and the elements of each sequence $s_i$ in
it, in an array:
\[
\begin{array}{c|c|c|c|c|c}
& 1 & 2 & 3 & 4 & \dots \\\hline
1 & \mathbf{s_{1}(1)} & s_{1}(2) & s_{1}(3) & s_1(4) & \dots \\\hline
2 & s_{2}(1)& \mathbf{s_{2}(2)} & s_2(3) & s_2(4) & \dots \\\hline
3 & s_{3}(1)& s_{3}(2) & \mathbf{s_3(3)} & s_3(4) & \dots \\\hline
4 & s_{4}(1)& s_{4}(2) & s_4(3) & \mathbf{s_4(4)} & \dots \\\hline
\vdots & \vdots & \vdots & \vdots & \vdots & \mathbf{\ddots}
\end{array}
\]
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
می‌توانیم این فهرست و اعضای هر دنبالهٔ $s_i$ در آن را در آرایه‌ای
مرتب کنیم:
\[
\begin{array}{c|c|c|c|c|c}
& 1 & 2 & 3 & 4 & \dots \\\hline
1 & \mathbf{s_{1}(1)} & s_{1}(2) & s_{1}(3) & s_1(4) & \dots \\\hline
2 & s_{2}(1)& \mathbf{s_{2}(2)} & s_2(3) & s_2(4) & \dots \\\hline
3 & s_{3}(1)& s_{3}(2) & \mathbf{s_3(3)} & s_3(4) & \dots \\\hline
4 & s_{4}(1)& s_{4}(2) & s_4(3) & \mathbf{s_4(4)} & \dots \\\hline
\vdots & \vdots & \vdots & \vdots & \vdots & \mathbf{\ddots}
\end{array}
\]
```

Keep every matrix cell, diagonal bolding and column/row ordering. The canon’s subset/binary sequence correspondence supports distinguishing entries from their positions.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C10: Matrix axis meaning

Action: correct; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115.

Source:
```latex
The labels down the side give the number of the sequence in the list
$s_1$, $s_2$, \dots; the numbers across the top label the !!{element}s
of the individual sequences. For instance, $s_{1}(1)$ is a name for
whatever number, a $0$ or a~$1$, is the first !!{element} in the
sequence $s_{1}$, and so on.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
برچسب‌های کنار آرایه شمارهٔ دنباله‌ها را در فهرستِ $s_1$، $s_2$،
\dots مشخص می‌کنند؛ اعداد بالای آرایه، شمارهٔ جایگاه اعضا را در هر
دنباله نشان می‌دهند. برای نمونه، $s_{1}(1)$ نامِ عددی،
یعنی یک $0$ یا یک~$1$، است که نخستین عضو در دنبالهٔ $s_{1}$
است؛ و به همین ترتیب.
```

Say column labels number the positions, not the 0/1 values. Replace “to the end” for an infinite sequence with “and likewise”; preserve all individual formula occurrences.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C11: Diagonal depends on the given list

Action: correct; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
Now we construct an infinite sequence, $\overline{s}$, of $0$'s and
$1$'s which cannot possibly be on this list.  The definition of
$\overline{s}$ will depend on the list $s_1$, $s_2$, \dots.  Any
infinite list of infinite sequences of $0$'s and $1$'s gives rise to
an infinite sequence~$\overline{s}$ which is guaranteed to not appear
on the list.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
اکنون دنبالهٔ نامتناهیِ $\overline{s}$ را از $0$ها و $1$ها می‌سازیم؛
دنباله‌ای که به‌هیچ‌وجه نمی‌تواند در این فهرست باشد. تعریف
$\overline{s}$ به فهرستِ $s_1$، $s_2$، \dots وابسته خواهد بود. هر
فهرست نامتناهی از دنباله‌های نامتناهیِ $0$ها و $1$ها، دنباله‌ای
نامتناهی مانند~$\overline{s}$ به دست می‌دهد که در آن فهرست نیست.
```

Retain dependence on each arbitrary list, not a single fixed sequence omitted by every possible list. Replace the passive guarantee calque with direct statement of omission.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C12: Pointwise complement rule

Action: correct; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115, FA-OL-CANON-0001:P0082.

Source:
```latex
To define $\overline{s}$, we specify what all its !!{element}s are,
i.e., we specify $\overline{s}(n)$ for all $n \in \PosInt$.  We do this
by reading down the diagonal of the array above (hence the name
``diagonal method'') and then changing every $1$ to a $0$ and every
$0$ to a~$1$. More abstractly, we define $\overline{s}(n)$ to be $0$
or $1$ according to whether the $n$-th !!{element} of the diagonal,
$s_n(n)$, is $1$ or $0$.
\[
\overline{s}(n) =
\begin{cases}
1 & \text{if $s_{n}(n) = 0$}\\
0 & \text{if $s_{n}(n) = 1$}.
\end{cases}
\]
If you like formulas better than definitions by cases, you could also
define $\overline{s}(n) = 1 - s_n(n)$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
برای تعریف $\overline{s}$، مقدار آن را در هر جایگاه مشخص می‌کنیم؛
یعنی $\overline{s}(n)$ را برای همهٔ $n \in \PosInt$ تعیین می‌کنیم.
برای این کار قطر آرایهٔ بالا را از بالا به پایین می‌خوانیم (نام «روش
قطری» نیز از همین‌جا می‌آید) و سپس هر $1$ را به $0$ و هر $0$ را به~$1$
تغییر می‌دهیم. به‌بیان انتزاعی‌تر، $\overline{s}(n)$ را برابر $0$ یا
$1$ تعریف می‌کنیم، بسته به اینکه عضو $n$اُمِ قطر، یعنی
$s_n(n)$، برابر $1$ یا $0$ باشد.
\[
\overline{s}(n) =
\begin{cases}
1 & \text{اگر $s_{n}(n) = 0$}\\
0 & \text{اگر $s_{n}(n) = 1$}.
\end{cases}
\]
اگر فرمول‌ها را بر تعریف موردی ترجیح می‌دهید، می‌توانید
$\overline{s}(n) = 1 - s_n(n)$ را نیز به‌عنوان تعریف به کار ببرید.
```

Specify value at every position by one mathematical rule, not an implied terminating process visiting infinitely many positions. Preserve cases, embedded if clauses, n positivity and equivalent 1-s_n(n) formula. No computability is asserted.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C13: Complement is bitwise, not reversed order

Action: correct; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115.

Source:
```latex
Clearly $\overline{s}$ is an infinite sequence of $0$'s and
$1$'s, since it is just the mirror sequence to the sequence of $0$'s
and $1$'s that appear on the diagonal of our array.  So $\overline{s}$
is !!a{element} of~$\Bin^\omega$.  But it cannot be on the list $s_1$,
$s_2$, \dots{} Why not?
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
آشکارا $\overline{s}$ دنباله‌ای نامتناهی از $0$ها و $1$هاست، زیرا
در دنبالهٔ روی قطر آرایه، تک‌تکِ مقدارهای $0$ و $1$ را با مقدار مقابلشان
عوض کرده‌ایم. پس $\overline{s}$ عضوی از~$\Bin^\omega$ است.
اما نمی‌تواند در فهرستِ $s_1$، $s_2$، \dots{} باشد. چرا؟
```

Explain the bit swap rather than leave مکمل open to interpretation as order reversal. Retain membership in Bin^omega, restore natural singular عضوی via verified locale token.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C14: First and second omitted rows

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115.

Source:
```latex
It can't be the first sequence in the list, $s_1$, because it differs from
$s_1$ in the first !!{element}.  Whatever $s_1(1)$ is, we defined
$\overline{s}(1)$ to be the opposite.  It can't be the second
sequence in the list, because $\overline{s}$ differs from $s_2$ in the second
element: if $s_2(2)$ is $0$, $\overline{s}(2)$ is $1$, and vice
versa. And so on.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
این دنباله نمی‌تواند نخستین دنبالهٔ فهرست، یعنی $s_1$، باشد، زیرا در
نخستین عضو با $s_1$ تفاوت دارد. مقدار $s_1(1)$ هرچه باشد،
$\overline{s}(1)$ را مخالف آن تعریف کرده‌ایم. همچنین نمی‌تواند دومین
دنبالهٔ فهرست باشد، زیرا $\overline{s}$ در عضو دوم با $s_2$ تفاوت
دارد: اگر $s_2(2)$ برابر $0$ باشد، $\overline{s}(2)$ برابر $1$ است و
برعکس. همین استدلال ادامه می‌یابد.
```

Check both binary cases and both diagonal positions. Preserve the informal examples and the transition to universal k, not a finite-evidence proof.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C15: Universal diagonal contradiction

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
More precisely: if $\overline{s}$ were on the list, there would be
some $k$ so that $\overline{s} = s_{k}$.  Two sequences are identical
iff they agree at every place, i.e., for any~$n$, $\overline{s}(n) =
s_{k}(n)$.  So in particular, taking $n = k$ as a special case,
$\overline{s}(k) = s_{k}(k)$ would have to hold. $s_k(k)$ is either
$0$ or~$1$. If it is $0$ then $\overline{s}(k)$ must be~$1$---that's
how we defined $\overline{s}$. But if $s_k(k) = 1$ then, again because
of the way we defined $\overline{s}$, $\overline{s}(k) = 0$. In either
case $\overline{s}(k) \neq s_{k}(k)$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
دقیق‌تر بگوییم: اگر $\overline{s}$ در فهرست بود، عددی مانند $k$ وجود
داشت که $\overline{s} = s_{k}$. دو دنباله یکسان‌اند اگر و تنها اگر در
هر جایگاه برابر باشند؛ یعنی برای هر~$n$، $\overline{s}(n) =
s_{k}(n)$. پس به‌ویژه، با گرفتن حالت خاصِ $n = k$، باید
$\overline{s}(k) = s_{k}(k)$ برقرار باشد. $s_k(k)$ یا $0$ است یا~$1$.
اگر $0$ باشد، $\overline{s}(k)$ باید~$1$ باشد---زیرا $\overline{s}$
را چنین تعریف کردیم. اما اگر $s_k(k) = 1$ باشد، باز هم به‌سبب نحوهٔ
تعریف $\overline{s}$، داریم $\overline{s}(k) = 0$. در هر دو حالت
$\overline{s}(k) \neq s_{k}(k)$.
```

Keep iff for extensional equality, every n, specialization n=k, both cases and inequality. No quantifier or index reassignment.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C16: Contradiction conclusion for every purported list

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115.

Source:
```latex
We started by assuming that there is a list of !!{element}s of
$\Bin^\omega$, $s_1$, $s_2$, \dots{} From this list we constructed a
sequence~$\overline{s}$ which we proved cannot be on the list.  But it
definitely is a sequence of $0$'s and $1$'s if all the $s_i$ are
sequences of $0$'s and $1$'s, i.e., $\overline{s} \in
\Bin^\omega$. This shows in particular that there can be no list of
\emph{all} !!{element}s of~$\Bin^\omega$, since for any such list we
could also construct a sequence~$\overline{s}$ guaranteed to not be on
the list, so the assumption that there is a list of all sequences
in~$\Bin^\omega$ leads to a contradiction.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
کار را با این فرض آغاز کردیم که فهرستی از اعضا در
$\Bin^\omega$، یعنی $s_1$، $s_2$، \dots{}، وجود دارد. از این فهرست
دنبالهٔ~$\overline{s}$ را ساختیم و ثابت کردیم که نمی‌تواند در فهرست
باشد. بااین‌حال، این نیز بی‌تردید دنباله‌ای از $0$ها و $1$هاست، اگر
همهٔ $s_i$ها دنباله‌هایی از $0$ها و $1$ها باشند؛ یعنی $\overline{s} \in
\Bin^\omega$. این نتیجه به‌ویژه نشان می‌دهد که هیچ
فهرستی از \emph{همهٔ} اعضا در~$\Bin^\omega$ نمی‌تواند وجود داشته
باشد، زیرا از هر فهرست این‌چنینی می‌توانستیم دنبالهٔ~$\overline{s}$ را
بسازیم که تضمین شده است در فهرست نباشد. بنابراین فرض وجود فهرستی از
همهٔ دنباله‌های~$\Bin^\omega$ به تناقض می‌انجامد.
\end{proof}
```

The opening all-element assumption and final contradiction retain the source chain: constructed sequence belongs to the function space yet is not among rows. No generalization from only the pictured rows.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C17: Diagonalization without a visible matrix

Action: retain_after_fresh_review; confidence 2/3: Editorial0–3, not calibrated probability. Source meaning checked; the stated exact-label or register attestation gap remains.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{explain}
This proof method is called ``diagonalization'' because it uses the
diagonal of the array to define~$\overline{s}$. Diagonalization need
not involve the presence of an array: we can show that sets are not
!!{enumerable} by using a similar idea even when no array and no
actual diagonal is involved.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
این روش برهان را «قطری‌سازی» می‌نامند، زیرا برای تعریف~$\overline{s}$
از قطر آرایه استفاده می‌کند. قطری‌سازی لزوماً به وجود آرایه نیاز
ندارد: می‌توانیم با اندیشه‌ای مشابه نشان دهیم که مجموعه‌ها
شمارا نیستند، حتی اگر هیچ آرایه و هیچ قطر واقعی‌ای در میان
نباشد.
\end{explain}
```

Retain the explanation that the construction can work without a literal array; diagonalization denotes the logical pattern, not a demand to draw a table.

Alternatives: No material alternative recorded; none invented.

Expert-review question: قطری‌سازی is transparent and source-defined but not directly printed in these consulted canon pages. Retained provisionally with the exact construction.

## FA-0033-C18: Power-set theorem

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{thm}
\ollabel{thm:nonenum-pownat}
$\Pow{\PosInt}$ is not !!{enumerable}.
\end{thm}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{thm}
\ollabel{thm:nonenum-pownat}
$\Pow{\PosInt}$ شمارا نیست.
\end{thm}
```

Pow of positive integers, not only finite subsets and not the integers themselves. Preserve theorem identity and negative enumeration predicate.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C19: Power-set diagonal definition

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{proof}
We proceed in the same way, by showing that for every list of subsets
of~$\PosInt$ there is a subset of $\PosInt$ which cannot be on the list.
Suppose the following is a given list of subsets of~$\PosInt$:
\[
Z_{1}, Z_{2}, Z_{3}, \dots
\]
We now define a set $\overline{Z}$ such that for any $n \in \PosInt$,
$n \in \overline{Z}$ iff $n \notin Z_{n}$:
\[
\overline{Z} = \Setabs{n \in \PosInt}{n \notin Z_n}
\]
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}
به همان شیوه پیش می‌رویم: نشان می‌دهیم که برای هر فهرستی از زیرمجموعه‌های
~$\PosInt$، زیرمجموعه‌ای از $\PosInt$ وجود دارد که نمی‌تواند در فهرست
باشد. فرض کنید فهرست زیر از زیرمجموعه‌های~$\PosInt$ داده شده است:
\[
Z_{1}, Z_{2}, Z_{3}, \dots
\]
اکنون مجموعه‌ای مانند $\overline{Z}$ چنان تعریف می‌کنیم که برای هر
$n \in \PosInt$، $n \in \overline{Z}$ اگر و تنها اگر $n \notin Z_{n}$:
\[
\overline{Z} = \Setabs{n \in \PosInt}{n \notin Z_n}
\]
```

Given every list of subsets, define the diagonal by n notin Z_n. Explicit bound n in positive integers establishes it is a subset. Retain all equations and tuple order.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C20: Diagonal subset lies in power set

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
$\overline{Z}$ is clearly a set of positive integers, since by
assumption each~$Z_n$ is, and thus $\overline{Z} \in
\Pow{\PosInt}$. But $\overline{Z}$ cannot be on the list.  To show
this, we'll establish that for each $k \in \PosInt$, $\overline{Z} \neq
Z_k$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
$\overline{Z}$ آشکارا مجموعه‌ای از اعداد صحیح مثبت است، زیرا بنا بر
فرض هر~$Z_n$ چنین مجموعه‌ای است، و ازاین‌رو $\overline{Z} \in
\Pow{\PosInt}$. اما $\overline{Z}$ نمی‌تواند در فهرست باشد. برای نشان
دادن این مطلب، ثابت می‌کنیم که برای هر $k \in \PosInt$، $\overline{Z} \neq
Z_k$.
```

Preserve set-of-positive-integers type and membership in its power set; not membership in the integers. Source’s redundant reference to Z_n types is harmless.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C21: Arbitrary k distinguishes two sets

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
So let $k \in \PosInt$ be arbitrary. We've defined $\overline{Z}$ so
that for any $n \in \PosInt$, $n \in \overline{Z}$ iff $n \notin Z_n$.
In particular, taking $n=k$, $k \in \overline{Z}$ iff $k \notin Z_k$.
But this shows that $\overline{Z} \neq Z_k$, since $k$ is !!a{element}
of one but not the other, and so $\overline{Z}$ and $Z_k$ have
different !!{element}s. Since $k$ was arbitrary, $\overline{Z}$ is not
on the list $Z_1$, $Z_2$, \dots
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
پس $k \in \PosInt$ را دلخواه بگیرید. $\overline{Z}$ را چنان تعریف
کرده‌ایم که برای هر $n \in \PosInt$، $n \in \overline{Z}$ اگر و تنها
اگر $n \notin Z_n$. به‌ویژه، با گرفتن $n=k$، داریم $k \in \overline{Z}$
اگر و تنها اگر $k \notin Z_k$. اما این نشان می‌دهد که
$\overline{Z} \neq Z_k$، زیرا $k$ عضو یکی از آن دو است، اما عضو
آن یکی نیست؛ پس $\overline{Z}$ و $Z_k$ از نظر اعضا تفاوت دارند.
ازآنجاکه $k$ دلخواه بود، $\overline{Z}$ در فهرستِ $Z_1$، $Z_2$،
\dots نیست.
\end{proof}
```

Retain iff and nonmembership directions, k arbitrary, and extensional inequality from differing membership. Distinguish an element of one but not the other from subset relation.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C22: Membership table and empty diagonal cells

Action: correct; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{explain}
The preceding proof did not mention a diagonal, but you can think of
it as involving a diagonal if you picture it this way: Imagine the
sets $Z_1$, $Z_2$, \dots, written in an array, where each
!!{element}~$j \in Z_i$ is listed in the~$j$-th column. Say the first
four sets on that list are $\{1,2,3,\dots\}$, $\{2, 4, 6, \dots\}$,
$\{1,2,5\}$, and $\{3,4,5,\dots\}$. Then the array would begin with
\[
\begin{array}{r@{}rrrrrrr}
  Z_1 = \{ & \mathbf{1}, & 2, & 3, & 4, & 5, & 6, & \dots\}\\
  Z_2 = \{ &  & \mathbf{2}, &  & 4, &  & 6, & \dots\}\\
  Z_3 = \{ & 1, & 2, &  &  & 5\phantom{,} &  & \}\\
  Z_4 = \{ &  &  & 3, & \mathbf{4}, & 5, & 6, & \dots\}\\
  \vdots & & & & & \ddots
\end{array}
\]
Then $\overline{Z}$ is the set obtained by going down the diagonal,
leaving out any numbers that appear along the diagonal and include
those $j$ where the array has a gap in the $j$-th row/column. In the
above case, we would leave out $1$ and $2$, include~$3$, leave
out~$4$, etc.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
برهان پیشین از قطر نام نبرد، اما اگر آن را به شکل زیر تصویر کنید،
می‌توانید قطر را در آن ببینید: مجموعه‌های $Z_1$، $Z_2$، \dots را در
آرایه‌ای بنویسید که در آن هر عضو مانند~$j \in Z_i$ در ستون
$j$اُم قرار گیرد. فرض کنید چهار مجموعهٔ نخست در آن فهرست به‌ترتیب
$\{1,2,3,\dots\}$، $\{2, 4, 6, \dots\}$، $\{1,2,5\}$ و
$\{3,4,5,\dots\}$ باشند. در این صورت آرایه چنین آغاز می‌شود:
\[
\begin{array}{r@{}rrrrrrr}
  Z_1 = \{ & \mathbf{1}, & 2, & 3, & 4, & 5, & 6, & \dots\}\\
  Z_2 = \{ &  & \mathbf{2}, &  & 4, &  & 6, & \dots\}\\
  Z_3 = \{ & 1, & 2, &  &  & 5\phantom{,} &  & \}\\
  Z_4 = \{ &  &  & 3, & \mathbf{4}, & 5, & 6, & \dots\}\\
  \vdots & & & & & \ddots
\end{array}
\]
آنگاه $\overline{Z}$ مجموعه‌ای است که با پایین‌رفتن روی قطر به دست
می‌آید: هر عددی را که روی قطر ظاهر می‌شود کنار می‌گذاریم و هر $j$ای را
که خانهٔ واقع در سطر $j$اُم و همان ستون خالی است، وارد مجموعه می‌کنیم. در نمونهٔ
بالا، $1$ و $2$ را کنار می‌گذاریم، $3$ را وارد می‌کنیم، $4$ را کنار
می‌گذاریم، و همین‌طور ادامه می‌دهیم.
\end{explain}
```

Keep every displayed set/cell. A blank at row j,column j means j absent from Z_j; clarify that single cell, not an entire row/column gap. Given example excludes1,2,4 and includes3.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C23: Power set of zero-based naturals exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{prob}
Show that $\Pow{\Nat}$ is !!{nonenumerable} by a diagonal argument.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
با یک استدلال قطری نشان دهید که $\Pow{\Nat}$ ناشمارا است.
\end{prob}
```

Retain Nat rather than PosInt. Explicit diagonal solutions account for one-based row versus zero-based argument; no unnecessary solution inserted in the exercise.

Alternatives: No material alternative recorded; none invented.

## FA-0033-C24: All positive-integer functions exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115, FA-OL-CANON-0001:P0082.

Source:
```latex
\begin{prob}\label{sfr:siz:nen:prob:f-posint}
Show that the set of functions $f \colon \PosInt \to \PosInt$ is
!!{nonenumerable} by an explicit diagonal argument. That is, show that
if $f_1$, $f_2$, \dots, is a list of functions and each $f_i\colon
\PosInt \to \PosInt$, then there is some $\overline{f}\colon \PosInt \to
\PosInt$ not on this list.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}\label{sfr:siz:nen:prob:f-posint}
با یک استدلال قطریِ صریح نشان دهید که مجموعهٔ توابع
$f \colon \PosInt \to \PosInt$ ناشمارا است. یعنی نشان دهید
اگر $f_1$، $f_2$، \dots فهرستی از توابع باشد و هر $f_i\colon
\PosInt \to \PosInt$ باشد، آنگاه تابعی مانند $\overline{f}\colon \PosInt \to
\PosInt$ وجود دارد که در این فهرست نیست.
\end{prob}
```

All total functions PosInt→PosInt, not computable functions. Explicit universal diagonal f_n(n)+1 validates the requested exercise; translated exercise retains its own full witness specification and remains unsolved.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C01: Reduction heading

Action: retain_after_fresh_review; confidence 2/3: Editorial0–3, not calibrated probability. Source meaning checked; the stated exact-label or register attestation gap remains.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0005:P0115.

Source:
```latex
\olsection{Reduction}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\olsection{کاهش}
```

کاهش is retained as a locally defined transfer of one enumeration problem to another. It does not mean lowering mathematical difficulty or computational many-one reducibility.

Alternatives: تحویل and انتقال may convey transfer, but no consulted page establishes one as the unique discipline-wide equivalent. No automatic replacement.

Expert-review question: The exact reduction label کاهش is not directly attested on these pages. Its direction and source-defined content are supported; compare انتقال/تحویل if later exact-language evidence warrants.

## FA-0034-C02: Editorial relation to alternative section

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P050.

Source:
```latex
\begin{editorial}
  This section proves non-enumerability by reduction, matching the
  results in \olref[nen]{sec}. An alternative, slightly more condensed
  version matching the results in \olref[nen-alt]{sec} is provided in
  \olref[red-alt]{sec}.
\end{editorial}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{editorial}
  این بخش ناشمارابودن را از راه کاهش ثابت می‌کند و با نتایجِ
  \olref[nen]{sec} مطابقت دارد. روایتی جایگزین و اندکی موجزتر که با
  نتایجِ \olref[nen-alt]{sec} مطابقت دارد، در \olref[red-alt]{sec}
  آمده است.
\end{editorial}
```

Preserve links to nen, nen-alt and red-alt and the relative brevity of the alternative version. Same provisional source-defined reduction label.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C03: Which problem reduces to which

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P050.

Source:
```latex
We showed $\Pow{\PosInt}$ to be !!{nonenumerable} by a diagonalization
argument. We already had a proof that $\Bin^\omega$, the set of all
infinite sequences of $0$s and $1$s, is !!{nonenumerable}.  Here's
another way we can prove that $\Pow{\PosInt}$ is !!{nonenumerable}:
Show that \emph{if $\Pow{\PosInt}$ is !!{enumerable} then $\Bin^\omega$
  is also !!{enumerable}}.  Since we know $\Bin^\omega$ is not
!!{enumerable}, $\Pow{\PosInt}$ can't be either.  This is called
\emph{reducing} one problem to another---in this case, we reduce the
problem of enumerating $\Bin^\omega$ to the problem of enumerating
$\Pow{\PosInt}$.  A solution to the latter---an enumeration of
$\Pow{\PosInt}$---would yield a solution to the former---an enumeration
of $\Bin^\omega$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
با استدلالی قطری نشان دادیم که $\Pow{\PosInt}$ ناشمارا است.
از پیش نیز برهانی داشتیم که $\Bin^\omega$، یعنی مجموعهٔ همهٔ
دنباله‌های نامتناهیِ $0$ها و $1$ها، ناشمارا است. راه دیگری
برای اثبات اینکه $\Pow{\PosInt}$ ناشمارا است چنین است: نشان دهید
که \emph{اگر $\Pow{\PosInt}$ شمارا باشد، آنگاه $\Bin^\omega$
  نیز شمارا است}. چون می‌دانیم $\Bin^\omega$ شمارا
نیست، $\Pow{\PosInt}$ نیز نمی‌تواند چنین باشد. این کار را
\emph{کاهش‌دادن} یک مسئله به مسئله‌ای دیگر می‌نامند---در اینجا، مسئلهٔ
برشمردن $\Bin^\omega$ را به مسئلهٔ برشمردن $\Pow{\PosInt}$ کاهش
می‌دهیم. حل مسئلهٔ دوم---یعنی برشماریِ $\Pow{\PosInt}$---راه‌حلی برای
مسئلهٔ نخست---یعنی برشماریِ $\Bin^\omega$---به دست می‌دهد.
```

Source problem Bin^omega enumeration is reduced to Pow(PosInt) enumeration: an enumeration of the latter would solve the former. Keep the implication, known contradiction, and order of both problem names.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C04: Surjective transfer and empty case

Action: correct; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0003:P0051.

Source:
```latex
How do we reduce the problem of enumerating a set~$B$ to that of
enumerating a set~$A$?  We provide a way of turning an enumeration
of~$A$ into an enumeration of~$B$.  The easiest way to do that is to
define !!a{surjective} function $f\colon A \to B$.  If $x_1$, $x_2$,
\dots{} enumerates~$A$, then $f(x_1)$, $f(x_2)$, \dots{} would
enumerate~$B$.  In our case, we are looking for a surjective
function $f\colon \Pow{\PosInt} \to \Bin^\omega$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
چگونه مسئلهٔ برشمردن مجموعهٔ~$B$ را به مسئلهٔ برشمردن مجموعهٔ~$A$
کاهش می‌دهیم؟ روشی ارائه می‌کنیم که برشماریِ~$A$ را به برشماریِ~$B$
تبدیل کند. آسان‌ترین راه آن است که تابعی پوشا به‌صورت
$f\colon A \to B$ تعریف کنیم. اگر $x_1$، $x_2$، \dots{} مجموعهٔ~$A$ را
برشمارد، آنگاه $f(x_1)$، $f(x_2)$، \dots{} مجموعهٔ~$B$ را برمی‌شمارد.
در مورد ما، در پی تابعی پوشا به‌صورت
$f\colon \Pow{\PosInt} \to \Bin^\omega$ هستیم.
\emph{یادداشت ویراستاری:} در بیان کلیِ بالا، اگر مجموعهٔ آغازین تهی باشد،
پوشابودن تابع مستلزم تهی‌بودن مجموعهٔ مقصد است؛ در این حالت هر دو مجموعه
طبق تعریف فصل شمارا هستند و به فهرست نامتناهی نیاز نیست.
```

The function maps A onto B while the problem of enumerating B reduces to that of A. Composition of a nonempty A enumeration covers B; if A empty, surjectivity makes B empty and source definition handles it. Label this explanatory empty-case note, not a theorem repair.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C05: Injective reverse-direction exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
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
نشان دهید اگر تابعی یک‌به‌یک به‌صورت $g\colon B \to A$ وجود داشته
باشد و $B$~ناشمارا باشد، آنگاه $A$ نیز چنین است. برای این
کار نشان دهید چگونه می‌توان با استفاده از~$g$، برشماریِ~$A$ را به
برشماریِ~$B$ تبدیل کرد.
\end{prob}
```

Keep g:B→A injective and B nonenumerable; cannot replace injection with surjection in that direction. Unique inverse on image plus a fixed default produces B enumeration from A, no Choice or decidability needed. Do not insert solution.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C06: Reduction proof assumption

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0003:P0053, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{proof}[Proof of {\olref[nen]{thm:nonenum-pownat}} by reduction]
Suppose that $\Pow{\PosInt}$ were !!{enumerable}, and thus that
there is an enumeration of it, $Z_{1}$, $Z_{2}$, $Z_{3}$, \dots
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{proof}[برهانِ {\olref[nen]{thm:nonenum-pownat}} از راه کاهش]
فرض کنید $\Pow{\PosInt}$ شمارا باشد و بنابراین برشماری‌ای از
آن به‌صورت $Z_{1}$، $Z_{2}$، $Z_{3}$، \dots وجود داشته باشد.
```

Preserve named theorem cross-reference and assumed enumeration of the nonempty power set, not assumed enumeration of binary sequences.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C07: Characteristic-sequence definition

Action: correct; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P046.

Source:
```latex
Define the function $f \colon \Pow{\PosInt} \to \Bin^\omega$ by letting
$f(Z)$ be the sequence $s_{k}$ such that $s_{k}(n) = 1$ iff $n \in Z$,
and $s_k(n) = 0$ otherwise.  This clearly defines a function, since
whenever $Z \subseteq \PosInt$, any $n \in \PosInt$ either is
!!a{element} of $Z$ or isn't.  For instance, the set $2\PosInt = \{2,
4, 6, \dots\}$ of positive even numbers gets mapped to the sequence
$010101\dots$, the empty set gets mapped to $0000\dots$ and the set
$\PosInt$ itself to $1111\dots$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
تابع $f \colon \Pow{\PosInt} \to \Bin^\omega$ را با قراردادنِ
$f(Z)$ برابر دنبالهٔ $s$ تعریف کنید، به‌گونه‌ای که $s(n) = 1$ اگر و تنها
اگر $n \in Z$، و در غیر این صورت $s(n) = 0$. این امر به‌روشنی تابعی
تعریف می‌کند، زیرا هرگاه $Z \subseteq \PosInt$، هر $n \in \PosInt$ یا
عضوی از $Z$ است یا نیست. برای نمونه، مجموعهٔ $2\PosInt = \{2,
4, 6, \dots\}$ از اعداد صحیح مثبت زوج به دنبالهٔ $010101\dots$ نگاشته
می‌شود، مجموعهٔ تهی به $0000\dots$ و خود مجموعهٔ $\PosInt$ به
$1111\dots$ نگاشته می‌شود.
\emph{یادداشت ویراستاری:} زیرنویسِ بی‌مرجعِ نام دنباله در متن مبدأ حذف شده است.
این دنباله را عضویت یا عدم عضویت در مجموعهٔ ورودی تعیین می‌کند؛
تعریف به فهرستی از همهٔ دنباله‌های دودویی نیاز ندارد.
```

Remove the unbound k subscript at all three occurrences, leaving s determined by membership in input Z. The canon directly supplies characteristic binary values, without naming them تابع مشخصه on this page. Preserve even/empty/all examples and explain the notation repair, not a false-proof claim.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C08: Surjectivity via selected positions

Action: correct; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P046.

Source:
```latex
It also is !!{surjective}: Every sequence of $0$s and $1$s corresponds
to some set of positive integers, namely the one which has as its
members those integers corresponding to the places where the sequence
has~$1$s. More precisely, suppose $s \in \Bin^\omega$.  Define $Z
\subseteq \PosInt$ by:
\[
Z = \Setabs{n \in \PosInt}{s(n) = 1}
\]
Then $f(Z) = s$, as can be verified by consulting the definition
of~$f$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
این تابع همچنین پوشا است: هر دنباله از $0$ها و $1$ها با
مجموعه‌ای از اعداد صحیح مثبت متناظر است؛ اعضای این مجموعه دقیقاً شمارهٔ
جایگاه‌هایی هستند که مقدار دنباله در آن‌ها~$1$ است. دقیق‌تر بگوییم، فرض کنید $s \in \Bin^\omega$. مجموعهٔ $Z
\subseteq \PosInt$ را چنین تعریف کنید:
\[
Z = \Setabs{n \in \PosInt}{s(n) = 1}
\]
آنگاه $f(Z) = s$؛ این را می‌توان با مراجعه به تعریفِ~$f$ بررسی کرد.
```

Unpack nested relative clauses: subset members are exactly the indices where s is1. Preserve set comprehension and iff correspondence; no arbitrary preimage selection or reversal.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C09: Composition really covers all sequences

Action: correct; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0005:P0115.

Source:
```latex
Now consider the list
\[
f(Z_1), f(Z_2), f(Z_3), \dots
\]
Since $f$ is !!{surjective}, every member of $\Bin^\omega$ must
appear as a value of~$f$ for some argument, and so must appear on the
list. This list must therefore enumerate all of~$\Bin^\omega$.
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
اکنون فهرست زیر را در نظر بگیرید:
\[
f(Z_1), f(Z_2), f(Z_3), \dots
\]
چون $f$ پوشا است، هر عضوِ $\Bin^\omega$ باید برای ورودی‌ای
به‌عنوان مقدارِ~$f$ ظاهر شود. آن ورودی نیز در برشماریِ مجموعه‌های ورودی
می‌آید؛ بنابراین مقدار تابع در فهرست بالا خواهد آمد. پس این
فهرست باید همهٔ~$\Bin^\omega$ را برشمارد.
```

Make explicit that the required input set occurs in the assumed enumeration. Thus every output appears. This fills an expository compression, not a new axiom or proof-gap accusation.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C10: Contradiction with the previous theorem

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115, FA-OL-CANON-0003:P0053.

Source:
```latex
So if $\Pow{\PosInt}$ were !!{enumerable}, $\Bin^\omega$ would be
!!{enumerable}.  But $\Bin^\omega$ is !!{nonenumerable}
(\olref[nen]{thm:nonenum-bin-omega}). Hence $\Pow{\PosInt}$ is
!!{nonenumerable}.
\end{proof}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
بنابراین اگر $\Pow{\PosInt}$ شمارا بود، $\Bin^\omega$ نیز
شمارا می‌بود. اما $\Bin^\omega$ ناشمارا است
(\olref[nen]{thm:nonenum-bin-omega}). پس $\Pow{\PosInt}$
ناشمارا است.
\end{proof}
```

Retain implication and contradiction with nonenum-bin-omega and both repeated predicates; the conclusion is about the power set, not its individual elements.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C11: Wrong direction and repaired constant map

Action: correct; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-REL-P046, FA-REL-P050, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{explain}
It is easy to be confused about the direction the reduction goes in.
For instance, !!a{surjective} function $g \colon \Bin^\omega \to B$
does \emph{not} establish that $B$ is !!{nonenumerable}.  (Consider $g
\colon \Bin^\omega \to \Bin$ defined by $g(s) = s(1)$, the function
that maps a sequence of $0$'s and $1$'s to its first !!{element}.  It
is !!{surjective}, because some sequences start with $0$ and some start
with $1$. But $\Bin$ is finite.)  Note also that the function~$f$ must
be !!{surjective}, or otherwise the argument does not go through:
$f(x_1)$, $f(x_2)$, \dots{} would then not be guaranteed to include
all the !!{element}s of~$B$. For instance, 
\[
h(n) = \underbrace{000\dots0}_{\text{$n$ $0$'s}}
\]
defines a function $h\colon \PosInt \to
\Bin^\omega$, but $\PosInt$ is !!{enumerable}.
\end{explain}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{explain}
ممکن است جهت کاهش به‌آسانی موجب سردرگمی شود. برای نمونه، تابعی
پوشا مانند $g \colon \Bin^\omega \to B$ \emph{ثابت نمی‌کند}
که $B$ ناشمارا است. (تابع $g
\colon \Bin^\omega \to \Bin$ را در نظر بگیرید که با $g(s) = s(1)$
تعریف می‌شود و هر دنباله از $0$ها و $1$ها را به نخستین عضو آن
می‌نگارد. این تابع پوشا است، زیرا بعضی دنباله‌ها با $0$ و
بعضی با $1$ آغاز می‌شوند؛ اما $\Bin$ متناهی است.) همچنین توجه کنید که
تابع~$f$ باید پوشا باشد، وگرنه استدلال پیش نمی‌رود:
فهرستِ $f(x_1)$، $f(x_2)$، \dots{} در آن صورت همهٔ
اعضای~$B$ را در بر نمی‌گیرد. برای نمونه، دنبالهٔ زیر را در نظر بگیرید که
پس از صفرهای نشان‌داده‌شده نیز در همهٔ جایگاه‌ها صفر است:
\[
h(n) = \underbrace{000\dots0}_{\text{$n$ تا $0$}}\dots
\]
تابعی به‌صورت $h\colon \PosInt \to
\Bin^\omega$ تعریف می‌کند، اما $\PosInt$ شمارا است.
\emph{یادداشت ویراستاری:} در متن مبدأ فقط تعداد متناهی صفر نوشته شده بود،
که عضوی از مجموعهٔ دنباله‌های نامتناهی نیست. در اینجا ادامهٔ نامتناهیِ
صفرها تصریح شده است. تابع حاصل ثابت است و، مثلاً، دنبالهٔ تماماً یک را
در برد خود ندارد؛ بنابراین پوشا نیست.
\end{explain}
```

Projection of sequence to first bit is onto a finite set and proves nothing about nonenumerability of that codomain. If f is not onto, its output list misses elements. Repair the invalid finite-string type by appending an explicitly infinite zero tail: h maps each n to the same infinite zero sequence, so omits the all-one sequence. Keep the n-zero underbrace as a finite prefix, and disclose its source error.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C12: Sets of pairs exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P046.

Source:
```latex
\begin{prob}
Show that the set of all \emph{sets of} pairs of positive integers is
!!{nonenumerable} by a reduction argument.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
با استدلالی کاهشی نشان دهید که مجموعهٔ همهٔ \emph{مجموعه‌های} زوج‌های
اعداد صحیح مثبت ناشمارا است.
\end{prob}
```

Preserve emphasized sets OF pairs; the object is Pow(PosInt×PosInt), not the countable Cartesian product itself. A fixed-column slice validates the reduction without entering a solution.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C13: All natural-number functions exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P046, FA-OL-CANON-0001:P0082.

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
\begin{prob}\label{sfr:siz:red:prob:nat-nat}
  با استدلالی کاهشی نشان دهید مجموعهٔ~$X$ از همهٔ توابع
  $f\colon \Nat \to \Nat$ ناشمارا است. (راهنمایی: تابعی پوشا
  از $X$ به~$\Bin^\omega$ بدهید.)
\end{prob}
```

Preserve all functions Nat→Nat and the hinted surjection X→Bin^omega. Zero versus positive indexing is handled in the review, not by changing source types.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C14: Infinite natural-number sequences exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0115, FA-REL-P046.

Source:
```latex
\begin{prob}
Show that $\Nat^\omega$, the set of infinite sequences of
natural numbers, is !!{nonenumerable} by a reduction argument.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
با استدلالی کاهشی نشان دهید $\Nat^\omega$، یعنی مجموعهٔ دنباله‌های
نامتناهیِ اعداد طبیعی، ناشمارا است.
\end{prob}
```

All infinite Nat-valued sequences, not finite strings or only binary sequences. Pointwise parity is an explicit onto reduction.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C15: Total versus partial zero-valued functions

Action: correct; confidence 2/3: Editorial0–3, not calibrated probability. Source meaning checked; the stated exact-label or register attestation gap remains.
Canon: FA-OL-CANON-0003:P0051, FA-REL-P046, FA-OL-CANON-0001:P0082.

Source:
```latex
\begin{prob}
Let $P$ be the set of functions from the set of positive
integers to the set $\{0\}$, and let $Q$ be the set of \emph{partial}
functions from the set of positive integers to the set $\{0\}$. Show
that $P$~is !!{enumerable} and $Q$~is not. (Hint: reduce the problem
of enumerating $\Bin^\omega$ to enumerating~$Q$).
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
فرض کنید $P$ مجموعهٔ توابعِ همه‌جا تعریف‌شده از مجموعهٔ اعداد صحیح مثبت به مجموعهٔ
$\{0\}$ باشد و $Q$ مجموعهٔ توابع \emph{جزئی} از مجموعهٔ اعداد صحیح
مثبت به مجموعهٔ $\{0\}$ باشد. نشان دهید $P$~شمارا است و
$Q$~نیست. (راهنمایی: مسئلهٔ برشمردن $\Bin^\omega$ را به مسئلهٔ
برشمردن~$Q$ کاهش دهید.)
\end{prob}
```

Explicitly say the P functions are everywhere defined, contrasting Q partial. Output values are always0 but the varying domains encode arbitrary subsets. Include nowhere-defined and total cases; no effective-domain restriction.

Alternatives: همه‌جا تعریف‌شده unpacks total, rather than replace جزئی with ناقص, which can suggest a defective function.

Expert-review question: جزئی is the established local chapter label, not directly attested on these seven pages. Source definition and actual algorithm/output contrast justify the distinction; no invented term quotation.

## FA-0034-C16: All onto binary-valued functions exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-REL-P046, FA-OL-CANON-0005:P0115.

Source:
```latex
\begin{prob}
Let $S$ be the set of all !!{surjective} functions from the set of
positive integers to the set \{0,1\}, i.e., $S$ consists of all
!!{surjective}~$f\colon \PosInt \to \Bin$.  Show that $S$ is
!!{nonenumerable}.
\end{prob}
```

Reviewed Persian (verified locale text tokens expanded; exact candidate retained in choices-evidence.json):
```latex
\begin{prob}
فرض کنید $S$ مجموعهٔ همهٔ توابع پوشا از مجموعهٔ اعداد صحیح
مثبت به مجموعهٔ \{0,1\} باشد؛ یعنی $S$ از همهٔ توابع
پوشا~$f\colon \PosInt \to \Bin$ تشکیل می‌شود. نشان دهید $S$
ناشمارا است.
\end{prob}
```

Preserve surjectivity in both occurrences and the set0,1. A prefix0,1 followed by an arbitrary binary sequence proves the exercise; do not forget to force both outputs or insert solution.

Alternatives: No material alternative recorded; none invented.

## FA-0034-C17: Real numbers exercise

Action: retain_after_fresh_review; confidence 3/3: Editorial0–3, not calibrated probability. Source meaning and the relevant scholarly construction checked; no material unresolved alternative.
Canon: FA-OL-CANON-0005:P0114, FA-OL-CANON-0005:P0115.

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

Retain all real numbers and nonenumerability. Reviewed ternary0/2 injection avoids binary expansion collisions; the canon’s cardinal equality is not misquoted as uniqueness of binary expansions.

Alternatives: No material alternative recorded; none invented.

## Validation boundary

Every substantive source and target character lies in an ordered non-overlapping reviewed span. Formal tokens are checked across inline, bracketed, multline and align mathematics. Text arguments in mathematics are separately aligned and manually reviewed for exact connective, quantifier and number-family meaning.
Finite tests support the written reasoning; they are not universal formal proofs. No new PDF was built or visually certified. Frozen owner inputs and reader releases are unchanged; corrections enter the owner’s normal next-batch build and visual QA.
Attribution: Open Logic Project and contributors, under existing CC BY 4.0 notices. https://github.com/OpenLogicProject/OpenLogic . Existing edition: https://github.com/KokunoYumeto/OpenLogic-fa-ir . Canon sources retain separate rights.
