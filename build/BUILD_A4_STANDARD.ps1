param(
  [string]$OutputDirectory = "",
  [string]$ExpectedCompleteSha256 = "B7C622A99E6317ADF9F5CCC903138A7BB1264266889A1F1D1C97094D57D2C3E7",
  [string]$ExpectedSupplementSha256 = "1019D4639FD0F56C17AF618BB877857D4A1BFD2A4EA354D0B164957145D826AB",
  [switch]$StageReleaseAssets
)

$ErrorActionPreference = "Stop"

$releaseRoot = Split-Path -Parent $PSScriptRoot
$localeRoot = Join-Path $releaseRoot "source\locale\fa-IR"
$repairScript = Join-Path $PSScriptRoot "repair_rtl_link_rects_fa_a4.py"
$completeDriverName = "open-logic-complete-fa-IR-screen.tex"
$supplementDriverName = "open-logic-closure-supplement-fa-IR-screen.tex"
$completeDriver = Join-Path $localeRoot $completeDriverName
$supplementDriver = Join-Path $localeRoot $supplementDriverName
$completeJob = [IO.Path]::GetFileNameWithoutExtension($completeDriverName)
$supplementJob = [IO.Path]::GetFileNameWithoutExtension($supplementDriverName)
$version = "OLP-0722-A4-STANDARD-20260819"
$expectedConceptDoi = "10.5281/zenodo.21921852"
$forbiddenPdfDois = @(
  "10.5281/zenodo.21987687",
  "10.5281/zenodo.22015765"
)
$expectedCompletePages = 798
$expectedSupplementPages = 113
$expectedCompleteLinks = 2986
$expectedSupplementLinks = 137
$expectedCompleteRawSha256 = "FBD13FA9EE4F77B0626E175D1D911E3FEDE4B2E17B8E72648D57FC3E61E6B78B"
$expectedSupplementRawSha256 = "AF01DA08D66B46CAD03BC4145BB2C6C0694B1C4B6659B974A96CA6885EA8ED7F"
$expectedCompleteWrapperSha256 = "5CD40F62DCAD37678CC41E5D660FB1FE0FECF30E9CE3CBEEB466DE4BEA64A9FA"
$expectedSupplementWrapperSha256 = "98459D24BF0BABF26FF86CBD118B290D17FAEBBD4E7DDBFFCCC3C9E75B57077E"

foreach ($driver in @($completeDriver, $supplementDriver)) {
  if (-not (Test-Path -LiteralPath $driver -PathType Leaf)) {
    throw "Packaged A4 driver is missing: $driver"
  }
  $driverText = [IO.File]::ReadAllText($driver)
  if (-not $driverText.Contains($expectedConceptDoi)) {
    throw "Stable concept DOI is absent from $driver"
  }
  foreach ($forbiddenDoi in $forbiddenPdfDois) {
    if ($driverText.Contains($forbiddenDoi)) {
      throw "Exact version DOI is forbidden in the A4 PDF driver: $driver"
    }
  }
}
if ((Get-FileHash -Algorithm SHA256 -LiteralPath $completeDriver).Hash -ne $expectedCompleteWrapperSha256) {
  throw "Complete A4 wrapper SHA-256 mismatch"
}
if ((Get-FileHash -Algorithm SHA256 -LiteralPath $supplementDriver).Hash -ne $expectedSupplementWrapperSha256) {
  throw "Supplement A4 wrapper SHA-256 mismatch"
}
if (-not (Test-Path -LiteralPath $repairScript -PathType Leaf)) {
  throw "A4 RTL link repair adapter is missing: $repairScript"
}

foreach ($commandName in @("lualatex", "bibtex", "python")) {
  if (-not (Get-Command $commandName -ErrorAction SilentlyContinue)) {
    throw "Required command is unavailable: $commandName"
  }
}
& python -c "import fitz, pypdf"
if ($LASTEXITCODE -ne 0) {
  throw "Python dependencies PyMuPDF and pypdf are required"
}

if ([string]::IsNullOrWhiteSpace($OutputDirectory)) {
  $OutputDirectory = Join-Path $PSScriptRoot "output-fa-IR-a4-standard-OLP-0722"
}
if (Test-Path -LiteralPath $OutputDirectory) {
  $existing = Get-ChildItem -LiteralPath $OutputDirectory -Force | Select-Object -First 1
  if ($null -ne $existing) {
    throw "Output directory must be empty: $OutputDirectory"
  }
} else {
  New-Item -ItemType Directory -Path $OutputDirectory | Out-Null
}
$resolvedOutput = (Resolve-Path -LiteralPath $OutputDirectory).Path
$outputArgument = "-output-directory=$resolvedOutput"
$latexArguments = @(
  "-interaction=nonstopmode",
  "-halt-on-error",
  "-file-line-error",
  "-recorder",
  $outputArgument
)

$oldSourceDateEpoch = [Environment]::GetEnvironmentVariable("SOURCE_DATE_EPOCH", "Process")
$oldForceSourceDate = [Environment]::GetEnvironmentVariable("FORCE_SOURCE_DATE", "Process")
$oldTimeZone = [Environment]::GetEnvironmentVariable("TZ", "Process")
$oldTexInputs = [Environment]::GetEnvironmentVariable("TEXINPUTS", "Process")

try {
  [Environment]::SetEnvironmentVariable("SOURCE_DATE_EPOCH", "1783874174", "Process")
  [Environment]::SetEnvironmentVariable("FORCE_SOURCE_DATE", "1", "Process")
  [Environment]::SetEnvironmentVariable("TZ", "UTC", "Process")
  $texInputs = if ([string]::IsNullOrEmpty($oldTexInputs)) {
    "$resolvedOutput;"
  } else {
    "$resolvedOutput;$oldTexInputs"
  }
  [Environment]::SetEnvironmentVariable("TEXINPUTS", $texInputs, "Process")

  Push-Location $localeRoot
  try {
    & lualatex @latexArguments $completeDriverName
    if ($LASTEXITCODE -ne 0) { throw "A4 reader LuaLaTeX pass 1 failed" }
    & bibtex (Join-Path $resolvedOutput $completeJob)
    if ($LASTEXITCODE -ne 0) { throw "A4 reader BibTeX pass failed" }
    for ($pass = 2; $pass -le 3; $pass++) {
      & lualatex @latexArguments $completeDriverName
      if ($LASTEXITCODE -ne 0) { throw "A4 reader LuaLaTeX pass $pass failed" }
    }
    for ($pass = 1; $pass -le 2; $pass++) {
      & lualatex @latexArguments $supplementDriverName
      if ($LASTEXITCODE -ne 0) { throw "A4 supplement LuaLaTeX pass $pass failed" }
    }
  } finally {
    Pop-Location
  }
} finally {
  [Environment]::SetEnvironmentVariable("SOURCE_DATE_EPOCH", $oldSourceDateEpoch, "Process")
  [Environment]::SetEnvironmentVariable("FORCE_SOURCE_DATE", $oldForceSourceDate, "Process")
  [Environment]::SetEnvironmentVariable("TZ", $oldTimeZone, "Process")
  [Environment]::SetEnvironmentVariable("TEXINPUTS", $oldTexInputs, "Process")
}

$completePdf = Join-Path $resolvedOutput "$completeJob.pdf"
$supplementPdf = Join-Path $resolvedOutput "$supplementJob.pdf"
$completeRaw = Join-Path $resolvedOutput "$completeJob.raw-before-link-repair.pdf"
$supplementRaw = Join-Path $resolvedOutput "$supplementJob.raw-before-link-repair.pdf"
$completeEvidence = Join-Path $resolvedOutput "$completeJob.link-rect-repair-evidence.json"
$supplementEvidence = Join-Path $resolvedOutput "$supplementJob.link-rect-repair-evidence.json"

foreach ($pdf in @($completePdf, $supplementPdf)) {
  if (-not (Test-Path -LiteralPath $pdf -PathType Leaf)) {
    throw "Expected compiled PDF is missing: $pdf"
  }
}
Move-Item -LiteralPath $completePdf -Destination $completeRaw
Move-Item -LiteralPath $supplementPdf -Destination $supplementRaw

$completeRawHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $completeRaw).Hash
$supplementRawHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $supplementRaw).Hash
if ($completeRawHash -ne $expectedCompleteRawSha256) {
  throw "Raw reader SHA-256 mismatch: expected $expectedCompleteRawSha256, got $completeRawHash"
}
if ($supplementRawHash -ne $expectedSupplementRawSha256) {
  throw "Raw supplement SHA-256 mismatch: expected $expectedSupplementRawSha256, got $supplementRawHash"
}

& python $repairScript --input $completeRaw --output $completePdf --evidence $completeEvidence
if ($LASTEXITCODE -ne 0) { throw "A4 reader link-rectangle repair failed" }
& python $repairScript --input $supplementRaw --output $supplementPdf --evidence $supplementEvidence
if ($LASTEXITCODE -ne 0) { throw "A4 supplement link-rectangle repair failed" }

$pdfFactsProgram = @'
import json
import sys
from pypdf import PdfReader

reader = PdfReader(sys.argv[1])
root = reader.trailer["/Root"]
links = 0
overflow = 0
geometry_ok = True
rotation_ok = True
for page in reader.pages:
    media = [float(v) for v in page.mediabox]
    crop = [float(v) for v in page.cropbox]
    geometry_ok = geometry_ok and all(abs(a-b) < 0.01 for a,b in zip(media,[0.0,0.0,595.276,841.89])) and crop == media
    rotation_ok = rotation_ok and int(page.get("/Rotate", 0)) == 0
    for ref in page.get("/Annots", []):
        annot = ref.get_object()
        if str(annot.get("/Subtype")) != "/Link":
            continue
        links += 1
        x0, y0, x1, y1 = [float(v) for v in annot["/Rect"]]
        if x0 < -0.01 or y0 < -0.01 or x1 > 595.286 or y1 > 841.90 or x1 < x0 or y1 < y0:
            overflow += 1
open_action = root.get("/OpenAction")
if hasattr(open_action, "get_object"):
    open_action = open_action.get_object()
if isinstance(open_action, dict):
    destination = open_action.get("/D")
else:
    destination = open_action
fit = str(destination[1]) if isinstance(destination, (list, tuple)) and len(destination) > 1 else ""
print(json.dumps({
    "pages": len(reader.pages),
    "encrypted": bool(reader.is_encrypted),
    "geometry_ok": geometry_ok,
    "rotation_ok": rotation_ok,
    "links": links,
    "link_overflow": overflow,
    "page_mode": str(root.get("/PageMode", "")),
    "page_layout": str(root.get("/PageLayout", "")),
    "open_view": fit,
}, separators=(",", ":")))
'@

function Get-PdfFacts {
  param([Parameter(Mandatory = $true)][string]$Path)
  $json = & python -c $pdfFactsProgram $Path
  if ($LASTEXITCODE -ne 0) { throw "PDF facts inspection failed for $Path" }
  return $json | ConvertFrom-Json
}

$completeFacts = Get-PdfFacts -Path $completePdf
$supplementFacts = Get-PdfFacts -Path $supplementPdf
$checks = @(
  @{Name="reader pages"; Actual=$completeFacts.pages; Expected=$expectedCompletePages},
  @{Name="supplement pages"; Actual=$supplementFacts.pages; Expected=$expectedSupplementPages},
  @{Name="reader links"; Actual=$completeFacts.links; Expected=$expectedCompleteLinks},
  @{Name="supplement links"; Actual=$supplementFacts.links; Expected=$expectedSupplementLinks},
  @{Name="reader link overflow"; Actual=$completeFacts.link_overflow; Expected=0},
  @{Name="supplement link overflow"; Actual=$supplementFacts.link_overflow; Expected=0}
)
foreach ($check in $checks) {
  if ($check.Actual -ne $check.Expected) {
    throw "$($check.Name) mismatch: expected $($check.Expected), got $($check.Actual)"
  }
}
foreach ($facts in @($completeFacts, $supplementFacts)) {
  if ($facts.encrypted -or -not $facts.geometry_ok -or -not $facts.rotation_ok) {
    throw "PDF encryption, A4 geometry, or rotation gate failed"
  }
  if ($facts.page_mode -ne "/UseOutlines" -or $facts.page_layout -ne "/SinglePage" -or $facts.open_view -ne "/Fit") {
    throw "A4 viewer-preference gate failed"
  }
}

$completeHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $completePdf).Hash
$supplementHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $supplementPdf).Hash
if ($completeHash -ne $ExpectedCompleteSha256.ToUpperInvariant()) {
  throw "Final reader SHA-256 mismatch: expected $ExpectedCompleteSha256, got $completeHash"
}
if ($supplementHash -ne $ExpectedSupplementSha256.ToUpperInvariant()) {
  throw "Final supplement SHA-256 mismatch: expected $ExpectedSupplementSha256, got $supplementHash"
}

foreach ($log in @(
  (Join-Path $resolvedOutput "$completeJob.log"),
  (Join-Path $resolvedOutput "$supplementJob.log")
)) {
  $logText = [IO.File]::ReadAllText($log)
  foreach ($pattern in @("(?m)^! ", "Missing character", "undefined reference", "undefined citation", "Rerun to get")) {
    if ([regex]::IsMatch($logText, $pattern, [Text.RegularExpressions.RegexOptions]::IgnoreCase)) {
      throw "Final log gate failed for pattern '$pattern' in $log"
    }
  }
}

if ($StageReleaseAssets) {
  $destinations = @(
    @{
      Source = $completePdf
      Destination = Join-Path $releaseRoot "00_OPENLOGIC_fa-IR_COMPLETE_LINKED_READER_A4_STANDARD_OLP-0722.pdf"
    },
    @{
      Source = $supplementPdf
      Destination = Join-Path $releaseRoot "01_OPENLOGIC_fa-IR_CLOSURE_SUPPLEMENT_80_UNITS_A4_STANDARD_OLP-0722.pdf"
    }
  )
  foreach ($item in $destinations) {
    if (Test-Path -LiteralPath $item.Destination) {
      throw "Refusing to overwrite an existing A4 release asset: $($item.Destination)"
    }
    Copy-Item -LiteralPath $item.Source -Destination $item.Destination
  }
}

[pscustomobject]@{
  Version = $version
  ConceptDoiOnly = $expectedConceptDoi
  CompletePdf = $completePdf
  CompletePages = $completeFacts.pages
  CompleteLinks = $completeFacts.links
  CompleteSha256 = $completeHash
  SupplementPdf = $supplementPdf
  SupplementPages = $supplementFacts.pages
  SupplementLinks = $supplementFacts.links
  SupplementSha256 = $supplementHash
  Geometry = "A4 210 x 297 mm portrait"
  OpenView = "/Fit"
  PageLayout = "/SinglePage"
  PageMode = "/UseOutlines"
  ReleaseAssetsStaged = [bool]$StageReleaseAssets
}
