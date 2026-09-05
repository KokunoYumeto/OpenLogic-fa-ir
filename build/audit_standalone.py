"""Independent immutable-source, recorder, and standalone-PDF checks.

This is not a linguistic certificate. PDF text boxes are diagnostic; rendered
pages still require visual inspection. Any structural PDF failure exits nonzero.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LOCALE = ROOT / 'source/locale/fa-IR'
AUDIT = Path('C:/interlanguage-task-state/openlogic-internationalization/persian-openlogic/SOURCE_READER_AUDIT.json')
AUDIT_HASH = 'e16d8e3fcfe8fe1099e2dfcd572632469c2961087db1d0878aeb42fbf671d819'
MANIFEST = Path('C:/interlanguage-task-state/openlogic-internationalization/persian-openlogic/standalone-staging/STAGED_FILE_MANIFEST.json')
MANIFEST_HASH = '97864216624a65e137332d70f6563515c3a17b304362e4267d2d589d4ded4103'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def bound_json(path, expected):
    data = path.read_bytes()
    if sha(data) != expected:
        raise ValueError(f'Input identity mismatch: {path.name}')
    return json.loads(data)

def source_audit():
    audit = bound_json(AUDIT, AUDIT_HASH)
    baseline = bound_json(MANIFEST, MANIFEST_HASH)
    failures = []
    for row in baseline['files']:
        path = ROOT / row['path']
        if not path.is_file():
            failures.append({'path': row['path'], 'error': 'missing'})
            continue
        data = path.read_bytes()
        if len(data) != row['bytes'] or sha(data) != row['sha256'].lower():
            failures.append({'path': row['path'], 'error': 'baseline bytes changed'})
    records = []
    for row in audit['records']:
        path = LOCALE / row['source_path']
        data = path.read_bytes()
        ok = len(data) == row['persian_bytes'] and sha(data) == row['persian_sha256'].lower()
        records.append({
            'id': row['id'], 'path': path.relative_to(ROOT).as_posix(),
            'sha256': sha(data), 'bytes': len(data), 'exact_baseline': ok,
            'role': row['source_role'], 'former_reader': row['manifest_reader_reachable'],
        })
        if not ok:
            failures.append({'id': row['id'], 'error': 'translation changed'})
    if len(records) != 722 or len({x['id'] for x in records}) != 722:
        failures.append({'error': 'expected exactly 722 unique source records'})
    return {'baseline_files': len(baseline['files']), 'source_units': len(records),
            'records': records, 'failures': failures,
            'source_audit_sha256': AUDIT_HASH, 'staging_manifest_sha256': MANIFEST_HASH}

def recorder_audit(fls, records):
    inputs = set()
    for line in fls.read_text(encoding='utf-8', errors='replace').splitlines():
        if not line.startswith('INPUT '):
            continue
        path = Path(line[6:].strip().strip('"'))
        if not path.is_absolute():
            path = LOCALE / path
        inputs.add(str(path.resolve()).casefold())
    missing = [r['id'] for r in records if str((ROOT / r['path']).resolve()).casefold() not in inputs]
    return {'fls_sha256': sha(fls.read_bytes()), 'expected_units': len(records),
            'included_units': len(records)-len(missing), 'missing_ids': missing,
            'note': 'FLS proves file access, not exact body execution; use assembly trace as well.'}

def pdf_audit(path):
    from pypdf import PdfReader
    import fitz
    reader = PdfReader(path)
    names = reader.named_destinations
    page_refs = {p.indirect_reference.idnum: i for i, p in enumerate(reader.pages)}
    failures, geometry, actions = [], [], Counter()
    def dest_valid(dest):
        if isinstance(dest, str):
            return dest in names
        if isinstance(dest, (list, tuple)) and dest:
            page = dest[0]
            return getattr(page, 'idnum', -1) in page_refs or isinstance(page, int) and 0 <= page < len(reader.pages)
        return False
    link_count = 0
    for n, page in enumerate(reader.pages, 1):
        box = list(map(float, page.mediabox))
        if abs(box[2]-box[0]-612) > .01 or abs(box[3]-box[1]-792) > .01:
            failures.append({'page': n, 'error': 'not Letter geometry', 'box': box})
        for ref in page.get('/Annots', []):
            item = ref.get_object()
            if item.get('/Subtype') != '/Link':
                continue
            link_count += 1
            rect = list(map(float, item.get('/Rect', [])))
            if len(rect) != 4 or rect[2] <= rect[0] or rect[3] <= rect[1]:
                failures.append({'page': n, 'xref': ref.idnum, 'error': 'nonpositive link rectangle', 'rect': rect})
            elif rect[0] < -.01 or rect[1] < -.01 or rect[2] > 612.01 or rect[3] > 792.01:
                geometry.append({'page': n, 'xref': ref.idnum, 'error': 'link outside page', 'rect': rect})
            action = item.get('/A')
            action = action.get_object() if action is not None else None
            if action:
                kind = str(action.get('/S'))
                actions[kind] += 1
                if kind == '/GoTo' and not dest_valid(action.get('/D')):
                    failures.append({'page': n, 'xref': ref.idnum, 'error': 'unresolved internal destination', 'destination': str(action.get('/D'))})
                elif kind not in ('/GoTo', '/URI'):
                    failures.append({'page': n, 'xref': ref.idnum, 'error': 'non-standalone or unsafe action', 'action': kind})
            elif '/Dest' in item:
                actions['/Dest'] += 1
                if not dest_valid(item['/Dest']):
                    failures.append({'page': n, 'xref': ref.idnum, 'error': 'unresolved direct destination'})
    outline_failures = []
    def visit(items):
        for item in items:
            if isinstance(item, list):
                visit(item)
            else:
                try:
                    number = reader.get_destination_page_number(item)
                    if number is None or not 0 <= number < len(reader.pages):
                        raise ValueError('invalid page')
                except Exception:
                    outline_failures.append(str(item.get('/Title', '')))
    visit(reader.outline)
    failures += [{'error': 'unresolved bookmark', 'title': t} for t in outline_failures]
    doc = fitz.open(path)
    protrusions, replacement_pages, empty_pages, fonts = [], [], [], set()
    for n, page in enumerate(doc, 1):
        text = page.get_text()
        if '\ufffd' in text:
            replacement_pages.append(n)
        if not text.strip():
            empty_pages.append(n)
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines', []):
                for span in line['spans']:
                    fonts.add(span['font'])
                    x0, y0, x1, y1 = span['bbox']
                    if span['text'].strip() and (x0 < 70 or x1 > 542 or y0 < 0 or y1 > 792):
                        protrusions.append({'page': n, 'bbox': [round(v, 2) for v in span['bbox']], 'text': span['text'][:100]})
    failures += [{'page': p, 'error': 'replacement glyph in extracted text'} for p in replacement_pages]
    return {'pdf': path.name, 'sha256': sha(path.read_bytes()), 'bytes': path.stat().st_size,
            'pages': len(reader.pages), 'link_count': link_count, 'actions': dict(actions),
            'named_destinations': len(names), 'failures': failures, 'geometry_failures': geometry,
            'layout_diagnostics': protrusions, 'empty_text_pages': empty_pages, 'fonts': sorted(fonts),
            'metadata_title': str((reader.metadata or {}).get('/Title', '')),
            'visual_review': 'required; not established by this script'}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pdf', type=Path)
    ap.add_argument('--fls', type=Path)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    report = {'schema': 'farsi-standalone-independent-audit-v1', 'source': source_audit()}
    if args.fls:
        report['recorder'] = recorder_audit(args.fls, report['source']['records'])
    if args.pdf:
        report['pdf'] = pdf_audit(args.pdf)
    failed = bool(report['source']['failures'] or report.get('recorder', {}).get('missing_ids') or
                  report.get('pdf', {}).get('failures') or report.get('pdf', {}).get('geometry_failures'))
    report['structural_status'] = 'FAIL' if failed else 'PASS'
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': report['structural_status'], 'baseline_files': report['source']['baseline_files'],
                      'units': report['source']['source_units'], 'pdf_pages': report.get('pdf', {}).get('pages'),
                      'pdf_errors': len(report.get('pdf', {}).get('failures', [])),
                      'geometry_errors': len(report.get('pdf', {}).get('geometry_failures', [])),
                      'layout_diagnostics': len(report.get('pdf', {}).get('layout_diagnostics', []))}))
    raise SystemExit(1 if failed else 0)

if __name__ == '__main__':
    main()
