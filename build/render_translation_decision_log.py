"""Validate and render the partial standard-Farsi decision ledger."""
from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "evidence/TRANSLATION_DECISION_LOG.json"
TARGET = ROOT / "evidence/TRANSLATION_DECISION_LOG.md"
QA = ROOT / "evidence/TRANSLATION_DECISION_LOG_QA.json"
REQUIRED = {
    "id", "status", "retrospective_label", "source_locations",
    "target_locations", "wording_or_sense", "authorities_checked",
    "authorities_not_checked", "rationale", "alternatives_considered",
    "uncertainty", "optional_expert_question",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


data = json.loads(SOURCE.read_text(encoding="utf-8"))
assert data["schema"] == "openlogic-translation-decision-log/1"
assert data["status"] == "PARTIAL_LIVE_LEDGER"
assert "not a sentence-by-sentence review of all 722 units" in data["coverage"]["not_claimed"][0]
entries = data["entries"]
assert entries and len({entry["id"] for entry in entries}) == len(entries)
assert [entry["id"] for entry in entries] == [f"FAD-{i:03d}" for i in range(1, len(entries) + 1)]
for entry in entries:
    assert set(entry) == REQUIRED, (entry["id"], set(entry) ^ REQUIRED)
    for key in ("source_locations", "target_locations", "authorities_checked", "authorities_not_checked", "alternatives_considered"):
        assert isinstance(entry[key], list) and entry[key], (entry["id"], key)
    for key in ("status", "retrospective_label", "wording_or_sense", "rationale", "uncertainty"):
        assert isinstance(entry[key], str) and entry[key].strip(), (entry["id"], key)

source_text = SOURCE.read_text(encoding="utf-8")
assert all(f"OLFUN-00{i}" in source_text for i in range(1, 6))
assert any(entry["status"] == "provisional_not_installed" for entry in entries)
assert any("not evidence of historical consultation" in entry["retrospective_label"] for entry in entries)

source_hash = sha(SOURCE)
lines = [
    "# Standard-Farsi translation and difficult-choice log",
    "",
    f"Machine-readable authority: `TRANSLATION_DECISION_LOG.json` (SHA-256 `{source_hash}`).",
    "",
    "This is a partial live ledger for substantive decisions made during the standalone-reader task. "
    "It is not a sentence-by-sentence review of all 722 units, does not invent historical expert review, "
    "and does not promote provisional technical experiments to accepted fixes. It is packaged beside the "
    "translation in the next fully validated, nonduplicative release.",
    "",
    "English source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`.  ",
    "Inherited Farsi revision: `95fed67628b4e9113ca7890441082b470e0a1b29`.",
    "",
]
for entry in entries:
    lines.extend([
        f"## {entry['id']} — {entry['status']}",
        "",
        f"**Decision / sense.** {entry['wording_or_sense']}",
        "",
        f"**Rationale.** {entry['rationale']}",
        "",
        "**Source locations.** " + "; ".join(f"`{item}`" for item in entry["source_locations"]),
        "",
        "**Target locations.** " + "; ".join(f"`{item}`" for item in entry["target_locations"]),
        "",
        "**Authorities actually checked.** " + "; ".join(entry["authorities_checked"]),
        "",
        "**Not checked / not claimed.** " + "; ".join(entry["authorities_not_checked"]),
        "",
        "**Alternatives considered.** " + "; ".join(entry["alternatives_considered"]),
        "",
        f"**Uncertainty.** {entry['uncertainty']}",
        "",
        f"**Provenance label.** {entry['retrospective_label']}",
        "",
        "**Optional precise expert question.** " + (
            entry["optional_expert_question"] or "None; the current decision rests on deterministic source or mathematical evidence."
        ),
        "",
    ])
TARGET.write_text("\n".join(lines), encoding="utf-8")
receipt = {
    "schema": "openlogic-translation-decision-log-qa/1",
    "status": "PASS_PARTIAL_TRACEABLE_LEDGER",
    "edition": data["edition"],
    "entries": len(entries),
    "accepted_or_implemented_entries": sum(
        entry["status"].startswith(("accepted", "implemented")) for entry in entries
    ),
    "provisional_entries": sum(entry["status"] == "provisional_not_installed" for entry in entries),
    "coverage_is_partial": True,
    "publication_state": "LOCAL_READY_TO_PACKAGE_WITH_FINAL_READER_NOT_YET_PUBLISHED",
    "files": [
        {"path": path.relative_to(ROOT).as_posix(), "bytes": path.stat().st_size, "sha256": sha(path)}
        for path in (SOURCE, TARGET, Path(__file__))
    ],
    "limits": data["coverage"]["not_claimed"],
}
QA.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False, indent=2))
