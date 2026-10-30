"""The two Persian changes from rzach's student (OpenLogic-translations issue 1), as one reusable function.

1. Ezafe after a final silent he: هٔ (U+0647 U+0654) and ۀ (U+06C0) become ه‌ی (he, ZWNJ, yeh).
2. The noun 'enumeration' برشماری becomes شمارش, with its plural and ezafe forms; the indefinite برشماری‌ای becomes
   شمارشی. Verb forms (برشماریم, برشمارید, برشمارد, ...), برشمردن, برشمردنی and برشمارنده are left alone.

usage: python -I fa_fix.py dry FILE...   (prints every noun context and the counts; changes nothing)"""
import re
import sys

HE_HAMZA, HE_YEH_ABOVE, ZWNJ = "هٔ", "ۀ", "‌"
EZAFE = "ه" + ZWNJ + "ی"
LETTER = "ء-يٮ-ۓەۺ-ۿ"  # Arabic-script letters (no diacritics, no ZWNJ)
NOUN = re.compile(r"(?<![" + LETTER + r"])برشماری(" + ZWNJ + r"ای(?![" + LETTER + r"])|(?![" + LETTER + r"]))")


def fix(text):
    """Return (new_text, counts)."""
    counts = {"ezafe_he_hamza": text.count(HE_HAMZA), "ezafe_heh_yeh_above": text.count(HE_YEH_ABOVE)}
    text = text.replace(HE_HAMZA, EZAFE).replace(HE_YEH_ABOVE, EZAFE)
    n_indef = n_noun = 0

    def sub(m):
        nonlocal n_indef, n_noun
        if m.group(1):
            n_indef += 1
            return "شمارشی"
        n_noun += 1
        return "شمارش"

    text = NOUN.sub(sub, text)
    counts["enumeration_noun"] = n_noun
    counts["enumeration_indefinite"] = n_indef
    return text, counts


if __name__ == "__main__" and sys.argv[1:2] == ["dry"]:
    sys.stdout.reconfigure(encoding="utf-8")
    for path in sys.argv[2:]:
        t = open(path, encoding="utf-8").read()
        print("=====", path.rsplit("/", 1)[-1])
        for m in NOUN.finditer(t):
            a, b = max(0, m.start() - 45), min(len(t), m.end() + 35)
            print("  ", t[a:m.start()].replace("\n", " "), "【" + m.group(0) + "】", t[m.end():b].replace("\n", " "))
        left = re.findall(r"[" + LETTER + ZWNJ + r"ِ]*برشمار[" + LETTER + ZWNJ + r"ِ]*", NOUN.sub("", t))
        from collections import Counter
        print("left unchanged:", dict(Counter(left)))
        print("counts:", fix(t)[1])
