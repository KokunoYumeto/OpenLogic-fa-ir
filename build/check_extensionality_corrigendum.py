"""Verify the concrete extensionality/existence correction's source and model."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source_path = ROOT / 'source/locale/fa-IR/content/sets-functions-relations/sets/basics.tex'
source = source_path.read_bytes()
assert hashlib.sha256(source).hexdigest() == '129320e9eea66762b41c28c6970dbac6a87d84433aec529a18bde8ae903f849c'
note_path = ROOT / 'source/locale/fa-IR/standalone-errata.tex'
note = note_path.read_text(encoding='utf-8')
assert note.count(r'\OLSADeclareAfter{OLP-0005}') == 1
assert 'یگانگی، نه وجود' in note and 'وجود داشته باشد' in note
domain = (0,)
relation = {(0, 0)}
extension = lambda a: {x for x in domain if (x, a) in relation}
assert all(extension(a) != extension(b) or a == b for a in domain for b in domain)
assert not any(extension(a) == set() for a in domain)
paths = [source_path, note_path, Path(__file__)]
receipt = {
    'schema': 'standalone-extensionality-corrigendum-v1', 'status': 'PASS',
    'unit': 'OLP-0005', 'source_files_changed': 0,
    'defect': 'The inherited example attributes existence as well as uniqueness to extensionality alone.',
    'correction': 'If a set with the specified members exists, extensionality implies it is unique.',
    'countermodel': {'domain': [0], 'membership_relation': [[0, 0]],
                     'satisfies_extensionality': True, 'has_empty_extension_object': False},
    'reasoning': 'The one-object membership structure satisfies extensionality but has no empty set. Thus even the false property has no corresponding set in a model of extensionality alone. If two sets do have precisely the objects satisfying a property, their extensions coincide and extensionality identifies them.',
    'scope': 'This is a countermodel to an entailment from extensionality alone, not a model of all ZF axioms or a whole-book semantic certificate.',
    'identities': [{'path': p.relative_to(ROOT).as_posix(), 'bytes': p.stat().st_size,
                    'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths],
}
(ROOT / 'evidence/EXTENSIONALITY_CORRIGENDUM_QA.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': 'PASS', 'countermodels': 1, 'source_files_changed': 0}))
