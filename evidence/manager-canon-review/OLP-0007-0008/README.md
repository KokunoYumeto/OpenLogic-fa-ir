# Persian OpenLogic: important sets, unions and intersections

Full-section source/canon review of OLP-0007 and OLP-0008. Reviewed source/correction evidence, not a new compiled reader. All canon consultation recorded here is retrospective; original translation-time consultation is not asserted.

## Review priorities

- Correct two singular no-element constructions; leave genuine plurals intact.
- Clarify family-intersection membership direction, with an explicit nonempty-family/ambient-universe editorial note.
- Exact string, continuum, disjoint and index terminology limitations are exposed below, not filled with invented attestations.
- Confidence is editorial 0-3, not calibrated probability. Human review is a later opportunity, not a gate.

## Scholarly pages actually consulted

- نظریهٔ مجموعه‌ها; محسن خانی, افشین زارعی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/jozve-kamel.pdf). PDF SHA-256: dbd518c80232921264ab5d79b79be01fe42efe8c01a766327db248b2d261de04. Canon PDFs are privately retained, not redistributed.
- منطق ریاضی; محسن خانی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/chapter2_0.pdf). PDF SHA-256: 0f3fb75ed1fcb0cbc669c04493acf520888e1ebfd62795bb28fc510bc41c7e79. Canon PDFs are privately retained, not redistributed.
- مبانی منطق و نظریهٔ مجموعه‌ها; محسن خانی; دانشگاه صنعتی اصفهان. [Source](https://mohsen-khani.github.io/logic97-1/jozve/logic-full.pdf). PDF SHA-256: 565558b76701858236844f19663de27ee10a8d72fd8b007e69b85159ac49f86d. Canon PDFs are privately retained, not redistributed.
- FA-OL-CANON-0003:P0010, PDF 10, printed 9: Bottom clauses (a)-(b), and Russell statement above. Membership implication defines inclusion and disjunction defines union. Arbitrary abstraction defines a class, not necessarily a set.
- FA-OL-CANON-0003:P0011, PDF 11, printed 10: Clauses (c)-(h), specification axiom and consequence 8. Conjunction defines intersection; membership/nonmembership defines difference. Family union uses existential membership, family intersection universal implication. These are class definitions. Intersection of a set with a class is a set; V is not a set.
- FA-OL-CANON-0003:P0024, PDF 24, printed 23: Middle paragraph before definition 3. Actual scholarly no-element syntax uses a singular indefinite noun. Supports local هیچ عضو مشترکی without changing the edition-wide vocabulary.
- FA-OL-CANON-0003:P0046, PDF 46, printed 45: Peano theorem 36 and bottom definition 38. Naturals include zero. A sequence is omega-indexed; a finite sequence has a natural-number domain. Does not attest رشته or رشته تهی.
- FA-OL-CANON-0003:P0054, PDF 54, printed 53: Opening CH paragraph and section 5.2. Attests پیوستار in continuum hypothesis and uses indexed unions/cardinal operations. Does not directly attest the parenthetical name of R or مجموعهٔ اندیس.
- FA-OL-CANON-0001:P0004, PDF 4, printed 3: Grammar introduction and first-order-language section. Letters form words under rules, then sentences. Supports alphabet and letter vocabulary, not an exact string-term attestation.
- FA-OL-CANON-0001:P0013, PDF 13, printed 12: Examples 19-20 and exercises 21-22. Native integer-group, rational, natural and real domains and mathematical expository register.
- FA-OL-CANON-0005:P0084, PDF 84, printed 84: Opening integer/rational construction and definition 200. Number-family vocabulary and عضو/عنصر set exposition. Do not adopt the informal real-as-Cauchy-sequence sentence: it suppresses equivalence classes.

## FA-0007-C01: Heading and mathematical objects

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0005:P0084, FA-OL-CANON-0001:P0013.

Source:
```latex
\olsection{Some Important Sets}

\begin{ex}
We will mostly be dealing with sets whose !!{element}s are
mathematical objects. Four such sets are important enough to have
specific names:
```

Reviewed Persian:
```latex
\olsection{برخی مجموعه‌های مهم}

\begin{ex}
بیشتر با مجموعه‌هایی سروکار خواهیم داشت که در آن‌ها همهٔ
!!{element}s اشیای ریاضی‌اند. چهار مجموعه از این دست آن‌قدر مهم‌اند که
نام‌های ویژه‌ای دارند:
```

The descriptive heading and سروکار داشتن retain adult exposition. همهٔ اعضا has plural scope. The canon itself uses both عضو and عنصر; no global term substitution is justified.

Alternatives: Do not force عنصر everywhere or replace the full sentence with word-by-word equivalents.

## FA-0007-C02: The four number families

Action: retain_after_fresh_review; confidence 2/3: Source meaning is checked; the specific usage limitation remains.
Canon: FA-OL-CANON-0001:P0013, FA-OL-CANON-0005:P0084, FA-OL-CANON-0003:P0046, FA-OL-CANON-0003:P0054.

Source:
```latex
\begin{multline*}
    \Nat = \{0, 1, 2, 3, \ldots\} \\
    \shoveright{\text{the set of natural numbers}}\\
    \shoveleft{\Int = \{\ldots, -2, -1, 0, 1, 2, \ldots\}} \\
    \shoveright{\text{the set of integers}}\\
    \shoveleft{\Rat = \Setabs{\nicefrac{m}{n}}{m, n \in \Int\text{ and }n \neq 0}}\\
    \shoveright{\text{the set of rationals}}\\
    \shoveleft{\Real = (-\infty, \infty)}\\
    \text{the set of real numbers (the continuum)}
\end{multline*}
```

Reviewed Persian:
```latex
\begin{multline*}
    \Nat = \{0, 1, 2, 3, \ldots\} \\
    \shoveright{\text{مجموعهٔ اعداد طبیعی}}\\
    \shoveleft{\Int = \{\ldots, -2, -1, 0, 1, 2, \ldots\}} \\
    \shoveright{\text{مجموعهٔ اعداد صحیح}}\\
    \shoveleft{\Rat = \Setabs{\nicefrac{m}{n}}{m, n \in \Int\text{ و }n \neq 0}}\\
    \shoveright{\text{مجموعهٔ اعداد گویا}}\\
    \shoveleft{\Real = (-\infty, \infty)}\\
    \text{مجموعهٔ اعداد حقیقی (پیوستار)}
\end{multline*}
```

Natural numbers include zero; integers include both signs; rationals have integer numerator and nonzero integer denominator. و preserves conjunction. The real line and all labels retain source meaning.

Alternatives: اعداد کسری risks blurring the exact rational definition. More numbers later does not mean larger cardinality.

Expert-review question: پیوستار is attested within CH; its exact standalone use as the parenthetical name of R is only indirectly supported.

## FA-0007-C03: Infinity

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0046, FA-OL-CANON-0003:P0054.

Source:
```latex
These are all \emph{infinite} sets, that is, they each have
infinitely many !!{element}s.
```

Reviewed Persian:
```latex
اینها همگی مجموعه‌هایی \emph{نامتناهی} هستند؛ یعنی شمار !!{element}s
در هر یک نامتناهی است.
```

نامتناهی applies to each set and its number of members, not to a new claim that successive countable sets have different cardinalities.

Alternatives: بی‌نهایت is possible ordinary wording; نامتناهی fits this technical register.

## FA-0007-C04: Inclusion chain, strict witnesses and reference

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0010, FA-OL-CANON-0001:P0013.

Source:
```latex
As we move through these sets, we are adding \emph{more} numbers to
our stock. Indeed, it should be clear that $\Nat \subseteq \Int
\subseteq \Rat \subseteq \Real$: after all, every natural number is an
integer; every integer is a rational; and every rational is a real.
Equally, it should be clear that $\Nat \subsetneq \Int \subsetneq
\Rat$, since $-1$ is an integer but not a natural number, and
$\nicefrac{1}{2}$ is rational but not integer. It is less obvious
that $\Rat \subsetneq \Real$, i.e., that there are some real numbers
which are not rational\oliflabeldef{sfr:arith:real:realline}{, but we'll
return to this in \olref[arith][real]{realline}}{}.
```

Reviewed Persian:
```latex
با گذر از هر یک از این مجموعه‌ها به مجموعهٔ بعدی، اعداد \emph{بیشتری}
به ذخیرهٔ خود می‌افزاییم. در واقع، باید روشن باشد که $\Nat \subseteq \Int
\subseteq \Rat \subseteq \Real$؛ زیرا هر عدد طبیعی یک عدد صحیح، هر
عدد صحیح یک عدد گویا، و هر عدد گویا یک عدد حقیقی است. همچنین باید روشن
باشد که $\Nat \subsetneq \Int \subsetneq
\Rat$، زیرا $-1$ عددی صحیح است اما طبیعی نیست و
$\nicefrac{1}{2}$ عددی گویاست اما صحیح نیست. این نکته کمتر آشکار است
که $\Rat \subsetneq \Real$؛ یعنی عددهای حقیقی‌ای وجود دارند
که گویا نیستند\oliflabeldef{sfr:arith:real:realline}{؛ اما در
\olref[arith][real]{realline} به این موضوع بازمی‌گردیم}{}.
```

Every natural is an integer, every integer rational and every rational real. Strictness witnesses -1 and 1/2 remain exact. بیشتری means additional elements. The less-obvious real/rational strictness keeps the same conditional realline cross-reference.

Alternatives: Do not render more as cardinally larger, or silently delete the conditional reference.

## FA-0007-C05: Positive integers and binary alphabet

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0046, FA-OL-CANON-0001:P0013.

Source:
```latex
We'll sometimes also use the set of positive integers $\PosInt = \{1,
2, 3, \dots\}$ and the set containing just the first two natural
numbers $\Bin = \{0, 1\}$.
\end{ex}

\begin{tagblock}{compsci}
```

Reviewed Persian:
```latex
گاهی از مجموعهٔ اعداد صحیح مثبت $\PosInt = \{1,
2, 3, \dots\}$ و مجموعه‌ای که تنها دو عدد طبیعی نخست را در بر دارد،
یعنی $\Bin = \{0, 1\}$، نیز استفاده خواهیم کرد.
\end{ex}

\begin{tagblock}{compsci}
```

مثبت excludes zero in PosInt. نخست respects the displayed convention that 0 and 1 are the first naturals. Both explicit sets are unchanged.

Alternatives: Nonnegative is not interchangeable with positive.

## FA-0007-C06: Finite strings and empty string

Action: retain_after_fresh_review; confidence 2/3: Source meaning is checked; the specific usage limitation remains.
Canon: FA-OL-CANON-0001:P0004, FA-OL-CANON-0003:P0046.

Source:
```latex
\begin{ex}[Strings] 
Another interesting example  is the set $A^{*}$ of \emph{finite
strings} over an alphabet $A$: any finite sequence of elements of~$A$
is a string over $A$. We include the \emph{empty string $\Lambda$}
among the strings over~$A$, for every alphabet~$A$. For instance,
```

Reviewed Persian:
```latex
\begin{ex}[رشته‌ها]
نمونهٔ جالب دیگر، مجموعهٔ $A^{*}$ از \emph{رشته‌های متناهی}
بر الفبای $A$ است: هر دنبالهٔ متناهی از عناصر~$A$ رشته‌ای بر $A$
است. \emph{رشتهٔ تهی $\Lambda$} را نیز در شمار رشته‌های بر~$A$، برای
هر الفبای~$A$، می‌آوریم. برای نمونه،
```

A string is a finite sequence of alphabet elements; the empty string belongs for every alphabet, including the empty alphabet. The selected native canon was actually consulted for alphabet and sequence concepts, but does not establish an exact رشته witness. Retention is explicitly provisional.

Alternatives: واژه is a meaningful alternative; do not invent an attestation for it. Empty string must not become empty set.

Expert-review question: Exact scholarly رشته/واژه and رشتهٔ تهی attestations remain to be bound by a later targeted corpus comparison; no human response is a gate.

## FA-0007-C07: Binary-string enumeration

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0001:P0004, FA-OL-CANON-0003:P0046.

Source:
```latex
\begin{multline*}
\Bin^*
=\{\Lambda,0,1,00,01,10,11,\\
000,001,010,011,100,101,110,111,0000,\ldots\}.
\end{multline*}
```

Reviewed Persian:
```latex
\begin{multline*}
\Bin^*
=\{\Lambda,0,1,00,01,10,11,\\
000,001,010,011,100,101,110,111,0000,\ldots\}.
\end{multline*}
```

Lambda, lengths one through three and the start of length four are identical. Order and repeated letters matter within a string.

Alternatives: Do not treat leading zeroes as a number or deduplicate repeated letters.

## FA-0007-C08: Length and indexed letters

Action: retain_after_fresh_review; confidence 2/3: Source meaning is checked; the specific usage limitation remains.
Canon: FA-OL-CANON-0001:P0004, FA-OL-CANON-0003:P0046.

Source:
```latex
If $x=x_{1}\ldots x_{n}\in A^{*}$is a string consisting of $n$
``letters'' from $A$, then we say \emph{length} of the string is~$n$
and write $\len{x}=n$.
\end{ex}
\end{tagblock}
```

Reviewed Persian:
```latex
اگر $x=x_{1}\ldots x_{n}\in A^{*}$ رشته‌ای متشکل از $n$
``حرف'' از $A$ باشد، می‌گوییم \emph{طول} رشته برابر~$n$ است
و می‌نویسیم $\len{x}=n$.
\end{ex}
\end{tagblock}
```

Quoted حرف allows formal alphabet elements, not just human-language letters. طول counts the n positions, including zero; len and subscripts are preserved. The missing English space before is is not inherited.

Alternatives: اندازه risks confusing string length with set size.

Expert-review question: The selected pages support the finite-sequence construction, not the exact compound طول رشته.

## FA-0007-C09: One-way infinite sequences

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0046.

Source:
```latex
\begin{ex}[Infinite sequences]
For any set $A$ we may also consider the set~$A^\omega$ of infinite
sequences of !!{element}s of~$A$. An infinite sequence
$a_1a_2a_3a_4\dots$ consists of a one-way infinite list of objects,
each one of which is !!a{element} of~$A$.
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}[دنباله‌های نامتناهی]
برای هر مجموعهٔ $A$ می‌توانیم مجموعهٔ~$A^\omega$ از دنباله‌های
نامتناهی را نیز در نظر بگیریم؛ دنباله‌هایی که از !!{element}s تشکیل
می‌شوند و این اعضا به~$A$ تعلق دارند. دنبالهٔ نامتناهی $a_1a_2a_3a_4\dots$
از فهرستی نامتناهی و یک‌سویه از اشیا تشکیل شده است که هر یک
!!a{element} مجموعهٔ~$A$ است.
\end{ex}
```

دنباله‌های نامتناهی and یک‌سویه preserve an omega-indexed list, not a bilateral or uncountably indexed family. Each entry belongs to A. This does not promise such a sequence when A is empty.

Alternatives: A two-sided sequence or an unordered infinite set changes the source.

## FA-0008-C01: Abstraction and inclusive union

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0010, FA-OL-CANON-0003:P0011.

Source:
```latex
\olsection{Unions and Intersections}

\begin{explain}
In \olref[sfr][set][bas]{sec}, we introduced definitions of sets by
abstraction, i.e., definitions of the form $\Setabs{x}{\phi(x)}$.
Here, we invoke some property~$\phi$, and this property can mention
sets we've already defined. So for instance, if $A$ and~$B$ are sets,
the set $\Setabs{x}{x \in A \lor x \in B}$ consists of all those
objects which are !!{element}s of either $A$ or~$B$, i.e., it's the
set that combines the !!{element}s of $A$ and~$B$. We can visualize
this as in \olref{fig:union}, where the highlighted area indicates the
!!{element}s of the two sets $A$ and~$B$ together.
```

Reviewed Persian:
```latex
\olsection{اجتماع‌ها و اشتراک‌ها}

\begin{explain}
در \olref[sfr][set][bas]{sec}، تعریف مجموعه‌ها به روش تجرید، یعنی
تعریف‌هایی به‌صورت $\Setabs{x}{\phi(x)}$، را معرفی کردیم. در این روش
ویژگی~$\phi$ را به کار می‌بریم و این ویژگی می‌تواند به مجموعه‌هایی که
پیش‌تر تعریف کرده‌ایم اشاره کند. بنابراین، برای نمونه، اگر $A$ و~$B$
مجموعه باشند، مجموعهٔ $\Setabs{x}{x \in A \lor x \in B}$ از همهٔ
اشیایی تشکیل شده است که در شمار !!{element}s $A$ یا~$B$ هستند؛ یعنی
مجموعه‌ای است که !!{element}s $A$ و~$B$ را با هم گرد می‌آورد.
می‌توان این وضعیت را مانند \olref{fig:union} مجسم کرد؛ در آنجا ناحیهٔ
برجسته، !!{element}s دو مجموعهٔ $A$ و~$B$ را در کنار هم نشان می‌دهد.
```

Abstraction, the previous-section reference and inclusive disjunction remain intact. Defined sets, their members and the property are distinguished. These particular operations yield sets; arbitrary abstraction is not asserted to do so.

Alternatives: Exclusive either-or is wrong. تجرید follows the preceding reviewed section, not an unexamined isolated word replacement.

## FA-0008-C02: Union caption and operation naming

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0010.

Source:
```latex
\begin{figure}
  \olasset{assets/diagrams/union.tikz}
  \caption{The union $A \cup B$ of two sets is set of !!{element}s of
   $A$ together with those of~$B$.}
  \ollabel{fig:union} 
\end{figure}

This operation on sets---combining them---is very useful and common,
and so we give it a formal name and a symbol. 
\end{explain}
```

Reviewed Persian:
```latex
\begin{figure}
  \olasset{assets/diagrams/union.tikz}
  \caption{اجتماع $A \cup B$ دو مجموعه، مجموعهٔ !!{element}s
   $A$ همراه با اعضای~$B$ است.}
  \ollabel{fig:union}
\end{figure}

این عمل روی مجموعه‌ها---یعنی باهم‌ترکیب‌کردن آنها---بسیار سودمند و
پرکاربرد است؛ ازاین‌رو نام و نمادی صوری به آن می‌دهیم.
\end{explain}
```

The caption combines members of either set, including shared members. اجتماع is the attested set operation, not arithmetic addition. Figure/label paths remain exact.

Alternatives: جمع would suggest a different operation. Asset identity checks are not a fresh rendered-reader visual certification.

## FA-0008-C03: Union definition

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0010.

Source:
```latex
\begin{defn}[Union]
The \emph{union} of two sets $A$ and $B$, written $A \cup B$, is the
set of all things which are !!{element}s of $A$, $B$, or both.
\[
A \cup B = \Setabs{x}{x \in A \lor x \in B}
\]
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[اجتماع]
\emph{اجتماع} دو مجموعهٔ $A$ و $B$ که آن را $A \cup B$ می‌نویسیم،
مجموعهٔ همهٔ اشیایی است که در شمار !!{element}s $A$ یا $B$ یا هر دو هستند.
\[
A \cup B = \Setabs{x}{x \in A \lor x \in B}
\]
\end{defn}
```

یا هر دو explicitly preserves inclusive disjunction; prose and membership formula agree.

Alternatives: Disjoint union is a different construction.

## FA-0008-C04: Multiplicity and three union examples

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0005:P0084, FA-OL-CANON-0003:P0010.

Source:
```latex
\begin{ex}
Since the multiplicity of !!{element}s doesn't matter, the union of two
sets which have !!a{element} in common contains that !!{element} only once,
e.g., $\{ a, b, c\} \cup \{ a, 0, 1\} = \{a, b, c, 0, 1\}$.

The union of a set and one of its subsets is just the bigger set: $\{a,
b, c \} \cup \{a \} = \{a, b, c\}$.

The union of a set with the empty set is identical to the set: $\{a,
b, c \} \cup \emptyset = \{a, b, c \}$.
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}
ازآنجاکه تعداد تکرار !!{element}s اهمیتی ندارد، اجتماع دو مجموعه که
!!a{element} مشترک دارند، آن !!{element} را تنها یک بار در بر می‌گیرد؛
برای نمونه، $\{ a, b, c\} \cup \{ a, 0, 1\} = \{a, b, c, 0, 1\}$.

اجتماع یک مجموعه با یکی از زیرمجموعه‌هایش همان مجموعهٔ بزرگ‌تر است:
$\{a, b, c \} \cup \{a \} = \{a, b, c\}$.

اجتماع یک مجموعه با مجموعهٔ تهی همان مجموعه است: $\{a,
b, c \} \cup \emptyset = \{a, b, c \}$.
\end{ex}
```

A shared member occurs once, union with a subset gives the larger set, and union with the empty set is unchanged. Example labels keep the source convention of distinct objects.

Alternatives: Do not import multiset or list-concatenation semantics.

## FA-0008-C05: Union inclusion exercise

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0010.

Source:
```latex
\begin{prob}
Prove that if $A \subseteq B$, then $A \cup B = B$.
\end{prob}
```

Reviewed Persian:
```latex
\begin{prob}
ثابت کنید اگر $A \subseteq B$، آنگاه $A \cup B = B$.
\end{prob}
```

Proof instruction, subset hypothesis and equality conclusion are all retained. It remains an exercise, not an abridged worked answer.

Alternatives: No material alternative recorded; none invented.

## FA-0008-C06: Dual construction and intersection caption

Action: retain_after_fresh_review; confidence 2/3: Source meaning is checked; the specific usage limitation remains.
Canon: FA-OL-CANON-0003:P0010, FA-OL-CANON-0003:P0011.

Source:
```latex
\begin{explain}
We can also consider a ``dual'' operation to union. This is the
operation that forms the set of all !!{element}s that are !!{element}s
of~$A$ and are also !!{element}s of~$B$. This operation is called 
\emph{intersection}, and can be depicted as in \olref{fig:intersection}.
\begin{figure}
  \olasset{assets/diagrams/intersection.tikz}
  \caption{The intersection $A \cap B$ of two sets is the set of
    !!{element}s they have in common.}
  \ollabel{fig:intersection}
\end{figure}
\end{explain}
```

Reviewed Persian:
```latex
\begin{explain}
می‌توانیم عملی ``دوگان'' با اجتماع را نیز در نظر بگیریم. این عمل
مجموعهٔ همهٔ !!{element}s را تشکیل می‌دهد که هم در شمار !!{element}s~$A$
و هم در شمار !!{element}s~$B$ هستند. این عمل \emph{اشتراک} نام دارد و می‌توان
آن را مانند \olref{fig:intersection} نمایش داد.
\begin{figure}
  \olasset{assets/diagrams/intersection.tikz}
  \caption{اشتراک $A \cap B$ دو مجموعه، مجموعهٔ
    !!{element}s مشترک آنهاست.}
  \ollabel{fig:intersection}
\end{figure}
\end{explain}
```

Membership in both sets is conjunction. دوگان remains a quoted informal comparison; the caption is common membership.

Alternatives: Do not inflate this into a formal duality theorem.

Expert-review question: The cited pages demonstrate the connective relationship, not exact دوگان wording.

## FA-0008-C07: Intersection and disjointness

Action: correct; confidence 2/3: Source meaning is checked; the specific usage limitation remains.
Canon: FA-OL-CANON-0003:P0011, FA-OL-CANON-0003:P0024.

Source:
```latex
\begin{defn}[Intersection]
The \emph{intersection} of two sets $A$ and $B$, written $A \cap B$, is
the set of all things which are !!{element}s of both $A$ and~$B$.
\[
A \cap B = \Setabs{x}{x \in A \land x \in B}
\]
Two sets are called \emph{disjoint} if their intersection is
empty. This means they have no !!{element}s in common.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[اشتراک]
\emph{اشتراک} دو مجموعهٔ $A$ و $B$ که آن را $A \cap B$ می‌نویسیم،
مجموعهٔ همهٔ اشیایی است که در شمار !!{element}s هر دو مجموعهٔ $A$ و~$B$ هستند.
\[
A \cap B = \Setabs{x}{x \in A \land x \in B}
\]
دو مجموعه را \emph{جدا از هم} می‌نامیم هرگاه اشتراکشان تهی باشد؛ یعنی
هیچ !!{element} مشترکی نداشته باشند.
\end{defn}
```

Both membership conditions must hold. جدا از هم is defined by empty intersection, not spatial distance. Removing the English plural suffix after هیچ gives هیچ عضو مشترکی, following the observed singular indefinite construction.

Alternatives: Do not change all اعضا tokens; other contexts are genuinely plural.

Expert-review question: Exact جدا از هم terminology is not attested on these pages; its displayed definition is precise.

## FA-0008-C08: Four intersection examples

Action: correct; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0011, FA-OL-CANON-0003:P0024.

Source:
```latex
\begin{ex}
If two sets have no !!{element}s in common, their intersection is empty:
$\{ a, b, c\} \cap \{ 0, 1\} = \emptyset$.

If two sets do have !!{element}s in common, their intersection is the set of
all those: $\{a, b, c \} \cap \{a, b, d \} = \{a, b\}$.

The intersection of a set with one of its subsets is just the smaller
set: $\{a, b, c\} \cap \{a, b\} = \{a, b\}$.

The intersection of any set with the empty set is empty: $\{a, b, c \}
\cap \emptyset = \emptyset$.
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}
اگر دو مجموعه هیچ !!{element} مشترکی نداشته باشند، اشتراکشان تهی است:
$\{ a, b, c\} \cap \{ 0, 1\} = \emptyset$.

اگر دو مجموعه !!{element}s مشترک داشته باشند، اشتراکشان مجموعهٔ همهٔ
آن اعضاست: $\{a, b, c \} \cap \{a, b, d \} = \{a, b\}$.

اشتراک یک مجموعه با یکی از زیرمجموعه‌هایش همان مجموعهٔ کوچک‌تر است:
$\{a, b, c\} \cap \{a, b\} = \{a, b\}$.

اشتراک هر مجموعه با مجموعهٔ تهی، تهی است: $\{a, b, c \}
\cap \emptyset = \emptyset$.
\end{ex}
```

The no-common-member, common-member, subset and empty-set cases stay distinct. Only the no-member singular inflection changes; the remaining plural common-member constructions are correct.

Alternatives: Do not change all-members intersection to at-least-one union.

## FA-0008-C09: Rigorous intersection exercise

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0010, FA-OL-CANON-0003:P0011.

Source:
```latex
\begin{prob}
Prove rigorously that if $A \subseteq B$, then $A \cap B = A$.
\end{prob}
```

Reviewed Persian:
```latex
\begin{prob}
به‌دقت ثابت کنید اگر $A \subseteq B$، آنگاه $A \cap B = A$.
\end{prob}
```

به‌دقت ثابت کنید retains the request for a rigorous proof and every hypothesis/conclusion.

Alternatives: No material alternative recorded; none invented.

## FA-0008-C10: A family of sets

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0011.

Source:
```latex
\begin{explain}
We can also form the union or intersection of more than two
sets. An elegant way of dealing with this in general is the
following: suppose you collect all the sets you want to form the union
(or intersection) of into a single set. Then we can define the union
of all our original sets as the set of all objects which belong to at
least one !!{element} of the set, and the intersection as the set of
all objects which belong to every !!{element} of the set.
\end{explain}

\begin{defn}
```

Reviewed Persian:
```latex
\begin{explain}
می‌توانیم اجتماع یا اشتراک بیش از دو مجموعه را نیز تشکیل دهیم. راهی
ظریف برای بررسی حالت کلی چنین است: فرض کنید همهٔ مجموعه‌هایی را که
می‌خواهید اجتماع (یا اشتراک) آنها را تشکیل دهید، در یک مجموعه گرد
آورید. سپس می‌توانیم اجتماع همهٔ مجموعه‌های نخستین را مجموعهٔ همهٔ
اشیایی تعریف کنیم که دست‌کم به یک !!{element} از آن مجموعه تعلق دارند،
و اشتراک را مجموعهٔ همهٔ اشیایی که به هر !!{element} آن مجموعه تعلق دارند.
\end{explain}

\begin{defn}
```

The family contains sets; objects belong to at least one or every member-set. The labelled note qualifies generalized intersections, not unions.

Alternatives: Do not collapse the two levels of membership.

## FA-0008-C11: Generalized union

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0011.

Source:
```latex
If $A$ is a set of sets, then $\bigcup A$ is the set of !!{element}s of
!!{element}s of~$A$:
\begin{align*}
\bigcup A & = \Setabs{x}{x \text{ belongs to !!a{element} of } A},
\text{ i.e.,}\\
& = \Setabs{x}{\text{there is a } B \in A
  \text{ so that } x \in B}
\end{align*}
\end{defn}

\begin{defn}
```

Reviewed Persian:
```latex
اگر $A$ مجموعه‌ای از مجموعه‌ها باشد، آنگاه $\bigcup A$ مجموعهٔ همهٔ
اشیایی است که در شمار !!{element}sِ !!{element}s~$A$ هستند:
\begin{align*}
\bigcup A & = \Setabs{x}{x \text{ متعلق به !!a{element}ی از } A},
\text{ یعنی}\\
& = \Setabs{x}{\text{یک } B \in A
  \text{ وجود دارد به‌طوری‌که } x \in B}
\end{align*}
\end{defn}

\begin{defn}
```

The prose and aligned display express existence of a member-set B. !!a{element}ی realizes عضوی correctly. Empty-family union remains valid and empty.

Alternatives: Adding a nonempty restriction to union is unnecessary.

## FA-0008-C12: Generalized intersection: membership direction and domain

Action: correct; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0011.

Source:
```latex
If $A$ is a set of sets, then $\bigcap A$ is the set of objects which
all elements of~$A$ have in common:
\begin{align*}
\bigcap A & = \Setabs{x}{x \text{ belongs to every !!{element} of } A},
\text{ i.e.,}\\
 & = \Setabs{x}{\text{for all } B \in A, x \in B}
\end{align*}
\end{defn}
```

Reviewed Persian:
```latex
اگر $A$ مجموعه‌ای ناتهی از مجموعه‌ها باشد، آنگاه $\bigcap A$
مجموعهٔ همهٔ اشیایی است که به هر یک از مجموعه‌های عضوِ~$A$ تعلق دارند\footnote{یادداشت ویراستاری: در اینجا، برای اشتراک یک خانوادهٔ دلخواه از مجموعه‌ها فرض می‌کنیم خانواده ناتهی است؛ در حالت اندیس‌دار نیز همین شرط برقرار است. برای خانوادهٔ تهی، شرط «عضویت در همهٔ مجموعه‌های خانواده» به‌تنهایی مجموعه‌ای معین نمی‌کند. اگر از پیش یک مجموعهٔ مرجع ثابت شده باشد، می‌توان اشتراک خانوادهٔ تهی را نسبت به آن مرجع، خودِ مجموعهٔ مرجع تعریف کرد.}:
\begin{align*}
\bigcap A & = \Setabs{x}{x \text{ متعلق به هر !!{element} از } A},
\text{ یعنی}\\
 & = \Setabs{x}{\text{برای هر } B \in A, x \in B}
\end{align*}
\end{defn}
```

The old sentence confusingly placed family members inside shared objects. The candidate says each object belongs to every member-set. A visible editorial note discloses the source’s omitted nonempty-family condition. The unrestricted empty-family predicate defines the universal class, not a set. For a nonempty family choose a member B0: its intersection is a class contained in B0, hence a set by specification. A fixed ambient-set convention for an empty family is separately allowed. Original formulas stay exact.

Alternatives: Do not silently add a hypothesis. Do not arbitrarily declare the unrestricted empty intersection empty. This is a source qualification, not evidence of a transcription mistake.

## FA-0008-C13: Three-set family example

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0011.

Source:
```latex
\begin{ex}
Suppose $A = \{ \{ a, b \}, \{ a, d, e \}, \{ a, d \} \}$.
Then $\bigcup A = \{ a, b, d, e \}$ and $\bigcap A = \{ a \}$.
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}
فرض کنید $A = \{ \{ a, b \}, \{ a, d, e \}, \{ a, d \} \}$.
آنگاه $\bigcup A = \{ a, b, d, e \}$ و $\bigcap A = \{ a \}$.
\end{ex}
```

All three member-sets and both answers are preserved. The union has four displayed labels, the intersection only a; the family is nonempty.

Alternatives: No material alternative recorded; none invented.

## FA-0008-C14: Membership versus inclusion exercise

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0010, FA-OL-CANON-0003:P0011.

Source:
```latex
\begin{prob}
	Show that if $A$ is a set and $A \in B$, then $A \subseteq \bigcup B$.
\end{prob}
```

Reviewed Persian:
```latex
\begin{prob}
	نشان دهید اگر $A$ یک مجموعه و $A \in B$ باشد، آنگاه $A \subseteq \bigcup B$.
\end{prob}
```

A belongs to B, whereas A is a subset of the union of B. The two relations stay distinct.

Alternatives: Changing A in B to A subset B changes the problem.

## FA-0008-C15: Sequence-indexed operations

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0046, FA-OL-CANON-0003:P0011.

Source:
```latex
We could also do the same for a sequence of sets $A_1$, $A_2$, \dots
\begin{align*}
\bigcup_i A_i & = \Setabs{x}{x \text{ belongs to one of the } A_i}\\
\bigcap_i A_i & = \Setabs{x}{x \text{ belongs to every } A_i}.
\end{align*}
```

Reviewed Persian:
```latex
می‌توان همین کار را برای دنباله‌ای از مجموعه‌ها مانند $A_1$، $A_2$، \dots
نیز انجام داد:
\begin{align*}
\bigcup_i A_i & = \Setabs{x}{x \text{ متعلق به یکی از مجموعه‌های } A_i}\\
\bigcap_i A_i & = \Setabs{x}{x \text{ متعلق به همهٔ مجموعه‌های } A_i}.
\end{align*}
```

A1,A2,... is a nonempty sequence. یکی is existential at-least-one here; همهٔ is universal. No uniqueness condition is introduced.

Alternatives: Exactly one or almost all would change the quantifier.

## FA-0008-C16: General index set

Action: retain_after_fresh_review; confidence 2/3: Source meaning is checked; the specific usage limitation remains.
Canon: FA-OL-CANON-0003:P0054, FA-OL-CANON-0003:P0011.

Source:
```latex
When we have an \emph{index} of sets, i.e., some set $I$ such that we
are considering $A_i$ for each $i \in I$, we may also use these
abbreviations:
\begin{align*}
	\bigcup_{i \in I} A_i & = \bigcup \Setabs{A_i }{i \in I}\\
	\bigcap_{i \in I} A_i & = \bigcap\Setabs{A_i}{i \in I}
\end{align*}
```

Reviewed Persian:
```latex
هنگامی که یک \emph{مجموعهٔ اندیس} مانند $I$ داریم و مجموعه‌های مورد
نظر را با $A_i$ نشان می‌دهیم، به‌گونه‌ای که برای هر $i \in I$ یک
مجموعه در نظر گرفته شده است، می‌توانیم از صورت‌های اختصاری زیر نیز
استفاده کنیم:
\begin{align*}
	\bigcup_{i \in I} A_i & = \bigcup \Setabs{A_i }{i \in I}\\
	\bigcap_{i \in I} A_i & = \bigcap\Setabs{A_i}{i \in I}
\end{align*}
```

مجموعهٔ اندیس states the source explanation that I indexes Ai. Both abbreviation formulas retain i in I. The visible note also covers empty indexed intersections.

Alternatives: An index set is not one subscript value.

Expert-review question: The canon uses indexed unions/اندیس, but the exact compound مجموعهٔ اندیس is not directly attested here.

## FA-0008-C17: Difference explanation and caption

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0011.

Source:
```latex
Finally, we may want to think about the set of all !!{element}s in~$A$
which are not in~$B$. We can depict this as in \olref{difference}.

\begin{figure}
  \olasset{assets/diagrams/difference.tikz}
  \caption{The difference $A \setminus B$ of two sets is the set of
    those !!{element}s of~$A$ which are not also !!{element}s of~$B$.}
  \ollabel{difference}
\end{figure}
```

Reviewed Persian:
```latex
سرانجام، ممکن است بخواهیم مجموعهٔ همهٔ !!{element}s~$A$ را در نظر
بگیریم که در~$B$ نیستند. می‌توان آن را مانند \olref{difference} نمایش داد.

\begin{figure}
  \olasset{assets/diagrams/difference.tikz}
  \caption{تفاضل $A \setminus B$ دو مجموعه، مجموعهٔ
    !!{element}s~$A$ است که !!{element}s~$B$ نیستند.}
  \ollabel{difference}
\end{figure}
```

Membership is in A and not B; the caption and diagram path preserve the direction of subtraction.

Alternatives: Symmetric difference or B minus A is not equivalent.

## FA-0008-C18: Difference definition

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0011.

Source:
```latex
\begin{defn}[Difference]
The \emph{set difference}~$A \setminus B$ is the set of all !!{element}s of
$A$ which are not also !!{element}s of~$B$, i.e.,
\[
A\setminus B = \Setabs{x}{x\in A \text{ and } x \notin B}.
\]
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[تفاضل]
\emph{تفاضل مجموعه‌ای}~$A \setminus B$ مجموعهٔ همهٔ !!{element}s
$A$ است که در شمار !!{element}s~$B$ نیستند؛ یعنی
\[
A\setminus B = \Setabs{x}{x\in A \text{ و } x \notin B}.
\]
\end{defn}
```

تفاضل is directly attested. مجموعه‌ای clarifies its domain. و preserves conjunction with nonmembership in the display.

Alternatives: Complement requires an ambient set and is not a synonym for this binary operation.

## FA-0008-C19: Proper-subset difference exercise

Action: retain_after_fresh_review; confidence 3/3: Source meaning and the cited native mathematical construction agree.
Canon: FA-OL-CANON-0003:P0010, FA-OL-CANON-0003:P0011.

Source:
```latex
\begin{prob}
	Prove that if $A \subsetneq B$, then $B \setminus A \neq \emptyset$.
\end{prob}
```

Reviewed Persian:
```latex
\begin{prob}
	ثابت کنید اگر $A \subsetneq B$، آنگاه $B \setminus A \neq \emptyset$.
\end{prob}
```

Strict inclusion guarantees an element in B not A. The operands B minus A and the nonempty conclusion remain exact.

Alternatives: Weak inclusion allows empty difference and changes the theorem.

## Validation boundary

Every substantive source and target character lies in an ordered non-overlapping reviewed span. Formal tokens are checked across inline, bracketed, multline and align mathematics. Text arguments in mathematics are separately aligned and manually reviewed for exact connective, quantifier and number-family meaning.
Finite tests support the written reasoning; they are not universal formal proofs. No new PDF was built or visually certified. Frozen owner inputs and reader releases are unchanged; corrections enter the owner’s normal next-batch build and visual QA.
Attribution: Open Logic Project and contributors, under existing CC BY 4.0 notices. https://github.com/OpenLogicProject/OpenLogic . Existing edition: https://github.com/KokunoYumeto/OpenLogic-fa-ir . Canon sources retain separate rights.
