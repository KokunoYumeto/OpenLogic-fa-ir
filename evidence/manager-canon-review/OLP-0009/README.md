# Persian OpenLogic: pairs, tuples and Cartesian products

Complete OLP-0009 source/canon review, including proof, table, exercises and words. Reviewed source evidence, not a new compiled reader. All consultation is retrospective.

## Review priorities

- Fix six contextually singular counted-member occurrences, not global plural vocabulary.
- Clarify that set membership alone supplies no ordering; align the proper-name spelling with the selected Persian source.
- Explicitly restrict words to finite sequences and disclose the arbitrary-alphabet length-collision defect in the source representation.
- Preserve all original formulas; label the final displayed word union as a representational shorthand and supply the correct finite-function construction in a visible note.
- Distinguish exact canon attestations from still-provisional واژه and چندتایی register choices.
- Confidence is editorial 0-3, not calibrated probability. Human review is a later opportunity, not a gate.

## Scholarly pages actually consulted

- نظریهٔ مجموعه‌ها; محسن خانی, افشین زارعی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/jozve-kamel.pdf). PDF SHA-256: dbd518c80232921264ab5d79b79be01fe42efe8c01a766327db248b2d261de04. Canon PDFs are privately retained, not redistributed.
- مبانی منطق و نظریهٔ مجموعه‌ها; محسن خانی; دانشگاه صنعتی اصفهان. [Source](https://mohsen-khani.github.io/logic97-1/jozve/logic-full.pdf). PDF SHA-256: 565558b76701858236844f19663de27ee10a8d72fd8b007e69b85159ac49f86d. Canon PDFs are privately retained, not redistributed.
- FA-OL-CANON-0003:P0014, PDF 14, printed 13: Definition17, lemma18 and definition19. Exact set encoding of an ordered pair, coordinatewise equality, product membership and مؤلفه usage. The spelling کوراتوفسکی is directly present; no historical priority claim follows.
- FA-OL-CANON-0005:P0089, PDF 89, printed 89: Definitions206-207 and lemma208; pairing discussion. Same ordered-pair encoding and coordinatewise equality; extensionality identifies repeated set entries. Its footnote presents a slightly different proper-name spelling, so the chosen form is house consistency, not the sole permissible spelling.
- FA-OL-CANON-0005:P0090, PDF 90, printed 90: Definition211, existence proof and bottom function definition. Product membership uses an ordered pair with its first coordinate in a and second in b. The product is a subset of a double power set, giving existence. Higher products and graph-based functions are explicitly discussed.
- FA-OL-CANON-0005:P0116, PDF 116, printed 116: Theorem264 and its opening explanation. Direct attestation of the full Cartesian-product term; ordered-pair coordinate comparison in the proof. Its infinite-cardinal theorem is not imported into the finite counting argument.
- FA-OL-CANON-0003:P0024, PDF 24, printed 23: Definition5 at bottom and no-successor paragraph above. Attests singular noun after a count, as well as هیچ عنصری. Supports contextual counted-member grammar, not a global ban on plurals.
- FA-OL-CANON-0003:P0062, PDF 62, printed 61: Opening section and definition of n-element subsets. Native counted-set syntax explicitly tied to cardinality n. The Ramsey theorem is not used as authority for the elementary product theorem.
- FA-OL-CANON-0003:P0046, PDF 46, printed 45: Definition38 at bottom; Peano discussion above. Sequences are functions; finite sequences have a natural-number domain. This supplies a length-aware rigorous representation for arbitrary alphabets. It does not directly attest the term واژه.

## FA-0009-C01: Heading, unstructured sets and ordering

Action: correct; confidence 2/3: Mathematical content is checked; the exact-register limitation is stated.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0089, FA-OL-CANON-0005:P0116.

Source:
```latex
\olsection{Pairs, Tuples, Cartesian Products}

\begin{explain}
It follows from extensionality that sets have no order to their
elements. So if we want to represent order, we use \emph{ordered
pairs} $\tuple{x, y}$. In an unordered pair $\{x, y\}$, the order does
not matter: $\{x, y\} = \{y, x\}$. In an ordered pair, it does: if $x
\neq y$, then $\tuple{x, y} \neq \tuple{y, x}$.
```

Reviewed Persian:
```latex
\olsection{زوج‌های مرتب، چندتایی‌ها و ضرب‌های دکارتی}

\begin{explain}
از اصل گسترش نتیجه می‌شود که خودِ مجموعه ترتیبی برای اعضایش تعیین نمی‌کند.
پس اگر بخواهیم ترتیب را بازنمایی کنیم، از \emph{زوج‌های مرتب}
$\tuple{x, y}$ استفاده می‌کنیم. در زوج نامرتب $\{x, y\}$، ترتیب
اهمیتی ندارد: $\{x, y\} = \{y, x\}$. اما در زوج مرتب اهمیت دارد:
اگر $x \neq y$، آنگاه $\tuple{x, y} \neq \tuple{y, x}$.
```

The expanded heading faithfully identifies ordered pairs and products. The first sentence is clarified: membership alone does not specify order; sets may still be equipped with an ordering. The unordered-pair equality and the conditional ordered-pair inequality are unchanged. No distinctness is assumed when x equals y.

Alternatives: Saying sets cannot be ordered would be false. چندتایی is retained with explicit n-tuple examples rather than given a fabricated attestation.

Expert-review question: The viewed pages attest ordered pairs and higher products, not the exact general heading word چندتایی.

## FA-0009-C02: Coordinatewise equality and proper name

Action: correct; confidence 3/3: Direct source comparison and actual canon construction agree.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0089.

Source:
```latex
How should we think about ordered pairs in set theory? Crucially, we
want to preserve the idea that ordered pairs are identical iff they
share the same first element and share the same second element, i.e.:
\[
  \tuple{a, b}= \tuple{c, d}\text{ iff both }a = c \text{ and }b=d.
\]
We can define ordered pairs in set theory using the Wiener--Kuratowski
definition.
\end{explain}
```

Reviewed Persian:
```latex
در نظریهٔ مجموعه‌ها چگونه باید به زوج‌های مرتب بیندیشیم؟ نکتهٔ اساسی
این است که می‌خواهیم این اندیشه را حفظ کنیم که دو زوج مرتب یکسان‌اند
اگر و تنها اگر مؤلفهٔ نخستشان یکسان و مؤلفهٔ دومشان نیز یکسان باشد؛ یعنی:
\[
  \tuple{a, b}= \tuple{c, d}\text{ اگر و تنها اگر هم }a = c
  \text{ و هم }b=d.
\]
می‌توانیم زوج‌های مرتب را در نظریهٔ مجموعه‌ها با تعریف
وینر--کوراتوفسکی تعریف کنیم.
\end{explain}
```

مؤلفهٔ نخست/دوم names positions, not set membership. اگر و تنها اگر هم ... و هم preserves both directions and conjunction. Proper-name spelling follows the selected set-theory definition کوراتوفسکی; Wiener is retained from the English attribution, and the stable wienerkuratowski identifier is not altered.

Alternatives: Do not turn iff into only if or swap coordinate order. The other canon spelling is a legitimate variant, not evidence of mathematical error.

## FA-0009-C03: Ordered-pair set encoding

Action: retain_after_fresh_review; confidence 3/3: Direct source comparison and actual canon construction agree.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0089.

Source:
```latex
\begin{defn}[Ordered pair]\ollabel{wienerkuratowski}
	$\tuple{a, b} = \{\{a\}, \{a, b\}\}$.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[زوج مرتب]\ollabel{wienerkuratowski}
	$\tuple{a, b} = \{\{a\}, \{a, b\}\}$.
\end{defn}
```

The exact nested singletons/unordered pair encoding is retained, including the degenerate a=b case. The scholarly sources give the same construction and its existence from pairing.

Alternatives: A plain unordered pair or a right/left swapped encoding is not equivalent notation here.

## FA-0009-C04: Equality-characterization exercise

Action: retain_after_fresh_review; confidence 3/3: Direct source comparison and actual canon construction agree.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0089.

Source:
```latex
\begin{prob}
	Using \olref[sfr][set][pai]{wienerkuratowski}, prove that $\tuple{a,
	b}= \tuple{c, d}$ iff both $a = c$ and $b=d$.
\end{prob}
```

Reviewed Persian:
```latex
\begin{prob}
	با استفاده از \olref[sfr][set][pai]{wienerkuratowski} ثابت کنید
	$\tuple{a, b}= \tuple{c, d}$ اگر و تنها اگر هم $a = c$ و هم $b=d$.
\end{prob}
```

The original exercise, named definition reference and both coordinate equalities remain. The learner is still asked to prove the characterization, not merely read its statement.

Alternatives: No material alternative recorded; none invented.

## FA-0009-C05: Nested triples, quadruples and n-tuples

Action: retain_after_fresh_review; confidence 2/3: Mathematical content is checked; the exact-register limitation is stated.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0090.

Source:
```latex
\begin{explain}
Having fixed a definition of an ordered pair, we can use it to define
further sets. For example, sometimes we also want ordered sequences of
more than two objects, e.g., \emph{triples} $\tuple{x, y, z}$,
\emph{quadruples} $\tuple{x, y, z, u}$, and so on.  We can think of
triples as special ordered pairs, where the first element is itself an
ordered pair: $\tuple{x, y, z}$ is $\tuple{\tuple{x, y},z}$. The same
is true for quadruples: $\tuple{x,y,z,u}$ is
$\tuple{\tuple{\tuple{x,y},z},u}$, and so on. In general, we talk of
\emph{ordered $n$-tuples} $\tuple{x_1, \dots, x_n}$.

Certain sets of ordered pairs, or other ordered $n$-tuples, will be useful.
\end{explain}
```

Reviewed Persian:
```latex
\begin{explain}
اکنون که تعریفی برای زوج مرتب تثبیت کرده‌ایم، می‌توانیم آن را برای
تعریف مجموعه‌های دیگری به کار بریم. برای نمونه، گاهی دنباله‌های مرتبِ
بیش از دو شیء را نیز می‌خواهیم، مانند \emph{سه‌تایی‌ها}
$\tuple{x, y, z}$، \emph{چهارتایی‌ها} $\tuple{x, y, z, u}$ و
همین‌طور ادامه. می‌توانیم سه‌تایی‌ها را زوج‌های مرتب خاصی بدانیم که
مؤلفهٔ نخستشان خود یک زوج مرتب است: $\tuple{x, y, z}$ همان
$\tuple{\tuple{x, y},z}$ است. دربارهٔ چهارتایی‌ها نیز چنین است:
$\tuple{x,y,z,u}$ همان $\tuple{\tuple{\tuple{x,y},z},u}$ است و
به همین ترتیب ادامه می‌یابد. به‌طور کلی، از \emph{$n$-تایی‌های مرتب}
$\tuple{x_1, \dots, x_n}$ سخن می‌گوییم.

برخی مجموعه‌های زوج‌های مرتب یا دیگر $n$-تایی‌های مرتب سودمند خواهند بود.
\end{explain}
```

The first coordinate is itself a pair: nesting is left-associated exactly as in the source. سه‌تایی and چهارتایی identify fixed arities and the explicit examples anchor their meaning. General ordered n-tuples are not unordered n-element subsets.

Alternatives: Do not silently use right-associated tuples or treat arbitrary nested pair codes as length-separated words.

Expert-review question: The exact tuple-family naming is only indirectly supported by the consulted higher-product and ordered-pair passages.

## FA-0009-C06: Cartesian-product definition

Action: retain_after_fresh_review; confidence 3/3: Direct source comparison and actual canon construction agree.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0090, FA-OL-CANON-0005:P0116.

Source:
```latex
\begin{defn}[Cartesian product]
Given sets $A$ and $B$, their \emph{Cartesian product} $A \times B$ is
defined by
\[
  A \times B = \Setabs{\tuple{x, y}}{x \in A \text{ and } y \in B}.
\]
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[ضرب دکارتی]
برای مجموعه‌های $A$ و $B$، \emph{ضرب دکارتیِ} آنها، $A \times B$،
چنین تعریف می‌شود:
\[
  A \times B = \Setabs{\tuple{x, y}}{x \in A \text{ و } y \in B}.
\]
\end{defn}
```

ضرب دکارتی is a shorter form of the directly attested حاصلضرب دکارتی, with the same set construction and explicit formula. The first coordinate belongs to A, second to B; و is conjunction. Product existence is licensed by the canon construction, not unrestricted comprehension.

Alternatives: Ordinary numerical multiplication, unordered pairs, or coordinates in A union B do not convey this definition.

## FA-0009-C07: Six-pair example

Action: retain_after_fresh_review; confidence 3/3: Direct source comparison and actual canon construction agree.
Canon: FA-OL-CANON-0005:P0090.

Source:
```latex
\begin{ex}
If $A = \{0, 1\}$, and $B = \{1, a, b\}$, then their product is
\[
A \times B = \{ \tuple{0, 1}, \tuple{0, a}, \tuple{0, b},
    \tuple{1, 1}, \tuple{1, a}, \tuple{1, b} \}.
\]
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}
اگر $A = \{0, 1\}$ و $B = \{1, a, b\}$ باشند، ضرب آنها برابر است با
\[
A \times B = \{ \tuple{0, 1}, \tuple{0, a}, \tuple{0, b},
    \tuple{1, 1}, \tuple{1, a}, \tuple{1, b} \}.
\]
\end{ex}
```

All six displayed ordered pairs and their row/coordinate order remain. The source treats 1,a,b as distinct labels; with that convention the finite enumeration is correct.

Alternatives: Do not deduplicate pairs that merely share one coordinate.

## FA-0009-C08: Powers and recursive arity

Action: retain_after_fresh_review; confidence 3/3: Direct source comparison and actual canon construction agree.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0090.

Source:
```latex
\begin{ex}
If $A$ is a set, the product of $A$ with itself, $A \times A$, is also
written~$A^2$. It is the set of \emph{all} pairs $\tuple{x, y}$ with
$x, y \in A$. The set of all triples $\tuple{x, y, z}$ is $A^3$, and
so on. We can give a recursive definition:
\begin{align*}
  A^1 & = A\\
  A^{k+1} & = A^k \times A
\end{align*}
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}
اگر $A$ مجموعه‌ای باشد، ضرب $A$ در خودش، $A \times A$، را
$A^2$ نیز می‌نویسیم. این مجموعهٔ \emph{همهٔ} زوج‌های $\tuple{x, y}$
با $x, y \in A$ است. مجموعهٔ همهٔ سه‌تایی‌های $\tuple{x, y, z}$
برابر $A^3$ است و به همین ترتیب ادامه می‌یابد. می‌توانیم تعریفی
بازگشتی به دست دهیم:
\begin{align*}
  A^1 & = A\\
  A^{k+1} & = A^k \times A
\end{align*}
\end{ex}
```

The recurrence starts at A to the first power and forms the next power by multiplying on the right by A. همهٔ includes every pair or triple. بازگشتی indicates the recursive definition, not a proof by induction. Powers are fixed-arity code sets; they are not asserted disjoint for different arities.

Alternatives: Do not silently set A to power zero here or replace recursion by numerical exponentiation.

## FA-0009-C09: Twenty-seven-triple exercise

Action: retain_after_fresh_review; confidence 3/3: Direct source comparison and actual canon construction agree.
Canon: FA-OL-CANON-0005:P0090, FA-OL-CANON-0003:P0062.

Source:
```latex
\begin{prob}
List all !!{element}s of $\{1, 2, 3\}^3$.
\end{prob}
```

Reviewed Persian:
```latex
\begin{prob}
همهٔ !!{element}s $\{1, 2, 3\}^3$ را فهرست کنید.
\end{prob}
```

Every element of the third Cartesian power is requested. The plural token is correct after همهٔ and is retained. This has 27 ordered triples, not the one unordered three-element subset.

Alternatives: No material alternative recorded; none invented.

## FA-0009-C10: Finite product cardinality

Action: correct; confidence 3/3: Direct source comparison and actual canon construction agree.
Canon: FA-OL-CANON-0003:P0024, FA-OL-CANON-0003:P0062, FA-OL-CANON-0005:P0090.

Source:
```latex
\begin{prop}\ollabel{cardnmprod}
If $A$ has $n$ !!{element}s and $B$ has $m$ !!{element}s, then $A
\times B$ has $n\cdot m$ elements.
\end{prop}
```

Reviewed Persian:
```latex
\begin{prop}\ollabel{cardnmprod}
اگر $A$ دارای $n$ !!{element} و $B$ دارای $m$ !!{element} باشد،
آنگاه $A \times B$ دارای $n\cdot m$ عضو است.
\end{prop}
```

The n and m member nouns are singular in native counted syntax. Correct both English plural suffixes locally; the already singular n times m conclusion remains. The theorem includes zero cardinalities.

Alternatives: Do not narrow n,m to positive numbers merely to match the drawn nonempty grid.

## FA-0009-C11: Disjoint rows proof

Action: correct; confidence 3/3: Direct source comparison and actual canon construction agree.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0005:P0090, FA-OL-CANON-0003:P0062.

Source:
```latex
\begin{proof}
For every !!{element}~$x$ in~$A$, there are $m$ !!{element}s of the
form $\tuple{x, y} \in A \times B$. Let $B_x = \Setabs{\tuple{x, y}}{y
  \in B}$. Since whenever $x_1 \neq x_2$, $\tuple{x_1, y} \neq
\tuple{x_2, y}$, $B_{x_1} \cap B_{x_2} = \emptyset$. But if $A = \{x_1,
\dots, x_n\}$, then $A \times B = B_{x_1} \cup \dots \cup B_{x_n}$, and so has
$n\cdot m$ !!{element}s.
```

Reviewed Persian:
```latex
\begin{proof}
برای هر !!{element}~$x$ در~$A$، تعداد $m$ !!{element} به صورت
$\tuple{x, y} \in A \times B$ وجود دارد. بگذارید
$B_x = \Setabs{\tuple{x, y}}{y \in B}$. چون هرگاه $x_1 \neq x_2$،
$\tuple{x_1, y} \neq \tuple{x_2, y}$، داریم
$B_{x_1} \cap B_{x_2} = \emptyset$. اما اگر
$A = \{x_1, \dots, x_n\}$، آنگاه
$A \times B = B_{x_1} \cup \dots \cup B_{x_n}$ و در نتیجه دارای
$n\cdot m$ !!{element} است.
```

Each fixed-first-coordinate row contains m elements, rows with unequal first coordinates are disjoint by the established full coordinatewise equality lemma, and their union is the product. The displayed same-y inequality is a witness, while the earlier lemma justifies disjointness even for different second coordinates. Correct counted m and n times m nouns; retain genuinely plural members elsewhere. Empty-factor cases give an empty product and zero rows or columns.

Alternatives: No equal-x or equal-y premise may be added to all pairs. The row disjointness is not based solely on a same-y inequality.

## FA-0009-C12: Grid and count conclusion

Action: retain_after_fresh_review; confidence 3/3: Direct source comparison and actual canon construction agree.
Canon: FA-OL-CANON-0003:P0014, FA-OL-CANON-0003:P0062, FA-OL-CANON-0005:P0090.

Source:
```latex
To visualize this, arrange the !!{element}s of~$A \times B$ in a grid:
\[
\begin{array}{rcccc}
  B_{x_1} = & \{\tuple{x_1, y_1} & \tuple{x_1, y_2} & \dots & \tuple{x_1, y_m}\}\\
  B_{x_2} = & \{\tuple{x_2, y_1} & \tuple{x_2, y_2} & \dots & \tuple{x_2, y_m}\}\\
  \vdots & & \vdots\\
  B_{x_n} = & \{\tuple{x_n, y_1} & \tuple{x_n, y_2} & \dots & \tuple{x_n, y_m}\}
\end{array}
\]
Since the $x_i$ are all different, and the $y_j$ are all different, no
two of the pairs in this grid are the same, and there are $n\cdot m$
of them.
\end{proof}
```

Reviewed Persian:
```latex
برای تجسم این مطلب، !!{element}s~$A \times B$ را در جدولی بچینید:
\[
\begin{array}{rcccc}
  B_{x_1} = & \{\tuple{x_1, y_1} & \tuple{x_1, y_2} & \dots & \tuple{x_1, y_m}\}\\
  B_{x_2} = & \{\tuple{x_2, y_1} & \tuple{x_2, y_2} & \dots & \tuple{x_2, y_m}\}\\
  \vdots & & \vdots\\
  B_{x_n} = & \{\tuple{x_n, y_1} & \tuple{x_n, y_2} & \dots & \tuple{x_n, y_m}\}
\end{array}
\]
ازآنجاکه همهٔ $x_i$ها با یکدیگر و همهٔ $y_j$ها با یکدیگر متفاوت‌اند،
هیچ دو زوجی در این جدول یکسان نیستند و شمار آنها $n\cdot m$ است.
\end{proof}
```

All array cells, row names and first/second coordinate indices match the source. Since each row and column label is distinct, no two table entries coincide; the final count is n times m. هیچ دو زوجی correctly uses a singular counted noun.

Alternatives: Do not confuse visually arranged rows with an intrinsic order on the product set.

## FA-0009-C13: Power-cardinality induction exercise

Action: correct; confidence 3/3: Direct source comparison and actual canon construction agree.
Canon: FA-OL-CANON-0003:P0062, FA-OL-CANON-0005:P0090.

Source:
```latex
\begin{prob}
Show, by induction on~$k$, that for all $k \ge 1$, if $A$ has $n$
!!{element}s, then $A^k$ has $n^k$ !!{element}s.
\end{prob}
```

Reviewed Persian:
```latex
\begin{prob}
با استقرا روی~$k$ نشان دهید که برای هر $k \ge 1$، اگر $A$ دارای
$n$ !!{element} باشد، آنگاه $A^k$ دارای $n^k$ !!{element} است.
\end{prob}
```

استقرا is the proof method, with k at least one and every indicated exponent unchanged. Correct both counted nouns after n and n to power k. For an empty A and positive k the count is zero; the excluded k=0 ambiguity is not imported.

Alternatives: Do not weaken the quantified k bound or replace ordered powers with power sets.

## FA-0009-C14: Finite words, length and representational collision

Action: correct; confidence 2/3: Mathematical content is checked; the exact-register limitation is stated.
Canon: FA-OL-CANON-0003:P0046, FA-OL-CANON-0005:P0090, FA-OL-CANON-0003:P0014.

Source:
```latex
\begin{ex}
If $A$ is a set, a \emph{word} over~$A$ is any sequence of
!!{element}s of~$A$. A sequence can be thought of as an $n$-tuple of
!!{element}s of~$A$. For instance, if $A = \{a, b, c\}$, then the
sequence ``$bac$'' can be thought of as the triple~$\tuple{b, a, c}$.
Words, i.e., sequences of symbols, are of crucial importance in
computer science. By convention, we count !!{element}s of~$A$ as
sequences of length~$1$, and $\emptyset$ as the sequence of length~$0$.
The set of \emph{all} words over~$A$ then is
\[
A^* = \{\emptyset\} \cup A \cup A^2 \cup A^3 \cup \dots
\]
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}
اگر $A$ مجموعه‌ای باشد، \emph{واژه‌ای} بر روی~$A$ هر دنبالهٔ متناهی از
!!{element}s~$A$ است. می‌توان یک دنباله را $n$-تایی‌ای از
!!{element}s~$A$ دانست. برای نمونه، اگر $A = \{a, b, c\}$، آنگاه
دنبالهٔ ``$bac$'' را می‌توان سه‌تایی~$\tuple{b, a, c}$ دانست.
واژه‌ها، یعنی دنباله‌های نمادها، در علوم رایانه اهمیتی اساسی دارند.
طبق قرارداد، !!{element}s~$A$ را دنباله‌هایی به طول~$1$ و
$\emptyset$ را دنباله‌ای به طول~$0$ می‌شماریم. با این قراردادِ نمایشی، مجموعهٔ
\emph{همهٔ} واژه‌ها بر روی~$A$ را چنین می‌نویسیم\footnote{یادداشت ویراستاری: در این مثال، دنباله‌ها متناهی‌اند و طول، بخشی از مشخصات هر واژه است. فرمول زیر را باید اختصاری برای گردآوردن واژه‌های همهٔ طول‌ها دانست، نه تساویِ بی‌قیدوشرط میان کدهای مجموعه‌ایِ معرفی‌شده در بالا. برای الفبای دلخواه، برخوردِ کدها ممکن است رخ دهد: اگر مجموعهٔ تهی حرفی از الفبا باشد، کدِ واژهٔ تهی و کدِ واژهٔ تک‌حرفیِ آن یکسان است. همچنین اگر کدِ زوج مرتبِ دو حرف از الفبا نیز در الفبا باشد، کدِ واژهٔ تک‌حرفیِ آن زوج با کدِ واژهٔ دوحرفیِ متناظر یکسان است؛ آن دو حرف لازم نیست متمایز باشند. در تعریف دقیق، هر واژه را تابعی از یک قطعهٔ آغازینِ متناهی از اعداد طبیعی به الفبا می‌گیریم. دامنهٔ تابع طول را مشخص می‌کند؛ واژهٔ تهی تابعِ تهی است و با واژهٔ تک‌حرفی‌ای که حرف آن مجموعهٔ تهی است، تفاوت دارد. این همان قراردادِ طول‌دار برای رشته‌های متناهی است.}:
\[
A^* = \{\emptyset\} \cup A \cup A^2 \cup A^3 \cup \dots
\]
\end{ex}
```

The definition is explicitly finite, as its n-tuple examples and A-star enumeration require. واژه preserves the source word/string distinction while acknowledging the synonym relationship to the earlier string section. The source’s untagged codes can collide across lengths for arbitrary set alphabets. The displayed formula is preserved as an explicitly qualified representational shorthand, not endorsed as a literal unconditional equality of those raw code sets. A visible editorial note supplies the rigorous finite-function representation: domain is the finite initial natural-number segment, which distinguishes lengths, including empty word versus the one-letter word whose symbol is empty set.

Alternatives: Do not solve the collision by excluding the empty alphabet or the empty-set symbol. Do not silently replace source formulas or claim the old raw union is a disjoint union.

Expert-review question: Exact واژه terminology remains provisionally justified by definition and disciplinary context; the finite-function construction itself is directly supported by the canon.

## Validation boundary

Every substantive source and target character lies in an ordered non-overlapping reviewed span. Formal tokens are checked across inline, bracketed, multline and align mathematics. Text arguments in mathematics are separately aligned and manually reviewed for exact connective, quantifier and number-family meaning.
Finite tests support the written reasoning; they are not universal formal proofs. No new PDF was built or visually certified. Frozen owner inputs and reader releases are unchanged; corrections enter the owner’s normal next-batch build and visual QA.
Attribution: Open Logic Project and contributors, under existing CC BY 4.0 notices. https://github.com/OpenLogicProject/OpenLogic . Existing edition: https://github.com/KokunoYumeto/OpenLogic-fa-ir . Canon sources retain separate rights.
