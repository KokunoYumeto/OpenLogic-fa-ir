"""Finite exhaustive regression check of the explicitly stated decoder.

Not a proof of construction of a universal TM: checks the corrected final
output-validation phase against the source's unary-output definition.
"""
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
EN = Path('C:/interlanguage-production/openlogic-interfarsi/repo/source/upstream')
REL = 'content/turing-machines/undecidability/universal-tm.tex'
BASE = ROOT / 'source/locale/fa-IR' / REL
EXPECTED = '7fc0a70aaaccbdf6ecb21cf1f2dc686f65c4593f035922371f3df5b6847967df'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def reference(codes):
    if not codes or codes[0] != 1:
        return None
    tape = list(codes[1:])
    while tape and tape[-1] == 2:
        tape.pop()
    return len(tape) if all(c == 3 for c in tape) else None

def corrected(codes):
    if not codes or codes[0] != 1:
        return None
    strokes, blanks_started = 0, False
    for symbol in codes[1:]:
        if symbol == 2:
            blanks_started = True
        elif symbol == 3 and not blanks_started:
            strokes += 1
        else:
            return None
    return strokes

def inherited(codes):
    if not codes or codes[0] != 1:
        return None
    strokes = 0
    for symbol in codes[1:]:
        if symbol == 2:
            return strokes
        if symbol != 3:
            return None
        strokes += 1
    return strokes

# Bind actual current bytes explicitly rather than silently modifying them.
assert digest(BASE) == EXPECTED, 'Baseline identity differs; inspect before proceeding'
checked = 0
old_false_accepts = 0
for length in range(9):
    for word in product((2, 3, 4), repeat=length):
        codes = (1,) + word
        assert corrected(codes) == reference(codes), codes
        old_false_accepts += inherited(codes) is not None and reference(codes) is None
        checked += 1
for malformed in ((), (2,), (3,), (4,), (1, 1), (1, 3, 1)):
    assert corrected(malformed) == reference(malformed) is None
    checked += 1
counterexample = [1, 3, 2, 3]
assert inherited(counterexample) == 1 and corrected(counterexample) is None
paths = {
    'persian_baseline': BASE,
    'english_universal_tm': EN / REL,
    'english_output_definition': EN / 'content/turing-machines/machines-computations/configuration.tex',
    'english_unary_definition': EN / 'content/turing-machines/machines-computations/unary-numbers.tex',
    'corrigendum': ROOT / 'source/locale/fa-IR/standalone-errata.tex',
    'test_script': Path(__file__),
}
report = {
    'schema': 'universal-tm-output-corrigendum-v1', 'unit': 'OLP-0267',
    'status': 'finite-regression-PASS', 'source_files_changed': 0,
    'reader_policy': 'Explicit adjacent corrigendum replaces the identified final validation instruction; original source is preserved.',
    'definitions': {'1': 'end marker', '2': 'blank', '3': 'stroke', '4': 'other symbol'},
    'tested_cases': checked, 'inherited_false_accepts_in_test_domain': old_false_accepts,
    'counterexample': {'encoded_tape': counterexample, 'inherited_output': 1, 'defined_numeric_output': None},
    'scope': 'All 9841 well-marked tape words up to 8 symbols over blank/stroke/other, plus 6 malformed cases.',
    'limits': 'Finite regression evidence plus direct invariant reasoning, not machine-verified unbounded proof or full universal-machine construction.',
    'invariant_reasoning': 'Before the first blank only strokes are counted; after the first blank only blanks are accepted. Thus accepted suffixes are exactly stroke* blank*, including empty suffix for zero. This equals the source output word after trimming trailing blanks.',
    'identities': {name: {'filename': path.name, 'bytes': path.stat().st_size, 'sha256': digest(path)} for name, path in paths.items()},
}
(ROOT / 'evidence/UNIVERSAL_TM_CORRIGENDUM_QA.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'status': report['status'], 'cases': checked, 'baseline_unchanged': True, 'counterexample': counterexample}))
