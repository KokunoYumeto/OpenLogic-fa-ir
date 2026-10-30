# LuaLaTeX build of the Persian standalone reader with the orthography fix (embedded-source driver).
# Mirrors the bundle's BUILD_STANDALONE.ps1 environment: TEXINPUTS = build dir and locale root, BibTeX inputs from the
# locale root and source/bib. Four LuaLaTeX passes with BibTeX after the first, then extra passes while LaTeX asks.
$ErrorActionPreference = 'Stop'
$locale = Join-Path $PSScriptRoot 'pdf\source\locale\fa-IR'
$bib = Join-Path $PSScriptRoot 'pdf\source\bib'
$log = Join-Path $PSScriptRoot 'build_pdf.log'
$env:TEXINPUTS = ".;$locale;"
$env:BIBINPUTS = "$locale;$bib;"
$env:BSTINPUTS = "$locale;$bib;"
Set-Location $locale
$job = 'open-logic-standalone-fa-IR'
$latexArgs = @('-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-synctex=0', "-jobname=$job", "$job.tex")
"start $(Get-Date -Format o)" | Out-File $log -Encoding utf8
for ($i = 1; $i -le 7; $i++) {
    & lualatex @latexArgs *> "lualatex-$i.out"
    "pass $i exit $LASTEXITCODE $(Get-Date -Format o)" | Out-File $log -Append -Encoding utf8
    if ($LASTEXITCODE -ne 0) { "FAILED in pass $i" | Out-File $log -Append -Encoding utf8; exit 1 }
    if ($i -eq 1 -or $i -eq 2) {
        & bibtex $job *> "bibtex-$i.out"
        "bibtex after pass $i exit $LASTEXITCODE" | Out-File $log -Append -Encoding utf8
    }
    $texlog = Get-Content "$job.log" -Raw
    if ($i -ge 4 -and $texlog -notmatch 'Rerun to get|Label\(s\) may have changed|Please \(re\)run|has changed') { break }
}
"done $(Get-Date -Format o)" | Out-File $log -Append -Encoding utf8
