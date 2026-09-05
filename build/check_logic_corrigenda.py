"""Bounded countermodel regressions plus explicit unbounded reasoning notes."""
from pathlib import Path
from itertools import product
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
FA = ROOT / 'source/locale/fa-IR'
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

tests = []
for bits in product((False, True), repeat=2):
    for y in (0, 1):
        wide = all((not bits[x]) or bits[y] for x in (0, 1))
        narrow = (not all(bits)) or bits[y]
        assert narrow
        tests.append({'predicate': list(bits), 'y': y, 'wide_scope_alternative': wide, 'intended_narrow_scope': narrow})
assert sum(not x['wide_scope_alternative'] for x in tests) == 2

# Pin the actually loaded definition before modeling its expansion. This
# regression must stop if a later configuration introduces matrix grouping.
config_path = ROOT / 'source/open-logic-config.sty'
assert sha(config_path) == 'ab19be71b50b415738603290317b504d9fa6b82850fe640d585c62db1540ced3'
config = config_path.read_text(encoding='utf-8')
body = re.search(r'\\DeclareDocumentCommand \\lforall \{ o o \} \{(.*?)\n\}', config, re.S).group(1)
body = re.sub(r'%[^\n]*', '', body)
normalize = lambda s: re.sub(r'\s+', '', s)
expected = r'\IfNoValueTF{#1}{\forall}{\forall#1}\IfNoValueTF{#2}\relax{\,#2}'
assert normalize(body) == normalize(expected)
locale = (FA / 'open-logic-config.sty').read_text(encoding='utf-8')
assert r'\lforall' not in re.sub(r'%[^\n]*', '', locale)
antecedent = r'\Subst{!A}{x}{c}'
consequent = r'\Subst{!A}{x}{c}\Subst{}{y}{x}'
expanded_wide_argument = r'\forall x\,' + antecedent + r'\lif' + consequent
expanded_narrow_argument = (r'\forall x\,' + antecedent) + r'\lif' + consequent
assert expanded_wide_argument == expanded_narrow_argument
note = (FA / 'standalone-errata.tex').read_text(encoding='utf-8')
assert r'\bigl(\lforall[x][\Subst{!A}{x}{c}]\bigr)' in note
assert 'خطای معناییِ فرمولِ' in note and 'چاپ‌شده را اثبات نمی‌کند' in note

# The arithmetic counterexample is over N, not a finite model. A finite
# executable prefix checks the stated functions; the argument is inductive.
def successor(n): return n+1
def altered_addition(n, m): return n
numeral_value = 0
for n in range(1001):
    assert numeral_value == n
    numeral_value = successor(numeral_value)
assert altered_addition(1, 1) == 1 and 1+1 == 2

paths = [FA / 'content/model-theory/models-of-arithmetic/non-standard-models.tex',
         FA / 'content/first-order-logic/axiomatic-deduction/provability.tex',
         FA / 'standalone-errata.tex', config_path, FA / 'open-logic-config.sty', Path(__file__)]
report = {
    'schema': 'standalone-logic-corrigenda-regression-v2', 'status': 'PASS',
    'supersedes_classification_only': 'LOGIC_CORRIGENDA_QA.json; historical receipt preserved',
    'source_files_changed': 0,
    'quantifier_scope': {'unit': 'OLP-0643', 'cases': tests,
                        'intended_formula': '(forall x P(x)) -> P(y)',
                        'distinct_alternative_formula': 'forall x (P(x) -> P(y))',
                        'origin': 'shared macro-argument grouping inconsistency; explicit-parenthesis clarification',
                        'printed_semantic_error_proven': False,
                        'default_macro_outputs_equal': True,
                        'partial_expansion': expanded_wide_argument,
                        'macro_regression': 'Pinned loaded body, absent locale override, equal partial expansions; not a TeX rendering test'},
    'nonstandard_implication': {
        'unit': 'OLP-0194', 'correct_direction': 'nonstandard element implies nonstandard structure',
        'counterexample_domain': 'N', 'zero': 0, 'successor': 'n+1', 'addition': 'first projection',
        'numeral_prefix_tests': 1001,
        'unbounded_argument': 'By induction every numeral denotes its natural number. Any isomorphism preserving zero and successor fixes every numeral, hence is the identity on N. It cannot preserve addition since altered 1+1=1 but standard 1+1=2. The structure is nonstandard despite all elements being standard. It is not a model of Q.',
    },
    'limitations': 'Finite tests corroborate explicit arguments; not a complete translation certificate or proof-assistant verification.',
    'identities': [{'path': p.relative_to(ROOT).as_posix(), 'sha256': sha(p), 'bytes': p.stat().st_size} for p in paths],
}
(ROOT / 'evidence/LOGIC_CORRIGENDA_QA_V2.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'status': 'PASS', 'quantifier_cases': len(tests), 'numeral_prefix_cases': 1001}))
