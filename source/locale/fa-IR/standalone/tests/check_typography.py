"""Pinned-source and formula-preservation checks. This script never runs TeX."""
from pathlib import Path
import argparse
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
STANDALONE = HERE.parent
STAGING = Path("C:/interlanguage-task-state/openlogic-internationalization/persian-openlogic/standalone-staging/STAGED_FILE_MANIFEST.json")
STAGING_SHA = "97864216624a65e137332d70f6563515c3a17b304362e4267d2d589d4ded4103"
PREVIOUS_EVIDENCE = ROOT / "evidence/STANDALONE_TYPOGRAPHY_QA.json"
PREVIOUS_EVIDENCE_SHA = "d8f6f53d77fe91c9d6781a745f873e260202ff5f9aa20ae43f0eef1235006164"
EXPECTED_RULES = {
    "height-two-premises": ("OLP-0668", "period"),
    "height-three-premises": ("OLP-0668", "period"),
    "representability-equivalence": ("OLP-0290", "none"),
    "encoded-formula": ("OLP-0291", "none"),
    "substitution-before-expansion": ("OLP-0369", "comma"),
    "substitution-after-expansion": ("OLP-0369", "period"),
    "valuation-tuple": ("OLP-0163", "comma"),
    "sequent-depth-binary-case": ("OLP-0702", "period"),
    "sequent-height-two-premises": ("OLP-0711", "period"),
    "q-provability-m": ("OLP-0291", "comma"),
    "q-provability-l": ("OLP-0291", "period"),
    "composition-g-formula": ("OLP-0295", "none"),
    "relation-formula": ("OLP-0298", "none"),
    "relation-characteristic-positive": ("OLP-0298", "comma"),
    "second-order-term-set": ("OLP-0325", "comma"),
    "ordinal-type-beta": ("OLP-0556", "comma"),
    "union-injection-map": ("OLP-0588", "none"),
    "invertibility-b-context-sequent": ("OLP-0701", "atomic"),
}
EXPECTED_COUNTS = {name: 1 for name in EXPECTED_RULES}
EXPECTED_COUNTS.update({"q-provability-m": 2, "relation-formula": 3,
                        "invertibility-b-context-sequent": 2})
EXPECTED_EVENTS = sum(EXPECTED_COUNTS.values())

def expected_trace():
    return [(unit, name, str(i))
            for name, (unit, _) in EXPECTED_RULES.items()
            for i in range(1, EXPECTED_COUNTS[name] + 1)]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def normalized(text):
    return re.sub(r"\s", "", text)

def uncomment(text):
    return re.sub(r"(?<!\\)%[^\n]*", "", text)

def argument(text, offset):
    while text[offset].isspace():
        offset += 1
    assert text[offset] == "{", (offset, text[offset:offset + 50])
    start = offset + 1
    depth = 1
    offset = start
    while depth:
        if text[offset] == "\\":
            offset += 2
            continue
        if text[offset] == "{":
            depth += 1
        elif text[offset] == "}":
            depth -= 1
        offset += 1
    return text[start:offset - 1], offset

def registry(text):
    result = []
    declaration = re.compile(
        r"\\(?P<command>OLSADeclareDisplay|OLSADeclareAtomicInline)(?=\{)")
    for match in declaration.finditer(text):
        offset = match.end()
        args = []
        arity = 4 if match.group("command") == "OLSADeclareDisplay" else 3
        for _ in range(arity):
            value, offset = argument(text, offset)
            args.append(value)
        if arity == 4:
            unit, rule, punctuation, formula = args
        else:
            unit, rule, formula = args
            punctuation = "atomic"
        result.append({"unit": unit, "rule": rule, "punctuation": punctuation,
                       "formula": formula, "key": (unit, normalized(formula)),
                       "expected": 1})
    by_name = {row["rule"]: row for row in result}
    seen = set()
    for match in re.finditer(r"\\OLSASetDisplayCount(?=\{)", text):
        name, offset = argument(text, match.end())
        count, offset = argument(text, offset)
        assert name in by_name and name not in seen
        assert int(count) > 0
        by_name[name]["expected"] = int(count)
        seen.add(name)
    return result

def pairs(text):
    # The complete scoped files and their nested rule fragment have neither
    # display-dollar pairs nor literal escaped dollars. Nested maths in \text,
    # proof-tree boxes and \tag still use complete, ordinary paired delimiters.
    assert "$$" not in text
    assert r"\$" not in text
    assert text.count("$") % 2 == 0
    matches = list(re.finditer(r"\$([^$]*)\$", text))
    assert 2 * len(matches) == text.count("$")
    return matches

def model_reflow(unit, text, rules):
    by_key = {r["key"]: r for r in rules}
    count = {r["rule"]: 0 for r in rules if r["unit"] == unit}
    edits = []
    for match in pairs(text):
        key = (unit, normalized(match.group(1)))
        if key not in by_key:
            continue
        rule = by_key[key]
        count[rule["rule"]] += 1
        end = match.end()
        punctuation = {"none": "", "period": ".", "comma": "،",
                       "atomic": ""}[rule["punctuation"]]
        if punctuation:
            assert text[end:end + 1] == punctuation, rule["rule"]
            end += 1
        # Original payload is transported byte-for-byte in the text model.
        payload = match.group(1)
        if rule["punctuation"] == "atomic":
            replacement = r"\mbox{$" + payload + "$}"
        else:
            replacement = r"\[" + payload
            if punctuation:
                replacement += r"\text{" + punctuation + "}"
            replacement += r"\]"
        edits.append((match.start(), end, replacement, payload, rule["rule"]))
    assert count == {r["rule"]: r["expected"] for r in rules if r["unit"] == unit}, count
    transformed = text
    for start, end, replacement, _, _ in reversed(edits):
        transformed = transformed[:start] + replacement + transformed[end:]
    # Undo the exact planned edits and prove all source prose, formula payloads,
    # comments and punctuation are retained in the model.
    restored = transformed
    delta = 0
    for start, end, replacement, payload, name in edits:
        begin = start + delta
        assert restored[begin:begin + len(replacement)] == replacement
        original = text[start:end]
        restored = restored[:begin] + original + restored[begin + len(replacement):]
        # Earlier replacements have been undone, so offsets remain original.
        assert payload in replacement
    assert restored == text
    return edits

def expect_failure(fn):
    try:
        fn()
    except AssertionError:
        return
    raise AssertionError("negative test unexpectedly passed")

def check_trace(text):
    lines = text.splitlines()
    assert lines[0] == "source_id|rule|occurrence"
    observed = [tuple(line.split("|")) for line in lines[1:] if line]
    assert sorted(observed) == sorted(expected_trace()), observed
    assert len(observed) == EXPECTED_EVENTS
    return observed

def check_proof_transports(sources, typography):
    """Check the exact local dollar bridge, not an assumed mode toggle."""
    interfaces = {"Axiom": ("axiom", "Axiom"),
                  "Deduce": ("deduce", "Deduce"),
                  "UnaryInf": ("unary", "Unary"),
                  "BinaryInf": ("binary", "Binary")}
    selected = {
        "OLP-0701": ("Deduce", "UnaryInf", "BinaryInf"),
        "OLP-0702": ("Axiom", "Deduce", "UnaryInf", "BinaryInf"),
        "OLP-0711": ("Axiom", "UnaryInf", "BinaryInf"),
    }
    observed = []
    for name, (original, suffix) in interfaces.items():
        assert rf"\NewCommandCopy \olsa_typography_original_{original} \{name}" in typography
        assert rf"{{\olsa_typography_original_{original} $#1$}}" in typography
        assert rf"\protected\long\gdef\OLSATypographyActive{suffix}$#1${{\OLSATypography{suffix}Transport{{#1}}}}" in typography
        assert rf"\cs_set_eq:NN \{name} \olsa_typography_original_{original}" in typography
    for unit, expected_interfaces in selected.items():
        marker = rf"\str_if_eq:VnT \l_olsa_typography_key_tl {{{unit}}}"
        marker_offset = typography.index(marker) + len(marker)
        selection_block, _ = argument(typography, marker_offset)
        for name, (_, suffix) in interfaces.items():
            assignment = rf"\cs_set_eq:NN \{name} \OLSATypographyActive{suffix}"
            assert (assignment in selection_block) == (name in expected_interfaces)
        source = sources[unit]
        for name in interfaces:
            matches = list(re.finditer(r"\\" + name + r"\$([^$]*)\$", source))
            assert bool(matches) == (name in expected_interfaces), (unit, name, len(matches))
            for match in matches:
                payload = match.group(1)
                assert payload.count(r"\fCenter") == 1
                # Active entry consumes exactly the pair; transport emits the
                # same pair with cat-3 delimiters, without retokenizing #1.
                transported = "\\" + name + "$" + payload + "$"
                assert transported == match.group(0)
                observed.append({"source_id": unit, "command": name,
                                 "source_line": source.count("\n", 0, match.start()) + 1,
                                 "payload_sha256": sha(payload.encode("utf-8")),
                                 "payload_preserved_exactly": True})
    counts = {(unit, name): sum(r["source_id"] == unit and r["command"] == name
                                for r in observed)
              for unit, names in selected.items() for name in names}
    assert counts == {
        ("OLP-0701", "Deduce"): 20,
        ("OLP-0701", "UnaryInf"): 4,
        ("OLP-0701", "BinaryInf"): 8,
        ("OLP-0702", "Axiom"): 14,
        ("OLP-0702", "Deduce"): 9,
        ("OLP-0702", "UnaryInf"): 37,
        ("OLP-0702", "BinaryInf"): 8,
        ("OLP-0711", "Axiom"): 9,
        ("OLP-0711", "UnaryInf"): 4,
        ("OLP-0711", "BinaryInf"): 3,
    }, counts
    assert len(observed) == 116, len(observed)
    assert typography.index(r"{\olsa_typography_original_axiom $#1$}") < typography.index(r"\catcode`\$=13")
    return observed

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-evidence", action="store_true")
    parser.add_argument("--trace-log", type=Path)
    parser.add_argument("--trace-file", type=Path)
    args = parser.parse_args()
    staging_bytes = STAGING.read_bytes()
    assert sha(staging_bytes) == STAGING_SHA
    baseline = json.loads(staging_bytes.decode("utf-8-sig"))["files"]
    assert len(baseline) == 828
    for record in baseline:
        data = (ROOT / record["path"]).read_bytes()
        assert len(data) == record["bytes"], record["path"]
        assert sha(data) == record["sha256"], record["path"]

    ledger = json.loads((ROOT / "evidence/STANDALONE_INTEGRATION_LEDGER.json").read_text(encoding="utf-8"))
    rows = {r["id"]: r for r in ledger["rows"]}
    typography = (STANDALONE / "typography.tex").read_text(encoding="utf-8")
    rules = registry(typography)
    assert len(rules) == 18
    assert len({r["key"] for r in rules}) == 18
    assert {r["rule"]: (r["unit"], r["punctuation"]) for r in rules} == EXPECTED_RULES
    assert {r["rule"]: r["expected"] for r in rules} == EXPECTED_COUNTS
    previous_bytes = PREVIOUS_EVIDENCE.read_bytes()
    assert sha(previous_bytes) == PREVIOUS_EVIDENCE_SHA
    previous = json.loads(previous_bytes)
    by_name = {r["rule"]: r for r in rules}
    assert len(previous["display_rules"]) == 6
    for old in previous["display_rules"]:
        current = by_name[old["rule"]]
        assert current["unit"] == old["source_id"]
        assert current["punctuation"] == old["punctuation"]
        assert current["expected"] == old["expected_runtime_occurrences"] == 1
        assert sha(normalized(current["formula"]).encode("utf-8")) == old["normalized_formula_sha256"]
    results = []
    sources = {}
    for unit in sorted({r["unit"] for r in rules}):
        row = rows[unit]
        path = ROOT / "source/locale/fa-IR" / row["source_path"]
        data = path.read_bytes()
        assert sha(data) == row["source_sha256"]
        text = data.decode("utf-8")
        sources[unit] = text
        edits = model_reflow(unit, text, rules)
        occurrences = {}
        for start, end, replacement, payload, name in edits:
            occurrences[name] = occurrences.get(name, 0) + 1
            results.append({
                "rule": name, "source_id": unit,
                "source_path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "source_sha256": sha(data), "source_line": text.count("\n", 0, start) + 1,
                "expected_runtime_occurrences": EXPECTED_COUNTS[name],
                "occurrence": occurrences[name],
                "original_payload_sha256": sha(payload.encode("utf-8")),
                "normalized_formula_sha256": sha(normalized(payload).encode("utf-8")),
                "original_payload_preserved_exactly": True,
                "prose_and_punctuation_reversible": True,
                "punctuation": EXPECTED_RULES[name][1],
            })
        # A numerical formula change is rejected rather than approximately matched.
        target = next(r for r in rules if r["unit"] == unit)
        original = next(m.group(1) for m in pairs(text) if normalized(m.group(1)) == target["key"][1])
        expect_failure(lambda: model_reflow(unit, text.replace(original, original + "+0", 1), rules))
        final_mark = {"none": "", "period": ".", "comma": "،",
                      "atomic": ""}[target["punctuation"]]
        expect_failure(lambda: model_reflow(unit, text + "\n$" + original + "$" + final_mark, rules))
        # Matching is stable-unit scoped; same maths in another unit is unchanged.
        assert model_reflow("UNREGISTERED-UNIT", "$" + original + "$", rules) == []

    # Nested source resets to ordinary dollar catcode. It also has no matching
    # rule in the independent model, including its proof-tree arguments.
    fragment = ROOT / "source/locale/fa-IR" / rows["OLP-0666"]["source_path"]
    assert model_reflow("OLP-0666", fragment.read_text(encoding="utf-8"), rules) == []
    # Repeated math inside an existing display is paired, not toggled by mode.
    assert model_reflow("UNREGISTERED-UNIT", r"\[\AxiomC{$x$}\text{if $y$}\tag{$Q_1$}\]", rules) == []
    # Target the two-premise item, not the earlier non-target one-premise item.
    target = next(r for r in rules if r["rule"] == "height-two-premises")
    hit = next(m for m in pairs(sources["OLP-0668"]) if normalized(m.group(1)) == target["key"][1])
    terminal = sources["OLP-0668"][:hit.end()] + "!" + sources["OLP-0668"][hit.end() + 1:]
    expect_failure(lambda: model_reflow("OLP-0668", terminal, rules))
    # The full-reader visual gate found the characteristic-function statement
    # escaping the left text-block margin on physical page 729. Its exact
    # formula and following Persian comma are now pinned independently of the
    # three pre-existing relation-formula occurrences.
    target = next(r for r in rules if r["rule"] == "relation-characteristic-positive")
    hit = next(m for m in pairs(sources["OLP-0298"])
               if normalized(m.group(1)) == target["key"][1])
    payload = hit.group(1)
    expect_failure(lambda: model_reflow(
        "OLP-0298", sources["OLP-0298"].replace(payload, payload + "+0", 1), rules))
    wrong_punctuation = (sources["OLP-0298"][:hit.end()] + "." +
                         sources["OLP-0298"][hit.end() + 1:])
    expect_failure(lambda: model_reflow("OLP-0298", wrong_punctuation, rules))
    # The three new overflow mappings have exactly one source occurrence, and
    # the atomic OLP-0701 payload has exactly the two independently mapped hits.
    assert {name: sum(r["rule"] == name for r in results) for name in (
        "second-order-term-set", "ordinal-type-beta", "union-injection-map",
        "invertibility-b-context-sequent")} == {
            "second-order-term-set": 1, "ordinal-type-beta": 1,
            "union-injection-map": 1, "invertibility-b-context-sequent": 2}
    assert r"{atomic}{\mbox{\c_math_toggle_token #1\c_math_toggle_token}}" in typography
    proof_transports = check_proof_transports(sources, typography)
    expect_failure(lambda: check_proof_transports(sources, typography.replace(r"{\olsa_typography_original_axiom $#1$}", r"{\olsa_typography_original_axiom #1}", 1)))
    expect_failure(lambda: check_proof_transports(sources, typography.replace(r"{\olsa_typography_original_deduce $#1$}", r"{\olsa_typography_original_deduce #1}", 1)))
    expect_failure(lambda: check_proof_transports(sources, typography.replace(r"\cs_set_eq:NN \Axiom \olsa_typography_original_axiom", "", 1)))
    expect_failure(lambda: check_proof_transports(sources, typography.replace(r"\cs_set_eq:NN \Deduce \olsa_typography_original_deduce", "", 1)))
    expect_failure(lambda: check_proof_transports(sources, typography.replace(r"\cs_set_eq:NN \Deduce \OLSATypographyActiveDeduce", "", 1)))
    expect_failure(lambda: check_proof_transports(sources, typography.replace(r"\cs_set_eq:NN \Axiom \OLSATypographyActiveAxiom", r"\cs_set_eq:NN \Axiom \olsa_typography_original_axiom", 1)))
    expect_failure(lambda: registry(typography + "\n" + r"\OLSASetDisplayCount{unknown-rule}{1}"))
    expect_failure(lambda: registry(typography + "\n" + r"\OLSASetDisplayCount{relation-formula}{4}"))

    runtime = (STANDALONE / "runtime.tex").read_text(encoding="utf-8")
    body = (STANDALONE / "body.tex").read_text(encoding="utf-8")
    variants = (STANDALONE / "variants.tex").read_text(encoding="utf-8")
    assert r"\NewCommandCopy \olsa_original_cref \cref" in runtime
    assert r"\OLSADeclareAfter {m +m}" in runtime
    assert r"\ensuremath{\leftarrow}" in runtime
    assert r"محل~متن~در~همین~خوانشگر" in runtime
    assert r"\cs_if_exist:NT \OLSAApplyTypography {\OLSAApplyTypography}" in runtime
    assert r"\cs_if_exist:NT \OLSATypographyStart {\OLSATypographyStart}" in runtime
    assert r"\cs_if_exist:NT \OLSATypographyVerify {\OLSATypographyVerify}" in runtime
    assert body.index(r"\input{standalone/context.tex}") < body.index(r"\input{standalone/typography.tex}") < body.index(r"\OLSAStart")
    assert r"\c_math_toggle_token #1\c_math_toggle_token" in typography
    assert r"{\char_set_catcode_math_toggle:n {36}}" in typography
    assert r"\protected\long\gdef$#1${\OLSAProcessInlineMath{#1}}" in typography
    assert r"\let\c@section\c@OLSAVariantSection" in variants
    assert r"\renewcommand{\thesection}{A.\arabic{OLSAVariantSection}}" in variants
    assert r"\renewcommand{\theHsection}{olsa-variant.\arabic{OLSAVariantSection}}" in variants
    assert r"\markboth{پیوست: ساختارهای جایگزین منبع}{پیوست: ساختارهای جایگزین منبع}" in variants
    assert r"\setcounter{chapter}" not in variants and r"\appendix" not in uncomment(variants)
    assert variants.rstrip().endswith("\\clearpage\n\\endgroup")

    valid_trace = "source_id|rule|occurrence\n" + "\n".join(
        "|".join(event) for event in expected_trace()) + "\n"
    check_trace(valid_trace)
    expect_failure(lambda: check_trace(valid_trace.rsplit("\n", 2)[0] + "\n"))
    expect_failure(lambda: check_trace(valid_trace + valid_trace.splitlines()[1] + "\n"))
    expect_failure(lambda: check_trace(valid_trace.replace("|1", "|2", 1)))
    expect_failure(lambda: check_trace(valid_trace.replace("OLP-0668", "OLP-0001", 1)))
    trace = {}
    if args.trace_file:
        actual = check_trace(args.trace_file.read_text(encoding="utf-8"))
        trace["sidecar"] = {"path": str(args.trace_file), "sha256": sha(args.trace_file.read_bytes()), "status": "PASS_EXPECTED_EXACT_DISPLAY_EVENTS", "events": len(actual)}
    if args.trace_log:
        log = args.trace_log.read_text(encoding="utf-8", errors="replace")
        hits = re.findall(r"^OL-STANDALONE-TYPOGRAPHY\|(OLP-\d{4})\|([^|\n]+)\|(\d+)$", log, re.M)
        assert sorted(hits) == sorted(expected_trace()), hits
        assert "OL-STANDALONE-TYPOGRAPHY-COVERAGE|18|18" in log
        trace["log"] = {"path": str(args.trace_log), "sha256": sha(args.trace_log.read_bytes()), "status": "PASS_EXPECTED_EXACT_DISPLAY_EVENTS"}

    files = [STANDALONE / n for n in ("body.tex", "runtime.tex", "typography.tex", "variants.tex", "tests/check_typography.py")]
    evidence = {
        "schema": "farsi-standalone-additive-typography/3",
        "status": "PASS_STATIC_BASELINE_AND_FORMULA_PRESERVATION_NOT_TEX_OR_VISUAL_VALIDATED",
        "baseline_files_rehashed": len(baseline),
        "staging_manifest_sha256": STAGING_SHA,
        "display_rules": sorted(results, key=lambda r: r["rule"]),
        "source_units": len(sources),
        "expected_display_rules": len(rules),
        "expected_display_events": EXPECTED_EVENTS,
        "expected_trace": expected_trace(),
        "previous_six_formula_rules_preserved": True,
        "previous_evidence_sha256": PREVIOUS_EVIDENCE_SHA,
        "proof_dollar_transport_static_checks": proof_transports,
        "appendix": {"section_counter": "OLSAVariantSection", "visible_numbering": "A.1 through A.4", "hyperref_prefix": "olsa-variant", "explicit_running_marks": True, "canonical_chapter_counter_changed": False},
        "negative_tests": ["numerically_changed_formula_rejected", "excess_formula_occurrence_rejected", "wrong_source_id_passthrough", "unexpected_terminal_punctuation_rejected", "nested_inline_math_passthrough", "trace_missing_duplicate_count_and_source_mutations_rejected", "broken_proof_transport_delimiters_resets_and_all_target_selections_rejected", "unknown_or_redeclared_occurrence_count_rejected", "page_729_characteristic_formula_and_punctuation_mutations_rejected", "three_new_overflow_formulas_exactly_once", "olp_0701_atomic_formula_exactly_twice"],
        "runtime_trace": trace or None,
        "files": [{"path": str(p.relative_to(ROOT)).replace("\\", "/"), "bytes": p.stat().st_size, "sha256": sha(p.read_bytes())} for p in files],
        "unresolved": ["Actual TeX macro expansion, dollar-interface adapters and new page geometry require an owner-managed build and full-page render checks.", "Literal shorthand leakage and generated English reference conjunctions are not fixed by formula reflow; separate owner lanes investigate them.", "No final visual PASS; root owns bibliography, build runner and publication."],
    }
    if args.write_evidence:
        output = ROOT / "evidence/STANDALONE_TYPOGRAPHY_REFLOW_02_QA.json"
        output.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(evidence, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
