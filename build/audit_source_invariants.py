"""Compare protected formula/reference inventories against pinned English.

Exact inventory parity is useful evidence, not proof of prose equivalence.
Differences are persisted, never normalized away as automatic acceptance.
"""
import hashlib
import json
from collections import Counter
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
EN = Path('C:/interlanguage-production/openlogic-interfarsi/repo')
INDEX = EN / 'corpus/source-index.jsonl'
assert hashlib.sha256(INDEX.read_bytes()).hexdigest() == '4974d40e4ea7ffe915b7d2f6725d1535a34d9a897e04aab2cedcdf2553a581f2'

def strip_comments(s):
    return re.sub(r'(?<!\\)%[^\n]*', '', s)

def group(s, pos, opener='{', closer='}'):
    assert s[pos] == opener
    depth, cursor = 1, pos+1
    while cursor < len(s) and depth:
        if s[cursor] == '\\':
            cursor += 2
            continue
        if s[cursor] == opener:
            depth += 1
        elif s[cursor] == closer:
            depth -= 1
        cursor += 1
    if depth:
        raise ValueError('unbalanced protected argument')
    return s[pos+1:cursor-1], cursor

def math_inventory(s):
    chunks = []
    pattern = re.compile(r'(?<!\\)\$\$?|\\\[|\\\(|\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|eqnarray\*?)\}')
    cursor = 0
    while (m := pattern.search(s, cursor)):
        begin = m.group()
        end = {'$': '$', '$$': '$$', r'\[': r'\]', r'\(': r'\)'}.get(begin)
        end = end or r'\end{' + m.group(1) + '}'
        finish_start, finish_end = None, None
        if end.startswith('$'):
            depth, at = 0, m.end()
            while at < len(s):
                if s[at] == '\\':
                    at += 2
                    continue
                if s[at] == '{':
                    depth += 1
                elif s[at] == '}':
                    depth -= 1
                elif depth == 0 and s.startswith(end, at):
                    finish_start, finish_end = at, at+len(end)
                    break
                at += 1
        else:
            finish = re.search(re.escape(end), s[m.end():])
            if finish:
                finish_start, finish_end = m.end()+finish.start(), m.end()+finish.end()
        if finish_start is None:
            chunks.append('<UNTERMINATED:'+begin+'>')
            break
        raw = s[m.end():finish_start]
        chunks.append(re.sub(r'\s+', '', raw))
        cursor = finish_end
    return Counter(chunks)

def protected_calls(s):
    result = Counter()
    # Optional arguments are part of the exact reference identity. Compare
    # multisets because translated prose can move references within a sentence.
    pattern = re.compile(r'\\(?:[Oo]lref|[cC]ref|ref|eqref|pageref|label|ollabel|cite[a-zA-Z]*|url|href)\*?(?![A-Za-z])')
    for m in pattern.finditer(s):
        pos, args = m.end(), []
        while pos < len(s):
            while pos < len(s) and s[pos].isspace():
                pos += 1
            if pos >= len(s) or s[pos] not in '[{':
                break
            opener = s[pos]
            content, pos = group(s, pos, opener, ']' if opener == '[' else '}')
            args.append(opener+re.sub(r'\s+', '', content)+(']' if opener == '[' else '}'))
            if opener == '{':
                break  # href display prose is deliberately not an identifier
        if args:
            result[m.group()+''.join(args)] += 1
    return result

def delta(a, b):
    return {'english_only': list((a-b).elements()), 'persian_only': list((b-a).elements())}

def prose_projection(chunk):
    """Mask plain alphabetic labels only; retain embedded math and numerals.

    This merely identifies localizable text slots. It never certifies that
    their translations have the right meaning, and the raw difference remains.
    """
    pattern = re.compile(r'\\(?:text|textrm|textnormal|mbox)\{')
    cursor, out = 0, []
    for m in pattern.finditer(chunk):
        if m.start() < cursor:
            continue
        try:
            content, end = group(chunk, m.end()-1)
        except ValueError:
            return chunk  # retain any unparsed source bytes without masking
        allowed = all(c.isalpha() or c.isspace() or unicodedata.category(c).startswith('M')
                      or c in '.,:;!?()\u060c\u061b\u061f\u200c\u200d-\u2013\u2014' for c in content)
        if not allowed:
            continue
        out.append(chunk[cursor:m.end()])
        out.append('<localized-prose>}')
        cursor = end
    out.append(chunk[cursor:])
    return ''.join(out)

rows = []
for row in map(json.loads, INDEX.read_text(encoding='utf-8').splitlines()):
    en_bytes = (EN / row['local_path']).read_bytes()
    assert hashlib.sha256(en_bytes).hexdigest().upper() == row['source_sha256']
    fa_bytes = (ROOT / 'source/locale/fa-IR' / row['source_path']).read_bytes()
    english, persian = [strip_comments(x.decode('utf-8-sig')) for x in (en_bytes, fa_bytes)]
    math = delta(math_inventory(english), math_inventory(persian))
    projected_math = delta(Counter(prose_projection(x) for x in math_inventory(english).elements()),
                           Counter(prose_projection(x) for x in math_inventory(persian).elements()))
    calls = delta(protected_calls(english), protected_calls(persian))
    rows.append({'id': row['unit_id'], 'path': row['source_path'],
                 'english_sha256': hashlib.sha256(en_bytes).hexdigest(),
                 'persian_sha256': hashlib.sha256(fa_bytes).hexdigest(),
                 'math_difference': math, 'math_plain_prose_projection_difference': projected_math,
                 'reference_difference': calls})

math_diff = [x['id'] for x in rows if any(x['math_difference'].values())]
ref_diff = [x['id'] for x in rows if any(x['reference_difference'].values())]
projected_diff = [x['id'] for x in rows if any(x['math_plain_prose_projection_difference'].values())]
report = {'schema': 'farsi-source-inventory-audit-v1', 'source_units': len(rows),
          'math_exact_inventory_units': len(rows)-len(math_diff), 'math_differing_units': math_diff,
          'reference_exact_inventory_units': len(rows)-len(ref_diff), 'reference_differing_units': ref_diff,
          'plain_math_prose_projection_exact_units': len(rows)-len(projected_diff),
          'plain_math_prose_projection_differing_units': projected_diff,
          'status': 'differences-require-classification' if math_diff or ref_diff else 'exact-inventory-parity',
          'limitations': 'Protected span inventory only; not proof of complete TeX parsing or prose semantics. No inherited source edits.',
          'records': rows}
output = ROOT / 'evidence/SOURCE_INVARIANT_AUDIT.json'
output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({k: v for k, v in report.items() if not isinstance(v, list)}))
