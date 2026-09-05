"""Generate additive, source-hash-bound standalone placement data; never run TeX.

Only generated files in locale/fa-IR/standalone and the named integration ledger
are written. --check performs exact deterministic byte comparison without writes.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import posixpath
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALE = ROOT / "source/locale/fa-IR"
OUT = LOCALE / "standalone"
MANIFEST = ROOT / "evidence/controls/CLOSURE_MANIFEST.csv"
MANIFEST_HASH = "ea3fa09516af7dd55851026ad597820544fc8750aa628f9d28780be02377b9a5"
LEDGER = ROOT / "evidence/STANDALONE_INTEGRATION_LEDGER.json"

# Target IDs, not translated prose or mathematical bodies. Injected subfiles keep
# their original bytes, file IDs and logical-system context. These choices are
# explicit, reversible editorial placements, not a claim of expert consultation.
AFTER_PATHS = {
    "content/first-order-logic/first-order-logic.tex": ["OLP-0685"],
    "content/sets-functions-relations/functions/composition.tex": ["OLP-0717"],
    "content/sets-functions-relations/sets/pairs-and-products.tex": ["OLP-0721"],
    "content/first-order-logic/axiomatic-deduction/provability-quantifiers.tex": ["OLP-0643"],
    "content/first-order-logic/completeness/complete-consistent-sets.tex": ["OLP-0644"],
    "content/incompleteness/representability-in-q/basic-representable.tex": ["OLP-0648", "OLP-0647"],
    "content/intuitionistic-logic/semantics/semantic-notions.tex": ["OLP-0649"],
    "content/lambda-calculus/lambda-definability/pairs.tex": ["OLP-0650"],
    "content/lambda-calculus/syntax/eta.tex": ["OLP-0651"],
    "content/many-valued-logic/sequent-calculus/propositional-rules.tex": ["OLP-0652"],
    "content/model-theory/basics/dlo.tex": ["OLP-0653"],
    "content/normal-modal-logic/syntax-and-semantics/entailment.tex": ["OLP-0654"],
    "content/proof-theory/sequent-calculus/rules-proofs.tex": ["OLP-0705", "OLP-0708", "OLP-0709", "OLP-0710"],
    "content/proof-theory/cut-elimination/ce-largest.tex": ["OLP-0660"],
    "content/proof-theory/normalization/normalization.tex": ["OLP-0681"],
    "content/proof-theory/propositions-as-types/introduction.tex": ["OLP-0694"],
    "content/first-order-logic/axiomatic-deduction/provability-propositional.tex": ["OLP-0715", "OLP-0714"],
    "content/second-order-logic/syntax-and-semantics/introduction.tex": ["OLP-0716"],
}
BEFORE_PATHS = {
    "content/first-order-logic/syntax-and-semantics/first-order-languages.tex": ["OLP-0645"],
    "content/methods/induction/introduction.tex": ["OLP-0718"],
}
VARIANTS = ["OLP-0720", "OLP-0719", "OLP-0722", "OLP-0646"]
NAMESPACED = {"OLP-0643": "retained:OLP-0643"} | {i: "variant:" + i for i in VARIANTS}
CANONICAL_ANCHORS = {"OLP-0720": "OLP-0003", "OLP-0719": "OLP-0011", "OLP-0722": "OLP-0027", "OLP-0646": "OLP-0149"}
FRAGMENT = "OLP-0660"
INJECTION_CONTEXT = {"OLP-0644": "FOL", "OLP-0715": "PL", "OLP-0714": "PL"}

EDGE = re.compile(r"\\(?P<kind>olimport|subfile)(?P<star>\*)?\s*(?:\[(?P<directory>[^\]]*)\])?\s*\{(?P<file>[^{}]*)\}(?:\s*\[(?P<section>[^\]]*)\])?")
FILEID = re.compile(r"\\olfileid(?:\[[^\]]*\])?\{([^{}]+)\}\{([^{}]+)\}\{([^{}]+)\}")
CHAPTER = re.compile(r"\\olchapter(?:\[[^\]]*\])?\{([^{}]+)\}\{([^{}]+)\}")
PART = re.compile(r"\\olpart(?:\[[^\]]*\])?\{([^{}]+)\}")
LITERAL_LABEL = re.compile(r"\\label\{([^{}]+)\}")
OL_LABEL = re.compile(r"\\ollabel\{([^{}]+)\}")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def uncomment(text: str) -> str:
    # Import and identifier syntax contains no verbatim command examples. Preserve
    # escaped percent signs and remove TeX line comments deterministically.
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def explicit_labels(text: str) -> list[str]:
    labels = set(LITERAL_LABEL.findall(text))
    ids = FILEID.findall(text)
    for pieces in ids:
        prefix = ":".join(pieces)
        labels.update(prefix + ":" + suffix for suffix in OL_LABEL.findall(text))
        if r"\olsection" in text:
            labels.add(prefix + ":sec")
    labels.update(a + ":" + b + "::chap" for a, b in CHAPTER.findall(text))
    labels.update(a + ":::part" for a in PART.findall(text))
    return sorted(labels)


def balanced_argument(text, pos):
    while pos < len(text) and text[pos].isspace():
        pos += 1
    if pos >= len(text) or text[pos] != "{":
        raise ValueError("Expected literal braced tag argument")
    start, depth = pos + 1, 1
    pos += 1
    while pos < len(text):
        if text[pos] == "\\":
            pos += 2
            continue
        if text[pos] == "{":
            depth += 1
        elif text[pos] == "}":
            depth -= 1
            if not depth:
                return text[start:pos], start, pos, pos + 1
        pos += 1
    raise ValueError("Unbalanced source tag branch")


def edge_context(text, edge_position, incoming_context, defaults):
    tags = dict(defaults)
    tags["FOL"] = incoming_context == "FOL"
    tags["notFOL"] = incoming_context != "FOL"
    for m in re.finditer(r"\\tag(true|false)\{([^{}]+)\}", text[:edge_position]):
        for tag in m[2].split(","):
            tags[tag.strip()] = m[1] == "true"
            tags["not" + tag.strip()] = m[1] != "true"
    for m in re.finditer(r"\\iftag\s*\{", text):
        names, _, _, end = balanced_argument(text, m.end() - 1)
        _, true_start, true_end, end = balanced_argument(text, end)
        _, false_start, false_end, _ = balanced_argument(text, end)
        choice = any(tags.get(name.strip(), False) for name in names.split(","))
        if true_start <= edge_position < true_end and not choice:
            return None
        if false_start <= edge_position < false_end and choice:
            return None
    return "FOL" if tags["FOL"] else "PL"


def generate() -> dict[Path, bytes]:
    manifest_bytes = MANIFEST.read_bytes()
    if sha(manifest_bytes) != MANIFEST_HASH:
        raise ValueError("Pinned closure manifest hash mismatch")
    rows = list(csv.DictReader(io.StringIO(manifest_bytes.decode("utf-8-sig"))))
    assert len(rows) == 722
    by_id = {r["closure_id"]: r for r in rows}
    by_path = {r["source_path"]: r for r in rows}
    assert len(by_id) == len(by_path) == 722
    defaults = {}
    for m in re.finditer(r"\\tag(true|false)\{([^{}]+)\}", uncomment((ROOT / "source/open-logic-config.sty").read_text(encoding="utf-8-sig"))):
        for tag in m[2].split(","):
            defaults[tag.strip()] = m[1] == "true"
            defaults["not" + tag.strip()] = m[1] != "true"
    assert defaults["FOL"] and all(defaults[t] for t in ("prfSC", "prfND", "prfAX", "prfTab"))
    edges: dict[str, list[dict]] = {}
    texts: dict[str, str] = {}
    for row in rows:
        data = (LOCALE / row["source_path"]).read_bytes()
        if sha(data) != row["fa_IR_sha256"].lower():
            raise ValueError("Baseline target changed: " + row["source_path"])
        text = uncomment(data.decode("utf-8-sig"))
        texts[row["closure_id"]] = text
        edges[row["closure_id"]] = []
        for match in EDGE.finditer(text):
            g = match.groupdict()
            if g["star"]:
                base = "content"
            else:
                base = posixpath.dirname(row["source_path"])
            target = posixpath.normpath(posixpath.join(base, g["directory"] or "", g["file"]))
            if not target.endswith(".tex"):
                target += ".tex"
            if target not in by_path:
                raise ValueError(f"Unresolved edge {row['source_path']} -> {target}")
            edges[row["closure_id"]].append({
                "kind": g["kind"] + (g["star"] or ""),
                "directory": g["directory"] or "",
                "argument": g["file"], "section_mode": g["section"] or "section",
                "target": by_path[target]["closure_id"],
                "source_position": match.start(),
            })
    before = {by_path[p]["closure_id"]: v for p, v in BEFORE_PATHS.items()}
    after = {by_path[p]["closure_id"]: v for p, v in AFTER_PATHS.items()}
    for mapping in (before, after):
        for target_ids in mapping.values():
            for identifier in target_ids:
                assert identifier in by_id
    assert len([i for ids in before.values() for i in ids] + [i for ids in after.values() for i in ids]) == len(set(i for ids in list(before.values()) + list(after.values()) for i in ids))

    def walk(roots: list[str], *, integrated: bool):
        visited, order, repeats, suppressed = set(), [], [], []
        ancestry = []

        def visit(identifier, parent=None, how="root", context="FOL"):
            key = identifier + "/" + context
            if key in visited:
                repeats.append({"id": identifier, "context": context, "from": parent, "kind": how})
                return
            if key in ancestry:
                raise ValueError("Recursive source graph")
            ancestry.append(key)
            if integrated:
                for child in before.get(identifier, []):
                    if INJECTION_CONTEXT.get(child, context) == context:
                        visit(child, identifier, "insert_before", context)
            visited.add(key)
            order.append({"id": identifier, "context": context, "key": key, "parent": parent, "via": how})
            for edge in edges[identifier]:
                if integrated and identifier in VARIANTS:
                    suppressed.append({"from": identifier, **edge})
                else:
                    child_context = edge_context(texts[identifier], edge["source_position"], context, defaults)
                    if child_context is not None:
                        visit(edge["target"], identifier, "source_" + edge["kind"], child_context)
            if integrated:
                for child in after.get(identifier, []):
                    if INJECTION_CONTEXT.get(child, context) == context:
                        visit(child, identifier, "insert_after", context)
            ancestry.pop()

        for root in roots:
            visit(root)
        return visited, order, repeats, suppressed

    primary_keys, _, primary_repeats, _ = walk(["OLP-0001", "OLP-0002"], integrated=False)
    primary = {key.split("/")[0] for key in primary_keys}
    expected_primary = {r["closure_id"] for r in rows if r["canonical_reader_reachable"] == "true"}
    assert primary == expected_primary and len(primary) == 642, (len(primary), sorted(primary ^ expected_primary))
    visited, order, repeats, suppressed = walk(["OLP-0001", "OLP-0002"] + VARIANTS, integrated=True)
    visited_ids = {key.split("/")[0] for key in visited}
    if visited_ids != set(by_id):
        raise ValueError("Unplaced units: " + repr(sorted(set(by_id) - visited_ids)))
    positions = defaultdict(list)
    for n, item in enumerate(order):
        positions[item["id"]].append({"order": n + 1, **item})

    generated = ["% Generated by build/make_standalone_ledger.py; do not edit.", "% All 722 baseline hashes checked before generation."]
    placements = []
    label_remaps = []
    for row in rows:
        identifier = row["closure_id"]
        namespace = NAMESPACED.get(identifier, "canonical")
        mode = "variant" if identifier in VARIANTS else "input" if identifier == FRAGMENT else "subfile"
        occurrences = positions[identifier]
        item = occurrences[0]
        generated.append(r"\OLSADeclareUnit{%s}{%s}{%s}{%s}{%s}" % (identifier, row["source_path"], namespace, mode, row["source_role"]))
        if namespace != "canonical":
            owned = explicit_labels(texts[identifier])
            if not owned:
                raise ValueError("Namespaced unit has no resolved labels: " + identifier)
            for label in owned:
                mapped = namespace + ":" + label
                generated.append(r"\OLSADeclareLabel{%s}{%s}{%s}" % (identifier, label, mapped))
                label_remaps.append({"id": identifier, "source_label": label, "standalone_label": mapped})
        placements.append({
            "id": identifier, "source_path": row["source_path"], "source_sha256": row["fa_IR_sha256"].lower(),
            "source_bytes": len((LOCALE / row["source_path"]).read_bytes()), "source_role": row["source_role"],
            "former_reader_reachable": identifier in primary, "placement_order": item["order"],
            "placement_parent": item["parent"], "placement_mechanism": item["via"],
            "namespace": namespace, "inclusion_mode": mode,
            "source_imports": edges[identifier], "suppress_imports": identifier in VARIANTS,
            "expected_body_occurrences": len(occurrences), "expected_context_occurrences": occurrences,
            "display_policy": "internal_variant_appendix_without_shared_body_replay" if identifier in VARIANTS else "contextual_rule_fragment" if row["source_role"] == "auxiliary_fragment" else "coherent_subject_hierarchy",
        })
        for edge in edges[identifier]:
            generated.append(r"\OLSADeclareEdge{%s}{%s}{%s}{%s}{%s}" % (identifier, edge["kind"], edge["directory"], edge["argument"], edge["target"]))
    for mapping, macro in ((before, "Before"), (after, "After")):
        for anchor, targets in sorted(mapping.items()):
            generated.append(r"\OLSADeclare%s{%s}{%s}" % (macro, anchor, "".join(r"\OLSAInContext{%s}{%s}" % (INJECTION_CONTEXT.get(i, "any"), i) for i in targets)))
    for variant, canonical in CANONICAL_ANCHORS.items():
        assert variant in by_id and canonical in primary
        generated.append(r"\OLSADeclareCanonicalAnchor{%s}{%s}" % (variant, canonical))
    generated.append(r"\OLSADeclareExpectedOrder{%s}" % ",".join(i["key"] for i in order))
    assert len({r["standalone_label"] for r in label_remaps}) == len(label_remaps)
    all_source_labels = set().union(*(set(explicit_labels(text)) for text in texts.values()))
    aliases = []
    for source, target in re.findall(r"\\OLSADeclareAlias\{([^{}]+)\}\{([^{}]+)\}", (OUT / "context.tex").read_text(encoding="utf-8")):
        if target not in all_source_labels:
            raise ValueError("Alias target not found in source label inventory: " + target)
        aliases.append({"source_label": source, "target_label": target, "validation": "literal_source_target_exists; runtime AUX convergence still required"})
    assert len(aliases) == 16 and len({a["source_label"] for a in aliases}) == 16

    ledger = {
        "schema": "farsi-standalone-integration-ledger/1", "status": "PASS_STATIC_PLACEMENT_NOT_TEX_VALIDATED",
        "closure_manifest_sha256": MANIFEST_HASH, "source_targets": 722,
        "primary_graph_targets": 642, "retained_targets": 80,
        "integrated_proof_theory_targets": sum(r["source_path"].startswith("content/proof-theory/") for r in rows),
        "variant_wrappers": VARIANTS, "injections_before": before, "injections_after": after,
        "variant_canonical_anchor_targets": CANONICAL_ANCHORS,
        "expected_order": [i["key"] for i in order], "expected_unique_body_paths": 722,
        "expected_context_body_occurrences": len(order), "default_tags": defaults,
        "primary_lexical_duplicate_requests": primary_repeats,
        "integrated_lexical_duplicate_requests": repeats, "suppressed_variant_imports": suppressed,
        "label_remaps": label_remaps, "rows": placements,
        "reference_aliases": aliases,
        "validation": {"all_target_hashes_match": True, "all_import_edges_resolve": True, "every_source_context_placed_once": True, "all_722_unique_source_units_placed": True, "unique_namespaced_label_targets": True, "tex_run": False},
        "runtime_gate": "body runtime checks exact source-entry ID order/count and writes jobname.olunits; FLS and source bytes require post-build comparison too",
        "uncertainties": ["TeX expansion, floating layout, references, and typesetting have not been executed.", "Literal import replay is a deterministic structural model; runtime exact-order validation detects changed tag branches.", "Source-linked scholarly canon consultation remains separate from this placement implementation."],
    }
    return {
        OUT / "generated-ledger.tex": ("\n".join(generated) + "\n").encode("utf-8"),
        LEDGER: (json.dumps(ledger, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
    }


def verify_trace(ledger, trace_text):
    """Compare actual source-start records, not repetitive recorder INPUT lines."""
    expected = []
    by_id = {row["id"]: row for row in ledger["rows"]}
    for key in ledger["expected_order"]:
        identifier, context = key.split("/")
        row = by_id[identifier]
        expected.append("|".join([identifier, row["source_path"], row["namespace"], context, "1"]))
    lines = trace_text.lstrip("\ufeff").splitlines()
    if not lines or lines[0] != "id|source_path|namespace|FOL_context|occurrence":
        raise ValueError("Unexpected source-entry trace header")
    actual = lines[1:]
    if actual != expected:
        first = next((n for n, (a, b) in enumerate(zip(actual, expected), 1) if a != b), min(len(actual), len(expected)) + 1)
        raise ValueError(f"Source-entry trace mismatch at occurrence {first}; expected {len(expected)}, got {len(actual)}")
    return {"status": "PASS_TRACE", "source_paths": len(by_id), "context_occurrences": len(actual)}


def self_test(ledger):
    by_id = {r["id"]: r for r in ledger["rows"]}
    lines = ["id|source_path|namespace|FOL_context|occurrence"]
    for key in ledger["expected_order"]:
        identifier, context = key.split("/")
        row = by_id[identifier]
        lines.append("|".join([identifier, row["source_path"], row["namespace"], context, "1"]))
    verify_trace(ledger, "\n".join(lines))
    mutations = [lines[:-1], lines + [lines[-1]], lines[:1] + list(reversed(lines[1:])), [lines[0], lines[1].replace("canonical", "wrong")] + lines[2:]]
    for mutation in mutations:
        try:
            verify_trace(ledger, "\n".join(mutation))
        except ValueError:
            continue
        raise AssertionError("Negative trace mutation unexpectedly accepted")
    assert ledger["expected_unique_body_paths"] == 722
    assert ledger["expected_context_body_occurrences"] == 774
    assert sum(row["expected_body_occurrences"] == 2 for row in ledger["rows"]) == 52
    return {"positive_trace_test": "PASS", "negative_trace_tests": len(mutations), "tex_run": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--trace", type=Path, help="Verify an actual jobname.olunits; implies read-only --check")
    parser.add_argument("--self-test", action="store_true", help="In-memory positive/negative trace tests")
    args = parser.parse_args()
    products = generate()
    for path, data in products.items():
        if args.check or args.trace:
            if not path.exists() or path.read_bytes() != data:
                raise ValueError("Generated artifact differs: " + str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    ledger = json.loads(products[LEDGER])
    report = {"status": "PASS_CHECK" if args.check or args.trace else "PASS_GENERATED", "rows": len(ledger["rows"]), "files": {str(p.relative_to(ROOT)): sha(d) for p, d in products.items()}, "tex_run": False}
    if args.trace:
        report["actual_trace"] = verify_trace(ledger, args.trace.read_text(encoding="utf-8-sig"))
    if args.self_test:
        report["self_test"] = self_test(ledger)
    print(json.dumps(report))


if __name__ == "__main__":
    main()
