"""Read-only glyph-trace audit of standalone PDF link hit regions.

Use drawing-level trace bounds, not text extraction's synthesized RTL spaces.
This diagnostic does not alter any PDF. All coordinates are top-left PDF points.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
from pathlib import Path

import fitz


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def box(rect):
    return [round(float(x), 5) for x in rect]


def overlap(a, b):
    return max(0, min(a[3], b[3]) - max(a[1], b[1])) / max(.001, min(a[3]-a[1], b[3]-b[1]))


def glyph_groups(page):
    groups = {}
    for span in page.get_texttrace():
        if span['type'] != 0:
            continue
        colour = tuple(round(float(c), 4) for c in span['color'])
        if colour in {(0., 0., 0.), (0.,)}:
            continue
        for char in span['chars']:
            if chr(char[0]).isspace():
                continue
            # A baseline partition prevents merging wrapped URL segments.
            key = (span['seqno'], colour, round(char[2][1], 1))
            group = groups.setdefault(key, {'seqno': span['seqno'], 'color': colour,
                'baseline': key[2], 'chars': [], 'bbox': None})
            group['chars'].append({'text':chr(char[0]), 'bbox':box(char[3])})
            r = fitz.Rect(char[3])
            group['bbox'] = r if group['bbox'] is None else group['bbox'] | r
    result = []
    for group in groups.values():
        group['text'] = ''.join(c['text'] for c in group['chars'])
        group['bbox'] = box(group['bbox'])
        result.append(group)
    return result


def audit(path):
    document = fitz.open(path)
    rows = []
    all_groups = []
    for page in document:
        groups = glyph_groups(page)
        for i, group in enumerate(groups):
            group['index'] = i
            group['page'] = page.number+1
        all_groups.extend(groups)
        for link in page.get_links():
            rect = list(link['from'])
            annotation = document.xref_object(link['xref'])
            color_string = document.xref_get_key(link['xref'], 'C')[1]
            color = tuple(round(float(c),4) for c in color_string.strip('[]').split())
            # URL annotations retain hyperref's cyan annotation colour while
            # the printed text is the configured achromatic ``darkgray``.
            # The full reader uses 0.20 and the isolated fixture uses xcolor's
            # 0.25 definition, so admit exactly those reviewed render colours.
            draw_colors = {(.2,.2,.2),(.25,.25,.25)} if color == (0.,1.,1.) else {color}
            same_band = [g for g in groups if g['color'] in draw_colors and overlap(rect,g['bbox']) >= .45]
            left = [g for g in same_band if .25 <= g['bbox'][0] - rect[0] <= 1.75]
            right = [g for g in same_band if .25 <= rect[2] - g['bbox'][2] <= 1.75]
            enclosed = [g for g in same_band if g['bbox'][0] >= rect[0]-.05 and g['bbox'][2] <= rect[2]+.05]
            rows.append({'page':page.number+1, 'xref':link['xref'], 'rect':box(rect),
                'width':round(rect[2]-rect[0],5), 'color':color,
                'draw_colors':[list(value) for value in sorted(draw_colors)],
                'target':link.get('nameddest') or link.get('uri') or link.get('file'),
                'outside':not page.rect.contains(link['from']),
                'left':[g['index'] for g in left], 'right':[g['index'] for g in right],
                'enclosed':[g['index'] for g in enclosed], 'band':[g['index'] for g in same_band]})
    return {'input':str(Path(path).resolve()),'sha256':digest(path),'pages':len(document),
            'links':rows,'glyph_groups':all_groups,
            'counts':{'links':len(rows),'outside':sum(r['outside'] for r in rows),
            'full_width_468':sum(abs(r['width']-468.244)<.02 for r in rows),
            'color':dict(collections.Counter(str(r['color']) for r in rows)),
            'anchors':dict(collections.Counter(f"{len(r['left'])}/{len(r['right'])}/{len(r['enclosed'])}" for r in rows))}}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=audit(args.input)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result['counts'],indent=2))


if __name__ == '__main__':
    main()
