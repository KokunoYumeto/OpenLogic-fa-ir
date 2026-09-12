# Meaning checks on the revised Persian

These are same-agent back-reading checks against the exact source and candidate, not an independent translation or a human validation study. The complete57-span aligned review is in README.md and choices-evidence.json. Editorial additions below are deliberately disclosed, not falsely attributed to the source.

| Unit and passage | Persian reading | Back-reading and invariant |
| --- | --- | --- |
|0037, last paragraph|«مقایسه را در دو جهت جداگانه انجام دهیم»|Carry out the comparison in two separate directions: construct each of the two injections. Not a partition into cases; not equality of the sets themselves.|
|0038, ceiling|«کوچک‌ترین عدد صحیحِ بزرگ‌تر یا مساویِ آن»|The least integer greater than or equal to the argument. Equality at integers and rounding toward positive infinity are preserved.|
|0038, definition|«اگر و تنها اگر یا … باشد یا برشماری‌ای … وجود داشته باشد»|If and only if either the set is empty or an enumeration exists. Both directions and the empty exception remain.|
|0039, index sentence|«رقم mاُمِ رشتهٔ nاُمِ»|The mth digit of the nth string. Off-diagonal meaning agrees with the row/column convention; the two variable tokens were repaired, not translated away.|
|0039, bit flip|«هر1 را به0 و هر0 را به1»|Complement both binary values. Not a one-direction replacement, which could reproduce an original row. Actual candidate retains all four numbers as math spans.|
|0039, finite qualification|«برای یک مجموعهٔ نامتناهی»|The characterization is restricted to an infinite set. The adjacent note discloses why finite and empty sets prevent the unrestricted statement.|
|0040, surjective list|«هر عضو … را دست‌کم یک بار …» and «نخستین رخدادِ هر مقدار»|Every element occurs at least once; keep the first occurrence of each value. Exhaustiveness is not silently equated with injectivity.|
|0040, characteristic map|«رشتهٔ حاصل، عضویتِ هر عدد طبیعی در مجموعهٔ ورودی را تعیین می‌کند»|The output determines membership of every natural number in the input set, hence the input itself. This justifies injectivity, not merely surjectivity.|
|0040, disabled partial functions|«ممکن است برای بعضی ورودی‌ها تعریف نشده باشند»|Some inputs may have no defined value. No requirement of computation, finite domain, or nontermination is introduced.|

All eleven active exercises remain unsolved in the translation. Their mathematical soundness is checked separately in SOURCE_MATHEMATICS_REVIEW.md and the independent source audit. Conditional branches, cited page numbers, theorem labels and the existing disambiguated exercise label are preserved or explicitly mapped. The actual24-cell membership table check supplements these prose checks.
