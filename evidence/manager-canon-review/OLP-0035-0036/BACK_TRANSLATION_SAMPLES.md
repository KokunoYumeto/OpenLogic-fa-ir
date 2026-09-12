# Meaning-preservation samples

Same-reviewer Persian-to-English readings of the final candidates, checked against the frozen English and the documented source repairs. These are targeted semantic checks, not independent human testing or calibrated evidence of readability. The complete source/target spans and consulted canon are in choices-evidence.json.

## FA-0035-C03: two-sided correspondence

Persian: «بشقاب‌ها و چاقوها از هر دو طرف به‌طور یکتا با یکدیگر متناظر می‌شوند».

English reading: the plates and knives correspond uniquely to each other in both directions. This retains the English quotation’s unique correspondence and makes the German original’s two-sided uniqueness explicit. It does not say merely that each plate has some knife. The location, objects and section citation remain unchanged.

## FA-0035-C14 and C15: empty-case function identity

Both translated empty-case parentheticals now use f(x)=y. Reading: if B contained y while A were empty, no x in A could map to y under the already fixed bijection f. This contradicts surjectivity of f. The enumeration g belongs to the nonempty alternative and cannot justify the empty alternative. The change is a disclosed source repair, not an unnoticed departure from the English.

## FA-0036-C04 to C06: three different relation properties

Persian non-strict comparison: «بازتابی و تراگذری است، اما متقارن نیست».

English reading: it is reflexive and transitive, but not symmetric. This is not a claim of asymmetry. The strict definition says an injection exists but no bijection exists. Its property statement uses «پادبازتابی» and explains that no set is strictly smaller than itself. It does not merely assert that some set fails reflexivity; nor does that explanatory clause define transitivity.

## FA-0036-C06: limited scope of the assumption note

The Persian note says the second equivalence, about nonenumerability, is stated here assuming Choice; under that assumption every infinite set has a countably infinite subset. It expressly says that the first equivalence, about enumerability, and the subsequent Cantor theorem do not need this assumption. Reading the whole paragraph preserves all three scopes. The note is marked editorial, not presented as translated original wording.

## FA-0036-C11: all inputs in the diagonal argument

Persian conclusion: «با توجه به تعریفِ مجموعه و دلخواه‌بودنِ $x$، برای هر $x \in A$».

English reading: by the set’s definition and the arbitrary choice of x, the following holds for every x in A. The following biconditional is x in g(x) iff x not in the diagonal set; consequently g(x) differs from that set. The quantified domain is the entire function domain, not only the diagonal subset. The separate valid earlier antecedent x in the diagonal subset is retained.

## FA-0036-C16: the reversed injection exercise

The Persian exercise prohibits an injection from Pow(A) into A for every set A. Its hint defines D using images g(B), where B is a subset of A and g(B) is not in B, then sets x=g(D). This is not the theorem’s different definition D={x in A:x not in g(x)} and does not reverse the arrow to A→Pow(A). The conjunction and the use of injectivity are retained.

Result: these high-risk meanings are preserved, with the three explicitly disclosed formal repairs. Full mathematical reasoning, including empty sets and both proof branches, is in SOURCE_MATHEMATICS_REVIEW.md. Subsequent reader integration and PDF/EPUB checks remain the edition owner’s production work; this packet does not claim that integration has happened.
