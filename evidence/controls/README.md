# Open Logic Arabic and Iranian-Persian production control

This directory controls two separate complete target editions at one immutable
source release. The Arabic and Persian worktrees are independent Git branches
sharing only the owned bare source repository and source identities.

The 722-unit closure and stable order are whole-corpus controls. `OLP-0001` is
the first scheduling unit, not the product boundary. The shared accepted cursor
advances only when both target units have passed their stated checks. One
language may be repaired independently without overwriting or certifying the
other.

The existing Bahasa Indonesia edition is a separate owner. Its manifest and QA
scripts supplied useful source-closure and localization-method evidence, but no
Indonesian prose, terminology, target hash or review claim enters either target.

The current shared cursor is recorded in `CURRENT_STATE.json`. Paired
direct-file closure is complete through `OLP-0722`; there is no next
translation cursor for this pinned source release. Fifteen post-closure target
repairs across fourteen manifest rows are rebound by
`QA_RECEIPT_POST_CLOSURE_BUILD_REPAIRS_OLP0001_0722_AR_FA_20260818.md`.
The active gate is now the complete dependency build, PDF convergence,
rendering, extraction and accessibility replay. Generated outputs from earlier
attempts were removed after verified cleanup and are not currently present;
fresh outputs and their hashes must be generated before release claims are
made.
