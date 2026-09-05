"""Fail-closed, read-only repair plan for the pinned reader's body references.

The order rule is restricted to the pinned PDF; it is corroborated against all
exact two-edge anchors and against auxiliary destination labels for every
changed reference. It must not be reused as an unverified general PDF rule.
"""
from __future__ import annotations
import argparse
import collections
import hashlib
import json
import re
from pathlib import Path

import fitz
from diagnose_standalone_link_geometry import digest, overlap, box

PIN = '51c0d396feb86eef17cffe38c58a7b1a1556e49c8a218d12d9e63111151e9aec'


def braces(text):
    parts=[]
    depth=0
    start=None
    for i,c in enumerate(text):
        if c=='{' and (i==0 or text[i-1]!='\\'):
            if depth==0:start=i+1
            depth+=1
        elif c=='}' and (i==0 or text[i-1]!='\\'):
            depth-=1
            if depth==0:parts.append(text[start:i])
            if depth<0:raise ValueError('unbalanced braces')
    if depth:raise ValueError('unbalanced braces')
    return parts


def read_labels(path):
    labels=collections.defaultdict(set)
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.startswith('\\newlabel{'):continue
        outer=braces(line)
        if len(outer)!=2:continue
        fields=braces(outer[1])
        if len(fields)>=4 and fields[0]:labels[fields[3]].add(fields[0])
    return labels


def horizontal_components(chars, other_chars, band):
    """Split a linked drawing run wherever a gap contains unrelated ink.

    A single annotation cannot describe a disjoint hit area. These components
    are a plan for duplicated action-preserving annotations, not blind clips.
    """
    intervals=sorted((c['bbox'][0],c['bbox'][2]) for c in chars if c['bbox'][2]>c['bbox'][0])
    output=[]
    for left,right in intervals:
        if not output:output.append([left,right]);continue
        prev=output[-1]
        foreign=any(prev[1]+.05 < (c[0]+c[2])/2 < left-.05 and overlap(c,band)>.45 for c in other_chars)
        if foreign:output.append([left,right])
        else:prev[1]=max(prev[1],right)
    return output


def make_plan(pdf,aux,audit_path):
    if digest(pdf)!=PIN:raise ValueError('PDF is not the inspected pinned input')
    audit=json.loads(audit_path.read_text(encoding='utf-8'))
    if audit['sha256']!=PIN:raise ValueError('trace audit is not pinned input')
    labels=read_labels(aux)
    document=fitz.open(pdf)
    repairs=[]
    failures=[]
    exact_anchor_count=0
    body_count=0
    for page_number in range(29,len(document)+1):
        links=[r for r in audit['links'] if r['page']==page_number and r['color']==[1.,0.,0.]]
        groups=[g for g in audit['glyph_groups'] if g['page']==page_number and g['color']==[1.,0.,0.]]
        if len(links)!=len(groups):raise ValueError(f'Body mapping cardinality mismatch p{page_number}')
        page=document[page_number-1]
        all_chars=[list(c[3]) for span in page.get_texttrace() for c in span['chars'] if not chr(c[0]).isspace()]
        for link,group in zip(links,groups):
            body_count+=1
            if len(link['left'])==len(link['right'])==1 and link['left']==link['right']:
                if link['left'] != [group['index']]:raise ValueError(f'Order contradicts exact anchors {link}')
                exact_anchor_count+=1
            r=link['rect']; g=group['bbox']
            own={tuple(c['bbox']) for c in group['chars']}
            others=[c for c in all_chars if tuple(round(v,5) for v in c) not in own]
            components=horizontal_components(group['chars'],others,g)
            horizontal_error=max(abs((g[0]-.996)-r[0]),abs((g[2]+.996)-r[2]))
            if horizontal_error <= 1.5 and len(components)==1:continue
            expected=sorted(labels.get(link['target'],set()))
            numbers=re.findall(r'\d+(?:\.\d+)*',group['text'])
            numeric_expected=[s for s in expected if re.fullmatch(r'\d+(?:\.\d+)*',s)]
            proven=len(numeric_expected)==1 and numeric_expected[0] in numbers
            if not proven:
                failures.append({'page':page_number,'xref':link['xref'],'target':link['target'],
                    'text':group['text'],'expected_labels':expected,'reason':'Auxiliary label does not prove drawing-run ownership'})
                continue
            new_rects=[[round(c[0]-.996,5),r[1],round(c[1]+.996,5),r[3]] for c in components]
            repairs.append({'page':page_number,'xref':link['xref'],'target':link['target'],
                'old_rect':r,'glyph_text':group['text'],'glyph_group':group['index'],
                'glyph_bbox':g,'expected_label':numeric_expected[0],
                'new_rects':new_rects,'was_outside':link['outside'],
                'proof':'pinned body annotation/drawing order; exact-anchor corroboration; auxiliary destination label and visible numeric token agree'})
    return {'schema':'standalone-reference-geometry-plan-v1','input_sha256':PIN,
        'aux_sha256':digest(aux),'audit_sha256':digest(audit_path),
        'input':str(pdf.resolve()),'aux':str(aux.resolve()),'status':'PROPOSED_NOT_APPLIED',
        'body_references':body_count,'exact_two_edge_order_corroborations':exact_anchor_count,
        'repairs':repairs,'unresolved':failures,
        'counts':{'proposed_reference_repairs':len(repairs),'outside':sum(r['was_outside'] for r in repairs),
            'in_page':sum(not r['was_outside'] for r in repairs),'split_disjoint':sum(len(r['new_rects'])>1 for r in repairs),
            'unresolved':len(failures)}}


def main():
    p=argparse.ArgumentParser()
    for name in ('input','aux','audit','output'):p.add_argument('--'+name,required=True,type=Path)
    args=p.parse_args()
    q=make_plan(args.input,args.aux,args.audit)
    args.output.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:q[k] for k in ('status','body_references','exact_two_edge_order_corroborations','counts','unresolved')},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
