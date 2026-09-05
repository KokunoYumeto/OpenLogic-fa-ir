#requires -Version 7.0
# Static/pure-function tests only. Never sources the build entrypoint, constructs
# a Guard, acquires the TeX mutex, or creates a native process/PDF.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$scriptPath = Join-Path $PSScriptRoot 'BUILD_STANDALONE.ps1'
$helperPath = Join-Path $PSScriptRoot 'StandaloneTeXProcessGuard.cs'
$tokens = $null
$parseErrors = $null
$ast = [Management.Automation.Language.Parser]::ParseFile($scriptPath, [ref]$tokens, [ref]$parseErrors)
if ($parseErrors.Count) { throw ($parseErrors | Out-String) }
$classifier = $ast.FindAll({ param($node)
    $node -is [Management.Automation.Language.FunctionDefinitionAst] -and $node.Name -eq 'Get-LogDiagnosticsFromText'
}, $true)
if ($classifier.Count -ne 1) { throw 'Expected one pure diagnostic classifier.' }
# Define only this actual pure function, never evaluate the full entrypoint.
. ([scriptblock]::Create($classifier[0].Extent.Text))

function Assert-True([bool]$Condition, [string]$Message) {
    if (-not $Condition) { throw "Static assertion failed: $Message" }
}

$clean = Get-LogDiagnosticsFromText "Output written on x.pdf (1 page).`nLaTeX Font Warning: Font shape abc undefined"
foreach ($key in @('fatal', 'duplicate', 'unresolved', 'rerun', 'bibliography_warning')) {
    Assert-True ($clean[$key].Count -eq 0) "Benign log classification ($key)"
}
$samples = @(
    @('unresolved', "LaTeX Warning: Reference `x' on page 2 undefined on input line 7."),
    @('unresolved', "Package natbib Warning: Citation `a' on page 1`n(natbib)                undefined on input line 4."),
    @('unresolved', 'LaTeX Warning: There were undefined citations.'),
    @('unresolved', "Warning--I didn't find a database entry for abc"),
    @('duplicate', "LaTeX Warning: Label `a' multiply defined."),
    @('duplicate', 'pdfTeX warning: destination with the same identifier has been already used, duplicate ignored'),
    @('fatal', 'Missing character: There is no x in font y!'),
    @('fatal', '! Emergency stop.'),
    @('rerun', 'LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.'),
    @('rerun', "Package rerunfilecheck Warning: File `x.out' has changed.")
)
foreach ($sample in $samples) {
    $result = Get-LogDiagnosticsFromText $sample[1]
    Assert-True ($result[$sample[0]].Count -gt 0) "Recognize $($sample[0]): $($sample[1])"
}

$metadata = Get-LogDiagnosticsFromText "This is BibTeX`nWarning--missing publisher in Berkeley1734`nWarning--can't use both author and editor fields in Frege1953`nWarning--empty journal in Weston2003`n"
Assert-True ($metadata.unresolved.Count -eq 0) 'Metadata warnings are not missing citations'
Assert-True ($metadata.bibliography_warning.Count -eq 3) 'Every BibTeX warning remains explicitly classified'
Assert-True (($metadata.bibliography_warning.line -join ',') -ceq '2,3,4') 'Exact indexed line numbers'
Assert-True ($metadata.bibliography_warning[0].text -ceq 'Warning--missing publisher in Berkeley1734') 'Keep complete warning context'
$multiline = Get-LogDiagnosticsFromText "prefix`nprefix`nPackage natbib Warning: Citation abc on page 1`n(natbib) undefined on input line 4."
Assert-True ($multiline.unresolved[0].line -eq 3) 'Multiline diagnostic retains starting line'
$firstLine = Get-LogDiagnosticsFromText '! Emergency stop.'
Assert-True ($firstLine.fatal[0].line -eq 1) 'No-newline log index works'

if ('Interlanguage.StandaloneTeX.V1.Guard' -as [type]) { throw 'Use a fresh pwsh process for static compilation tests.' }
Add-Type -Path $helperPath -ErrorAction Stop
$guardType = [Interlanguage.StandaloneTeX.V1.Guard]
Assert-True ($guardType::QuoteArgument('') -ceq '""') 'Empty argument quoting'
Assert-True ($guardType::QuoteArgument('a"b') -ceq '"a\"b"') 'Embedded quote escaping'
Assert-True ($guardType::QuoteArgument('C:\path with spaces\') -ceq '"C:\path with spaces\\"') 'Trailing slash doubling'
$rejected = $false
try { $guardType::QuoteArgument("a`0b") | Out-Null } catch { $rejected = $true }
Assert-True $rejected 'NUL argument rejection'

if ([Environment]::Is64BitProcess) {
    $flags = [Reflection.BindingFlags]::NonPublic
    $expectedSizes = @{ STARTUPINFO = 104; STARTUPINFOEX = 112; PROCESS_INFORMATION = 24;
        JOBOBJECT_EXTENDED_LIMIT_INFORMATION = 144; JOBOBJECT_BASIC_ACCOUNTING_INFORMATION = 48 }
    foreach ($name in $expectedSizes.Keys) {
        $abiValue = [Activator]::CreateInstance($guardType.GetNestedType($name, $flags))
        $size = [Runtime.InteropServices.Marshal]::SizeOf($abiValue)
        Assert-True ($size -eq $expectedSizes[$name]) "Windows x64 ABI size $name = $size"
    }
}
$helper = [IO.File]::ReadAllText($helperPath)
$entrypoint = [IO.File]::ReadAllText($scriptPath)
Assert-True ($helper.IndexOf('if (!AssignProcessToJobObject') -lt $helper.IndexOf('if (ResumeThread')) 'Assignment precedes resume'
Assert-True ($helper.Contains('new IntPtr(0x20002)')) 'Explicit inherited handle allowlist'
Assert-True ($helper.Contains('lastClosedUnassignedProcess')) 'Unassigned root double-close defense'
Assert-True ($helper.Contains('RetainedUnsafeSessions.Add(this)')) 'Unconfirmed cleanup retains reservation'
Assert-True ($entrypoint.Contains("'-no-shell-escape'")) 'Shell escape disabled'
Assert-True ($entrypoint.Contains("[ValidatePattern('^standalone-probe-[a-z0-9-]+\.tex$')]")) 'Probe filenames cannot escape locale directory'
Assert-True ($entrypoint.Contains("ProbeDriver is Diagnostic-only")) 'Probe cannot claim full-reader acceptance'
Assert-True ($entrypoint.Contains("generate_source_correction_overlays.py")) 'Derived source-correction verifier is pinned'
Assert-True ($entrypoint.IndexOf('$derivedPreflightOutput = @(& $pythonExecutable $derivedGeneratorPath 2>&1)') -lt $entrypoint.IndexOf('$initialInventory = @(Get-ScopedSourceInventory)')) 'Derived source-correction verification precedes source inventory and TeX'
Assert-True ($entrypoint.Contains('(Get-Sha256 $derivedGeneratorPath) -cne $receipt.derived_source_generator_sha256')) 'Derived generator remains pinned through build completion'
Assert-True (-not ($entrypoint -match '(?im)^\s*(?:&\s+(?:lua|pdf|xe)?latex|Start-Process|&\s*bibtex)')) 'No direct TeX launch bypass'
Write-Output 'PASS: PowerShell AST, actual diagnostic classifier, C# compilation, pure quoting, x64 ABI, and structural safety assertions.'
Write-Output 'No Guard constructed; no mutex acquired; no TeX/native worker/PDF launched.'
