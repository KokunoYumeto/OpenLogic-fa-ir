# Sizes of sets: source mathematics and Persian scope review

Reviewed units: OLP-0027 chapter wrapper, OLP-0028 introduction, OLP-0029 enumerability, OLP-0030 zig-zag. Authority is the exact frozen English source at revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`, not a modernized source silently substituted for it. SOURCE_IDENTITIES.json supplies exact path/byte identities and target alignment. This is a main-agent review. The attempted independent reviewer produced no report, and no independent certification is claimed.

## Book title and scope

The chapter wrapper contains two substantive editorial paragraphs and13 imports; it is not an empty file. Its second paragraph cites Tim Button's *Open Set Theory*. The author's [official OER page](https://www.homepages.ucl.ac.uk/~uctytbu/OERs.html) identifies this as the2019 title, subsequently revised as *Set Theory: An open introduction*. The old Persian title meant the theory of topologically open sets and is a translation error. Preserve the actual historical English title rather than invent a published Persian title or change the cited edition.

The wrapper's first overview mentions bijections with the naturals; its second expressly includes finite initial segments. Adding that qualification in the first editorial overview reconciles two statements in the same source. It is not a new cardinality definition. All imports and references remain.

## Enumeration and countability

OpenLogic's informal enumeration is a possibly finite list in which every member appears at some finite position. Repetition is allowed. Its formal enumeration is a surjection from the positive integers onto a nonempty set. These notions characterize the same nonempty sets, not identical enumerating objects. A finite nonempty list becomes a total surjection by repeating its final value. The empty list has no corresponding map from the nonempty positive integers to the empty set. OpenLogic therefore explicitly defines a countable set as empty OR admitting an enumeration.

Khani/Zarei PDF53 (printed52), definition10, instead uses شمارا for equinumerosity with omega, hence the infinite-only convention. That page also allows ordinal-indexed, potentially transfinite شمارش. The Persian translation retains OpenLogic's inclusive countability and finite-position scope, with a labelled terminology note. It does not import the canon's narrower cardinality convention, transfinite scope, or an algorithmic computability requirement.

The first bullet's purported equivalence between having a beginning/immediate predecessors and having finite positions is false if taken as a characterization of linear order. Counterexample: order type omega followed by the integers in their usual order. There is a least element; every other element has an immediate predecessor. But an element in the integer block has infinitely many predecessors, including the whole omega block. Thus the finite-position condition is independent of the stated predecessor condition. The source definition already supplies it: the target replaces “in other words” with “also required” and labels the explanation. This is not a claim that the entire definition is false.

Removing repeated entries by retaining first occurrences preserves the range. For a finite set it produces a finite list, not an injective function on the whole positive integers. The proposition before the formal definition is correct in its informal context; the candidate makes that context explicit. Repetitions and permutations affect the particular list without changing the represented set. The reversed endless positive list has no first entry; the odd-then-even list puts its even part beyond all finite positions. Neither example makes the underlying positive-integer set uncountable.

## Integer table: one explicit mathematical correction

The formula is

`f(n) = (-1)^n ceil((n-1)/2)`, for positive integer n.

For n=1 it gives0. For n=2k it gives k; for n=2k+1 with k>=1 it gives -k. Thus the first seven values are0,1,-1,2,-2,3,-3. The source's symbolic row has the seventh value `-ceil(6/2)`, but its last numeric row omits -3 and places the ellipsis in that column. Restore the missing numeric cell and explicitly disclose it. The formula and three case conditions are already correct and remain unchanged. The canon's سقف means the least integer greater than or equal to its input; this also resolves negative inputs correctly.

The even/odd examples have declared codomain the positive integers, and neither is onto that codomain. Their assertion that they enumerate even/odd positive integers uses the implicit restriction of codomain to the respective range. Preserve the distinction, not a silently altered function type.

## Closure exercises and index shifts

For two nonempty enumerated sets, interleave their given enumerations to enumerate their union. If one is empty, use the other's enumeration; if both are empty, the empty disjunct applies. For a nonempty subset B of an enumerated A, select a single fixed b in B and replace outputs outside B by b. Every element of B still occurs. B empty is handled separately. A finite union follows by induction (including the empty union if the zero case is admitted). None of these arguments requires an arbitrary countable family of choice selections. Exercises remain exercises in the translation; these checking arguments are not inserted as solutions.

The shift `g(n)=f(n+1)` takes a positive-integer enumeration to a natural-number enumeration; its converse `f(n)=g(n-1)` is defined only for positive n, so it never evaluates a negative natural input. Both existence statements are false for an empty codomain, and the countability corollary includes empty separately.

For first-unused-value recursion, the next value is chosen by the least positive index whose value has not appeared. If A is infinite, such an index always exists. If a value first occurs at index k, at most k distinct values occur through index k, so first-occurrence ordering selects that value within at most k selections. This proves surjectivity, while construction gives injectivity. Finite A gives domain1..n; shifting it to0..n-1 yields the statement with0..m for some natural m. This is a parameter change, not an off-by-one error. The empty set remains a separate case.

The final injection characterization uses no general axiom of choice: from a surjection choose the least preimage for each element; from an injection into the positive integers and a nonempty A, use the unique inverse on its image and one fixed default elsewhere. The empty injection exists and is handled by the empty disjunct.

## Cantor diagonals and finite sequences

Let `T_s=s(s+1)/2`. Cell(n,m) has index `T_(n+m)+n`. On diagonal s=n+m, n runs0..s; these indices are exactly the consecutive interval from T_s through T_(s+1)-1. These finite intervals partition the naturals because their endpoints increase without bound. Therefore every index has one cell and every ordered pair has a finite index. The inverse assignment is a bijection, in particular a surjection. The15 displayed numeric cells and first10 explicit pairs agree with this rule. The traversal is not alternating direction; the source's informal “zig-zag” label does not change its actual order.

The source proof states the assignment but leaves these existence/uniqueness/surjectivity reasons implicit. A labelled Persian proof explanation supplies them; the theorem itself is not false. The triple array groups a triple as a pair consisting of a pair and one number. This is a canonical identification, not a universal literal equality between every possible encoding of tuples. Iterating the specified pairing gives countability of every positive finite power. The zero-fold product is the singleton containing the empty tuple; the candidate explicitly notes this case because the quantified statement includes zero.

For all finite positive-integer sequences, define an injective code recursively by pairing the accumulated code with each entry and then pairing the length with the resulting code. Given the length, injectivity of pairing permits recovery of the sequence entry by entry, so no two sequences have the same final code. This supplies an injection into the naturals for the star collection, not the collection of infinite streams. Again, it uses specified uniform constructions rather than arbitrary selections of enumerations.

## Validation and remaining boundary

Finite witnesses check200 formula/case inputs,201 outputs covering integers -100..100,15 displayed diagonal values,325 consecutive diagonal indices, the empty tuple, and364 bounded finite sequences. These are regression checks, not universal proofs. The arguments above justify the unbounded statements. Source and candidate math spans are compared with exactly one authorized repair: the missing table value. Embedded mathematical text, labels, imports, conditional references, cref, Unicode and source/target alignment are checked separately.

Six full canon page images were read: Khani/Zarei51 and53, and Ghaffari Hadigheh/Toumanian44,45,46,50. The exact textual/page/hash identities and limitations are recorded in the choice ledger. Actual-infinity philosophical phrasing and the exact enumeration/zig-zag labels have explicit attestation limits; mathematical pages are not independent historical scholarship. Expert questions are mandatory records, not approval gates.

This packet is a corrected source and expert-review deliverable. It is not a new compiled reader, visual acceptance of a reader, completed722-file review, or proof that the edition owner has integrated it. Frozen originals remain unchanged; normal reader integration and build/visual checks follow.
