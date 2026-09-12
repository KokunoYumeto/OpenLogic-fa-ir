# Pairing functions: mathematical review and correction scope

Authority: OLP-0031 pairing.tex and OLP-0032 pairing-alt.tex at frozen revision9620cc73f9c8e0ad003c514a5d3748f29611c4c0. Exact source, original Persian and corrected candidate identities are in SOURCE_IDENTITIES.json. Both sections were read in full. This is main-agent review, not independent human or formal-prover certification. The frozen originals are preserved.

## Cantor pairing and two missing qualifications

Write T_s=s(s+1)/2 and g(n,m)=T_(n+m)+n. A diagonal n+m=s has s+1 cells, whose codes run from T_s through T_(s+1)-1. These intervals are consecutive, disjoint and cover the naturals. Thus every pair has one code and every code has one pair: g is a bijection and the inverse of the previously defined diagonal enumeration. In particular g(1,2)=6+1=7.

For m>0, g(n+1,m-1)=T_(n+m)+n+1=g(n,m)+1. At m=0 the proposed target column is -1 and no such natural-indexed cell exists. Add the positive-column condition in prose; do not modify the formula or reverse coordinates for RTL.

The source says the kth triangular number is the sum of natural numbers strictly less than k, then gives k(k+1)/2. At k=1 the strict sum is0, not1. The displayed sequence0,1,3,6 and the pairing formula consistently use the sum through k. Therefore replace the inline strict inequality by the inclusive one, retaining the established triangular sequence. This is one explicit formal source correction, not an assertion that all math was unchanged.

## Injection is not surjection; inverse is not automatically enumeration

The general pairing definition asks only for an injection f:A×B→Nat. It therefore guarantees that each used code has a unique pair, but not that every natural number is a code. Its inverse is a total function on its image, and a partial function if all naturals are regarded as possible inputs. The alternative section explicitly recognizes this distinction.

Counterexample to the unqualified inverse exercise: let A=B={0}, and let f assign2 to its sole input(0,0). It is an injection, but the inverse has domain{2}. It is neither a total Nat enumeration nor a total positive-integer enumeration as defined earlier. The product is countable; the stated object simply has the wrong domain to be that enumeration.

If D=A×B is nonempty, let I=f[D] and choose one fixed d in D. Extend the inverse to Nat by returning its unique inverse value on I and returning d elsewhere. This total map is onto D. Reindexing gives a positive-integer enumeration if required. Alternatively, enumerate I and compose with the inverse. No family of arbitrary choices is needed: there is one default object, and inverse values on I are unique. If D is empty, countability follows from the separate empty-set clause, not a nonexistent map from Nat into the empty set.

The corrected exercise asks the reader to construct an enumeration from the inverse-on-image in the nonempty case and consider the empty case separately. It does not insert the solution. The decoding paragraph now restricts its inputs to valid codes. The definition remains injective, not silently strengthened to bijective or computable.

## Other exercises and their scope

- Nonnegative rationals: enumerate pairs of a natural numerator and a positive denominator, and map a pair to its quotient. Repetitions of the same rational are allowed. Include zero; do not permit denominator zero.
- All rationals: combine an explicit integer enumeration with positive denominators. The given z/m, integer numerator and positive denominator are retained.
- Finite binary strings: order by length and then by binary digits, including the empty string. For example, a length-k word can be injected into the interval from2^k-1 through2^(k+1)-2. This does not enumerate infinite bit streams.
- Truth functions: for fixed finite arity k there are2^(2^k) functions from the Boolean k-tuples to Boolean values. An explicit truth-table order for each k and a length/arity code enumerate the union over finite arities. At arity zero there are two constant truth functions. The canon distinguishes the finite-arity function F from a valuation mu assigning values to propositions; the Persian terminology must not collapse them.
- Finite subsets of an arbitrary infinite countable set: take one enumeration/bijection for that one set and encode a finite subset by the finite ordered list of its member indices. Include the empty subset. There is no selection of enumerations for a whole family here.
- Cofinite subsets of Nat: complementation gives a correspondence with finite subsets, so the union of these two collections is countable. The source's malformed “complement of a finite set Nat” is resolved by its immediately following formula. The old Persian already read the intended finite subset correctly; the new packet records that fact rather than inventing a fresh correction. This is known source finding OLSIZ-002.

These checking arguments belong to the review record. The translated exercises remain unsolved.

## Countable-union assumption disclosure

The ordinary diagonal proof chooses an enumeration for each nonempty set in a countable family, then enumerates pairs consisting of a set index and an entry index. Every element of the union occurs at such a pair. Empty sets can be skipped or handled with one fixed default element of the union; if the entire union is empty, use the empty clause.

Distinguish the data required by this proof: if a family of enumerations has already been supplied, there is no extra selection step. If only existence of an enumeration for each set is given, the customary proof makes a countable family of selections. The note identifies the use of Choice in that proof; it does not claim full Choice is the weakest equivalent axiom, does not label the theorem false in ZFC, and does not pretend a proof-theoretic independence result was established in this audit. The consulted set-theory page expressly uses اصل انتخاب for a related reverse-selection argument. Avoid importing its unrelated notation slips.

## Alternative pairing: positive positions then zero-based codes

The filling procedure places row n at positions2^n(2m+1), with m natural. Every positive integer p has a unique decomposition p=2^n q with q odd, obtained by dividing out factors of2; then q=2m+1 determines a unique natural m. Thus each positive position is filled exactly once after the finite row index n is reached. The description is a mathematical assignment, not an instruction to finish an infinite computation before proceeding.

The first row is(0,0),(0,1),(0,2),... . The prose's second pair(0,2) is a typo; the immediately following table correctly has(0,1). After row(2,m), the next family is(3,m), not a second copy of(2,m). These are two explicitly declared math-span corrections. The row duplication is already-known OLSIZ-003; no claim that either defect is newly discovered or remains unfixed in current upstream is made.

Subtracting1 gives h(n,m)=2^n(2m+1)-1, a bijection Nat²→Nat. Its inverse takes k+1, removes its largest power of2, and maps the odd remainder q to(q-1)/2. The examples h(0,0)=0, h(1,2)=9 and h(2,6)=51 are all correct. The21 displayed numeric array cells are positive positions h+1, not h; keep that distinction instead of “fixing” valid table entries.

Finally, j(n,m)=2^n3^m is injective by unique prime factorization and always positive. Viewing this map as landing in Nat after inclusion of the positive integers is legitimate, not a type error. It is not onto:5 is absent, since a power of2 times a power of3 has no prime factor5. Accordingly its inverse is defined only on its image, precisely illustrating the missing qualification in0031. Saying an encoding need not be onto does not imply every admissible encoding is nonsurjective; the Persian partial-inverse statement is explicitly conditional.

## Canon, testing, and delivery boundary

Six complete pages were directly consulted: Khani mathematical logic PDF93 (printed92), Khani foundations PDF13, Khani/Zarei set theory PDF51 and53 (printed50 and52), and Ghaffari Hadigheh/Toumanian PDF46 and50 (printed36 and40). Direct attestation includes numerical کدگذاری/کد, جدول ارزش and valuation distinctions, معکوس, one-to-one/onto, and choice language. Exact جفت‌سازی, هم‌متناهی, کدگشایی and partial-function labels remain contextual with disclosed limits. The extra logic PDF89 was inspected while searching but supplies no new pairing attestation; it is not misrepresented as support for that label.

The machine record checks source/target span alignment, three authorized formal replacements, embedded math-text translation, labels/structure/Unicode, and private source/canon identities. Arithmetic regression checks include300 Cantor codes,400 diagonal steps,101 triangular sums,2000 h outputs,400 h input pairs,21 displayed positive positions,400 j input pairs, finite inverse-extension cases, and negative controls for the erroneous strict inequality and inverse domain. Those finite checks support but do not replace the general arguments above.

This packet is not a new reader build, visual-reader certification, complete722-file review, or proof of owner integration. The exact corrections are ready for the owner's existing derived-source mechanism. Human review remains a later opportunity, never a gate. Existing public access and frozen originals remain unchanged.
