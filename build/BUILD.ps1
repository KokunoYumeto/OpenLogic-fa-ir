param(
  [string]$OutputDirectory = ""
)

$ErrorActionPreference = "Stop"
$releaseRoot = Split-Path -Parent $PSScriptRoot
$localeRoot = Join-Path $releaseRoot "source\locale\fa-IR"
$driver = Join-Path $localeRoot "open-logic-through-olp0010-fa-IR.tex"
$expectedHash = "6CF8F82A0C05775C9C4852C3C8D3D09D1B5E08DAEB6E6942E75C3487F0C2229D"

if (-not (Test-Path -LiteralPath $driver -PathType Leaf)) {
  throw "Packaged checkpoint driver is missing: $driver"
}
if ([string]::IsNullOrWhiteSpace($OutputDirectory)) {
  $OutputDirectory = Join-Path $PSScriptRoot "output-fa-IR"
}
New-Item -ItemType Directory -Path $OutputDirectory -Force | Out-Null
$resolvedOutput = (Resolve-Path -LiteralPath $OutputDirectory).Path

$env:SOURCE_DATE_EPOCH = "1783874174"
$env:FORCE_SOURCE_DATE = "1"
$env:TZ = "UTC"
$outputArgument = "-output-directory=$resolvedOutput"

Push-Location $localeRoot
try {
  for ($pass = 1; $pass -le 6; $pass++) {
    & lualatex -interaction=nonstopmode -halt-on-error -file-line-error -recorder $outputArgument $driver
    if ($LASTEXITCODE -ne 0) {
      throw "LuaLaTeX failed on pass $pass"
    }
  }
} finally {
  Pop-Location
}

$pdf = Join-Path $resolvedOutput "open-logic-through-olp0010-fa-IR.pdf"
$actualHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $pdf).Hash
if ($actualHash -ne $expectedHash) {
  throw "Checkpoint PDF hash mismatch: expected $expectedHash, got $actualHash"
}

$reader = Join-Path $releaseRoot "reader\00_OPENLOGIC_fa-IR_CUMULATIVE_LINKED_READER_OLP-0010.pdf"
Copy-Item -LiteralPath $pdf -Destination $reader -Force
Get-Item -LiteralPath $reader | Select-Object FullName, Length
Get-FileHash -Algorithm SHA256 -LiteralPath $reader
