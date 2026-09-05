"""Fail-closed primitives shared by bounded standalone diagnostic validators.

This module never launches TeX.  It validates a completed, guarded diagnostic
receipt and the bytes which that receipt names.  Probe-specific modules remain
responsible for semantic sidecars, PDF text, and source-specific invariants.
"""
from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import math
import os
import re
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
RUNS = (ROOT / "tmp/pdfs/standalone").resolve()
EVIDENCE = (ROOT / "evidence").resolve()
SOURCE = (ROOT / "source").resolve()
LOCALE = (SOURCE / "locale/fa-IR").resolve()
ENTRYPOINT = (ROOT / "build/BUILD_STANDALONE.ps1").resolve()
HELPER = (ROOT / "build/StandaloneTeXProcessGuard.cs").resolve()
RECEIPT_SCHEMA = "interlanguage-standalone-tex-build-v1"
MUTEX_NAME = r"Global\InterlanguageTeXSlotV1"
MEMORY_LIMIT = 2_147_483_648
PYMUPDF_VERSION = "1.27.2.3"


class ValidationError(RuntimeError):
    """A deterministic diagnostic acceptance condition was not met."""


def require(condition: object, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@dataclass(frozen=True)
class FileSnapshot:
    path: Path
    data: bytes
    size: int
    sha256: str


_SNAPSHOT_CACHE: dict[str, FileSnapshot] = {}


def clear_snapshot_cache() -> None:
    _SNAPSHOT_CACHE.clear()


def file_snapshot(path: Path) -> FileSnapshot:
    """Read a stable regular-file snapshot once and memoize its bound identity."""

    resolved = path.resolve()
    key = os.path.normcase(str(resolved))
    cached = _SNAPSHOT_CACHE.get(key)
    if cached is not None:
        return cached
    require(resolved.is_file(), f"file missing: {resolved}")
    with resolved.open("rb") as handle:
        before = os.fstat(handle.fileno())
        data = handle.read()
        after = os.fstat(handle.fileno())
    stable_fields = ("st_dev", "st_ino", "st_size", "st_mtime_ns", "st_ctime_ns")
    require(
        all(getattr(before, field, None) == getattr(after, field, None) for field in stable_fields),
        f"file changed while being read: {resolved}",
    )
    require(len(data) == after.st_size, f"short or inconsistent file read: {resolved}")
    snapshot = FileSnapshot(resolved, data, len(data), sha256_bytes(data))
    _SNAPSHOT_CACHE[key] = snapshot
    return snapshot


def sha256_file(path: Path) -> str:
    return file_snapshot(path).sha256


def file_size(path: Path) -> int:
    return file_snapshot(path).size


def read_file_bytes(path: Path) -> bytes:
    return file_snapshot(path).data


def read_file_text(path: Path, *, encoding: str = "utf-8") -> str:
    try:
        return read_file_bytes(path).decode(encoding)
    except UnicodeDecodeError as exc:
        raise ValidationError(f"file is not strict {encoding}: {path}: {exc}") from exc


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValidationError(f"duplicate JSON key rejected: {key!r}")
        result[key] = value
    return result


def load_json(path: Path) -> object:
    require(path.is_file(), f"JSON input missing: {path}")
    try:
        return json.loads(
            read_file_text(path, encoding="utf-8-sig"),
            object_pairs_hook=_unique_object,
            parse_constant=lambda value: (_ for _ in ()).throw(
                ValidationError(f"non-finite JSON number rejected: {value}")
            ),
        )
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f"invalid UTF-8 JSON: {path}: {exc}") from exc


def as_mapping(value: object, label: str) -> Mapping[str, object]:
    require(isinstance(value, Mapping), f"{label} must be a JSON object")
    return value


def as_list(value: object, label: str) -> list[object]:
    require(isinstance(value, list), f"{label} must be a JSON array")
    return value


def require_exact_keys(
    value: Mapping[str, object], expected: Iterable[str], label: str,
) -> None:
    expected_set = set(expected)
    actual_set = set(value)
    require(
        actual_set == expected_set,
        f"{label} fields changed: missing={sorted(expected_set - actual_set)!r}; "
        f"unexpected={sorted(actual_set - expected_set)!r}",
    )


def is_json_integer(value: object) -> bool:
    """JSON booleans are Python ints, but never valid receipt integers."""

    return isinstance(value, int) and not isinstance(value, bool)


def same_path(left: Path | str, right: Path | str) -> bool:
    return os.path.normcase(str(Path(left).resolve())) == os.path.normcase(
        str(Path(right).resolve())
    )


def under(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def relative_repo_path(path: Path) -> str:
    resolved = path.resolve()
    require(under(resolved, ROOT), f"path escapes repository: {path}")
    return resolved.relative_to(ROOT.resolve()).as_posix()


def validate_receipt_path(path: Path) -> Path:
    resolved = path.resolve()
    require(resolved.name == "BUILD_RECEIPT.json", "receipt basename must be BUILD_RECEIPT.json")
    require(under(resolved, RUNS), "receipt must be beneath tmp/pdfs/standalone")
    require(resolved.parent.parent == RUNS, "receipt must be directly inside one run directory")
    require(resolved.is_file(), f"receipt missing: {resolved}")
    return resolved


def validate_output_path(path: Path) -> Path:
    resolved = path.resolve()
    require(resolved.suffix.lower() == ".json", "evidence output must have a .json suffix")
    require(under(resolved, EVIDENCE), "evidence output must be an explicit path beneath evidence/")
    require(resolved.parent.exists(), "evidence output parent must already exist")
    require(not path.is_symlink(), "evidence output may not be a symlink")
    require(not resolved.exists() or resolved.is_file(), "evidence output must be a regular file")
    relative_parent = resolved.parent.relative_to(EVIDENCE)
    cursor = EVIDENCE
    for part in relative_parent.parts:
        cursor /= part
        require(not cursor.is_symlink(), "evidence output parent chain may not contain a symlink")
    return resolved


def write_json(path: Path, value: Mapping[str, object]) -> None:
    output = validate_output_path(path)
    output.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def _iso_utc(value: object, label: str) -> datetime:
    require(isinstance(value, str) and value, f"{label} must be a nonempty timestamp")
    try:
        stamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValidationError(f"{label} is not ISO-8601: {value!r}") from exc
    require(stamp.tzinfo is not None, f"{label} must be timezone-aware")
    require(stamp.utcoffset() == timezone.utc.utcoffset(stamp), f"{label} must be UTC")
    return stamp


def is_finite_number(value: object) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


DIAGNOSTIC_PATTERNS: dict[str, re.Pattern[str]] = {
    "fatal": re.compile(
        r"^!|Emergency stop|Fatal error|Missing character:|TeX capacity exceeded|Runaway argument",
        re.IGNORECASE | re.MULTILINE,
    ),
    "duplicate": re.compile(
        r"multiply[- ]defined|multiply defined|destination with the same identifier|"
        r"duplicate.*(?:destination|label)|duplicate ignored",
        re.IGNORECASE | re.MULTILINE,
    ),
    "unresolved": re.compile(
        r"There were undefined (?:references|citations)|"
        r"(?:Citation|Reference)[^\r\n]*(?:\r?\n[^\r\n]*)?undefined|"
        r"I couldn.t open database file|I didn.t find a database entry",
        re.IGNORECASE | re.MULTILINE,
    ),
    "bibliography_warning": re.compile(
        r"^Warning--[^\r\n]*", re.IGNORECASE | re.MULTILINE
    ),
    "rerun": re.compile(
        r"Label\(s\) may have changed|Rerun to get|"
        r"rerunfilecheck[^\r\n]*(?:\r?\n[^\r\n]*)?has changed|"
        r"Please \(re\)run (?:LaTeX|BibTeX|Biber)",
        re.IGNORECASE | re.MULTILINE,
    ),
}


def parse_log_diagnostics(text: str) -> dict[str, list[dict[str, object]]]:
    result: dict[str, list[dict[str, object]]] = {}
    for kind, pattern in DIAGNOSTIC_PATTERNS.items():
        result[kind] = [
            {"line": text.count("\n", 0, match.start()) + 1, "text": match.group(0)}
            for match in pattern.finditer(text)
        ]
    return result


def validate_diagnostics(
    reported: object, actual: Mapping[str, list[dict[str, object]]], *,
    allow_reference_warnings: bool,
    allow_latex_rerun_warnings: bool,
) -> dict[str, int]:
    diagnostic = as_mapping(reported, "pass diagnostics")
    require(set(diagnostic) == set(DIAGNOSTIC_PATTERNS), "diagnostic category set changed")
    require(dict(diagnostic) == dict(actual), "receipt diagnostics do not match the preserved log")
    for category in ("fatal", "duplicate", "bibliography_warning"):
        require(not actual[category], f"{category} diagnostics are not permitted")
    if allow_reference_warnings:
        for item in actual["unresolved"]:
            message = str(item["text"])
            lowered = message.casefold()
            require("citation" not in lowered, "undefined citations are not permitted")
            require("database" not in lowered, "missing bibliography databases are not permitted")
            require(
                "reference" in lowered or "undefined references" in lowered,
                f"unexpected unresolved diagnostic: {message!r}",
            )
    else:
        require(not actual["unresolved"], "unresolved diagnostics are not permitted")
    if allow_latex_rerun_warnings:
        for item in actual["rerun"]:
            message = str(item["text"])
            lowered = message.casefold()
            require("bibtex" not in lowered and "biber" not in lowered, "bibliography rerun request is not permitted")
            require(
                message.startswith("Label(s) may have changed")
                or message.startswith("Rerun to get")
                or message.casefold().startswith("rerunfilecheck")
                or message.startswith("Please (re)run LaTeX"),
                f"unexpected rerun diagnostic: {message!r}",
            )
    else:
        require(not actual["rerun"], "rerun diagnostics are not permitted")
    return {key: len(value) for key, value in actual.items()}


def _validate_inventory(receipt: Mapping[str, object], run_root: Path) -> dict[str, object]:
    inventory_record = as_mapping(receipt.get("source_inventory"), "source_inventory")
    require_exact_keys(
        inventory_record, {"path", "files", "signature", "sha256"}, "source_inventory",
    )
    inventory_path = Path(str(inventory_record.get("path", ""))).resolve()
    expected_path = (run_root / "SOURCE_INPUTS_BEFORE.json").resolve()
    require(same_path(inventory_path, expected_path), "source inventory path is outside this run")
    require(inventory_path.is_file(), "source inventory is missing")
    inventory_hash = sha256_file(inventory_path)
    require(inventory_hash == str(inventory_record.get("sha256", "")).lower(), "source inventory hash mismatch")
    rows = as_list(load_json(inventory_path), "source inventory")
    require(is_json_integer(inventory_record.get("files")), "source inventory file count must be an integer")
    require(len(rows) == inventory_record.get("files"), "source inventory count mismatch")
    normalized: list[tuple[str, int, str]] = []
    for index, raw in enumerate(rows):
        row = as_mapping(raw, f"source inventory row {index}")
        require(set(row) == {"path", "bytes", "sha256"}, "source inventory row fields changed")
        path = row["path"]
        byte_count = row["bytes"]
        digest = row["sha256"]
        require(isinstance(path, str) and path and "\\" not in path, "invalid inventory path")
        require(
            not Path(path).is_absolute()
            and not path.startswith("/")
            and ":" not in path
            and ".." not in Path(path).parts,
            "unsafe inventory path",
        )
        require(is_json_integer(byte_count) and byte_count >= 0, "invalid inventory byte count")
        require(isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest), "invalid inventory hash")
        normalized.append((path, byte_count, digest))
    # PowerShell Sort-Object is case-insensitive for these path strings.  Match
    # that receipt-producing contract rather than Python's ordinal case order.
    require(
        [row[0] for row in normalized]
        == sorted((row[0] for row in normalized), key=str.casefold),
        "source inventory is not sorted",
    )
    require(
        len({row[0].casefold() for row in normalized}) == len(normalized),
        "duplicate source inventory path under Windows case-folding",
    )
    signature_text = "\n".join(f"{path}\t{size}\t{digest}" for path, size, digest in normalized)
    signature = sha256_bytes(signature_text.encode("utf-8"))
    require(signature == inventory_record.get("signature"), "source inventory signature mismatch")
    return {
        "path": relative_repo_path(inventory_path),
        "sha256": inventory_hash,
        "files": len(rows),
        "signature": signature,
        "rows": normalized,
    }


def _current_identity(path_value: object, expected_suffix: str, label: str) -> dict[str, str]:
    require(isinstance(path_value, str) and path_value, f"{label} path is missing")
    path = Path(path_value).resolve()
    require(path.name.casefold() == expected_suffix.casefold(), f"unexpected {label} executable")
    require(path.is_file(), f"{label} executable is missing")
    return {"name": path.name, "sha256": sha256_file(path)}


def _validate_output_inventory(
    raw_inventory: object, primary: Path,
) -> dict[str, tuple[int, str]]:
    rows = as_list(raw_inventory, "build output_inventory")
    require(rows, "build output_inventory is empty")
    normalized: list[tuple[str, int, str]] = []
    for index, raw in enumerate(rows):
        row = as_mapping(raw, f"build output_inventory row {index}")
        require_exact_keys(row, {"path", "bytes", "sha256"}, f"build output_inventory row {index}")
        name = row.get("path")
        size = row.get("bytes")
        digest = row.get("sha256")
        require(
            isinstance(name, str)
            and name
            and name == Path(name).name
            and not Path(name).is_absolute()
            and "/" not in name
            and "\\" not in name
            and ":" not in name,
            "unsafe build output inventory path",
        )
        require(is_json_integer(size) and size >= 0, "invalid build output byte count")
        require(
            isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest),
            "invalid build output hash",
        )
        normalized.append((name, size, digest))
    names = [row[0] for row in normalized]
    require(names == sorted(names, key=str.casefold), "build output inventory is not sorted")
    require(len({name.casefold() for name in names}) == len(names), "duplicate build output inventory path")
    current_names = sorted(
        (entry.name for entry in primary.iterdir() if entry.is_file()), key=str.casefold,
    )
    require(names == current_names, "current build output file set differs from receipt inventory")
    result: dict[str, tuple[int, str]] = {}
    for name, size, digest in normalized:
        path = primary / name
        require(not path.is_symlink(), f"build output may not be a symlink: {name}")
        snapshot = file_snapshot(path)
        require(snapshot.size == size, f"build output byte count changed: {name}")
        require(snapshot.sha256 == digest, f"build output hash changed: {name}")
        result[name] = (size, digest)
    return result


def validate_diagnostic_receipt(
    receipt_path: Path,
    *,
    job: str,
    driver: Path,
    driver_sha256: str,
    allow_reference_warnings: bool,
    allow_latex_rerun_warnings: bool,
    require_layout_markers: bool = True,
) -> dict[str, object]:
    """Validate one completed Diagnostic-mode run and return sanitized facts."""

    receipt_path = validate_receipt_path(receipt_path)
    receipt = as_mapping(load_json(receipt_path), "build receipt")
    run_root = receipt_path.parent.resolve()
    expected_driver = driver.resolve()
    expected_driver_hash = driver_sha256.lower()

    require_exact_keys(
        receipt,
        {
            "schema", "mode", "started_utc", "status", "accepted_build",
            "publication_or_visual_qa_passed", "run_root", "driver",
            "driver_sha256", "helper_sha256", "entrypoint_sha256",
            "executable_identities", "limits", "deterministic_environment",
            "mutex", "events", "builds", "observed_peak_job_commit_bytes",
            "source_inventory", "finished_utc", "elapsed_guarded_seconds",
        },
        "successful Diagnostic receipt",
    )
    require(receipt.get("schema") == RECEIPT_SCHEMA, "unexpected build receipt schema")
    require(receipt.get("mode") == "Diagnostic", "receipt is not Diagnostic mode")
    require(receipt.get("status") == "DIAGNOSTIC_ONLY_NOT_ACCEPTED", "diagnostic run did not finish successfully")
    require(receipt.get("accepted_build") is False, "diagnostic run must never be accepted as a full build")
    require(receipt.get("publication_or_visual_qa_passed") is False, "diagnostic run cannot claim publication or visual QA")
    require(not receipt.get("failure"), "receipt records a failure")
    require(same_path(str(receipt.get("run_root", "")), run_root), "receipt run_root mismatch")
    require(same_path(str(receipt.get("driver", "")), expected_driver), "wrong diagnostic driver")
    require(expected_driver.is_file(), "diagnostic fixture is missing")
    require(sha256_file(expected_driver) == expected_driver_hash, "current diagnostic fixture hash mismatch")
    require(str(receipt.get("driver_sha256", "")).lower() == expected_driver_hash, "receipt driver hash mismatch")

    started = _iso_utc(receipt.get("started_utc"), "started_utc")
    finished = _iso_utc(receipt.get("finished_utc"), "finished_utc")
    require(finished >= started, "finished_utc precedes started_utc")
    elapsed = receipt.get("elapsed_guarded_seconds")
    require(is_finite_number(elapsed) and elapsed >= 0, "invalid guarded elapsed time")

    mutex = as_mapping(receipt.get("mutex"), "mutex")
    require_exact_keys(
        mutex,
        {"name", "acquired", "abandoned_recovery", "released_after_confirmed_tree_exit"},
        "mutex",
    )
    require(mutex.get("name") == MUTEX_NAME, "wrong machine-wide TeX mutex")
    require(mutex.get("acquired") is True, "TeX mutex was not acquired")
    require(isinstance(mutex.get("abandoned_recovery"), bool), "abandoned_recovery must be boolean")
    require(mutex.get("released_after_confirmed_tree_exit") is True, "mutex release lacks confirmed tree exit")

    limits = as_mapping(receipt.get("limits"), "limits")
    require_exact_keys(
        limits,
        {
            "mutex_acquisition_seconds", "per_worker_seconds",
            "complete_session_seconds", "maximum_latex_passes_per_build",
            "maximum_bibtex_passes_per_build", "job_commit_memory_bytes",
            "active_processes_in_owned_tree", "cleanup_deadline_seconds",
            "unconfirmed_exit_policy", "memory_semantics",
        },
        "limits",
    )
    require(limits.get("job_commit_memory_bytes") == MEMORY_LIMIT, "wrong guarded memory limit")
    process_limit = limits.get("active_processes_in_owned_tree")
    require(is_json_integer(process_limit) and 1 <= process_limit <= 16, "unsafe owned-tree process limit")
    require(limits.get("cleanup_deadline_seconds") == 60, "unexpected cleanup deadline")
    require(
        limits.get("unconfirmed_exit_policy")
        == "Retain host/job/mutex and observe same handles with 5-to-30-second backoff; never timeout-release",
        "unconfirmed-exit policy changed",
    )
    require(
        limits.get("memory_semantics")
        == "Windows Job Object aggregate committed memory; NOT working set or GPU memory",
        "guarded-memory semantics changed",
    )
    latex_pass_limit = limits.get("maximum_latex_passes_per_build")
    bibtex_pass_limit = limits.get("maximum_bibtex_passes_per_build")
    require(is_json_integer(latex_pass_limit) and latex_pass_limit in range(3, 11), "invalid configured LaTeX pass cap")
    require(is_json_integer(bibtex_pass_limit) and bibtex_pass_limit in range(1, 4), "invalid configured BibTeX pass cap")
    for key in ("mutex_acquisition_seconds", "per_worker_seconds", "complete_session_seconds"):
        require(is_json_integer(limits.get(key)) and limits[key] > 0, f"invalid {key}")
    require(limits["mutex_acquisition_seconds"] <= 300, "mutex acquisition limit exceeds producer schema")
    require(limits["per_worker_seconds"] <= 7200, "worker limit exceeds producer schema")
    require(limits["complete_session_seconds"] <= 28800, "session limit exceeds producer schema")

    environment = as_mapping(receipt.get("deterministic_environment"), "deterministic_environment")
    expected_environment = {
        "SOURCE_DATE_EPOCH": "1783874174",
        "FORCE_SOURCE_DATE": "1",
        "TZ": "UTC",
        "max_print_line": "1000",
        "openin_any": "a",
        "openout_any": "p",
        "shell_escape": "0",
    }
    require(dict(environment) == expected_environment, "deterministic TeX environment changed")

    require(ENTRYPOINT.is_file() and HELPER.is_file(), "guarded build infrastructure missing")
    require(str(receipt.get("entrypoint_sha256", "")).lower() == sha256_file(ENTRYPOINT), "entrypoint identity mismatch")
    require(str(receipt.get("helper_sha256", "")).lower() == sha256_file(HELPER), "guard helper identity mismatch")

    executables = as_list(receipt.get("executable_identities"), "executable_identities")
    require(len(executables) == 1, "Diagnostic mode must name only LuaLaTeX")
    executable_record = as_mapping(executables[0], "LuaLaTeX identity")
    require_exact_keys(executable_record, {"path", "sha256"}, "LuaLaTeX identity")
    executable = _current_identity(executable_record.get("path"), "lualatex.exe", "LuaLaTeX")
    require(executable["sha256"] == str(executable_record.get("sha256", "")).lower(), "LuaLaTeX hash mismatch")

    inventory = _validate_inventory(receipt, run_root)
    fixture_row = f"locale/fa-IR/{job}.tex"
    matching_fixture_rows = [row for row in inventory["rows"] if row[0] == fixture_row]
    require(matching_fixture_rows == [(fixture_row, file_size(expected_driver), expected_driver_hash)], "fixture missing or altered in source inventory")

    builds = as_list(receipt.get("builds"), "builds")
    require(len(builds) == 1, "Diagnostic mode must contain exactly one build")
    build = as_mapping(builds[0], "primary build")
    require_exact_keys(
        build,
        {
            "name", "directory", "accepted", "effective_deterministic_environment",
            "passes", "pdf", "fls", "output_inventory",
        },
        "primary build",
    )
    require(build.get("name") == "primary", "diagnostic build must be named primary")
    primary = (run_root / "primary").resolve()
    require(same_path(str(build.get("directory", "")), primary), "primary output directory mismatch")
    require(build.get("accepted") is False, "one-pass diagnostic build cannot claim convergence")
    effective_environment = as_mapping(
        build.get("effective_deterministic_environment"),
        "effective_deterministic_environment",
    )
    expected_effective_environment = {
        **expected_environment,
        "TEXINPUTS": f"{primary};{LOCALE};",
        "BIBINPUTS": f"{LOCALE};{SOURCE / 'bib'};",
        "BSTINPUTS": f"{LOCALE};{SOURCE / 'bib'};",
        "TEXMFOUTPUT": str(primary),
        "TEXMF_OUTPUT_DIRECTORY": str(primary),
    }
    require(
        dict(effective_environment) == expected_effective_environment,
        "effective deterministic worker environment changed or is incomplete",
    )

    passes = as_list(build.get("passes"), "primary passes")
    require(len(passes) == 1, "Diagnostic mode must have exactly one LuaLaTeX pass")
    pass_record = as_mapping(passes[0], "diagnostic pass")
    require_exact_keys(pass_record, {"pass", "log", "log_sha256", "diagnostics"}, "diagnostic pass")
    require(is_json_integer(pass_record.get("pass")) and pass_record.get("pass") == 1, "diagnostic pass number must be integer one")
    snapshot = (primary / "primary-latex-01.tex.log").resolve()
    canonical_log = (primary / f"{job}.log").resolve()
    require(same_path(str(pass_record.get("log", "")), snapshot), "preserved log path mismatch")
    require(snapshot.is_file() and canonical_log.is_file(), "diagnostic log or preserved snapshot missing")
    snapshot_bytes = read_file_bytes(snapshot)
    require(snapshot_bytes == read_file_bytes(canonical_log), "canonical and preserved TeX logs differ")
    snapshot_hash = sha256_bytes(snapshot_bytes)
    require(snapshot_hash == str(pass_record.get("log_sha256", "")).lower(), "preserved log hash mismatch")
    try:
        log_text = snapshot_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValidationError("preserved TeX log is not strict UTF-8") from exc
    actual_diagnostics = parse_log_diagnostics(log_text)
    diagnostic_counts = validate_diagnostics(
        pass_record.get("diagnostics"), actual_diagnostics,
        allow_reference_warnings=allow_reference_warnings,
        allow_latex_rerun_warnings=allow_latex_rerun_warnings,
    )
    expected_layout_markers = [
        "OL-R2-TEXTWIDTH=468.0pt",
        "OL-R2-TEXTHEIGHT=650.0pt",
        "OL-R2-FONTSIZE=14.4pt",
        "OL-R2-BASELINESKIP=18.37505pt",
        "OL-R2-ODDSIDEMARGIN=0.8773pt",
        "OL-R2-EVENSIDEMARGIN=0.8773pt",
        "OL-R2-UPPERMARGIN=72.485pt",
    ]
    layout_lines = [line for line in log_text.splitlines() if line.startswith("OL-R2-")]
    if require_layout_markers:
        require(
            layout_lines == expected_layout_markers,
            f"layout marker lines are missing, malformed, duplicated, extra, or reordered: {layout_lines!r}",
        )
    else:
        require(
            not layout_lines,
            f"isolated diagnostic unexpectedly emitted full-reader layout markers: {layout_lines!r}",
        )
        expected_layout_markers = []

    pdf = (primary / f"{job}.pdf").resolve()
    pdf_record = as_mapping(build.get("pdf"), "PDF record")
    require_exact_keys(pdf_record, {"path", "bytes", "sha256"}, "PDF record")
    require(same_path(str(pdf_record.get("path", "")), pdf), "PDF path mismatch")
    pdf_snapshot = file_snapshot(pdf)
    require(pdf_snapshot.size > 1024, "diagnostic PDF missing or too small")
    require(pdf_snapshot.data[:5] == b"%PDF-", "diagnostic output lacks a PDF header")
    pdf_hash = pdf_snapshot.sha256
    require(is_json_integer(pdf_record.get("bytes")), "PDF byte count must be an integer")
    require(pdf_record.get("bytes") == pdf_snapshot.size, "PDF byte count mismatch")
    require(str(pdf_record.get("sha256", "")).lower() == pdf_hash, "PDF hash mismatch")

    fls = (primary / f"{job}.fls").resolve()
    fls_record = as_mapping(build.get("fls"), "recorder record")
    require_exact_keys(fls_record, {"path", "sha256"}, "recorder record")
    require(same_path(str(fls_record.get("path", "")), fls), "recorder path mismatch")
    require(fls.is_file(), "recorder output missing")
    fls_hash = file_snapshot(fls).sha256
    require(str(fls_record.get("sha256", "")).lower() == fls_hash, "recorder hash mismatch")
    output_inventory = _validate_output_inventory(build.get("output_inventory"), primary)
    require(
        output_inventory.get(pdf.name) == (pdf_snapshot.size, pdf_hash),
        "PDF record and output inventory disagree",
    )
    require(
        output_inventory.get(fls.name) == (file_size(fls), fls_hash),
        "recorder record and output inventory disagree",
    )

    events = as_list(receipt.get("events"), "events")
    expected_kinds = [
        "mutex_acquired",
        "worker_start",
        "worker_tree_exit",
        "immediate_log_check",
        "source_and_infrastructure_unchanged",
    ]
    kinds = [as_mapping(event, f"event {index}").get("kind") for index, event in enumerate(events)]
    require(kinds == expected_kinds, f"unexpected diagnostic event sequence: {kinds!r}")
    event_times: list[datetime] = []
    for index, raw in enumerate(events):
        event = as_mapping(raw, f"event {index}")
        require_exact_keys(event, {"utc", "kind", "details"}, f"event {index}")
        event_times.append(_iso_utc(event.get("utc"), f"event {index} utc"))
        require(isinstance(event.get("details"), Mapping), f"event {index} details missing")
    require(event_times == sorted(event_times), "diagnostic events are not chronological")
    require(started <= event_times[0] <= event_times[-1] <= finished, "event timestamps escape receipt interval")

    mutex_event = as_mapping(as_mapping(events[0], "mutex event").get("details"), "mutex event details")
    require_exact_keys(mutex_event, {"abandoned_recovery"}, "mutex event details")
    require(mutex_event.get("abandoned_recovery") is mutex.get("abandoned_recovery"), "mutex recovery event mismatch")
    label = "primary-latex-01"
    start_event = as_mapping(as_mapping(events[1], "worker start").get("details"), "worker start details")
    exit_event = as_mapping(as_mapping(events[2], "worker exit").get("details"), "worker exit details")
    immediate_event = as_mapping(as_mapping(events[3], "immediate log check").get("details"), "log event details")
    source_event = as_mapping(as_mapping(events[4], "source event").get("details"), "source event details")
    require_exact_keys(start_event, {"label", "executable", "arguments", "timeout_seconds"}, "worker start details")
    require_exact_keys(exit_event, {"label", "result"}, "worker exit details")
    require_exact_keys(immediate_event, {"label", "diagnostics"}, "log-check event details")
    require_exact_keys(source_event, {"source_signature"}, "source event details")
    require(start_event.get("label") == exit_event.get("label") == immediate_event.get("label") == label, "worker labels do not match")
    require(same_path(str(start_event.get("executable", "")), str(executable_record.get("path", ""))), "worker executable identity mismatch")
    expected_arguments = [
        "-no-shell-escape",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        "-recorder",
        "-synctex=0",
        f"-jobname={job}",
        f"-output-directory={primary}",
        f"{job}.tex",
    ]
    require(start_event.get("arguments") == expected_arguments, "LuaLaTeX argument vector changed")
    timeout = start_event.get("timeout_seconds")
    require(is_json_integer(timeout) and 0 < timeout <= limits["per_worker_seconds"], "worker timeout is outside receipt limits")
    result = as_mapping(exit_event.get("result"), "worker exit result")
    require(set(result) == {"ProcessId", "ExitCode", "ElapsedSeconds", "PeakJobCommitBytes"}, "worker result fields changed")
    require(is_json_integer(result.get("ProcessId")) and result["ProcessId"] > 0, "invalid worker process id")
    require(is_json_integer(result.get("ExitCode")) and result.get("ExitCode") == 0, "LuaLaTeX worker exit code must be integer zero")
    require(is_finite_number(result.get("ElapsedSeconds")) and result["ElapsedSeconds"] >= 0, "invalid worker elapsed time")
    require(result["ElapsedSeconds"] <= timeout, "worker elapsed time exceeds its recorded timeout")
    require(result["ElapsedSeconds"] <= elapsed, "worker elapsed time exceeds guarded elapsed time")
    worker_wall_seconds = (event_times[2] - event_times[1]).total_seconds()
    require(worker_wall_seconds >= 0, "worker event interval is negative")
    require(
        result["ElapsedSeconds"] <= worker_wall_seconds + 1.0,
        "guard-reported worker time exceeds event wall time",
    )
    require(
        worker_wall_seconds <= result["ElapsedSeconds"] + 30.0,
        "worker exit event is implausibly delayed",
    )
    require(elapsed <= limits["complete_session_seconds"], "guarded elapsed time exceeds session limit")
    peak = result.get("PeakJobCommitBytes")
    require(is_json_integer(peak) and 0 < peak <= MEMORY_LIMIT, "worker peak exceeded guarded memory limit")
    observed_peak = receipt.get("observed_peak_job_commit_bytes")
    require(is_json_integer(observed_peak) and observed_peak == peak, "single-worker receipt peak memory is inconsistent")
    require(immediate_event.get("diagnostics") == pass_record.get("diagnostics"), "immediate diagnostic event mismatch")
    require(source_event.get("source_signature") == inventory["signature"], "post-build source identity event mismatch")
    inputs = recorder_inputs(fls)
    outputs = recorder_outputs(fls)
    require(pdf in outputs, "diagnostic PDF is absent from recorder OUTPUT records")
    validate_repo_recorder_input_freshness(inputs, inventory["rows"])

    return {
        "receipt": receipt,
        "receipt_path": receipt_path,
        "receipt_sha256": file_snapshot(receipt_path).sha256,
        "run_root": run_root,
        "primary": primary,
        "log": snapshot,
        "log_sha256": snapshot_hash,
        "log_text": log_text,
        "pdf": pdf,
        "pdf_sha256": pdf_hash,
        "fls": fls,
        "fls_sha256": fls_hash,
        "recorder_inputs": inputs,
        "recorder_outputs": outputs,
        "output_inventory": output_inventory,
        "diagnostic_counts": diagnostic_counts,
        "layout_markers": expected_layout_markers,
        "inventory": inventory,
        "lualatex": executable,
        "abandoned_recovery": mutex["abandoned_recovery"],
        "peak_job_commit_bytes": observed_peak,
    }


@dataclass(frozen=True)
class RecorderManifest:
    pwd: Path
    inputs: frozenset[Path]
    outputs: frozenset[Path]


def recorder_manifest(path: Path) -> RecorderManifest:
    try:
        text = read_file_text(path)
    except ValidationError as exc:
        raise ValidationError("recorder output is not strict UTF-8") from exc
    require("\x00" not in text, "recorder output contains NUL")
    pwd_rows = [line[4:].strip().strip('"') for line in text.splitlines() if line.startswith("PWD ")]
    require(len(pwd_rows) == 1 and pwd_rows[0], "recorder must contain exactly one nonempty PWD")
    pwd = Path(pwd_rows[0])
    require(pwd.is_absolute(), "recorder PWD must be absolute")
    require(same_path(pwd, LOCALE), "recorder PWD is not the expected locale directory")
    inputs: set[Path] = set()
    outputs: set[Path] = set()
    for line in text.splitlines():
        if line.startswith("INPUT "):
            destination = inputs
            raw = line[6:].strip().strip('"')
        elif line.startswith("OUTPUT "):
            destination = outputs
            raw = line[7:].strip().strip('"')
        else:
            continue
        require(raw, "recorder contains an empty input/output path")
        candidate = Path(raw)
        if not candidate.is_absolute():
            candidate = pwd / candidate
        destination.add(candidate.resolve())
    require(inputs, "recorder contains no INPUT records")
    require(outputs, "recorder contains no OUTPUT records")
    return RecorderManifest(pwd.resolve(), frozenset(inputs), frozenset(outputs))


def recorder_inputs(path: Path) -> set[Path]:
    return set(recorder_manifest(path).inputs)


def recorder_outputs(path: Path) -> set[Path]:
    return set(recorder_manifest(path).outputs)


def require_bound_output(common: Mapping[str, object], path: Path) -> FileSnapshot:
    resolved = path.resolve()
    require(resolved in common["recorder_outputs"], f"artifact is absent from recorder OUTPUT records: {path.name}")
    inventory = common["output_inventory"]
    require(isinstance(inventory, Mapping), "validated build output inventory is unavailable")
    snapshot = file_snapshot(resolved)
    require(
        inventory.get(resolved.name) == (snapshot.size, snapshot.sha256),
        f"artifact is not hash-bound by build output inventory: {path.name}",
    )
    return snapshot


def validate_repo_recorder_input_freshness(
    inputs: set[Path], inventory_rows: object,
) -> None:
    """Re-hash every source-tree input that the recorder proves was consumed."""

    rows = inventory_rows
    require(isinstance(rows, list), "validated source inventory rows are unavailable")
    inventory = {path: (size, digest) for path, size, digest in rows}
    consumed = 0
    for path in sorted(inputs, key=lambda value: str(value).casefold()):
        if not under(path, SOURCE):
            continue
        relative = path.resolve().relative_to(SOURCE).as_posix()
        require(relative in inventory, f"recorder source input absent from inventory: {relative}")
        require(path.is_file(), f"recorder source input is no longer a file: {relative}")
        size, digest = inventory[relative]
        snapshot = file_snapshot(path)
        require(snapshot.size == size, f"recorder source input byte count changed: {relative}")
        require(snapshot.sha256 == digest, f"recorder source input hash changed: {relative}")
        consumed += 1
    require(consumed > 0, "recorder named no repository source input")


def require_recorder_inputs(inputs: set[Path], expected: Iterable[Path]) -> None:
    missing = [relative_repo_path(path) for path in expected if path.resolve() not in inputs]
    require(not missing, f"required recorder inputs missing: {missing}")


def compact_text(text: str) -> str:
    normalized = unicodedata.normalize("NFC", text)
    return "".join(
        character
        for character in normalized
        if not character.isspace()
        and character not in {"\u200c", "\u200d", "\u200e", "\u200f", "\u2066", "\u2067", "\u2068", "\u2069", "\ufeff"}
    )


def require_compact_phrases(text: str, phrases: Sequence[str], label: str) -> None:
    compact = compact_text(text)
    missing = [phrase for phrase in phrases if compact_text(phrase) not in compact]
    require(not missing, f"{label} required PDF phrases missing: {missing}")


def require_compact_phrases_in_pages(
    pages: Sequence[str], phrases: Sequence[str], label: str,
) -> None:
    compact_pages = [compact_text(page) for page in pages]
    missing = [
        phrase
        for phrase in phrases
        if not any(compact_text(phrase) in page for page in compact_pages)
    ]
    require(not missing, f"{label} required PDF phrases missing within individual pages: {missing}")


def require_compact_phrases_in_blocks(
    blocks_by_page: Sequence[Sequence[str]], phrases: Sequence[str], label: str,
) -> None:
    compact_blocks = [
        compact_text(block)
        for page_blocks in blocks_by_page
        for block in page_blocks
    ]
    missing = [
        phrase
        for phrase in phrases
        if not any(compact_text(phrase) in block for block in compact_blocks)
    ]
    require(not missing, f"{label} required PDF phrases missing within individual text blocks: {missing}")


def reject_compact_phrases(text: str, phrases: Sequence[str], label: str) -> None:
    compact = compact_text(text)
    present = [phrase for phrase in phrases if compact_text(phrase) in compact]
    require(not present, f"{label} rejected PDF phrases present: {present}")


def reject_compact_phrases_in_pages(
    pages: Sequence[str], phrases: Sequence[str], label: str,
) -> None:
    compact_pages = [compact_text(page) for page in pages]
    present = [
        phrase
        for phrase in phrases
        if any(compact_text(phrase) in page for page in compact_pages)
    ]
    require(not present, f"{label} rejected PDF phrases present: {present}")


def load_pdf_text(
    path: Path,
) -> tuple[
    list[str], list[list[str]], list[list[dict[str, object]]], str,
    list[dict[str, object]],
]:
    try:
        import fitz
    except ImportError as exc:  # pragma: no cover - environment failure
        raise ValidationError("PyMuPDF is required for native PDF checks") from exc
    try:
        require(
            getattr(fitz, "VersionBind", None) == PYMUPDF_VERSION,
            f"unreviewed PyMuPDF version: {getattr(fitz, 'VersionBind', None)!r}",
        )
        document = fitz.open(stream=read_file_bytes(path), filetype="pdf")
    except Exception as exc:
        raise ValidationError(f"cannot parse diagnostic PDF: {exc}") from exc
    try:
        require(document.is_pdf, "diagnostic artifact is not a PDF")
        require(not document.is_encrypted, "diagnostic PDF may not be encrypted")
        require(document.page_count > 0, "diagnostic PDF has no pages")
        pages: list[str] = []
        blocks_by_page: list[list[str]] = []
        lines_by_page: list[list[dict[str, object]]] = []
        geometry: list[dict[str, object]] = []
        for page_index, page in enumerate(document):
            rectangle = tuple(float(value) for value in page.rect)
            require(
                len(rectangle) == 4
                and all(math.isfinite(value) for value in rectangle)
                and rectangle[2] > rectangle[0]
                and rectangle[3] > rectangle[1],
                f"PDF page {page_index + 1} has invalid geometry",
            )
            require(
                abs(rectangle[0]) < 0.01
                and abs(rectangle[1]) < 0.01
                and abs(rectangle[2] - 612.0) < 0.01
                and abs(rectangle[3] - 792.0) < 0.01
                and page.rotation == 0,
                f"PDF page {page_index + 1} is not unrotated US Letter geometry",
            )
            page_dictionary = page.get_text("dict", flags=fitz.TEXTFLAGS_TEXT)
            page_blocks: list[str] = []
            page_lines: list[dict[str, object]] = []
            opaque_nonwhite_spans = 0
            opaque_nonwhite_characters = 0
            zero_width_combining_mark_spans = 0
            fonts: set[str] = set()
            for block_index, block in enumerate(page_dictionary.get("blocks", [])):
                if block.get("type") != 0:
                    continue
                lines: list[str] = []
                for line in block.get("lines", []):
                    pieces: list[str] = []
                    for span in line.get("spans", []):
                        span_text = span.get("text")
                        require(isinstance(span_text, str), "PDF text span lacks text")
                        pieces.append(span_text)
                        if not span_text.strip():
                            continue
                        bbox = span.get("bbox")
                        require(
                            isinstance(bbox, (tuple, list))
                            and len(bbox) == 4
                            and all(is_finite_number(value) for value in bbox),
                            f"PDF page {page_index + 1} has a text span with invalid coordinates",
                        )
                        x0, y0, x1, y1 = (float(value) for value in bbox)
                        require(y1 > y0 and x1 >= x0, f"PDF page {page_index + 1} has an invalid text-span area")
                        if x1 == x0:
                            # HarfBuzz/LuaTeX may expose a separately positioned
                            # Arabic combining mark (for example U+0650 KASRA)
                            # as a zero-advance span.  It still has vertical ink
                            # and is not hidden text.  Admit only an all-mark span;
                            # zero-width letters, digits, punctuation, or format
                            # controls remain a hard failure.
                            require(
                                all(unicodedata.category(character).startswith("M") for character in span_text),
                                f"PDF page {page_index + 1} has a zero-width non-combining text span",
                            )
                            zero_width_combining_mark_spans += 1
                        require(
                            x0 >= rectangle[0] - 1.0
                            and y0 >= rectangle[1] - 1.0
                            and x1 <= rectangle[2] + 1.0
                            and y1 <= rectangle[3] + 1.0,
                            f"PDF page {page_index + 1} has clipped/out-of-page extracted text",
                        )
                        require(span.get("alpha") == 255, f"PDF page {page_index + 1} has non-opaque extracted text")
                        color = span.get("color")
                        require(is_json_integer(color) and color != 0xFFFFFF, f"PDF page {page_index + 1} has white/invalid extracted text")
                        font = span.get("font")
                        require(isinstance(font, str) and font, f"PDF page {page_index + 1} has an unnamed text font")
                        size = span.get("size")
                        require(is_finite_number(size) and size > 0, f"PDF page {page_index + 1} has invalid text size")
                        fonts.add(font)
                        opaque_nonwhite_spans += 1
                        opaque_nonwhite_characters += len(span_text)
                    line_text = "".join(pieces)
                    lines.append(line_text)
                    if line_text.strip():
                        direction = line.get("dir")
                        bbox = line.get("bbox")
                        require(
                            isinstance(direction, (tuple, list))
                            and len(direction) == 2
                            and all(is_finite_number(value) for value in direction),
                            f"PDF page {page_index + 1} has an invalid text-line direction",
                        )
                        require(
                            isinstance(bbox, (tuple, list))
                            and len(bbox) == 4
                            and all(is_finite_number(value) for value in bbox),
                            f"PDF page {page_index + 1} has invalid text-line geometry",
                        )
                        page_lines.append(
                            {
                                "text": line_text,
                                "direction": [float(value) for value in direction],
                                "bbox": [float(value) for value in bbox],
                                "block_index": block_index,
                            }
                        )
                block_text = "\n".join(lines)
                if block_text.strip():
                    page_blocks.append(block_text)
            require(page_blocks, f"diagnostic PDF page {page_index + 1} has no extracted text block")
            page_text = "\n".join(page_blocks)
            require(page_text.strip(), f"diagnostic PDF page {page_index + 1} has empty extracted text")
            pages.append(page_text)
            blocks_by_page.append(page_blocks)
            lines_by_page.append(page_lines)
            geometry.append(
                {
                    "page_one_based": page_index + 1,
                    "effective_page_rect_points": list(rectangle),
                    "rotation_degrees": page.rotation,
                    "text_blocks": len(page_blocks),
                    "text_lines": len(page_lines),
                    "opaque_nonwhite_extracted_text_spans": opaque_nonwhite_spans,
                    "opaque_nonwhite_extracted_characters": opaque_nonwhite_characters,
                    "zero_width_combining_mark_spans": zero_width_combining_mark_spans,
                    "fonts": sorted(fonts),
                }
            )
        text = "\n\f\n".join(pages)
        require("\ufffd" not in text, "PDF extraction contains a replacement character")
        return pages, blocks_by_page, lines_by_page, PYMUPDF_VERSION, geometry
    finally:
        document.close()


def base_evidence(
    *, kind: str, common: Mapping[str, object], fixture: Path, fixture_manifest: Path,
) -> dict[str, object]:
    return {
        "diagnostic_kind": kind,
        "fixture": {
            "path": relative_repo_path(fixture),
            "bytes": file_size(fixture),
            "sha256": sha256_file(fixture),
        },
        "fixture_manifest": {
            "path": relative_repo_path(fixture_manifest),
            "bytes": file_size(fixture_manifest),
            "sha256": sha256_file(fixture_manifest),
        },
        "guarded_run": {
            "receipt_path": relative_repo_path(common["receipt_path"]),
            "receipt_sha256": common["receipt_sha256"],
            "mode": "Diagnostic",
            "status": "DIAGNOSTIC_ONLY_NOT_ACCEPTED",
            "accepted_build": False,
            "mutex": MUTEX_NAME,
            "abandoned_recovery": common["abandoned_recovery"],
            "released_after_confirmed_tree_exit": True,
            "workers": 1,
            "worker_tree_exits": 1,
            "peak_job_commit_bytes": common["peak_job_commit_bytes"],
            "lualatex": common["lualatex"],
            "diagnostic_counts": common["diagnostic_counts"],
            "source_inventory": {
                key: common["inventory"][key]
                for key in ("path", "sha256", "files", "signature")
            },
        },
        "artifacts": {
            "log": {
                "path": relative_repo_path(common["log"]),
                "sha256": common["log_sha256"],
            },
            "pdf": {
                "path": relative_repo_path(common["pdf"]),
                "bytes": file_size(common["pdf"]),
                "sha256": common["pdf_sha256"],
            },
            "recorder": {
                "path": relative_repo_path(common["fls"]),
                "sha256": common["fls_sha256"],
            },
        },
    }


def expect_validation_error(function, *args, **kwargs) -> None:
    try:
        function(*args, **kwargs)
    except ValidationError:
        return
    raise AssertionError("adversarial input was accepted")


def self_test_common_primitives() -> int:
    """Exercise fail-closed primitives without launching TeX or writing files."""

    negative_controls = 0
    expect_validation_error(require_exact_keys, {"a": 1, "extra": 2}, {"a"}, "sample")
    negative_controls += 1
    require(is_json_integer(1) and not is_json_integer(True), "JSON integer type guard failed")

    diagnostics = {key: [] for key in DIAGNOSTIC_PATTERNS}
    diagnostics["rerun"] = [{"line": 1, "text": "Please (re)run BibTeX"}]
    expect_validation_error(
        validate_diagnostics,
        diagnostics,
        diagnostics,
        allow_reference_warnings=False,
        allow_latex_rerun_warnings=True,
    )
    negative_controls += 1

    diagnostics = {key: [] for key in DIAGNOSTIC_PATTERNS}
    diagnostics["unresolved"] = [{"line": 1, "text": "Citation `X' undefined"}]
    expect_validation_error(
        validate_diagnostics,
        diagnostics,
        diagnostics,
        allow_reference_warnings=True,
        allow_latex_rerun_warnings=True,
    )
    negative_controls += 1

    # A phrase assembled only by concatenating two pages must not pass.
    expect_validation_error(
        require_compact_phrases_in_pages, ["alpha beta", "gamma delta"],
        ["beta gamma"], "page boundary",
    )
    negative_controls += 1
    return negative_controls
