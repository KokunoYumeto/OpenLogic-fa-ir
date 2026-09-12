# OLP-0043: two source-and-canon corrections

This packet fixes two specific errors in the Iranian Persian rationals section. It does **not** certify the whole section or supply a newly built reader.

1. **Source sign reversal.** In the order-definition sentence, the difference must remain `s-r`, not switch to `r-s`. The source itself uses `s-r` immediately before this typo and in the following displayed formula. Taking `r=0,s=1` disproves the reversed wording. The candidate corrects the inherited error in Persian.
2. **Technical terminology.** The opening translates “naïve set theory” as “natural set theory.” The candidate instead uses `نظریهٔ ساده‌انگارانهٔ مجموعه‌ها`. Khani and Zarei's university set-theory notes explicitly associate this Persian term with “naive” (physical PDF page7, printed page6, footnote1; reiterated in the next page's heading). The complete pages were read visually as well as searched. The source PDF is cited and hashed, not redistributed.

The exact before/after choices, consulted canon locations, rationale, rejected form and editorial confidence are in `CHOICES.json`. Confidence scores are not calibrated probabilities. Human review is welcome but is not a release gate.

## Priority expert review and remaining work

Check terminology consistently across the arithmetization chapter and verify the sign correction in every reader representation. Three English `\\text{ iff }` strings remain in the inherited section and require proper Persian mathematical-text rendering. Neither the other wording in this candidate nor the complete unit has been newly admitted as canon-verified.

The candidate changes exactly two substrings, leaving all other target text unchanged apart from line-ending normalization. The frozen English source and owner production files are untouched. `TARGETED_QA.json` records the original/candidate hashes, canon identities and441 rational regression pairs. The general justification is the algebraic equivalence in the choice ledger, not the finite test count.

Integrate these corrections reversibly into the existing chapter-sized production batch, then carry them into the full Persian PDF/EPUB. Do not issue a standalone book release for this packet. The EPUBs, full-reader progress and remaining source/canon audit retain their own scopes.
