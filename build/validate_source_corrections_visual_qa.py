"""Fail-closed integrity check for the complete source-correction visual review.

This does not manufacture visual judgment.  It binds the recorded judgment to
the exact semantic receipt, PDF, and every inspected raster/sheet byte so a
later change cannot inherit the review accidentally.
"""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import struct
import sys


ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_VISUAL_QA.json"
EXPECTED_SCHEMA = "farsi-combined-source-corrections-native-probe-visual-qa-v1"
EXPECTED_STATUS = "PASS_COMPLETE_VISUAL_INSPECTION_NATIVE_DIAGNOSTIC_NOT_FULL_READER"
EXPECTED_SEMANTIC_STATUS = "PASS_NATIVE_DIAGNOSTIC_PENDING_COMPLETE_VISUAL_INSPECTION_NOT_FULL_READER"
EXPECTED_PAGES = list(range(1, 30))


class ValidationError(RuntimeError):
    pass


def require(condition: object, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def load_json(path: Path) -> dict[str, object]:
    require(path.is_file() and not path.is_symlink(), f"missing or linked JSON: {path}")
    try:
        value = json.loads(
            path.read_text(encoding="utf-8-sig"),
            object_pairs_hook=unique_object,
            parse_constant=lambda token: (_ for _ in ()).throw(
                ValidationError(f"non-finite JSON token: {token}")
            ),
        )
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f"invalid strict JSON: {path}: {exc}") from exc
    require(isinstance(value, dict), f"JSON root is not an object: {path}")
    return value


def mapping(value: object, label: str) -> dict[str, object]:
    require(isinstance(value, dict), f"{label} is not an object")
    return value


def sequence(value: object, label: str) -> list[object]:
    require(isinstance(value, list), f"{label} is not an array")
    return value


def exact_keys(value: dict[str, object], keys: set[str], label: str) -> None:
    require(set(value) == keys, f"{label} fields changed")


def resolve_repo_file(relative: object, label: str) -> Path:
    require(isinstance(relative, str) and relative, f"{label} path missing")
    path = (ROOT / relative).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise ValidationError(f"{label} path escapes repository") from exc
    require(path.is_file() and not path.is_symlink(), f"{label} file missing or linked")
    return path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def file_identity(path: Path, record: dict[str, object], label: str) -> None:
    size = record.get("bytes")
    digest = record.get("sha256")
    require(isinstance(size, int) and not isinstance(size, bool) and size >= 0, f"invalid {label} byte count")
    require(isinstance(digest, str) and len(digest) == 64, f"invalid {label} hash")
    require(path.stat().st_size == size, f"{label} byte count changed")
    require(sha256(path) == digest, f"{label} hash changed")


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    require(len(data) == 24 and data[:8] == b"\x89PNG\r\n\x1a\n" and data[12:16] == b"IHDR", f"not a PNG: {path.name}")
    width, height = struct.unpack(">II", data[16:24])
    require(width > 0 and height > 0, f"invalid PNG geometry: {path.name}")
    return width, height


def manifest_hash(records: list[tuple[str, int, str, str]]) -> str:
    canonical = "\n".join(
        f"{name}|{size}|{digest}|{dimensions}"
        for name, size, digest, dimensions in records
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def validate() -> dict[str, object]:
    receipt = load_json(RECEIPT)
    exact_keys(
        receipt,
        {
            "schema", "status", "inspected_utc", "source_pdf",
            "semantic_qa_receipt", "renderer", "page_rasters",
            "inspection_sheets", "inspection", "limitations",
        },
        "visual receipt",
    )
    require(receipt.get("schema") == EXPECTED_SCHEMA, "visual receipt schema changed")
    require(receipt.get("status") == EXPECTED_STATUS, "visual receipt is not accepted")

    pdf_record = mapping(receipt.get("source_pdf"), "source_pdf")
    pdf = resolve_repo_file(pdf_record.get("path"), "source PDF")
    file_identity(pdf, pdf_record, "source PDF")
    require(pdf.read_bytes()[:5] == b"%PDF-", "source artifact is not a PDF")
    require(pdf_record.get("pages") == 29, "source PDF page count record changed")
    require(pdf_record.get("page_geometry_points") == [0, 0, 612, 792], "source PDF geometry record changed")

    semantic_record = mapping(receipt.get("semantic_qa_receipt"), "semantic_qa_receipt")
    semantic_path = resolve_repo_file(semantic_record.get("path"), "semantic receipt")
    file_identity(semantic_path, semantic_record, "semantic receipt")
    semantic = load_json(semantic_path)
    require(semantic.get("status") == EXPECTED_SEMANTIC_STATUS, "semantic receipt status changed")
    semantic_pdf = mapping(mapping(semantic.get("artifacts"), "semantic artifacts").get("pdf"), "semantic PDF")
    require(semantic_pdf.get("bytes") == pdf_record.get("bytes"), "semantic and visual PDF byte counts differ")
    require(semantic_pdf.get("sha256") == pdf_record.get("sha256"), "semantic and visual PDF hashes differ")
    require(mapping(semantic.get("pdf_text"), "semantic PDF text").get("pages") == 29, "semantic receipt page count changed")

    raster_record = mapping(receipt.get("page_rasters"), "page_rasters")
    require(raster_record.get("count") == 29, "visual raster count changed")
    require(raster_record.get("contiguous_pages_one_based") == [1, 29], "visual raster range changed")
    require(raster_record.get("common_dimensions_pixels") == [1275, 1650], "visual raster dimensions changed")
    raster_dir = ROOT / "tmp/pdfs/source-corrections-visual-qa-6a339641"
    require(raster_dir.is_dir() and not raster_dir.is_symlink(), "visual raster directory missing or linked")
    raster_inventory = sequence(raster_record.get("inventory"), "raster inventory")
    require(len(raster_inventory) == 29, "raster inventory does not contain 29 rows")
    raster_manifest: list[tuple[str, int, str, str]] = []
    for page, raw in zip(EXPECTED_PAGES, raster_inventory, strict=True):
        row = mapping(raw, f"raster page {page}")
        exact_keys(row, {"file", "bytes", "sha256"}, f"raster page {page}")
        expected_name = f"page-{page:02d}.png"
        require(row.get("file") == expected_name, f"raster sequence changed at page {page}")
        path = raster_dir / expected_name
        require(path.is_file() and not path.is_symlink(), f"raster missing or linked: {expected_name}")
        file_identity(path, row, f"raster page {page}")
        dimensions = png_dimensions(path)
        require(dimensions == (1275, 1650), f"raster dimensions changed: {expected_name}")
        raster_manifest.append((expected_name, path.stat().st_size, sha256(path), f"{dimensions[0]}x{dimensions[1]}"))
    require(
        sorted(path.name for path in raster_dir.glob("page-*.png")) == [f"page-{page:02d}.png" for page in EXPECTED_PAGES],
        "raster directory has missing or extra page images",
    )
    require(manifest_hash(raster_manifest) == raster_record.get("canonical_manifest_sha256"), "raster manifest hash changed")

    sheet_record = mapping(receipt.get("inspection_sheets"), "inspection_sheets")
    sheet_inventory = sequence(sheet_record.get("inventory"), "inspection sheet inventory")
    require(len(sheet_inventory) == 8, "inspection sheet count changed")
    sheet_dir = raster_dir / "sheets"
    require(sheet_dir.is_dir() and not sheet_dir.is_symlink(), "inspection sheet directory missing or linked")
    sheet_manifest: list[tuple[str, int, str, str]] = []
    expected_sheet_names = [
        "sheet-01-pages-01-04.png", "sheet-02-pages-05-08.png",
        "sheet-03-pages-09-12.png", "sheet-04-pages-13-16.png",
        "sheet-05-pages-17-20.png", "sheet-06-pages-21-24.png",
        "sheet-07-pages-25-28.png", "sheet-08-pages-29-29.png",
    ]
    for index, (expected_name, raw) in enumerate(zip(expected_sheet_names, sheet_inventory, strict=True), 1):
        row = mapping(raw, f"inspection sheet {index}")
        exact_keys(row, {"file", "bytes", "sha256", "dimensions"}, f"inspection sheet {index}")
        require(row.get("file") == expected_name, f"inspection sheet sequence changed at {index}")
        path = sheet_dir / expected_name
        require(path.is_file() and not path.is_symlink(), f"inspection sheet missing or linked: {expected_name}")
        file_identity(path, row, f"inspection sheet {index}")
        dimensions = png_dimensions(path)
        require(row.get("dimensions") == list(dimensions), f"inspection sheet dimensions changed: {expected_name}")
        sheet_manifest.append((expected_name, path.stat().st_size, sha256(path), f"{dimensions[0]}x{dimensions[1]}"))
    require(
        sorted(path.name for path in sheet_dir.glob("*.png")) == sorted(expected_sheet_names),
        "inspection sheet directory has missing or extra images",
    )
    require(manifest_hash(sheet_manifest) == sheet_record.get("canonical_manifest_sha256"), "inspection sheet manifest hash changed")

    inspection = mapping(receipt.get("inspection"), "inspection")
    require(inspection.get("pages_reviewed_one_based") == EXPECTED_PAGES, "not every page is recorded as reviewed")
    require(inspection.get("visual_defects") == [], "visual receipt records defects")
    checks = mapping(inspection.get("checks"), "inspection checks")
    require(checks and all(value is True for value in checks.values()), "one or more visual checks did not pass")
    require(len(sequence(receipt.get("limitations"), "limitations")) == 2, "visual limitations changed")

    return {
        "schema": "farsi-source-corrections-visual-qa-integrity-check-v1",
        "status": "PASS",
        "visual_receipt_sha256": sha256(RECEIPT),
        "semantic_receipt_sha256": sha256(semantic_path),
        "pdf_sha256": sha256(pdf),
        "pages": 29,
        "page_raster_manifest_sha256": raster_record["canonical_manifest_sha256"],
        "inspection_sheet_manifest_sha256": sheet_record["canonical_manifest_sha256"],
        "visual_defects": 0,
    }


if __name__ == "__main__":
    try:
        print(json.dumps(validate(), sort_keys=True))
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
