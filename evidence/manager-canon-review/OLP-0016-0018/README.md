# Persian OpenLogic: orders, directed graphs and trees

Complete source/target review of three frozen sections, with nine Persian scholarly page images actually read in this review. Consultation is retrospective, not a claim about the original translation workflow. These are source-preserving integration candidates and a human-readable review register, not a new compiled reader. Definitions in OpenLogic govern even where the consulted Persian textbooks use other conventions.

## Review priorities

- Preserve strict/nonstrict order, graph carrier sets, rooted well-ordered trees, maximal branches and immediate predecessors without conflating their definitions.
- Repair three evidenced source issues: alphabet-size qualification for nonlinear prefix order; undefined X in the branch condition; nonempty prefix-closed subtree requirement.
- Apply directly attested پادبازتابی consistently and explain order comparability without importing graph-path connectedness.
- Preserve all formula and diagram tokens except the single explicitly recorded X-to-A domain correction. Keep exercises unsolved and record lexical uncertainties for later expert review.
- Confidence is editorial 0-3, not calibrated probability. Human review is a later opportunity, not a gate.

## Scholarly pages actually consulted

- نظریهٔ مجموعه‌ها; محسن خانی, افشین زارعی; دانشگاه صنعتی اصفهان. [Source](https://khani.iut.ac.ir/sites/khani.iut.ac.ir/files//u145/jozve-kamel.pdf). PDF SHA-256: dbd518c80232921264ab5d79b79be01fe42efe8c01a766327db248b2d261de04. Canon PDFs are privately retained, not redistributed.
- ریاضیات گسسته و کاربردها; علیرضا غفاری حدیقه, مگردیچ تومانیان; مؤسسه چاپ و انتشارات دانشگاه جامع امام حسین (ع). [Source](https://hadigheha.github.io/books/teaching/Textbooks/Tarkibiyat.pdf). PDF SHA-256: 8f79c45a926c1cea819c4fefa86383f2a65ae23b1d526baaf99cf2506bb9f317. Canon PDFs are privately retained, not redistributed.
- FA-OL-CANON-0003:P0023, PDF 23, printed 22: Chapter2 definition1: strict order, linear comparability and well-ordering. Direct universal non-diagonal formula supports پادبازتابی. The notes use a strict-order convention and متعدی, whereas OpenLogic also defines reflexive preorders and partial orders. Do not copy the canon definition over the source.
- FA-OL-CANON-0003:P0024, PDF 24, printed 23: Observation2 and definition3: successors, initial parts and well-ordered sets. Context for initial segments and immediate-successor vocabulary in well-orders. بخش ابتدایی and تالی are printed; the target compounds قطعهٔ آغازین and جانشین are not claimed verbatim attestations. Well-orders need not give every noninitial element an immediate predecessor.
- FA-OL-CANON-0003:P0064, PDF 64, printed 63: Definition5, example6 and tree/subtree/branch definitions. Direct tree/subtree/branch vocabulary. This canon allows an arbitrary well-ordered chain as a branch and does not require a single root. OpenLogic requires a root and maximal chains. Preserve the latter definitions, explicitly resisting terminology-induced mathematical drift.
- FA-OL-CANON-0003:P0065, PDF 65, printed 64: Remark3 and lemma7: infinite height and branching. Contextual set-theoretic register for infinite height and branching. The remark distinguishes height omega from a node at height omega, and lemma7 concerns cardinal bounds. It is not a statement or proof of König’s lemma, and it does not directly attest با انشعاب متناهی.
- FA-REL-P053, PDF 53, printed 43: Binary relations and arrow diagrams. Directly describes an arrow x to y as x related to y, and uses a pair for carrier plus relation. Supports orientation, graph/relation connection and diagram prose, not a new definition of all graph types.
- FA-REL-P055, PDF 55, printed 45: Relation properties, partial orders and comparability. Direct nonstrict partial-order definition and linear/total comparability, with divisibility and subset examples. It uses ترتیب کلی or خطی; the target synonym تام is retained provisionally. It does not establish همبند as an order-specific technical label.
- FA-REL-P101, PDF 101, printed 91: Chapter4 definitions and directed-graph example. Direct carrier/edge-pair definition and direction convention. Supports the core Persian graph terms and G=(V,E). The book’s undirected convention is not imported into OpenLogic’s directed definition.
- FA-REL-P102, PDF 102, printed 92: Graph diagrams, loops, parallel edges and isolated vertex. Direct graph presentation and isolated-vertex concept; the drawing includes a loop and an isolated vertex. منفرد is directly printed, while the target منزوی is a provisional synonymous label. The descriptive source discussion permits varied conventions; its later directed definition still uses an edge set, not a multiset.
- FA-REL-P113, PDF 113, printed 103: Connected and disconnected graph diagrams. Directly attests graph connectedness, not pairwise order comparability. Used as a contrast witness so OLP0016’s homographic همبند is explained in the order sense rather than misread as reachability by paths.

## FA-0016-C01: Title and classification motivation

Action: retain_after_fresh_review; confidence 2/3: Conceptual contrast and terminology are attested; this precise introductory syntax is a contextual scholarly-register judgement.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0023.

Source:
```latex
\olsection{Orders}

\begin{explain}
Many of our comparisons involve describing some objects as being
``less than'', ``equal to'', or ``greater than'' other objects, in a
certain respect. These involve \emph{order} relations. But there are
different kinds of order relations. For instance, some require that
any two objects be comparable, others don't. Some include identity
(like~$\le$) and some exclude it (like~$<$). It will help us to have a
taxonomy here.
\end{explain}
```

Reviewed Persian:
```latex
\olsection{ترتیب‌ها}

\begin{explain}
بسیاری از مقایسه‌های ما متضمن آن‌اند که اشیایی را، از جهتی معین،
«کوچک‌تر از»، «برابر با» یا «بزرگ‌تر از» اشیای دیگر وصف کنیم. این
مقایسه‌ها با روابط \emph{ترتیب} سروکار دارند. اما روابط ترتیب گونه‌های
متفاوتی دارند. برای نمونه، برخی ایجاب می‌کنند که هر دو شیءِ دلخواه با
یکدیگر مقایسه‌پذیر باشند و برخی چنین ایجابی ندارند. برخی همانی را در بر می‌گیرند
(مانند~$\le$) و برخی آن را کنار می‌گذارند (مانند~$<$). داشتن یک
رده‌بندی در اینجا سودمند خواهد بود.
\end{explain}
```

ترتیب‌ها and the comparison-based motivation fit both canon expositions. The source distinguishes equality-inclusive and strict comparisons and comparability requirements; all remain. The existing متضمن آن‌اند is formal Persian rather than the clearest ordinary-adult paraphrase, but this is the scholarly register lane, and no separate plain-Persian certification is claimed.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C02: Preorder

Action: retain_after_fresh_review; confidence 2/3: Exact definition preserved; lexical attestation gap exposed.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0023.

Source:
```latex
\begin{defn}[Preorder]
A relation which is both reflexive and transitive is called a
\emph{preorder.}  
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[پیش‌ترتیب]
رابطه‌ای که هم بازتابی و هم تراگذری باشد \emph{پیش‌ترتیب} نامیده
می‌شود.
\end{defn}
```

The two and only two requirements are reflexivity and transitivity. Retain پیش‌ترتیب as a transparent, explicitly defined compound. Neither selected page directly names preorders; do not import antisymmetry from the partial-order canon.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Locate further target-language attestation for پیش‌ترتیب; the present pages support its ingredients, not the compound.

## FA-0016-C03: Partial order

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P055.

Source:
```latex
\begin{defn}[Partial order]
A preorder which is also anti-symmetric is called a
\emph{partial order}.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[ترتیب جزئی]
پیش‌ترتیبی که پادمتقارن نیز باشد \emph{ترتیب جزئی} نامیده می‌شود.
\end{defn}
```

ترتیب جزئی and پادمتقارن are directly attested. Combined with the preceding preorder, the target has exactly the canon’s three nonstrict requirements.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C04: Linear order and comparability

Action: correct; confidence 2/3: Exact comparability and linear-order term attested; تام and order-specific همبند are not attested on these pages.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0023, FA-REL-P113.

Source:
```latex
\begin{defn}[Linear order]\ollabel{def:linearorder}
A partial order which is also connected is called a
\emph{total order} or \emph{linear order.}
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[ترتیب خطی]\ollabel{def:linearorder}
ترتیب جزئی‌ای که هر دو عضو متمایز آن مقایسه‌پذیر باشند (یعنی همبند باشد) \emph{ترتیب تام} یا
\emph{ترتیب خطی} نامیده می‌شود.
\end{defn}
```

Replace bare همبند with its exact local defining condition, every two distinct elements comparable, while retaining همبند in parentheses for consistency. The graph page attests a different connectivity concept and is a warning against semantic conflation. خطی is direct; تام remains an explicit synonym with provisional lexical support.

Alternatives: ترتیب کلی is directly attested; retaining source-aligned تام avoids an isolated global terminology change.

Expert-review question: Whole-lane choice between کلی and تام; current definition is unambiguous.

## FA-0016-C05: Universal-relation counterexample

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P055.

Source:
```latex
\begin{ex}
Every linear order is also a partial order, and every partial order is
also a preorder, but the converses don't hold. The universal relation
on~$A$ is a preorder, since it is reflexive and transitive. But, if
$A$ has more than one !!{element}, the universal relation is not
anti-symmetric, and so not a partial order.
\end{ex}

\begin{ex}
```

Reviewed Persian:
```latex
\begin{ex}
هر ترتیب خطی یک ترتیب جزئی نیز هست، و هر ترتیب جزئی یک پیش‌ترتیب نیز
هست، اما عکس این گزاره‌ها برقرار نیست. رابطهٔ جهان‌شمول روی~$A$ یک
پیش‌ترتیب است، زیرا بازتابی و تراگذری است. اما اگر $A$ بیش از یک
!!{element} داشته باشد، رابطهٔ جهان‌شمول پادمتقارن نیست و بنابراین
ترتیب جزئی نیست.
\end{ex}

\begin{ex}
```

Retain the hierarchy and its nonconverses. The universal relation fails antisymmetry only when the carrier has more than one element, exactly the source qualification. The element token remains governed by the existing Persian locale.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C06: Length preorder on binary words

Action: retain_after_fresh_review; confidence 2/3: Source-specific descriptive label, with exact formulas and counterexample retained.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0024.

Source:
```latex
Consider the \emph{no longer than} relation $\preccurlyeq$
on~$\Bin^*$: $x \preccurlyeq y$ iff $\len{x} \le \len{y}$. This is a
preorder (reflexive and transitive), and even connected, but not a
partial order, since it is not anti-symmetric. For instance, $01
\preccurlyeq 10$ and $10 \preccurlyeq 01$, but $01 \neq 10$.
\end{ex}

\begin{ex}
```

Reviewed Persian:
```latex
رابطهٔ \emph{طولانی‌تر نبودن} $\preccurlyeq$ را روی~$\Bin^*$ در نظر
بگیرید: $x \preccurlyeq y$ اگر و تنها اگر $\len{x} \le \len{y}$. این
رابطه یک پیش‌ترتیب (بازتابی و تراگذری) و حتی همبند است، اما ترتیب جزئی
نیست، زیرا پادمتقارن نیست. برای نمونه، $01
\preccurlyeq 10$ و $10 \preccurlyeq 01$، اما $01 \neq 10$.
\end{ex}

\begin{ex}
```

The explanatory label طولانی‌تر نبودن conveys length at most, not prefix extension. Preserve the iff, transitivity/reflexivity, comparability and the equal-length unequal strings01 and10. Canon support is relation/register context, not attestation of a standard name for this deliberately defined example.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C07: Subset partial order

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P055.

Source:
```latex
An important partial order is the relation $\subseteq$ on a set of
sets. This is not in general a linear order, since if $a \neq b$ and
we consider $\Pow{\{a, b\}} = \{\emptyset, \{a\}, \{b\}, \{a,b\}\}$,
we see that $\{a\} \nsubseteq \{b\}$ and $\{a\} \neq \{b\}$ and $\{b\}
\nsubseteq \{a\}$.
\end{ex}

\begin{ex}
```

Reviewed Persian:
```latex
یکی از ترتیب‌های جزئی مهم، رابطهٔ $\subseteq$ روی مجموعه‌ای از
مجموعه‌هاست. این رابطه در حالت کلی ترتیب خطی نیست، زیرا اگر $a \neq b$
و $\Pow{\{a, b\}} = \{\emptyset, \{a\}, \{b\}, \{a,b\}\}$ را در نظر
بگیریم، می‌بینیم که $\{a\} \nsubseteq \{b\}$ و
$\{a\} \neq \{b\}$ و $\{b\}
\nsubseteq \{a\}$.
\end{ex}

\begin{ex}
```

The canon gives subset inclusion as a partial order. Preserve every powerset member and both failed inclusions with distinct a,b; do not strengthen the source’s not-in-general qualification.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C08: Divisibility on naturals and integers

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P055.

Source:
```latex
The relation of \emph{divisibility without remainder} gives us a
partial order which isn't a linear order. For integers $n$ and~$m$, we
write $n \mid m$ to mean $n$ (evenly) divides $m$, i.e., iff there is
some integer~$k$ so that $m = kn$. On~$\Nat$, this is a partial order,
but not a linear order: for instance, $2 \nmid 3$ and also $3 \nmid
2$. Considered as a relation on $\Int$, divisibility is only a
preorder since it is not anti-symmetric: $1 \mid -1$ and $-1 \mid 1$
but $1 \neq -1$.
\end{ex}

\begin{ex}
```

Reviewed Persian:
```latex
رابطهٔ \emph{بخش‌پذیری بی‌باقی‌مانده} ترتیب جزئی‌ای به دست می‌دهد که
ترتیب خطی نیست. برای اعداد صحیح $n$ و~$m$، $n \mid m$ را به این معنا
می‌نویسیم که $n$، $m$ را (بی‌باقی‌مانده) تقسیم می‌کند؛ یعنی این رابطه
برقرار است اگر و تنها اگر عدد صحیحی~$k$ وجود داشته باشد که $m = kn$. این رابطه روی~$\Nat$
ترتیبی جزئی است، اما ترتیبی خطی نیست: برای نمونه، $2 \nmid 3$ و نیز
$3 \nmid
2$. اگر بخش‌پذیری را رابطه‌ای روی $\Int$ در نظر بگیریم، فقط یک
پیش‌ترتیب است، زیرا پادمتقارن نیست: $1 \mid -1$ و $-1 \mid 1$، اما
$1 \neq -1$.
\end{ex}

\begin{ex}
```

Direct بخش‌پذیری example supports the idiom and order classification. Source Nat may include zero, unlike the positive-integer canon example; retain the source domain and integer multiplier. Negative associates on Int make antisymmetry fail, while2 and3 witness nonlinearity on Nat.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C09: Prefix extension and missing alphabet qualification

Action: correct; confidence 2/3: Mathematical correction established by counterexamples and definition; lexical choices are contextual rather than verbatim attestations.
Canon: FA-OL-CANON-0003:P0024, FA-OL-CANON-0003:P0064, FA-REL-P055.

Source:
```latex
The \emph{extension} relation on a set of sequences~$A^*$ is the
following: $s \sqsubseteq s'$ iff $s = \emptyseq$ (the empty
sequence), $s = s'$, or $s = \tuple{s_1, \dots, s_n}$ and $s' =
\tuple{s_1, \dots, s_n, s_{n+1}, \dots, s_m}$. If $s \sqsubseteq s'$
we also say that $s$ is an \emph{initial segment} of~$s'$. The
extension relation on $A^*$ is a partial order but not a linear order,
e.g., if $a \neq b$, then $ab \not\sqsubseteq ba$ and $ba \not\sqsubseteq ab$.
\end{ex}
```

Reviewed Persian:
```latex
رابطهٔ \emph{امتداد} روی مجموعه‌ای از دنباله‌های~$A^*$ چنین است:
$s \sqsubseteq s'$ اگر و تنها اگر $s = \emptyseq$ (دنبالهٔ تهی)،
$s = s'$، یا $s = \tuple{s_1, \dots, s_n}$ و $s' =
\tuple{s_1, \dots, s_n, s_{n+1}, \dots, s_m}$. اگر $s \sqsubseteq s'$
باشد، می‌گوییم $s$ یک \emph{قطعهٔ آغازینِ}~$s'$ است. رابطهٔ امتداد
روی $A^*$ ترتیبی جزئی است؛ اگر الفبا دست‌کم دو عضو داشته باشد، ترتیبی خطی نیست. برای نمونه، اگر
$a \neq b$، آنگاه $ab \not\sqsubseteq ba$ و $ba \not\sqsubseteq ab$.
\emph{یادداشت ویراستاری:} قید اندازهٔ الفبا به ادعای متن مبدأ افزوده شد؛ برای الفبای تهی یا تک‌عضوی، رابطهٔ امتداد خطی است.
\end{ex}
```

Preserve the empty, equal and proper-prefix clauses and the direction s prefix of sprime. Initial-part canon supports the concept, not exact قطعهٔ آغازین or امتداد terminology. Explicitly qualify the nonlinearity claim by alphabet size at least two and disclose the source correction: the empty alphabet has only the empty word, while a singleton alphabet orders words by length.

Alternatives: بخش ابتدایی is directly printed in the well-order canon. قطعهٔ آغازین remains the existing clearly defined lane term.

Expert-review question: Confirm lane-wide preference for قطعهٔ آغازین versus بخش ابتدایی; do not change extension direction.

## FA-0016-C10: Strict order definition

Action: correct; confidence 2/3: Irreflexivity and order contrast are direct; asymmetry label remains provisional with exact defining condition inherited from prior section.
Canon: FA-OL-CANON-0003:P0023, FA-REL-P055.

Source:
```latex
\begin{defn}[Strict order]
A \emph{strict order} is a relation which is irreflexive, asymmetric,
and transitive.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[ترتیب اکید]
\emph{ترتیب اکید} رابطه‌ای است که پادبازتابی، نامتقارن و تراگذری باشد.
\end{defn}
```

Use directly attested پادبازتابی instead of ambiguous غیربازتابی, retaining asymmetry and transitivity even though one condition is logically redundant. This is universal failure of self-relatedness, not merely failure of reflexivity. اکید is directly used with strict inequality on the relation-property page. نامتقارن is a transparent existing label whose exact compound is not attested here.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C11: Strict linear order

Action: correct; confidence 2/3: Formal condition and خطی/اکید usage are direct; تام synonym remains provisional.
Canon: FA-OL-CANON-0003:P0023, FA-REL-P055, FA-REL-P113.

Source:
```latex
\begin{defn}[Strict linear order]\ollabel{def:strictlinearorder}
A strict order which is also connected is called a 
\emph{strict total order} or \emph{strict linear order.}
\end{defn}

\begin{ex}
```

Reviewed Persian:
```latex
\begin{defn}[ترتیب خطی اکید]\ollabel{def:strictlinearorder}
ترتیب اکیدی که هر دو عضو متمایز آن مقایسه‌پذیر باشند (یعنی همبند باشد) \emph{ترتیب تام اکید} یا
\emph{ترتیب خطی اکید} نامیده می‌شود.
\end{defn}

\begin{ex}
```

State the pairwise comparability condition explicitly as for nonstrict linear order. The target keeps both source synonyms and label, without requiring diagonal pairs in a strict relation.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C12: Examples of nonstrict/strict pairs

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0023.

Source:
```latex
$\le$ is the linear order corresponding to the strict linear
order~$<$. $\subseteq$ is the partial order corresponding to the
strict order~$\subsetneq$.
\end{ex}
```

Reviewed Persian:
```latex
$\le$ ترتیب خطیِ متناظر با ترتیب خطی اکید~$<$ است. $\subseteq$ ترتیب
جزئیِ متناظر با ترتیب اکید~$\subsetneq$ است.
\end{ex}
```

Keep le versus lt, subseteq versus subsetneq, and the corresponding linear/partial labels. Canon strict and nonstrict examples help check no inequality direction was swapped.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C13: Reflexive closure construction

Action: retain_after_fresh_review; confidence 2/3: Construction mathematically exact; lexical compound supported contextually only.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0023.

Source:
```latex
Any strict order $R$ on~$A$ can be turned into a partial order by
adding the diagonal $\Id{A}$, i.e., adding all the pairs~$\tuple{x,
x}$.  (This is called the \emph{reflexive closure} of~$R$.)
Conversely, starting from a partial order, one can get a strict order
by removing~$\Id{A}$. These next two results make this precise.
```

Reviewed Persian:
```latex
هر ترتیب اکید $R$ روی~$A$ را می‌توان با افزودن قطر $\Id{A}$، یعنی با
افزودن همهٔ زوج‌های~$\tuple{x,
x}$، به یک ترتیب جزئی تبدیل کرد. (این عمل \emph{بستار بازتابیِ}~$R$
نامیده می‌شود.) برعکس، با آغاز از یک ترتیب جزئی می‌توان از راه حذف
کردن~$\Id{A}$ یک ترتیب اکید به دست آورد. دو نتیجهٔ بعدی این مطلب را
دقیق می‌کنند.
```

Adding diagonal pairs gives the reflexive closure; removing them recovers a strict order. Preserve both directions. بستار بازتابی is descriptive lane terminology, not directly printed in these pages; its entire construction is explicit.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Further attestation of بستار بازتابی is desirable; the operation is unambiguously specified.

## FA-0016-C14: Strict-to-partial proposition

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0023.

Source:
```latex
\begin{prop}\ollabel{prop:stricttopartial}
If $R$ is a strict order on~$A$, then $R^+ = R \cup \Id{A}$ is a
partial order. Moreover, if $R$ is a strict linear order, then $R^+$ is 
a linear order.
\end{prop}
```

Reviewed Persian:
```latex
\begin{prop}\ollabel{prop:stricttopartial}
اگر $R$ ترتیبی اکید روی~$A$ باشد، آنگاه $R^+ = R \cup \Id{A}$ ترتیبی
جزئی است. افزون بر این، اگر $R$ ترتیبی خطی اکید باشد، آنگاه $R^+$
ترتیبی خطی است.
\end{prop}
```

Preserve carrier, union with identity, partial-order conclusion and additional linearity clause.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C15: Proof assumptions and targets

Action: correct; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0023.

Source:
```latex
\begin{proof}
Suppose $R$ is a strict order, i.e., $R \subseteq A^2$ and $R$ is
irreflexive, asymmetric, and transitive. Let $R^+ = R \cup \Id{A}$. We
have to show that $R^+$ is reflexive, anti-symmetric, and transitive.
```

Reviewed Persian:
```latex
\begin{proof}
فرض کنید $R$ ترتیبی اکید باشد؛ یعنی $R \subseteq A^2$ و $R$
پادبازتابی، نامتقارن و تراگذری باشد. بگذارید $R^+ = R \cup \Id{A}$.
باید نشان دهیم که $R^+$ بازتابی، پادمتقارن و تراگذری است.
```

Correct the same irreflexivity term here; retain all assumptions and exactly the three properties to be proved.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C16: Reflexivity proof

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P055.

Source:
```latex
$R^+$ is clearly reflexive, since $\tuple{x, x} \in \Id{A} \subseteq
R^+$ for all $x \in A$.
```

Reviewed Persian:
```latex
$R^+$ آشکارا بازتابی است، زیرا $\tuple{x, x} \in \Id{A} \subseteq
R^+$ برای هر $x \in A$.
```

The universal diagonal inclusion proves reflexivity; the target preserves for every x in A, not just an example.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C17: Antisymmetry proof

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0023.

Source:
```latex
To show $R^+$ is anti-symmetric, suppose for reductio that $R^+xy$ and
$R^+yx$ but $x \neq y$. Since $\tuple{x,y} \in R \cup \Id{A}$, but
$\tuple{x, y} \notin \Id{A}$, we must have $\tuple{x, y} \in R$, i.e.,
$Rxy$. Similarly,~$Ryx$. But this contradicts the assumption
that $R$ is asymmetric.
```

Reviewed Persian:
```latex
برای نشان‌دادن پادمتقارن‌بودن $R^+$، به برهان خلف فرض کنید $R^+xy$ و
$R^+yx$، اما $x \neq y$. چون $\tuple{x,y} \in R \cup \Id{A}$، ولی
$\tuple{x, y} \notin \Id{A}$، باید $\tuple{x, y} \in R$، یعنی
$Rxy$. به همین ترتیب،~$Ryx$. اما این با فرض نامتقارن‌بودن $R$ تناقض
دارد.
```

Both non-diagonal pairs must belong to R; this contradicts asymmetry. The inequality assumption and reductio are preserved. Do not substitute symmetry or irreflexivity for the contradiction actually used.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C18: Transitivity proof case split

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P055.

Source:
```latex
To establish transitivity, suppose that $R^+xy$ and $R^+yz$. If both
$\tuple{x, y} \in R$ and $\tuple{y,z} \in R$, then $\tuple{x, z} \in
R$ since $R$~is transitive. Otherwise, either $\tuple{x, y} \in
\Id{A}$, i.e., $x = y$, or $\tuple{y, z} \in \Id{A}$, i.e., $y = z$.
In the first case, we have that $R^+yz$ by assumption, $x = y$, hence
$R^+xz$. Similarly in the second case. In either case, $R^+xz$, thus,
$R^+$ is also transitive.
```

Reviewed Persian:
```latex
برای اثبات تراگذری، فرض کنید $R^+xy$ و $R^+yz$. اگر هر دو
$\tuple{x, y} \in R$ و $\tuple{y,z} \in R$ برقرار باشند، آنگاه $\tuple{x, z} \in
R$، زیرا $R$~تراگذری است. در غیر این صورت، یا $\tuple{x, y} \in
\Id{A}$، یعنی $x = y$، یا $\tuple{y, z} \in \Id{A}$، یعنی $y = z$؛
دست‌کم یکی از این دو حالت برقرار است.
در حالت نخست، بنا بر فرض $R^+yz$ را داریم و $x = y$؛ پس $R^+xz$. حالت
دوم نیز مشابه است. در هر دو حالت، $R^+xz$؛ بنابراین $R^+$ نیز تراگذری
است.
```

Retain the both-in-R case and either-diagonal case. Persian دست‌کم یکی prevents an exclusive-or reading; equality substitution in each case preserves the source proof. No omitted case is supplied as a disguised new theorem.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C19: Linearity extension clause

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0023.

Source:
```latex
Concerning the ``moreover'' clause, suppose that $R$ is also connected. 
So for all $x \neq y$, either $Rxy$ or~$Ryx$, i.e., either 
$\tuple{x, y} \in R$ or $\tuple{y, x} \in R$. Since $R \subseteq R^+$, 
this remains true of $R^+$, so $R^+$ is connected as well.
\end{proof}
```

Reviewed Persian:
```latex
دربارهٔ بند «افزون بر این»، فرض کنید $R$ همبند نیز باشد. پس برای هر
$x \neq y$، دست‌کم یکی از $Rxy$ و~$Ryx$ برقرار است؛ یعنی دست‌کم یکی از
$\tuple{x, y} \in R$ و $\tuple{y, x} \in R$ برقرار است. چون $R \subseteq R^+$، این امر دربارهٔ $R^+$
نیز همچنان برقرار است؛ پس $R^+$ نیز همبند است.
\end{proof}
```

Every distinct pair is related in one direction already in R and hence in its superset. The target retains the inclusive alternatives and does not assert graph-path connectivity.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C20: Partial-to-strict proposition and exercise

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P055, FA-OL-CANON-0003:P0023.

Source:
```latex
\begin{prop}\ollabel{prop:partialtostrict}
If $R$ is a partial order on~$A$, then $R^- = R \setminus \Id{A}$ is a
strict order. Moreover, if $R$ is a linear order, then $R^-$ is a strict 
linear order.
\end{prop}

\begin{proof}
This is left as an exercise.
\end{proof}

\begin{prob}
Give a proof of \olref[sfr][rel][ord]{prop:partialtostrict}. 
\end{prob}
```

Reviewed Persian:
```latex
\begin{prop}\ollabel{prop:partialtostrict}
اگر $R$ ترتیبی جزئی روی~$A$ باشد، آنگاه $R^- = R \setminus \Id{A}$
ترتیبی اکید است. افزون بر این، اگر $R$ ترتیبی خطی باشد، آنگاه $R^-$
ترتیبی خطی اکید است.
\end{prop}

\begin{proof}
اثبات این گزاره به‌عنوان تمرین واگذار می‌شود.
\end{proof}

\begin{prob}
برهانی برای \olref[sfr][rel][ord]{prop:partialtostrict} به دست دهید.
\end{prob}
```

Remove exactly the identity diagonal. The optional linear clause remains. The proof remains assigned as an exercise, and the separate exercise points to the exact proposition label; no solution is inserted.

Alternatives: No material alternative recorded; none invented.

## FA-0016-C21: Extensionality-like claim

Action: retain_after_fresh_review; confidence 2/3: Formal theorem exact; precise extensionality label not newly attested here.
Canon: FA-OL-CANON-0003:P0023, FA-REL-P055.

Source:
```latex
The following simple result establishes that strict linear orders
satisfy an extensionality-like property:

\begin{prop}\ollabel{prop:extensionality-strictlinearorders}
If $<$ is a strict linear order on $A$, then:
\[
  (\forall a, b \in A)((\forall x \in A)(x < a \liff x < b) \lif a = b).
\]
\end{prop}

\begin{proof}
```

Reviewed Persian:
```latex
نتیجهٔ سادهٔ زیر نشان می‌دهد که ترتیب‌های خطی اکید خاصیتی شبیه اصل
گسترش دارند:

\begin{prop}\ollabel{prop:extensionality-strictlinearorders}
اگر $<$ ترتیبی خطی اکید روی $A$ باشد، آنگاه:
\[
  (\forall a, b \in A)((\forall x \in A)(x < a \liff x < b) \lif a = b).
\]
\end{prop}

\begin{proof}
```

The claim concerns equality from identical strict lower sets, with all quantifiers and biconditional unchanged. اصل گسترش is retained as the lane’s earlier extensionality label; the selected pages support order context, not this exact axiom name.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Lane-wide evidence for the extensionality label remains with the set-theory opening review.

## FA-0016-C22: Final irreflexivity and comparability proof

Action: correct; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-OL-CANON-0003:P0023, FA-REL-P055.

Source:
```latex
Suppose $(\forall x \in A)(x < a \liff x < b)$. If $a < b$, then $a <
a$, contradicting the fact that $<$ is irreflexive; so $a \nless b$.
Exactly similarly, $b \nless a$. So $a = b$, as $<$ is connected.
\end{proof}
```

Reviewed Persian:
```latex
فرض کنید $(\forall x \in A)(x < a \liff x < b)$. اگر $a < b$، آنگاه
$a <
a$، که با پادبازتابی‌بودن $<$ تناقض دارد؛ پس $a \nless b$. درست به
همین ترتیب، $b \nless a$. پس $a = b$، زیرا $<$ همبند است.
\end{proof}
```

The first hypothesis gives a<a if a<b; irreflexivity excludes it. The symmetric argument excludes b<a, and comparability yields equality. Correct پادبازتابی here as well, preserving the whole argument rather than only the heading.

Alternatives: No material alternative recorded; none invented.

## FA-0017-C01: Title, graph roles and convention diversity

Action: correct; confidence 2/3: Core terminology is direct; the synonym and idiomatic intensity are contextual choices.
Canon: FA-REL-P101, FA-REL-P102, FA-REL-P053.

Source:
```latex
\olsection{Graphs}

A \emph{graph} is a diagram in which points---called ``nodes'' or
``vertices'' (plural of ``vertex'')---are connected by edges.  Graphs
are a ubiquitous tool in discrete mathematics and in computer science.
They are incredibly useful for representing, and visualizing,
relationships and structures, from concrete things like networks of
various kinds to abstract structures such as the possible outcomes of
decisions.  There are many different kinds of graphs in the literature
which differ, e.g., according to whether the edges are directed or
not, have labels or not, whether there can be edges from a node to the
same node, multiple edges between the same nodes, etc.  \emph{Directed
  graphs} have a special connection to relations.
```

Reviewed Persian:
```latex
\olsection{گراف‌ها}

\emph{گراف} نموداری است که در آن نقطه‌هایی---که «گره» یا «رأس» نامیده
می‌شوند---با یال‌ها به هم متصل‌اند. (واژهٔ انگلیسی \foreignlanguage{english}{vertices} جمعِ \foreignlanguage{english}{vertex} است.) گراف‌ها ابزاری فراگیر در
ریاضیات گسسته و علوم رایانه‌اند. آنها برای بازنمایی و تجسم روابط و
ساختارها بسیار سودمندند؛ از چیزهای عینی، مانند انواع گوناگون
شبکه‌ها، تا ساختارهای انتزاعی، مانند پیامدهای ممکن تصمیم‌ها. در منابع،
گونه‌های متفاوت بسیاری از گراف‌ها وجود دارند که، برای نمونه، از این
جهت‌ها با هم فرق می‌کنند: یال‌ها جهت‌دارند یا نه، برچسب دارند یا نه،
ممکن است یالی از یک گره به همان گره وجود داشته باشد یا نه، ممکن است
میان همان دو گره چند یال وجود داشته باشد یا نه، و مانند اینها.
\emph{گراف‌های جهت‌دار} پیوندی ویژه با روابط دارند.
```

گراف، رأس and یال are directly attested in the mathematical exposition. The introductory applications and different edge conventions are retained. Restore the omitted English lexical note that vertices is the plural of vertex; keep it visibly about English, not Persian morphology. بسیار سودمندند expresses incredibly useful idiomatically without the stiff به‌طرزی چشمگیر. گره is retained as an explicit synonym for the already defined point, not claimed directly attested on these pages.

Alternatives: رأس throughout is directly supported, but deleting the source’s second synonym would lose information.

## FA-0017-C02: Directed graph definition

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P101, FA-REL-P053.

Source:
```latex
\begin{defn}[Directed graph]
A \emph{directed graph} $G = \tuple{V, E}$ is a set of
\emph{vertices}~$V$ and a set of \emph{edges}~$E \subseteq V^2$.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[گراف جهت‌دار]
یک \emph{گراف جهت‌دار} $G = \tuple{V, E}$ از مجموعه‌ای از
\emph{رأس‌ها}~$V$ و مجموعه‌ای از \emph{یال‌ها}~$E \subseteq V^2$
تشکیل می‌شود.
\end{defn}
```

Keep G=(V,E), vertex carrier V and edge set subset V squared. This definition permits loops and isolated vertices but not duplicate elements of a set; the broader introductory discussion of other conventions does not alter it.

Alternatives: No material alternative recorded; none invented.

## FA-0017-C03: Relations, arrows and explicit carrier

Action: retain_after_fresh_review; confidence 2/3: Definition and direction direct; one vertex adjective is provisional.
Canon: FA-REL-P053, FA-REL-P101, FA-REL-P102.

Source:
```latex
\begin{explain}
According to our definition, a graph just is a set together with a
relation on that set.  Of course, when talking about graphs, it's only
natural to expect that they are graphically represented: we can draw a
graph by connecting two vertices~$v_1$ and $v_2$ by an arrow iff
$\tuple{v_1, v_2} \in E$.  The only difference between a relation by
itself and a graph is that a graph specifies the set of vertices,
i.e., a graph may have isolated vertices. The important point,
however, is that every relation~$R$ on a set~$X$ can be seen as a
directed graph $\tuple{X, R}$, and conversely, a directed
graph~$\tuple{V, E}$ can be seen as a relation $E \subseteq V^2$ with
the set $V$ explicitly specified.
\end{explain}
```

Reviewed Persian:
```latex
\begin{explain}
بنا بر تعریف ما، گراف چیزی جز یک مجموعه به‌همراه رابطه‌ای روی آن
مجموعه نیست. البته وقتی از گراف‌ها سخن می‌گوییم، طبیعی است انتظار داشته
باشیم که آنها را به‌صورت تصویری بازنمایی کنند: می‌توانیم گراف را با
کشیدن پیکانی از رأس~$v_1$ به رأس $v_2$ رسم کنیم، اگر و تنها
اگر $\tuple{v_1, v_2} \in E$. تنها تفاوت میان یک رابطه به‌خودی‌خود و
یک گراف این است که گراف مجموعهٔ رأس‌ها را مشخص می‌کند؛ یعنی گراف ممکن
است رأس‌های منزوی داشته باشد. بااین‌حال، نکتهٔ مهم این است که هر
رابطهٔ~$R$ روی مجموعهٔ~$X$ را می‌توان گراف جهت‌دار $\tuple{X, R}$ در
نظر گرفت؛ و برعکس، گراف جهت‌دار~$\tuple{V, E}$ را می‌توان رابطهٔ
$E \subseteq V^2$ دانست که مجموعهٔ $V$ در آن به‌صراحت مشخص شده است.
\end{explain}
```

Arrow direction is v1 to v2 iff ordered pair(v1,v2) is in E. Preserve the explicit carrier and the possibility of isolated vertices, as well as both relation-to-graph and graph-to-relation directions. The canon calls an isolated vertex منفرد; existing منزوی is understandable but is not a direct attestation.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Consider a future lane-wide choice between رأس منفرد and رأس منزوی; no graph property changes.

## FA-0017-C04: Two graphs and isolated vertex contrast

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P101, FA-REL-P102.

Source:
```latex
\begin{ex}
The graph $\tuple{V, E}$ with $V = \{1, 2, 3, 4\}$ and $E =
\{\tuple{1,1}, \allowbreak \tuple{1, 2}, \allowbreak \tuple{1, 3},
\allowbreak \tuple{2, 3}\}$ looks like this:
\begin{align*}
& \begin{tikzpicture}[->,node distance=2cm]
  \node[draw,circle] (A) {$1$};
  \node[draw,circle] (B) [right of=A] {$2$};
  \node[draw,circle] (C) [below of=B] {$3$};
  \node[draw,circle] (D) [right of=B] {$4$};
  \draw (A) to [loop above]  (A);
  \draw (A) to  (B);
  \draw (A) to  (C);
  \draw (B) to  (C);
  \end{tikzpicture}
\intertext{This is a different graph than $\tuple{V', E}$ with $V' =
  \{1, 2, 3\}$, which looks like this:}
& \begin{tikzpicture}[->,node distance=2cm]
  \node[draw,circle] (A) {$1$};
  \node[draw,circle] (B) [right of=A] {$2$};
  \node[draw,circle] (C) [below of=B] {$3$};
  \draw (A) to [loop above]  (A);
  \draw (A) to  (B);
  \draw (A) to  (C);
  \draw (B) to  (C);
  \end{tikzpicture}
\end{align*}
\end{ex}
```

Reviewed Persian:
```latex
\begin{ex}
گراف $\tuple{V, E}$ با $V = \{1, 2, 3, 4\}$ و $E =
\{\tuple{1,1}, \allowbreak \tuple{1, 2}, \allowbreak \tuple{1, 3},
\allowbreak \tuple{2, 3}\}$ چنین شکلی دارد:
\begin{align*}
& \begin{tikzpicture}[->,node distance=2cm]
  \node[draw,circle] (A) {$1$};
  \node[draw,circle] (B) [right of=A] {$2$};
  \node[draw,circle] (C) [below of=B] {$3$};
  \node[draw,circle] (D) [right of=B] {$4$};
  \draw (A) to [loop above]  (A);
  \draw (A) to  (B);
  \draw (A) to  (C);
  \draw (B) to  (C);
  \end{tikzpicture}
\intertext{این گراف با گراف $\tuple{V', E}$ با $V' =
  \{1, 2, 3\}$ متفاوت است؛ گراف دوم چنین شکلی دارد:}
& \begin{tikzpicture}[->,node distance=2cm]
  \node[draw,circle] (A) {$1$};
  \node[draw,circle] (B) [right of=A] {$2$};
  \node[draw,circle] (C) [below of=B] {$3$};
  \draw (A) to [loop above]  (A);
  \draw (A) to  (B);
  \draw (A) to  (C);
  \draw (B) to  (C);
  \end{tikzpicture}
\end{align*}
\end{ex}
```

Both TikZ diagrams and their edge/vertex labels are preserved byte-for-byte. The second graph has the same E but omits vertex4; the Persian intertext correctly calls it a different graph. All math within intertext is separately compared, so translating prose cannot hide a changed Vprime or edge set.

Alternatives: No material alternative recorded; none invented.

## FA-0017-C05: Drawing exercise

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-REL-P053, FA-REL-P101.

Source:
```latex
\begin{prob}
  Consider the less-than-or-equal-to relation~$\le$ on the set $\{1,
  2, 3, 4\}$ as a graph and draw the corresponding diagram.
\end{prob}
```

Reviewed Persian:
```latex
\begin{prob}
  رابطهٔ کوچک‌تر یا مساوی~$\le$ روی مجموعهٔ $\{1,
  2, 3, 4\}$ را به‌صورت یک گراف در نظر بگیرید و نمودار متناظر را رسم کنید.
\end{prob}
```

The exercise still asks the reader to draw the less-than-or-equal relation on1,2,3,4, not the strict relation used in the Persian canon’s example. Retain the four-element carrier and do not supply the solution.

Alternatives: No material alternative recorded; none invented.

## FA-0018-C01: Title and logical applications

Action: retain_after_fresh_review; confidence 2/3: Tree concept and register direct; application-specific compounds require the wider logic canon.
Canon: FA-OL-CANON-0003:P0064, FA-OL-CANON-0003:P0065.

Source:
```latex
\olsection{Trees}

A particular kind of partial order which plays an important role in
all parts of logic is a \emph{tree}. Finite trees occur in elementary
parts of logic: for example, !!{formula}s can be understood in terms
of their decomposition into a syntax tree, while !!{derivation}s in
many !!{derivation} systems also take the form of finite trees.
%
Infinite trees appear already in the proof of the completeness
theorems for propositional and first-order logic, and are used
throughout mathematical logic.
```

Reviewed Persian:
```latex
\olsection{درخت‌ها}

نوع خاصی از ترتیب جزئی که در همهٔ بخش‌های منطق نقشی مهم ایفا می‌کند
\emph{درخت} است. درخت‌های متناهی در بخش‌های مقدماتی منطق پدیدار می‌شوند:
برای نمونه، !!{formula}s را می‌توان بر حسب تجزیه‌شان به یک درخت نحوی
فهمید، و !!{derivation}s در بسیاری از دستگاه‌های !!{derivation} نیز
صورت درخت‌های متناهی دارند.
%
درخت‌های نامتناهی از همان اثبات قضیه‌های تمامیت برای منطق گزاره‌ای و
منطق مرتبهٔ اول پدیدار می‌شوند و در سراسر منطق ریاضی به کار می‌روند.
```

درخت is directly attested in set-theoretic scholarship. Preserve finite syntax/derivation-tree applications and the appearance of infinite trees in propositional and first-order completeness. The source-controlled formula/derivation tokens remain untouched. درخت نحوی and the proof-system vocabulary are contextual existing terms, not direct attestations from these particular tree pages.

Alternatives: No material alternative recorded; none invented.

## FA-0018-C02: Finite tree diagram and graph relation

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-OL-CANON-0003:P0064, FA-REL-P101, FA-REL-P102.

Source:
```latex
The set-theoretic concept of a tree is closely related to the notion
of a tree in graph theory. Here is a picture of a (finite) tree:

\begin{center}
\begin{tikzpicture}[nodes={draw, circle}, -]
\node{$r$} [grow'=up]
    child { node {$a$} 
        child { node {$c$} }
        child { node {$d$} }
        child { node {$e$} }
    }
    child { node {$b$} };
\end{tikzpicture}
\end{center}
```

Reviewed Persian:
```latex
مفهوم مجموعه‌شناختی درخت پیوند نزدیکی با مفهوم درخت در نظریهٔ گراف
دارد. در زیر تصویری از یک درخت (متناهی) آمده است:

\begin{center}
\begin{tikzpicture}[nodes={draw, circle}, -]
\node{$r$} [grow'=up]
    child { node {$a$} 
        child { node {$c$} }
        child { node {$d$} }
        child { node {$e$} }
    }
    child { node {$b$} };
\end{tikzpicture}
\end{center}
```

Preserve the distinction between set-theoretic and graph-theoretic notions. Exact TikZ nodes and edges are unchanged; the source diagram is a finite rooted tree.

Alternatives: No material alternative recorded; none invented.

## FA-0018-C03: Root, parent and ancestry in pictured finite tree

Action: retain_after_fresh_review; confidence 2/3: Diagram and direction checked; lexical compounds provisional.
Canon: FA-OL-CANON-0003:P0064, FA-OL-CANON-0003:P0024.

Source:
```latex
The lowermost node~$r$ is the root. Every node other than $r$ has
exactly one parent node immediately below it. We can think of the relation
a node~$x$ stands in to a node~$y$ if $y$ can be reached from~$x$ by
following edges upwards as $x$ being an \emph{ancestor} of~$y$.
```

Reviewed Persian:
```latex
پایین‌ترین گره، یعنی~$r$، ریشه است. هر گره به‌جز $r$ دقیقاً یک گرهٔ
والد بلافاصله زیر خود دارد. رابطه‌ای را که گره~$x$ با گره~$y$ دارد،
هرگاه بتوان به $y$ با دنبال‌کردن یال‌ها رو به بالا از~$x$ رسید، می‌توان
چنین در نظر گرفت که $x$ یک \emph{نیای}~$y$ است.
```

The statement exactly one parent applies to the displayed finite tree, not arbitrary limit-height nodes. Preserve upward edge direction and x ancestor of y. ریشه، والد and نیا remain transparent explanatory labels; these exact compounds are not directly attested in the selected set-theory tree definition, which does not require a common root.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Seek wider Persian graph/tree attestation for the familial labels; preserve their explicit source definitions meanwhile.

## FA-0018-C04: Least element and well-ordering

Action: retain_after_fresh_review; confidence 2/3: Conditions direct; exact least-element compound is an explanatory lexical choice.
Canon: FA-OL-CANON-0003:P0023, FA-OL-CANON-0003:P0024, FA-OL-CANON-0003:P0064.

Source:
```latex
The ancestor relation in a tree is a strict partial order. This
motivates the set-theoretic definition. To state it we need two
concepts. A \emph{least element} in a set~$A$ partially ordered
by~$\le$ is !!a{element} $x \in A$ such that for all $y \in A$ we have
that~$x \le y$. A set is \emph{well-ordered} by~$\le$ if every one of
its non-empty subsets has a least element.
```

Reviewed Persian:
```latex
رابطهٔ نیا در یک درخت، یک ترتیب جزئیِ اکید است. این نکته انگیزهٔ تعریف
مجموعه‌شناختی را فراهم می‌کند. برای بیان آن به دو مفهوم نیاز داریم.
یک \emph{کوچک‌ترین عضو} در مجموعهٔ~$A$ که با~$\le$ به‌طور جزئی مرتب
شده، !!a{element} $x \in A$ است چنان‌که برای هر $y \in A$ داشته باشیم
که~$x \le y$. یک مجموعه \emph{خوش‌ترتیب} به‌وسیلهٔ~$\le$ است اگر هر
زیرمجموعهٔ ناتهی آن کوچک‌ترین عضو داشته باشد.
```

Preserve ancestor as a strict partial order, least element as below every carrier element, and well-ordering as a least element for every nonempty subset. خوش‌ترتیب is directly supported; the text uses کوچک‌ترین عضو to explicate the canon’s عنصر ابتدا, rather than confusing least with merely minimal.

Alternatives: No material alternative recorded; none invented.

## FA-0018-C05: Rooted tree definition

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-OL-CANON-0003:P0064, FA-OL-CANON-0003:P0023.

Source:
```latex
\begin{defn}[Tree]
A \emph{tree} is a pair $T = \tuple{A, \le}$ such that $A$ is a set
and $\le$ is a partial order on~$A$ with a unique least element
$r \in A$ (called the \emph{root}) such that for all $x \in A$,
the set $\Setabs{y}{y \le x}$ is well-ordered by~$\le$.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[درخت]
یک \emph{درخت} زوج $T = \tuple{A, \le}$ است، به‌طوری‌که $A$ مجموعه‌ای
است و $\le$ ترتیبی جزئی روی~$A$ است که یک کوچک‌ترین عضو یکتا
$r \in A$ دارد (که \emph{ریشه} نامیده می‌شود)، و برای هر $x \in A$،
مجموعهٔ $\Setabs{y}{y \le x}$ به‌وسیلهٔ~$\le$ خوش‌ترتیب است.
\end{defn}
```

OpenLogic requires a unique least root and every inclusive lower set to be well-ordered. Retain both, even though Khani/Zarei define the strict predecessor set and omit a global root requirement. No mathematical assumption may be silently imported or removed merely because the Persian canon differs.

Alternatives: No material alternative recorded; none invented.

## FA-0018-C06: Immediate successors

Action: retain_after_fresh_review; confidence 2/3: Concept directly supported; exact target label provisional.
Canon: FA-OL-CANON-0003:P0024, FA-OL-CANON-0003:P0064.

Source:
```latex
\begin{defn}[Successors]
Suppose $T = \tuple{A, \le}$ is a tree.
If $x,y \in A$, $x < y$, and there is no $z \in A$ such that
$x < z < y$, then we say that $y$ is a \emph{successor} of~$x$.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[جانشین‌ها]
فرض کنید $T = \tuple{A, \le}$ یک درخت باشد.
اگر $x,y \in A$، $x < y$، و هیچ $z \in A$ای وجود نداشته باشد که
$x < z < y$، آنگاه می‌گوییم $y$ یک \emph{جانشینِ}~$x$ است.
\end{defn}
```

Retain x<y and absence of any intermediate z. جانشین here means immediate successor in the tree, not numerical addition by1. The canon uses تالی in well-order discussion; retain the existing explicitly defined label with that attestation limit.

Alternatives: تالی is attested but a global synonym switch is not needed to preserve the exact immediate-successor definition.

## FA-0018-C07: Children, predecessor and parent

Action: retain_after_fresh_review; confidence 2/3: Direction exact; selected pages do not directly attest all familial compounds.
Canon: FA-OL-CANON-0003:P0024, FA-OL-CANON-0003:P0064.

Source:
```latex
The successors of $x \in A$ are also called its \emph{children}. If
$y$ is a successor of~$x$, then we call $x$ the \emph{predecessor} or
\emph{parent} of~$y$.
```

Reviewed Persian:
```latex
جانشین‌های $x \in A$، \emph{فرزندان} آن نیز نامیده می‌شوند. اگر
$y$ جانشین~$x$ باشد، آنگاه $x$ را \emph{پیشین} یا \emph{والدِ}~$y$
می‌نامیم.
```

Retain the source synonym mapping children=successors and parent=predecessor with direction x predecessor of y when y succeeds x. These family metaphors are source content, not a new pedagogical companion.

Alternatives: No material alternative recorded; none invented.

## FA-0018-C08: At most one predecessor

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-OL-CANON-0003:P0023, FA-OL-CANON-0003:P0024, FA-OL-CANON-0003:P0064.

Source:
```latex
\begin{prop}
If $\tuple{A,\le}$ is a tree, then every $x \in A$ other than the root
has at most one predecessor.
\end{prop}
```

Reviewed Persian:
```latex
\begin{prop}
اگر $\tuple{A,\le}$ یک درخت باشد، آنگاه هر $x \in A$ به‌جز ریشه،
حداکثر یک پیشین دارد.
\end{prop}
```

Preserve حداکثر یک rather than دقیقاً یک for an arbitrary nonroot node. A well-ordered chain of type omega+1 has a nonroot limit node with no immediate predecessor. The finite picture must not override the general proposition.

Alternatives: No material alternative recorded; none invented.

## FA-0018-C09: Predecessor proof

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-OL-CANON-0003:P0023, FA-OL-CANON-0003:P0064.

Source:
```latex
\begin{proof}
  Suppose $y_1 < x$ and $y_2 < x$ and $y_1 \neq y_2$. Then $\{y_1,
  y_2\} \subseteq \Setabs{z}{z<x}$. Since $\Setabs{z}{z<x}$ is
  well-ordered by~$\le$, its subset $\{y_1, y_2\}$ has a least
  element, which obviously must be either $y_1$ or~$y_2$. So either
  $y_1 \le y_2$ or $y_2 \le y_1$. We assumed that $y_1 \neq y_2$, so
  actually either $y_1 < y_2$ or $y_2 < y_1$. Since we assumed that
  $y_1 < x$ and $y_2 < x$, we furthermore have that either $y_1 < y_2
  < x$ or $y_2 < y_1 < x$. So $y_1$ and $y_2$ cannot both be
  predecessors of~$x$.
\end{proof}
```

Reviewed Persian:
```latex
\begin{proof}
  فرض کنید $y_1 < x$ و $y_2 < x$ و $y_1 \neq y_2$. آنگاه $\{y_1,
  y_2\} \subseteq \Setabs{z}{z<x}$. چون $\Setabs{z}{z<x}$
  به‌وسیلهٔ~$\le$ خوش‌ترتیب است، زیرمجموعهٔ $\{y_1, y_2\}$ از آن یک
  کوچک‌ترین عضو دارد که آشکارا باید یا $y_1$ یا~$y_2$ باشد. پس یا
  $y_1 \le y_2$ یا $y_2 \le y_1$. فرض کردیم $y_1 \neq y_2$؛ بنابراین
  در واقع یا $y_1 < y_2$ یا $y_2 < y_1$. چون فرض کردیم $y_1 < x$ و
  $y_2 < x$، افزون بر این یا $y_1 < y_2
  < x$ یا $y_2 < y_1 < x$. پس $y_1$ و $y_2$ نمی‌توانند هر دو
  پیشین‌های~$x$ باشند.
\end{proof}
```

Retain least element of the two-element lower-set subset, comparability of y1,y2, strictness from their inequality, and the resulting intervening node. The conclusion is they cannot both be immediate predecessors; it does not prove that a predecessor always exists.

Alternatives: No material alternative recorded; none invented.

## FA-0018-C10: Finite, infinite and finite branching

Action: retain_after_fresh_review; confidence 2/3: Definition exact; compound provisional.
Canon: FA-OL-CANON-0003:P0064, FA-OL-CANON-0003:P0065.

Source:
```latex
\begin{defn}
A tree $T = \tuple{A, \le}$ is said to be \emph{infinite} if $A$ is an
infinite set, and \emph{finite} otherwise. If $T$ is such that every
$x \in A$ has only finitely many successors, then we say that $T$ is
\emph{finitely branching}.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}
گفته می‌شود درخت $T = \tuple{A, \le}$ \emph{نامتناهی} است اگر $A$ یک
مجموعهٔ نامتناهی باشد، و در غیر این صورت \emph{متناهی} است. اگر $T$
چنان باشد که هر $x \in A$ فقط شمار متناهی‌ای از جانشین‌ها داشته باشد، آنگاه
می‌گوییم $T$ \emph{با انشعاب متناهی} است.
\end{defn}
```

Finite/infinite refers to carrier cardinality; finitely branching means finitely many immediate successors at each node, not finite height, finitely many branches or a uniform global numerical bound. با انشعاب متناهی is a transparent compound with contextual branching evidence, not a verbatim attestation.

Alternatives: No material alternative recorded; none invented.

Expert-review question: Further native attestation for با انشعاب متناهی is desirable; the local definition prevents ambiguity.

## FA-0018-C11: Maximal branches and domain-symbol correction

Action: correct; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-OL-CANON-0003:P0064, FA-REL-P055.

Source:
```latex
\begin{defn}[Branches]
Given a tree $T = \tuple{A, \le}$, a \emph{branch} of~$T$ is a
maximal chain in~$T$, i.e., a set $B \subseteq A$ such that
for any $x, y \in B$ either $x \le y$ or $y \le x$, and for any
$z \in X \setminus B$ there exists $u \in B$ such that neither
$z \le u$ nor $u \le z$.
%
We use $[T]$ to denote the set of all branches of $T$.
\end{defn}
```

Reviewed Persian:
```latex
\begin{defn}[شاخه‌ها]
با داشتن درخت $T = \tuple{A, \le}$، یک \emph{شاخه} از~$T$ زنجیری
بیشینه در~$T$ است؛ یعنی مجموعه‌ای $B \subseteq A$ چنان‌که برای هر
$x, y \in B$، یا $x \le y$ یا $y \le x$، و برای هر
$z \in A \setminus B$، یک $u \in B$ وجود دارد چنان‌که نه
$z \le u$ و نه $u \le z$.
%
از $[T]$ برای نمایش مجموعهٔ همهٔ شاخه‌های $T$ استفاده می‌کنیم.
\emph{یادداشت ویراستاری:} در شرط بیشینگی، نماد تعریف‌نشدهٔ متن مبدأ با نماد دامنهٔ درخت جایگزین شده است.
\end{defn}
```

Preserve maximal chain, not any well-ordered subchain as in the cited Persian notes. The outsider must range over A minus B, the declared tree carrier; frozen X is undefined here. Correct just that symbol and visibly disclose the editorial intervention. Retain both incomparability directions and all-branches notation. Maximal is بیشینه, not a largest unique branch.

Alternatives: No material alternative recorded; none invented.

Expert-review question: High-confidence source typo: undefined X replaced by declared A. Reviewable without an expert-dependent stop.

## FA-0018-C12: Infinite binary tree

Action: retain_after_fresh_review; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-OL-CANON-0003:P0064, FA-OL-CANON-0003:P0024.

Source:
```latex
\begin{ex}
A classic example of a finitely branching tree is the
\emph{infinite binary tree} of finite sequences of $0$s and~$1$s,
sometimes denoted $\{0,1\}^*$ or~$\Bin^*$, ordered by the extension
relation $\sqsubseteq$ (e.g., $101 \sqsubseteq 101101$).
Since any binary string can always be extended by adding
a $0$ or a $1$ on the end, this tree contains infinitely
many elements: every element~$s$ has exactly two successors, $s0$ and~$s1$. Its root is the empty sequence $\emptyseq$.
\end{ex}

\begin{ex}
```

Reviewed Persian:
```latex
\begin{ex}
یک نمونهٔ کلاسیک از درختی با انشعاب متناهی، \emph{درخت دودویی
نامتناهیِ} دنباله‌های متناهی از $0$ و~$1$ است که گاهی
$\{0,1\}^*$ یا~$\Bin^*$ نوشته می‌شود و با رابطهٔ امتداد $\sqsubseteq$
مرتب شده است (برای نمونه، $101 \sqsubseteq 101101$).
از آنجا که هر رشتهٔ دودویی را همواره می‌توان با افزودن
یک $0$ یا یک $1$ به انتهای آن امتداد داد، این درخت بی‌نهایت
عضو دارد: هر عضو~$s$ دقیقاً دو جانشین، یعنی $s0$ و~$s1$، دارد. ریشهٔ آن
دنبالهٔ تهی $\emptyseq$ است.
\end{ex}

\begin{ex}
```

Finite binary sequences ordered by prefix give a finitely branching but infinite tree; every word has exactly two immediate successors s0 and s1 and the empty word is its root. Retain exact strings and labels. The source definition, not the canon’s transfinite generalization, governs this example.

Alternatives: No material alternative recorded; none invented.

## FA-0018-C13: Natural-number sequence tree and nonempty subtrees

Action: correct; confidence 3/3: Exact source/target meaning was compared with the cited Persian passage; direct attestations and contextual inferences are distinguished.
Canon: FA-OL-CANON-0003:P0064, FA-OL-CANON-0003:P0065, FA-OL-CANON-0003:P0024.

Source:
```latex
Slightly more generally, the set of finite sequences of natural
numbers~$\Nat^*$ with the extension relation~$\sqsubseteq$ is also a
tree. It is obviously not finitely branching: every $s \in \Nat^*$ has
infinitely many successors~$sn$, one for every $n \in \Nat$. Every $A
\subseteq \Nat^*$ which is closed under~$\sqsubseteq$ is a
\emph{subtree} of~$\Nat^*$. (That is, $A$ is such that if $s \in A$
and $s' \sqsubseteq s$, then also $s' \in A$.) All finite trees can be
represented as finite subtrees of~$\Nat^*$.
\end{ex}
```

Reviewed Persian:
```latex
کمی کلی‌تر، مجموعهٔ دنباله‌های متناهی از اعداد طبیعی~$\Nat^*$ با
رابطهٔ امتداد~$\sqsubseteq$ نیز یک درخت است. آشکارا با انشعاب متناهی
نیست: هر $s \in \Nat^*$ بی‌نهایت جانشین~$sn$ دارد، یکی برای هر
$n \in \Nat$. هر زیرمجموعهٔ ناتهی $A
\subseteq \Nat^*$ که نسبت به~$\sqsubseteq$ بسته باشد، یک
\emph{زیردرختِ}~$\Nat^*$ است. (یعنی $A$ چنان است که اگر $s \in A$
و $s' \sqsubseteq s$، آنگاه $s' \in A$ نیز.) همهٔ درخت‌های متناهی را
می‌توان به‌صورت زیردرخت‌های متناهیِ~$\Nat^*$ بازنمایی کرد.
\emph{یادداشت ویراستاری:} قید ناتهی افزوده شده است، زیرا در تعریف این متن هر درخت باید ریشه داشته باشد؛ مجموعهٔ تهی نسبت به گرفتن قطعه‌های آغازین بسته است، اما ریشه ندارد.
\end{ex}
```

Every word in Nat-star has one successor for each natural n, hence infinitely many. Prefix closure is downward closure, not closure under extensions. Add nonempty to the proposed subtree carrier and disclose why: the empty set is prefix-closed but cannot have the root required by the source definition. Preserve that all finite source-defined rooted trees can be represented here.

Alternatives: No material alternative recorded; none invented.

## FA-0018-C14: König lemma

Action: retain_after_fresh_review; confidence 2/3: Source proposition preserved exactly; lemma-specific target attestation absent in selected pages.
Canon: FA-OL-CANON-0003:P0064, FA-OL-CANON-0003:P0065.

Source:
```latex
\begin{prop}[K\H{o}nig's lemma]
If $T = \tuple{A,\le}$ is a finitely branching infinite tree,
then $T$ has an infinite branch.
\end{prop}
```

Reviewed Persian:
```latex
\begin{prop}[لم \foreignlanguage{english}{K\H{o}nig}]
اگر $T = \tuple{A,\le}$ درختی نامتناهی با انشعاب متناهی باشد،
آنگاه $T$ یک شاخهٔ نامتناهی دارد.
\end{prop}
```

Retain both finitely branching and infinite hypotheses and the infinite-branch conclusion. The selected canon supports surrounding tree register but does not state this lemma; no such attestation is asserted. Retain the original Latin spelling inside the existing language switch rather than invent a Persian transliteration.

Alternatives: No material alternative recorded; none invented.

Expert-review question: A direct Persian source for the eponym and lemma register would strengthen this retained naming decision.

## FA-0018-C15: Weak König lemma

Action: retain_after_fresh_review; confidence 2/3: Formal and conceptual content exact; naming/register attestation remains provisional.
Canon: FA-OL-CANON-0003:P0064, FA-OL-CANON-0003:P0065.

Source:
```latex
A special case of K\H{o}nig's lemma widely used in computability
theory, known as \emph{weak K\H{o}nig's lemma}, is the following: any
infinite subtree of $\{0,1\}^*$ has an infinite branch.
```

Reviewed Persian:
```latex
حالت خاصی از لم \foreignlanguage{english}{K\H{o}nig} که به‌طور گسترده در نظریهٔ محاسبه‌پذیری به
کار می‌رود و \emph{لم ضعیف \foreignlanguage{english}{K\H{o}nig}} نام دارد، چنین است: هر زیردرخت
نامتناهی از $\{0,1\}^*$ یک شاخهٔ نامتناهی دارد.
```

Keep the restriction to infinite subtrees of the binary sequence tree and the infinite-branch conclusion, plus its use in computability. Weak names the special statement; it does not weaken infinite to arbitrarily long finite branches. The eponym and adjective are explicit source-aligned naming choices, not certified conventional Persian terminology.

Alternatives: No material alternative recorded; none invented.

## Validation boundary

Every substantive source and target character lies in an ordered non-overlapping reviewed span. Formal tokens are checked across inline, bracketed, multline and align mathematics. Text arguments in mathematics are separately aligned and manually reviewed for exact connective, quantifier and number-family meaning.
Finite tests support the written reasoning; they are not universal formal proofs. No new PDF was built or visually certified. Frozen owner inputs and reader releases are unchanged; corrections enter the owner’s normal next-batch build and visual QA.
Attribution: Open Logic Project and contributors, under existing CC BY 4.0 notices. https://github.com/OpenLogicProject/OpenLogic . Existing edition: https://github.com/KokunoYumeto/OpenLogic-fa-ir . Canon sources retain separate rights.
