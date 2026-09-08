# Persian OpenLogic: Subsets and Power Sets - expert review record

Complete section review: 15 aligned choices; one grammatical-number correction at two occurrences. This is a reviewed source candidate, not a newly released reader.

Evidence was obtained retrospectively; no original translation-time consultation is asserted. Confidence uses editorial0-3, not probabilities. Human response is welcome but not a gate.

## Review priorities

- C15: counted-member inflection corrected locally; global plural vocabulary is untouched.
- C01/C12: nominal versus adjectival power-set terminology; exact adjectival attestation not claimed.
- C04: source finite-set examples presume distinct labels; no transcription defect alleged.

## Canon actually consulted

نظریهٔ مجموعه‌ها, محسن خانی, افشین زارعی, دانشگاه صنعتی اصفهان. [University-hosted source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/jozve-kamel.pdf). PDF SHA-256 `dbd518c80232921264ab5d79b79be01fe42efe8c01a766327db248b2d261de04`. The privately retained PDF is not redistributed.

- FA-OL-CANON-0003:P0007: PDF page7, printed6; Bounded-quantifier notation immediately before section1.2.1. The two expansions use implication for universal and conjunction for existential restriction.

- FA-OL-CANON-0003:P0010: PDF page10, printed9; Bottom third, membership-based inclusion definition for classes. Class inclusion supplies the membership condition; it does not assert arbitrary set existence.

- FA-OL-CANON-0003:P0019: PDF page19, printed18; Section1.4, axiom1. The extensionality formula fixes equality by identical membership.

- FA-OL-CANON-0003:P0020: PDF page20, printed19; First paragraph, axiom6. Every subset is included in the collection which the axiom asserts is a set; the exact adjectival توانی is not attested here.

- FA-OL-CANON-0003:P0024: PDF page24, printed23; Definition5 near the bottom. Actual native counted-noun syntax; not a general published grammar theorem.

- FA-OL-CANON-0003:P0027: PDF page27, printed26; Proof of lemma14, proper-inclusion contradiction. Properness is witnessed by an outside element; do not import its well-ordering hypotheses into the elementary definition.

- FA-OL-CANON-0003:P0062: PDF page62, printed61; Section6.1, paragraph introducing [A]^n. Counted-set terminology is explicitly tied to |b|=n; supports the contextual counted-member decision.

## FA-0006-C01: Section heading

Action: retain_after_fresh_review. Confidence: 2/3. Canon: FA-OL-CANON-0003:P0020, FA-OL-CANON-0003:P0027.

Source:
```latex
\olsection{Subsets and Power Sets}
```

Persian reviewed candidate:
```latex
\olsection{زیرمجموعه‌ها و مجموعه‌های توانی}
```

Page20 directly attests مجموعه‌ی توان and all subsets; page27 directly attests زیرمجموعه‌ی سره. The plural adjectival heading مجموعه‌های توانی is a supported contextual editorial choice, not an exact phrase established by the cited canon. Preserve it provisionally because meaning is clear and no contrary requirement was found; do not claim additional unattested usage.

Meaningful alternatives: No material competing alternative was recorded; none invented.

Expert-review note: Register preference: the selected witness uses مجموعه‌ی توان rather than the exact adjectival توانی. Consider consistency with further attested disciplinary usage when available; this is not a human-dependent gate.

## FA-0006-C02: Membership comparison introduction

Action: retain_after_fresh_review. Confidence: 2/3. Canon: FA-OL-CANON-0003:P0010.

Source:
```latex
\begin{explain}
We will often want to compare sets. And one obvious kind of comparison
one might make is as follows: \emph{everything in one set is in the
other too}. This situation is sufficiently important for us to
introduce some new notation.
\end{explain}
```

Persian reviewed candidate:
```latex
\begin{explain}
اغلب می‌خواهیم مجموعه‌ها را با یکدیگر مقایسه کنیم. یک مقایسهٔ آشکار
می‌تواند چنین باشد: \emph{هر آنچه در یک مجموعه است، در مجموعهٔ دیگر
نیز هست}. این وضعیت آن‌قدر مهم است که برای آن نمادگذاری تازه‌ای
معرفی کنیم.
\end{explain}
```

The Persian sentence expresses every object in the first set being in the other, with no reversal or equality claim. The introduction's adult prose motivates the notation without deleting content. Canon's membership-based inclusion formula supports the mathematical construction; ordinary linking phrases are editorial applications, not falsely claimed quotations.

Meaningful alternatives: No material competing alternative was recorded; none invented.

## FA-0006-C03: Subset, negation and proper subset definition

Action: retain_after_fresh_review. Confidence: 3/3. Canon: FA-OL-CANON-0003:P0010, FA-OL-CANON-0003:P0027.

Source:
```latex
\begin{defn}[Subset]
If every !!{element} of a set $A$ is also !!a{element} of~$B$, then we
say that $A$ is a \emph{subset} of~$B$, and write $A \subseteq B$. If
$A$ is not a subset of~$B$ we write $A \not\subseteq B$.
If $A \subseteq B$ but $A \neq B$, we write $A \subsetneq B$ and say
that $A$ is a \emph{proper subset} of $B$.
\end{defn}
```

Persian reviewed candidate:
```latex
\begin{defn}[زیرمجموعه]
اگر هر !!{element} مجموعهٔ $A$، !!a{element} مجموعهٔ~$B$ نیز باشد،
می‌گوییم $A$ \emph{زیرمجموعهٔ}~$B$ است و می‌نویسیم $A \subseteq B$.
اگر $A$ زیرمجموعهٔ~$B$ نباشد، می‌نویسیم $A \not\subseteq B$.
اگر $A \subseteq B$ اما $A \neq B$، می‌نویسیم $A \subsetneq B$ و
می‌گوییم $A$ \emph{زیرمجموعهٔ سرهٔ} $B$ است.
\end{defn}
```

All three cases remain: inclusion, failure of inclusion, and inclusion together with inequality. زیرمجموعهٔ سره is directly attested on page27 in a context where properness is witnessed by an element outside the subset. Page10's inclusion formula is presented for classes; its membership condition applies to sets without importing class-comprehension or existence assumptions. Target symbols ⊆, not⊆ and ⊊ remain distinct.

Meaningful alternatives: عضو would confuse subsethood with membership. Dropping A≠B would turn proper subset into non-strict inclusion.

## FA-0006-C04: Reflexive, empty and finite subset examples

Action: retain_after_fresh_review. Confidence: 2/3. Canon: FA-OL-CANON-0003:P0010, FA-OL-CANON-0003:P0027.

Source:
```latex
Every set is a subset of itself, and $\emptyset$ is a subset of every
set. The set of natural even numbers is a subset of the set of natural
numbers. Also, $\{ a, b \} \subseteq \{ a, b, c \}$. But $\{ a, b, e
\}$ is not a subset of $\{ a, b, c \}$.
```

Persian reviewed candidate:
```latex
هر مجموعه زیرمجموعهٔ خودش است و $\emptyset$ زیرمجموعهٔ هر مجموعه است.
مجموعهٔ اعداد طبیعی زوج زیرمجموعهٔ مجموعهٔ اعداد طبیعی است. همچنین
$\{ a, b \} \subseteq \{ a, b, c \}$. اما $\{ a, b, e
\}$ زیرمجموعهٔ $\{ a, b, c \}$ نیست.
```

Self-inclusion, empty-set inclusion and the natural-even example are retained. Literal element lists match. The final non-inclusion example presumes e is distinct from a,b,c; the English source leaves the ordinary distinct-label convention implicit too. No translation error is alleged and no source transcription report is warranted.

Meaningful alternatives: No material competing alternative was recorded; none invented.

Expert-review note: Optional editorial note if a later consistency pass chooses to spell out the distinct-label convention across all finite-set examples. The current convention is recorded, not mistaken for a universal statement under arbitrary assignments.

## FA-0006-C05: Membership versus subsethood and nested sets

Action: retain_after_fresh_review. Confidence: 3/3. Canon: FA-OL-CANON-0003:P0010, FA-OL-CANON-0003:P0020.

Source:
```latex
The number $2$ is an !!{element} of the set of integers, whereas the
set of even numbers is a subset of the set of integers. However, a set
may happen to \emph{both} be !!a{element} and a subset of some other
set, e.g., $\{0\} \in \{0, \{0\}\}$ and also $\{0\} \subseteq \{0,
\{0\}\}$.
```

Persian reviewed candidate:
```latex
عدد $2$ یک !!{element} مجموعهٔ اعداد صحیح است، درحالی‌که مجموعهٔ
اعداد زوج زیرمجموعهٔ مجموعهٔ اعداد صحیح است. بااین‌حال، ممکن است
مجموعه‌ای \emph{هم} !!a{element} و هم زیرمجموعهٔ مجموعه‌ای دیگر باشد؛
برای نمونه، $\{0\} \in \{0, \{0\}\}$ و نیز $\{0\} \subseteq \{0,
\{0\}\}$.
```

The number2 is a member while the set of even integers is a subset. The nested example says {0} can be both a member and a subset of {0,{0}}. Both distinctions and both displayed relations survive. The source membership/inclusion definitions justify the contextual interpretation; the specific nested example is checked against source, not claimed as a canon quotation.

Meaningful alternatives: Rendering both relations as membership would erase the teaching point.

## FA-0006-C06: Extensionality and the two halves of equality

Action: retain_after_fresh_review. Confidence: 3/3. Canon: FA-OL-CANON-0003:P0010, FA-OL-CANON-0003:P0019.

Source:
```latex
Extensionality gives a criterion of identity for sets: $A = B$ iff
every !!{element} of~$A$ is also !!a{element} of~$B$ and vice versa.
The definition of ``subset'' defines $A \subseteq B$ precisely as the
first half of this criterion: every !!{element} of~$A$ is also
!!a{element} of~$B$. Of course the definition also applies if we
switch $A$ and $B$: that is, $B \subseteq A$ iff every !!{element}
of~$B$ is also !!a{element} of~$A$. And that, in turn, is exactly the
``vice versa'' part of extensionality. In other words, extensionality
entails that sets are equal iff they are subsets of one another.
```

Persian reviewed candidate:
```latex
اصل گسترش ملاکی برای یکسانی مجموعه‌ها به دست می‌دهد: $A = B$ اگر و
تنها اگر هر !!{element} مجموعهٔ~$A$، !!a{element} مجموعهٔ~$B$ نیز باشد
و برعکس. تعریف «زیرمجموعه» عبارت $A \subseteq B$ را دقیقاً به‌منزلهٔ
نیمهٔ نخست این ملاک تعریف می‌کند: هر !!{element} مجموعهٔ~$A$،
!!a{element} مجموعهٔ~$B$ نیز هست. البته اگر جای $A$ و $B$ را عوض کنیم،
این تعریف همچنان برقرار است؛ یعنی $B \subseteq A$ اگر و تنها اگر هر
!!{element} مجموعهٔ~$B$، !!a{element} مجموعهٔ~$A$ نیز باشد. این نیز
دقیقاً بخش «و برعکس» در اصل گسترش است. به بیان دیگر، از اصل گسترش
نتیجه می‌شود که دو مجموعه برابرند اگر و تنها اگر زیرمجموعهٔ یکدیگر باشند.
```

The target preserves first A⊆B and then B⊆A, the swap of variables, and iff. No existential inference from extensionality is made here, unlike the earlier opening clarification. Page19 supplies the extensionality formula; page10 supplies inclusion. ملاک/یکسانی expresses the source's criterion of identity, not an identity-function or bijection claim.

Meaningful alternatives: No material competing alternative was recorded; none invented.

## FA-0006-C07: Mutual-inclusion proposition

Action: retain_after_fresh_review. Confidence: 3/3. Canon: FA-OL-CANON-0003:P0010, FA-OL-CANON-0003:P0019.

Source:
```latex
\begin{prop}
$A = B$ iff both $A \subseteq B$ and $B \subseteq A$.
\end{prop}
```

Persian reviewed candidate:
```latex
\begin{prop}
$A = B$ اگر و تنها اگر هم $A \subseteq B$ و هم $B \subseteq A$.
\end{prop}
```

Both inclusions are connected by هم ... و هم and the biconditional remains. Equality is equivalent to mutual inclusion, not either inclusion alone. The same justified rule as C06 is contextually applied to the proposition.

Meaningful alternatives: یا instead of و would make the proposition false.

## FA-0006-C08: Preparing bounded-quantifier notation

Action: retain_after_fresh_review. Confidence: 2/3. Canon: FA-OL-CANON-0003:P0007.

Source:
```latex
Now is also a good opportunity to introduce some further bits of
helpful notation. In defining when $A$ is a subset of~$B$ we said that
``every !!{element} of~$A$ is \dots,'' and filled the ``$\dots$'' with
``!!a{element} of $B$''. But this is such a common \emph{shape} of
expression that it will be helpful to introduce some formal notation
for it.
```

Persian reviewed candidate:
```latex
اکنون فرصت مناسبی است تا چند نماد سودمند دیگر نیز معرفی کنیم. در تعریف
زیرمجموعه‌بودن $A$ از~$B$ گفتیم «هر !!{element} مجموعهٔ~$A$، \dots»
و جای «$\dots$» را با «!!a{element} مجموعهٔ $B$» پر کردیم. اما این
\emph{ساختار} عبارت چنان پرکاربرد است که بهتر است نمادگذاری صوری‌ای
برای آن معرفی کنیم.
```

The target explains filling an expression pattern and calls it ساختار عبارت, avoiding literal shape as a geometric notion. Page7 explains the same shortcut-notation practice for bounded quantification. The source's ellipsis is mentioned as notation, not an omitted translated clause.

Meaningful alternatives: Treating the quoted dots as a placeholder would misclassify intentionally explained notation.

## FA-0006-C09: Universal and existential restricted quantifiers

Action: retain_after_fresh_review. Confidence: 3/3. Canon: FA-OL-CANON-0003:P0007.

Source:
```latex
\begin{defn}\ollabel{forallxina}
$(\forall x \in A)\phi$ abbreviates $\forall x(x \in A \lif
\phi)$. Similarly, $(\exists x \in A)\phi$ abbreviates $\exists x(x
\in A \land \phi)$. 
\end{defn}
```

Persian reviewed candidate:
```latex
\begin{defn}\ollabel{forallxina}
$(\forall x \in A)\phi$ صورت اختصاریِ $\forall x(x \in A \lif
\phi)$ است. به همین ترتیب، $(\exists x \in A)\phi$ صورت اختصاریِ
$\exists x(x \in A \land \phi)$ است.
\end{defn}
```

The native canon explicitly expands the universal restriction with implication and existential restriction with conjunction. The target keeps exactly these two different connectives, variable binding, phi scope and the forallxina label. صورت اختصاری expresses an abbreviation, not an extra logical axiom. In particular empty-domain universal truth is preserved.

Meaningful alternatives: Using conjunction under ∀ or implication under ∃ would change the semantics.

## FA-0006-C10: Subset abbreviation using restricted forall

Action: retain_after_fresh_review. Confidence: 3/3. Canon: FA-OL-CANON-0003:P0007, FA-OL-CANON-0003:P0010.

Source:
```latex
Using this notation, we can say that $A \subseteq B$ iff $(\forall
x \in A)x \in B$. 
```

Persian reviewed candidate:
```latex
با این نمادگذاری می‌توانیم بگوییم $A \subseteq B$ اگر و تنها اگر
$(\forall x \in A)x \in B$.
```

This is precisely C03's membership condition expressed with C09's abbreviation. The target uses iff and quantifies over the smaller setA. Whitespace differs inside the formula but symbol order and meaning do not.

Meaningful alternatives: No material competing alternative was recorded; none invented.

## FA-0006-C11: Transition to the set of subsets

Action: retain_after_fresh_review. Confidence: 3/3. Canon: FA-OL-CANON-0003:P0020.

Source:
```latex
Now we move on to considering a certain kind of set: the set of all
subsets of a given set. 
```

Persian reviewed candidate:
```latex
اکنون به بررسی نوع خاصی از مجموعه می‌پردازیم: مجموعهٔ همهٔ
زیرمجموعه‌های یک مجموعهٔ داده‌شده.
```

The target preserves all subsets of a specified set and does not change subsets into elements. The native power-set statement provides exactly this construction. مجموعهٔ داده‌شده is a contextual mathematical expression, not an assertion that the set is algorithmically computable.

Meaningful alternatives: No material competing alternative was recorded; none invented.

## FA-0006-C12: Power-set definition

Action: retain_after_fresh_review. Confidence: 2/3. Canon: FA-OL-CANON-0003:P0020.

Source:
```latex
\begin{defn}[Power Set]
The set consisting of all subsets of a set~$A$ is called the
\emph{power set of}~$A$, written $\Pow{A}$.
  \[
    \Pow{A} = \Setabs{B}{B \subseteq A} 
  \]
\end{defn}
```

Persian reviewed candidate:
```latex
\begin{defn}[مجموعهٔ توانی]
مجموعه‌ای که از همهٔ زیرمجموعه‌های مجموعهٔ~$A$ تشکیل شده است،
\emph{مجموعهٔ توانیِ}~$A$ نام دارد و آن را $\Pow{A}$ می‌نویسند.
  \[
    \Pow{A} = \Setabs{B}{B \subseteq A}
  \]
\end{defn}
```

The native power-set axiom defines a set of all subsets, and OLP supplies the exact Pow/Setabs notation. The meaning and variable scope are preserved. The selected native witness attests مجموعه‌ی توان, not the exact adjectival form مجموعهٔ توانی; retain the intelligible current form as an explicitly documented editorial variant, linked to C01, without inventing an exact attestation.

Meaningful alternatives: No material competing alternative was recorded; none invented.

Expert-review note: Shared with C01: exact nominal versus adjectival power-set terminology remains a documented register choice, not a mathematical uncertainty.

## FA-0006-C13: Eight subsets of a three-element set

Action: retain_after_fresh_review. Confidence: 3/3. Canon: FA-OL-CANON-0003:P0020.

Source:
```latex
What are all the possible subsets of $\{ a, b, c \}$? They are:
$\emptyset$, $\{a \}$, $\{b\}$, $\{c\}$, $\{a, b\}$, $\{a, c\}$, $\{b,
c\}$, $\{a, b, c\}$. The set of all these subsets is
$\Pow{\{a,b,c\}}$:
\[
\Pow{\{ a, b, c \}} = \{\emptyset, \{a \}, \{b\}, \{c\}, \{a, b\},
\{b, c\}, \{a, c\}, \{a, b, c\}\}
\]
```

Persian reviewed candidate:
```latex
همهٔ زیرمجموعه‌های ممکنِ $\{ a, b, c \}$ کدام‌اند؟ این زیرمجموعه‌ها
عبارت‌اند از: $\emptyset$، $\{a \}$، $\{b\}$، $\{c\}$، $\{a, b\}$،
$\{a, c\}$، $\{b,
c\}$، $\{a, b, c\}$. مجموعهٔ همهٔ این زیرمجموعه‌ها
$\Pow{\{a,b,c\}}$ است:
\[
\Pow{\{ a, b, c \}} = \{\emptyset, \{a \}, \{b\}, \{c\}, \{a, b\},
\{b, c\}, \{a, c\}, \{a, b, c\}\}
\]
```

Both the prose list and display contain exactly the empty set, three singletons, three pairs and full set. The pair order differs between prose/display in both languages and is immaterial for sets. All symbols preserved. The mathematical check assumes a,b,c distinct as the source convention does; finite enumeration supplies a contextual check, not a substitute for source reading.

Meaningful alternatives: No material competing alternative was recorded; none invented.

## FA-0006-C14: Four-element enumeration exercise

Action: retain_after_fresh_review. Confidence: 3/3. Canon: FA-OL-CANON-0003:P0020.

Source:
```latex
List all subsets of $\{a, b, c, d\}$.
```

Persian reviewed candidate:
```latex
همهٔ زیرمجموعه‌های $\{a, b, c, d\}$ را فهرست کنید.
```

The imperative فهرست کنید asks for listing all subsets, not proving existence or selecting only proper subsets. The four source labels and the universal all remain. No exercise or answer is omitted or supplied in place of the requested exercise.

Meaningful alternatives: No material competing alternative was recorded; none invented.

## FA-0006-C15: Finite power-set cardinality exercise

Action: correct_counted_noun_inflection. Confidence: 2/3. Canon: FA-OL-CANON-0003:P0020, FA-OL-CANON-0003:P0024, FA-OL-CANON-0003:P0062.

Source:
```latex
Show that if $A$ has $n$ !!{element}s, then $\Pow{A}$ has $2^n$
!!{element}s.
```

Persian reviewed candidate:
```latex
نشان دهید اگر $A$ دارای $n$ !!{element} باشد، آنگاه $\Pow{A}$ دارای
$2^n$ !!{element} است.
```

The source proof task and n-to-2^n conclusion are correct. Reading the actual locale configuration reveals that the two English plural markers realize as اعضا, yielding دارای n اعضا and دارای 2^n اعضا. Use the singular token عضو after each explicit count, without changing the shared plural definition, the numbers or the mathematics. Page24 supplies actual دو عنصر counted-noun syntax; page62 supplies mathematical n عضوی terminology and binds it to |b|=n. These are usage witnesses supporting the contextual inflection decision, not a quoted general grammar rule nor a claim that the exact corrected sentence appears there. The unchanged ordinary plural اعضا remains appropriate when no explicit cardinal count governs it.

Meaningful alternatives: Keep the plural markers: carries English grammatical number into this Persian counted expression. Change the global element plural to عضو: would break correctly plural contexts elsewhere. Rewrite using مجموعه‌ای nعضوی: source-faithful and attested construction, but unnecessary for this two-token inflection repair.

Expert-review note: Editorial confidence2/3: source mathematics is unambiguous; counted-noun inflection is justified from native disciplinary usage. Later reviewers may prefer an nعضوی construction. No response is required before normal owner integration.

## Checks and boundaries

50 explicit checks pass; 65 formula spans preserve source symbols. Every substantive source and target character lies in an aligned reviewed span. Member-token inflection is the sole authorized marker difference. No English-source erratum is claimed. Full-corpus or current PDF visual acceptance does not follow from this section audit.

OpenLogic source and adaptation are attributed to the Open Logic Project and its contributors, under its CC BY 4.0 notices. Source: https://github.com/OpenLogicProject/OpenLogic. Existing edition: https://github.com/KokunoYumeto/OpenLogic-fa-ir. Canon references remain separately licensed.
