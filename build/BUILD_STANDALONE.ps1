#requires -Version 7.0
<#
.SYNOPSIS
Builds only the standalone Persian driver under one continuous machine-wide TeX mutex.
.DESCRIPTION
Run in a fresh 64-bit pwsh process. Full mode builds twice from separate fresh output
directories and requires identical PDF hashes. Diagnostic mode is ONE LuaLaTeX pass,
no BibTeX, and never declares an accepted build. This is not publication/visual QA.
All logs and receipts are preserved under repo/tmp/pdfs/standalone/<unique run>/.
No inherited build script, PDF repair script, Git operation, or publication is invoked.
Worker termination has a 60-second drain deadline. If the kernel cannot confirm
owned-tree exit, an exceptional safety fence retains the host/mutex beyond that
deadline, polling only the same captured handles with backoff. It launches nothing
and does not release merely because time elapsed. Forced host termination cannot
preserve that mutex guarantee and is not an ordinary cancellation route.
.EXAMPLE
pwsh -NoProfile -File build/BUILD_STANDALONE.ps1 -Mode Diagnostic
.EXAMPLE
pwsh -NoProfile -File build/BUILD_STANDALONE.ps1 -Mode Full
#>
[CmdletBinding()]
param(
    [ValidateSet('Diagnostic', 'Full')][string]$Mode = 'Diagnostic',
    [ValidatePattern('^standalone-probe-[a-z0-9-]+\.tex$')][string]$ProbeDriver,
    [ValidateRange(1, 300)][int]$MutexTimeoutSeconds = 60,
    [ValidateRange(1, 7200)][int]$WorkerTimeoutSeconds = 900,
    [ValidateRange(1, 28800)][int]$TotalBuildTimeoutSeconds = 7200,
    [ValidateRange(3, 10)][int]$MaxLatexPasses = 6,
    [ValidateRange(1, 3)][int]$MaxBibtexPasses = 2,
    [ValidateRange(268435456, 8589934592)][long]$MemoryLimitBytes = 2147483648,
    [ValidateRange(1, 32)][int]$ActiveProcessLimit = 16,
    [ValidateRange(0, 2147483647)][long]$SourceDateEpoch = 1783874174
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if (-not $IsWindows -or -not [Environment]::Is64BitProcess) {
    throw 'This entrypoint requires 64-bit PowerShell 7 on Windows.'
}

$releaseRoot = [IO.Path]::GetFullPath((Split-Path -Parent $PSScriptRoot))
$sourceRoot = Join-Path $releaseRoot 'source'
$localeRoot = Join-Path $sourceRoot 'locale/fa-IR'
$driverName = 'open-logic-standalone-fa-IR.tex'
if ($ProbeDriver) {
    # Diagnostic fixtures use the SAME guarded worker/mutex and never qualify
    # as a full reader. No path separators or arbitrary outside inputs.
    if ($Mode -ne 'Diagnostic') { throw 'ProbeDriver is Diagnostic-only; it cannot produce an accepted full build.' }
    $driverName = $ProbeDriver
}
$jobName = [IO.Path]::GetFileNameWithoutExtension($driverName)
$driverPath = Join-Path $localeRoot $driverName
$helperPath = Join-Path $PSScriptRoot 'StandaloneTeXProcessGuard.cs'
$derivedGeneratorPath = Join-Path $PSScriptRoot 'generate_source_correction_overlays.py'
$sourceCorrectionCheckerPath = Join-Path $PSScriptRoot 'check_functions_source_corrections.py'
foreach ($required in @($driverPath, $helperPath, $derivedGeneratorPath, $sourceCorrectionCheckerPath)) {
    if (-not (Test-Path -LiteralPath $required -PathType Leaf)) { throw "Required input is missing: $required" }
}

# Resolve only the explicit tools, without running them for discovery/versioning.
$latexExecutable = (Get-Command 'lualatex.exe' -CommandType Application -ErrorAction Stop | Select-Object -First 1).Source
$pythonExecutable = (Get-Command 'python.exe' -CommandType Application -ErrorAction Stop | Select-Object -First 1).Source
$bibtexExecutable = if ($Mode -eq 'Full') {
    (Get-Command 'bibtex.exe' -CommandType Application -ErrorAction Stop | Select-Object -First 1).Source
} else { $null }
if ('Interlanguage.StandaloneTeX.V1.Guard' -as [type]) {
    throw 'Guard type already loaded: run this entrypoint in a fresh pwsh process to avoid stale helper code.'
}
Add-Type -Path $helperPath -ErrorAction Stop

function Get-Sha256([string]$Path) {
    (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
}

function Get-ScopedSourceInventory {
    # This is the new, small release copy only. No Git/workspace scan is performed.
    # Reparse points could escape that scope; fail before following any directory.
    $pending = [Collections.Generic.Queue[string]]::new()
    $pending.Enqueue($sourceRoot)
    $files = [Collections.Generic.List[object]]::new()
    [long]$totalBytes = 0
    $directoryCount = 0
    while ($pending.Count -gt 0) {
        $currentDirectory = $pending.Dequeue()
        $directoryCount++
        if ($directoryCount -gt 5000 -or
            ((Get-Item -LiteralPath $currentDirectory).Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw 'Source inventory refuses excessive directories or a reparse point.'
        }
        foreach ($item in Get-ChildItem -LiteralPath $currentDirectory -Force) {
            if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
                throw "Source inventory refuses a reparse point: $($item.FullName)"
            }
            if ($item.PSIsContainer) { $pending.Enqueue($item.FullName); continue }
            $totalBytes += $item.Length
            if ($files.Count -ge 5000 -or $totalBytes -gt 536870912) {
                throw 'Scoped source inventory exceeded 5,000 files or 512 MiB; no broader scan is authorized.'
            }
            $files.Add([pscustomobject]@{
                path = [IO.Path]::GetRelativePath($sourceRoot, $item.FullName).Replace('\', '/')
                bytes = $item.Length
                sha256 = Get-Sha256 $item.FullName
            })
        }
    }
    @($files | Sort-Object path)
}

function Get-InventorySignature($Inventory) {
    $text = (@($Inventory | ForEach-Object { "$($_.path)`t$($_.bytes)`t$($_.sha256)" }) -join "`n")
    [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData([Text.Encoding]::UTF8.GetBytes($text))).ToLowerInvariant()
}

function Get-BuildOutputInventory([string]$Directory) {
    $files = @(Get-ChildItem -LiteralPath $Directory -File -Force | Sort-Object Name)
    if ($files.Count -gt 200) { throw 'Build output inventory exceeded 200 files.' }
    @($files | ForEach-Object {
        if (($_.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw "Build output inventory refuses a reparse point: $($_.FullName)"
        }
        [ordered]@{
            path = $_.Name
            bytes = $_.Length
            sha256 = Get-Sha256 $_.FullName
        }
    })
}

$runId = [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfffZ') + '-' + [Guid]::NewGuid().ToString('N')
$outputBase = [IO.Path]::GetFullPath((Join-Path $releaseRoot 'tmp/pdfs/standalone'))
$runRoot = [IO.Path]::GetFullPath((Join-Path $outputBase $runId))
if (-not $runRoot.StartsWith($outputBase + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Output scope validation failed.'
}
for ($ancestor = $outputBase; $ancestor -and $ancestor.StartsWith($releaseRoot, [StringComparison]::OrdinalIgnoreCase);
    $ancestor = Split-Path -Parent $ancestor) {
    if ((Test-Path -LiteralPath $ancestor) -and
        ((Get-Item -LiteralPath $ancestor -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        throw "Output ancestry refuses a reparse point: $ancestor"
    }
}
# No customizable output path, overwrite, release staging, or cleanup.
New-Item -ItemType Directory -Path $runRoot -ErrorAction Stop | Out-Null
$receiptPath = Join-Path $runRoot 'BUILD_RECEIPT.json'
$receipt = [ordered]@{
    schema = 'interlanguage-standalone-tex-build-v1'
    mode = $Mode
    started_utc = [DateTime]::UtcNow.ToString('o')
    status = 'PREFLIGHT'
    accepted_build = $false
    publication_or_visual_qa_passed = $false
    run_root = $runRoot
    driver = $driverPath
    driver_sha256 = Get-Sha256 $driverPath
    helper_sha256 = Get-Sha256 $helperPath
    entrypoint_sha256 = Get-Sha256 $PSCommandPath
    derived_source_generator_sha256 = Get-Sha256 $derivedGeneratorPath
    source_correction_checker_sha256 = Get-Sha256 $sourceCorrectionCheckerPath
    preflight_executable_identity = [ordered]@{ path = $pythonExecutable; sha256 = Get-Sha256 $pythonExecutable }
    executable_identities = @(
        [ordered]@{ path = $latexExecutable; sha256 = Get-Sha256 $latexExecutable }
        if ($bibtexExecutable) { [ordered]@{ path = $bibtexExecutable; sha256 = Get-Sha256 $bibtexExecutable } }
    )
    limits = [ordered]@{
        mutex_acquisition_seconds = $MutexTimeoutSeconds
        per_worker_seconds = $WorkerTimeoutSeconds
        complete_session_seconds = $TotalBuildTimeoutSeconds
        maximum_latex_passes_per_build = $MaxLatexPasses
        maximum_bibtex_passes_per_build = $MaxBibtexPasses
        job_commit_memory_bytes = $MemoryLimitBytes
        active_processes_in_owned_tree = $ActiveProcessLimit
        cleanup_deadline_seconds = 60
        unconfirmed_exit_policy = 'Retain host/job/mutex and observe same handles with 5-to-30-second backoff; never timeout-release'
        memory_semantics = 'Windows Job Object aggregate committed memory; NOT working set or GPU memory'
    }
    deterministic_environment = [ordered]@{
        SOURCE_DATE_EPOCH = "$SourceDateEpoch"
        FORCE_SOURCE_DATE = '1'
        TZ = 'UTC'
        max_print_line = '1000'
        openin_any = 'a'
        openout_any = 'p'
        shell_escape = '0'
    }
    mutex = [ordered]@{
        name = 'Global\InterlanguageTeXSlotV1'
        acquired = $false
        abandoned_recovery = $false
        released_after_confirmed_tree_exit = $false
    }
    events = [Collections.Generic.List[object]]::new()
    builds = [Collections.Generic.List[object]]::new()
    observed_peak_job_commit_bytes = 0
}

function Save-Receipt {
    # Receipt contains only this task's identities/settings; never dump inherited environment.
    $json = $receipt | ConvertTo-Json -Depth 18
    $next = $receiptPath + '.next'
    [IO.File]::WriteAllText($next, $json + "`n", [Text.UTF8Encoding]::new($false))
    [IO.File]::Move($next, $receiptPath, $true)
}

function Add-Event([string]$Kind, $Details) {
    $receipt.events.Add([ordered]@{ utc = [DateTime]::UtcNow.ToString('o'); kind = $Kind; details = $Details })
    Save-Receipt
}

function Assert-TimeRemaining {
    $remaining = $TotalBuildTimeoutSeconds - $buildTimer.Elapsed.TotalSeconds
    if ($remaining -lt 1) { throw 'The complete guarded build/replay wall-clock budget expired.' }
    [int][Math]::Max(1, [Math]::Min($WorkerTimeoutSeconds, [Math]::Floor($remaining)))
}

function Get-LogDiagnostics([string]$Path) {
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) { throw "Expected log is missing: $Path" }
    Get-LogDiagnosticsFromText ([IO.File]::ReadAllText($Path))
}

function Get-LogDiagnosticsFromText([string]$logText) {
    $patterns = [ordered]@{
        fatal = '(?im)^!|Emergency stop|Fatal error|Missing character:|TeX capacity exceeded|Runaway argument'
        duplicate = '(?im)multiply[- ]defined|multiply defined|destination with the same identifier|duplicate.*(?:destination|label)|duplicate ignored'
        unresolved = '(?im)There were undefined (?:references|citations)|(?:Citation|Reference)[^\r\n]*(?:\r?\n[^\r\n]*)?undefined|I couldn.t open database file|I didn.t find a database entry'
        bibliography_warning = '(?im)^Warning--[^\r\n]*'
        rerun = '(?im)Label\(s\) may have changed|Rerun to get|rerunfilecheck[^\r\n]*(?:\r?\n[^\r\n]*)?has changed|Please \(re\)run (?:LaTeX|BibTeX|Biber)'
    }
    $result = [ordered]@{}
    # Index newlines once. Recounting the entire prefix for every first-pass
    # unresolved reference was quadratic on this 722-unit reader's large log.
    [int[]]$newlineOffsets = @([regex]::Matches($logText, "`n") | ForEach-Object Index)
    foreach ($kind in $patterns.Keys) {
        $result[$kind] = @([regex]::Matches($logText, $patterns[$kind]) | ForEach-Object {
            $lo = 0
            $hi = $newlineOffsets.Length
            while ($lo -lt $hi) {
                $mid = ($lo + $hi) -shr 1
                if ($newlineOffsets[$mid] -lt $_.Index) { $lo = $mid + 1 }
                else { $hi = $mid }
            }
            [ordered]@{
                line = 1 + $lo
                text = $_.Value
            }
        })
    }
    $result
}

function Get-AuxState([string]$Directory) {
    $extensions = @('.aux', '.toc', '.out', '.bbl', '.thm', '.prb', '.pcr')
    $state = @(Get-ChildItem -LiteralPath $Directory -File | Where-Object Extension -In $extensions |
        Sort-Object Name | ForEach-Object { [pscustomobject]@{ path = $_.Name; bytes = $_.Length; sha256 = Get-Sha256 $_.FullName } })
    Get-InventorySignature $state
}

function Invoke-OwnedWorker([string]$Label, [string]$Executable, [string[]]$Arguments,
    [string]$Directory, [hashtable]$Environment) {
    $timeout = Assert-TimeRemaining
    Add-Event 'worker_start' ([ordered]@{ label = $Label; executable = $Executable; arguments = $Arguments; timeout_seconds = $timeout })
    $result = $guard.Run($Executable, $Arguments, $localeRoot,
        (Join-Path $Directory "$Label.stdout.log"), (Join-Path $Directory "$Label.stderr.log"), $Environment, $timeout)
    $receipt.observed_peak_job_commit_bytes = $guard.PeakJobCommitBytes
    Add-Event 'worker_tree_exit' ([ordered]@{ label = $Label; result = $result })
    if ($result.ExitCode -ne 0) { throw "$Label exited with code $($result.ExitCode); captured tree is drained, logs preserved." }
}

function Invoke-Build([string]$Name, [switch]$OnePass) {
    $directory = Join-Path $runRoot $Name
    New-Item -ItemType Directory -Path $directory -ErrorAction Stop | Out-Null
    $effectiveDeterministicEnvironment = [ordered]@{}
    foreach ($entry in $receipt.deterministic_environment.GetEnumerator()) {
        $effectiveDeterministicEnvironment[$entry.Key] = [string]$entry.Value
    }
    # Fixed, explicit search roots; a trailing separator retains TeX distribution defaults.
    # Do not inherit task-specific TEXINPUTS/BIBINPUTS/BSTINPUTS from an unrelated session.
    $effectiveDeterministicEnvironment.TEXINPUTS = "$directory;$localeRoot;"
    $effectiveDeterministicEnvironment.BIBINPUTS = "$localeRoot;$(Join-Path $sourceRoot 'bib');"
    $effectiveDeterministicEnvironment.BSTINPUTS = "$localeRoot;$(Join-Path $sourceRoot 'bib');"
    $effectiveDeterministicEnvironment.TEXMFOUTPUT = $directory
    $effectiveDeterministicEnvironment.TEXMF_OUTPUT_DIRECTORY = $directory
    $environment = @{}
    foreach ($entry in $effectiveDeterministicEnvironment.GetEnumerator()) {
        $environment[$entry.Key] = [string]$entry.Value
    }
    $arguments = [string[]]@('-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error',
        '-file-line-error', '-recorder', '-synctex=0', "-jobname=$jobName", "-output-directory=$directory", $driverName)
    $build = [ordered]@{
        name = $Name
        directory = $directory
        accepted = $false
        effective_deterministic_environment = $effectiveDeterministicEnvironment
        passes = [Collections.Generic.List[object]]::new()
    }
    $receipt.builds.Add($build)
    Save-Receipt
    $previousAuxState = $null
    $previousBibInput = $null
    $bibtexPasses = 0
    $converged = $false
    $passLimit = if ($OnePass) { 1 } else { $MaxLatexPasses }
    for ($pass = 1; $pass -le $passLimit; $pass++) {
        $label = '{0}-latex-{1:D2}' -f $Name, $pass
        Invoke-OwnedWorker $label $latexExecutable $arguments $directory $environment
        $texLog = Join-Path $directory "$jobName.log"
        $snapshot = Join-Path $directory "$label.tex.log"
        Copy-Item -LiteralPath $texLog -Destination $snapshot -ErrorAction Stop
        $diagnostics = Get-LogDiagnostics $snapshot
        $build.passes.Add([ordered]@{ pass = $pass; log = $snapshot; log_sha256 = Get-Sha256 $snapshot; diagnostics = $diagnostics })
        Add-Event 'immediate_log_check' ([ordered]@{ label = $label; diagnostics = $diagnostics })
        if ($diagnostics.fatal.Count -gt 0 -or $diagnostics.duplicate.Count -gt 0) {
            throw "$label has fatal/glyph/duplicate diagnostics; see receipt and preserved log."
        }
        if ($OnePass) { break }
        if (Test-Path -LiteralPath (Join-Path $directory "$jobName.bcf")) {
            throw 'Unexpected Biber input: this bounded driver contract supports BibTeX only.'
        }
        $auxPath = Join-Path $directory "$jobName.aux"
        if (-not (Test-Path -LiteralPath $auxPath -PathType Leaf)) { throw "Expected auxiliary file missing: $auxPath" }
        $auxText = [IO.File]::ReadAllText($auxPath)
        $bibInput = (@([regex]::Matches($auxText, '(?m)^\\(?:citation|bibdata|bibstyle)\{[^\r\n]*') | ForEach-Object Value) -join "`n")
        $ranBibtex = $false
        if ($auxText -match '\\bibdata\{' -and $bibInput -cne $previousBibInput) {
            if ($bibtexPasses -ge $MaxBibtexPasses) { throw 'Bibliography inputs did not stabilize within the BibTeX pass cap.' }
            $bibtexPasses++
            $bibLabel = '{0}-bibtex-{1:D2}' -f $Name, $bibtexPasses
            Invoke-OwnedWorker $bibLabel $bibtexExecutable ([string[]]@((Join-Path $directory $jobName))) $directory $environment
            $bibLog = Join-Path $directory "$jobName.blg"
            $bibSnapshot = Join-Path $directory "$bibLabel.blg"
            Copy-Item -LiteralPath $bibLog -Destination $bibSnapshot -ErrorAction Stop
            $bibDiagnostics = Get-LogDiagnostics $bibSnapshot
            Add-Event 'immediate_bibliography_check' ([ordered]@{ label = $bibLabel; log = $bibSnapshot; diagnostics = $bibDiagnostics })
            if ($bibDiagnostics.fatal.Count -gt 0 -or $bibDiagnostics.duplicate.Count -gt 0 -or
                $bibDiagnostics.unresolved.Count -gt 0 -or $bibDiagnostics.bibliography_warning.Count -gt 0) {
                throw "$bibLabel has unresolved/fatal/duplicate/bibliography-warning diagnostics."
            }
            $previousBibInput = $bibInput
            $ranBibtex = $true
        }
        $currentAuxState = Get-AuxState $directory
        if ($pass -ge 3 -and -not $ranBibtex -and $currentAuxState -ceq $previousAuxState -and
            $diagnostics.unresolved.Count -eq 0 -and $diagnostics.rerun.Count -eq 0) {
            $converged = $true
            break
        }
        $previousAuxState = $currentAuxState
    }
    if (-not $OnePass -and -not $converged) {
        throw "Build $Name failed reference/citation/auxiliary convergence within $MaxLatexPasses LuaLaTeX passes."
    }
    $pdfPath = Join-Path $directory "$jobName.pdf"
    if (-not (Test-Path -LiteralPath $pdfPath -PathType Leaf) -or (Get-Item -LiteralPath $pdfPath).Length -le 1024) {
        throw "Expected nonempty PDF missing: $pdfPath"
    }
    $stream = [IO.File]::OpenRead($pdfPath)
    try { $header = [byte[]]::new(5); if ($stream.Read($header, 0, 5) -ne 5 -or [Text.Encoding]::ASCII.GetString($header) -cne '%PDF-') { throw 'Output lacks a PDF header.' } }
    finally { $stream.Dispose() }
    $flsPath = Join-Path $directory "$jobName.fls"
    if (-not (Test-Path -LiteralPath $flsPath -PathType Leaf)) { throw 'Recorder output is missing.' }
    $build['pdf'] = [ordered]@{ path = $pdfPath; bytes = (Get-Item -LiteralPath $pdfPath).Length; sha256 = Get-Sha256 $pdfPath }
    $build['fls'] = [ordered]@{ path = $flsPath; sha256 = Get-Sha256 $flsPath }
    $build['output_inventory'] = Get-BuildOutputInventory $directory
    $build['accepted'] = [bool]$converged
    Save-Receipt
    $build
}

$guard = $null
$buildTimer = [Diagnostics.Stopwatch]::new()
$failure = $null
$verificationPassed = $false
Save-Receipt
try {
    $derivedPreflightOutput = @(& $pythonExecutable $derivedGeneratorPath 2>&1)
    $derivedPreflightExitCode = $LASTEXITCODE
    if ($derivedPreflightExitCode -ne 0) {
        throw "Derived source-correction preflight failed with code ${derivedPreflightExitCode}: $($derivedPreflightOutput -join ' ')"
    }
    $receipt['derived_source_preflight'] = [ordered]@{
        status = 'PASS'
        output = $derivedPreflightOutput -join "`n"
        generator = $derivedGeneratorPath
        generator_sha256 = Get-Sha256 $derivedGeneratorPath
        source_correction_checker_sha256 = Get-Sha256 $sourceCorrectionCheckerPath
    }
    Save-Receipt
    $initialInventory = @(Get-ScopedSourceInventory)
    $sourceSignature = Get-InventorySignature $initialInventory
    $manifestPath = Join-Path $runRoot 'SOURCE_INPUTS_BEFORE.json'
    [IO.File]::WriteAllText($manifestPath, ($initialInventory | ConvertTo-Json -Depth 5) + "`n", [Text.UTF8Encoding]::new($false))
    $receipt['source_inventory'] = [ordered]@{ path = $manifestPath; files = $initialInventory.Count; signature = $sourceSignature; sha256 = Get-Sha256 $manifestPath }
    Save-Receipt
    $guard = [Interlanguage.StandaloneTeX.V1.Guard]::new($MutexTimeoutSeconds, [ulong]$MemoryLimitBytes, [uint32]$ActiveProcessLimit)
    $receipt.mutex.acquired = $true
    $receipt.mutex.abandoned_recovery = $guard.AbandonedMutexRecovered
    $receipt.status = 'MUTEX_ACQUIRED'
    # Mandatory durable receipt BEFORE acknowledgement or any worker launch.
    Add-Event 'mutex_acquired' ([ordered]@{ abandoned_recovery = $guard.AbandonedMutexRecovered })
    $guard.AcknowledgePersistedMutexReceipt()
    $buildTimer.Start()
    $first = Invoke-Build 'primary' -OnePass:($Mode -eq 'Diagnostic')
    if ($Mode -eq 'Full') {
        $replay = Invoke-Build 'replay'
        if ($first.pdf.sha256 -cne $replay.pdf.sha256 -or $first.pdf.bytes -ne $replay.pdf.bytes) {
            throw 'Deterministic replay PDF byte/hash mismatch; both outputs retained.'
        }
        Add-Event 'deterministic_replay_match' $first.pdf
    }
    Assert-TimeRemaining | Out-Null
    $finalInventory = @(Get-ScopedSourceInventory)
    if ((Get-InventorySignature $finalInventory) -cne $sourceSignature) {
        throw 'Scoped source inputs changed during the build/replay; output is not accepted.'
    }
    if ((Get-Sha256 $helperPath) -cne $receipt.helper_sha256 -or
        (Get-Sha256 $PSCommandPath) -cne $receipt.entrypoint_sha256 -or
        (Get-Sha256 $derivedGeneratorPath) -cne $receipt.derived_source_generator_sha256 -or
        (Get-Sha256 $sourceCorrectionCheckerPath) -cne $receipt.source_correction_checker_sha256) {
        throw 'Build infrastructure changed while running; output is not accepted.'
    }
    Assert-TimeRemaining | Out-Null
    Add-Event 'source_and_infrastructure_unchanged' ([ordered]@{ source_signature = $sourceSignature })
    $verificationPassed = $true
    $receipt.status = 'VERIFICATION_COMPLETE_NOT_YET_RELEASED'
    Save-Receipt
}
catch {
    $failure = $_
    $receipt.status = 'FAILED'
    $receipt.accepted_build = $false
    $receipt['failure'] = $_.Exception.ToString()
    Save-Receipt
}
finally {
    if ($guard) {
        try {
            # The same mutex stays owned through all worker trees, log checks, hashes,
            # reproducibility checks, and source checks, including exception paths.
            $guard.ShutdownAndRelease()
            $receipt.observed_peak_job_commit_bytes = $guard.PeakJobCommitBytes
            $receipt.mutex.released_after_confirmed_tree_exit = $guard.Released
            if ($verificationPassed -and -not $failure -and $guard.Released) {
                $receipt.status = if ($Mode -eq 'Diagnostic') { 'DIAGNOSTIC_ONLY_NOT_ACCEPTED' } else { 'BUILD_AND_REPLAY_PASS_NOT_PUBLICATION_QA' }
                $receipt.accepted_build = ($Mode -eq 'Full')
            }
        }
        catch {
            $failure = $_
            $receipt.status = 'UNCONFIRMED_OWNED_TREE_EXIT_MUTEX_RETAINED'
            $receipt.accepted_build = $false
            $receipt['cleanup_failure'] = $_.Exception.ToString()
            # A fresh pwsh -File host must NOT exit and abandon the mutex while its
            # child tree is unconfirmed. This exceptional fence launches no work and
            # only observes the existing owned handles; it never repeats termination.
            Save-Receipt
            $fenceDelay = 5
            while (-not $guard.Released) {
                Start-Sleep -Seconds $fenceDelay
                try {
                    if ($guard.TryReleaseAfterConfirmedExit()) {
                        $receipt.mutex.released_after_confirmed_tree_exit = $true
                        $receipt.status = 'FAILED_BUT_DELAYED_OWNED_TREE_EXIT_CONFIRMED'
                        break
                    }
                }
                catch {
                    $receipt['safety_fence_last_observation_error'] = $_.Exception.Message
                }
                $fenceDelay = [Math]::Min(30, $fenceDelay * 2)
            }
        }
    }
    $receipt['finished_utc'] = [DateTime]::UtcNow.ToString('o')
    $receipt['elapsed_guarded_seconds'] = $buildTimer.Elapsed.TotalSeconds
    Save-Receipt
}

Write-Output "Build status: $($receipt.status)"
Write-Output "Preserved receipt: $receiptPath"
if ($failure) { throw $failure }
if ($Mode -eq 'Diagnostic') {
    Write-Output 'Diagnostic only: unresolved-reference/citation/rerun findings are recorded; this is NOT an accepted build.'
}
