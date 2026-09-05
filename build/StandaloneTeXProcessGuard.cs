// Only BUILD_STANDALONE.ps1 uses this helper. Loading/compiling it starts no process.
using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.IO;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;

namespace Interlanguage.StandaloneTeX.V1
{
    public sealed class WorkerResult
    {
        public int ProcessId { get; set; }
        public uint ExitCode { get; set; }
        public double ElapsedSeconds { get; set; }
        public ulong PeakJobCommitBytes { get; set; }
    }

    // One instance reserves the slot continuously, including between workers.
    public sealed class Guard
    {
        public const string MutexName = @"Global\InterlanguageTeXSlotV1";
        private static readonly List<Guard> RetainedUnsafeSessions = new List<Guard>();
        private readonly int ownerThread;
        private Mutex mutex;
        private IntPtr job;
        private IntPtr suspendedUnassignedProcess;
        private IntPtr lastClosedUnassignedProcess;
        private bool acquired;
        private bool receiptAcknowledged;
        private bool released;
        private bool retained;
        public bool AbandonedMutexRecovered { get; private set; }
        public bool Released { get { return released; } }
        public ulong PeakJobCommitBytes { get; private set; }

        public Guard(int mutexTimeoutSeconds, ulong memoryLimitBytes, uint activeProcessLimit)
        {
            if (Environment.OSVersion.Platform != PlatformID.Win32NT)
                throw new PlatformNotSupportedException("This guard requires Windows.");
            if (mutexTimeoutSeconds < 1 || mutexTimeoutSeconds > 300)
                throw new ArgumentOutOfRangeException("mutexTimeoutSeconds");
            if (memoryLimitBytes < 268435456UL || memoryLimitBytes > 8589934592UL)
                throw new ArgumentOutOfRangeException("memoryLimitBytes");
            if (activeProcessLimit < 1 || activeProcessLimit > 32)
                throw new ArgumentOutOfRangeException("activeProcessLimit");
            ownerThread = Thread.CurrentThread.ManagedThreadId;
            mutex = new Mutex(false, MutexName);
            try
            {
                try { acquired = mutex.WaitOne(TimeSpan.FromSeconds(mutexTimeoutSeconds)); }
                catch (AbandonedMutexException) { acquired = true; AbandonedMutexRecovered = true; }
                if (!acquired) throw new TimeoutException("Machine-wide TeX mutex acquisition timed out; no worker launched.");
                job = CreateJobObject(IntPtr.Zero, null);
                if (job == IntPtr.Zero) throw Win32("CreateJobObject");
                var limits = new JOBOBJECT_EXTENDED_LIMIT_INFORMATION();
                // No BREAKAWAY_OK or SILENT_BREAKAWAY_OK: all descendants remain captured.
                limits.BasicLimitInformation.LimitFlags = 0x2000 | 0x200 | 0x8 | 0x400;
                limits.BasicLimitInformation.ActiveProcessLimit = activeProcessLimit;
                limits.JobMemoryLimit = new UIntPtr(memoryLimitBytes);
                if (!SetInformationJobObject(job, 9, ref limits,
                    (uint)Marshal.SizeOf(typeof(JOBOBJECT_EXTENDED_LIMIT_INFORMATION))))
                    throw Win32("SetInformationJobObject");
            }
            catch
            {
                // Constructor has not started any child, so releasing here is safe.
                if (job != IntPtr.Zero) { CloseHandle(job); job = IntPtr.Zero; }
                if (acquired) { mutex.ReleaseMutex(); acquired = false; }
                mutex.Dispose(); mutex = null;
                throw;
            }
        }

        public void AcknowledgePersistedMutexReceipt()
        {
            CheckThread();
            receiptAcknowledged = true;
        }

        public static string QuoteArgument(string argument)
        {
            if (argument == null || argument.IndexOf('\0') >= 0)
                throw new ArgumentException("Null/NUL command argument is prohibited.");
            var b = new StringBuilder("\"");
            int slashes = 0;
            foreach (char c in argument)
            {
                if (c == '\\') { slashes++; continue; }
                if (c == '"') { b.Append('\\', slashes * 2 + 1); b.Append(c); }
                else { b.Append('\\', slashes); b.Append(c); }
                slashes = 0;
            }
            b.Append('\\', slashes * 2); b.Append('"');
            return b.ToString();
        }

        public WorkerResult Run(string executable, string[] arguments, string workingDirectory,
            string stdoutPath, string stderrPath, IDictionary environmentOverrides, int timeoutSeconds)
        {
            CheckThread();
            if (!receiptAcknowledged)
                throw new InvalidOperationException("Persist mutex acquisition/recovery before acknowledging or launching.");
            if (timeoutSeconds < 1 || timeoutSeconds > 7200)
                throw new ArgumentOutOfRangeException("timeoutSeconds");
            if (!Path.IsPathRooted(executable) || !File.Exists(executable) ||
                !Path.IsPathRooted(workingDirectory) || !Directory.Exists(workingDirectory))
                throw new ArgumentException("An existing absolute executable and working directory are required.");
            if (ActiveProcesses() != 0 || suspendedUnassignedProcess != IntPtr.Zero)
                throw new InvalidOperationException("An earlier owned worker is not fully drained.");

            IntPtr outHandle = IntPtr.Zero, errHandle = IntPtr.Zero, inHandle = IntPtr.Zero;
            IntPtr attributeList = IntPtr.Zero, inheritedHandles = IntPtr.Zero, environment = IntPtr.Zero;
            bool attributesInitialized = false;
            PROCESS_INFORMATION process = new PROCESS_INFORMATION();
            var timer = Stopwatch.StartNew();
            try
            {
                var security = new SECURITY_ATTRIBUTES();
                security.nLength = Marshal.SizeOf(typeof(SECURITY_ATTRIBUTES));
                security.bInheritHandle = true;
                // CREATE_NEW preserves existing logs and refuses accidental reuse.
                outHandle = CreateFile(stdoutPath, 0x40000000, 1, ref security, 1, 0x80, IntPtr.Zero);
                if (outHandle == new IntPtr(-1)) throw Win32("Create stdout log");
                errHandle = CreateFile(stderrPath, 0x40000000, 1, ref security, 1, 0x80, IntPtr.Zero);
                if (errHandle == new IntPtr(-1)) throw Win32("Create stderr log");
                inHandle = CreateFile("NUL", 0x80000000, 3, ref security, 3, 0x80, IntPtr.Zero);
                if (inHandle == new IntPtr(-1)) throw Win32("Open noninteractive stdin");

                IntPtr attributeBytes = IntPtr.Zero;
                InitializeProcThreadAttributeList(IntPtr.Zero, 1, 0, ref attributeBytes);
                if (attributeBytes == IntPtr.Zero) throw Win32("Size process attribute list");
                attributeList = Marshal.AllocHGlobal(attributeBytes);
                if (!InitializeProcThreadAttributeList(attributeList, 1, 0, ref attributeBytes))
                    throw Win32("Initialize process attribute list");
                attributesInitialized = true;
                inheritedHandles = Marshal.AllocHGlobal(3 * IntPtr.Size);
                Marshal.WriteIntPtr(inheritedHandles, 0, inHandle);
                Marshal.WriteIntPtr(inheritedHandles, IntPtr.Size, outHandle);
                Marshal.WriteIntPtr(inheritedHandles, 2 * IntPtr.Size, errHandle);
                // Explicit handle allowlist: no unrelated inheritable parent handles leak.
                if (!UpdateProcThreadAttribute(attributeList, 0, new IntPtr(0x20002), inheritedHandles,
                    new IntPtr(3 * IntPtr.Size), IntPtr.Zero, IntPtr.Zero))
                    throw Win32("Set inherited handle allowlist");

                var start = new STARTUPINFOEX();
                start.StartupInfo.cb = Marshal.SizeOf(typeof(STARTUPINFOEX));
                start.StartupInfo.dwFlags = 0x100;
                start.StartupInfo.hStdInput = inHandle;
                start.StartupInfo.hStdOutput = outHandle;
                start.StartupInfo.hStdError = errHandle;
                start.lpAttributeList = attributeList;
                var command = new StringBuilder(QuoteArgument(executable));
                foreach (string arg in arguments) { command.Append(' '); command.Append(QuoteArgument(arg)); }
                environment = Marshal.StringToHGlobalUni(BuildEnvironment(environmentOverrides));
                // CREATE_SUSPENDED | CREATE_UNICODE_ENVIRONMENT | EXTENDED_STARTUPINFO_PRESENT | CREATE_NO_WINDOW.
                if (!CreateProcess(executable, command, IntPtr.Zero, IntPtr.Zero, true,
                    0x4 | 0x400 | 0x80000 | 0x08000000, environment, workingDirectory, ref start, out process))
                    throw Win32("Create suspended process");
                suspendedUnassignedProcess = process.hProcess;
                if (!AssignProcessToJobObject(job, process.hProcess))
                    throw Win32("Assign suspended worker to job (worker has not executed)");
                suspendedUnassignedProcess = IntPtr.Zero;
                if (ResumeThread(process.hThread) == UInt32.MaxValue)
                    throw Win32("Resume assigned worker");
                while (ActiveProcesses() != 0)
                {
                    RefreshPeak();
                    if (timer.Elapsed.TotalSeconds >= timeoutSeconds)
                        throw new TimeoutException("Captured worker tree exceeded its wall-clock deadline.");
                    Thread.Sleep(100);
                }
                RefreshPeak();
                uint code;
                if (!GetExitCodeProcess(process.hProcess, out code)) throw Win32("Read worker exit code");
                if (code == 259) throw new InvalidOperationException("Job empty but root process still active; fail closed.");
                return new WorkerResult { ProcessId = (int)process.dwProcessId, ExitCode = code,
                    ElapsedSeconds = timer.Elapsed.TotalSeconds, PeakJobCommitBytes = PeakJobCommitBytes };
            }
            catch (Exception original)
            {
                try { CancelAndDrain(60); }
                catch (Exception cleanup)
                {
                    Retain();
                    throw new InvalidOperationException(
                        "Owned tree exit could not be confirmed; mutex/job retained, not released. Do not launch another build.",
                        new AggregateException(original, cleanup));
                }
                throw;
            }
            finally
            {
                if (process.hThread != IntPtr.Zero) CloseHandle(process.hThread);
                if (process.hProcess != IntPtr.Zero && process.hProcess != suspendedUnassignedProcess &&
                    process.hProcess != lastClosedUnassignedProcess)
                    CloseHandle(process.hProcess);
                if (process.hProcess == lastClosedUnassignedProcess) lastClosedUnassignedProcess = IntPtr.Zero;
                if (attributesInitialized) DeleteProcThreadAttributeList(attributeList);
                if (attributeList != IntPtr.Zero) Marshal.FreeHGlobal(attributeList);
                if (inheritedHandles != IntPtr.Zero) Marshal.FreeHGlobal(inheritedHandles);
                if (environment != IntPtr.Zero) Marshal.FreeHGlobal(environment);
                CloseValid(inHandle); CloseValid(outHandle); CloseValid(errHandle);
            }
        }

        public void ShutdownAndRelease()
        {
            CheckThread();
            try
            {
                CancelAndDrain(60);
                RefreshPeak();
                if (!TryReleaseAfterConfirmedExit())
                    throw new InvalidOperationException("Refusing to release with an owned process alive.");
            }
            catch { Retain(); throw; }
        }

        // Exceptional safety-fence observation only: no launch, retry of termination,
        // worker replacement, process enumeration, or timeout-based release.
        public bool TryReleaseAfterConfirmedExit()
        {
            CheckThread();
            if (suspendedUnassignedProcess != IntPtr.Zero)
            {
                uint wait = WaitForSingleObject(suspendedUnassignedProcess, 0);
                if (wait == 258) return false;
                if (wait != 0) throw Win32("Observe suspended root exit in safety fence");
                CloseHandle(suspendedUnassignedProcess); suspendedUnassignedProcess = IntPtr.Zero;
            }
            if (ActiveProcesses() != 0) return false;
            if (!CloseHandle(job)) throw Win32("Close confirmed-empty job");
            job = IntPtr.Zero;
            mutex.ReleaseMutex(); acquired = false; released = true;
            mutex.Dispose(); mutex = null;
            return true;
        }

        private void CancelAndDrain(int seconds)
        {
            CheckThread();
            var deadline = Stopwatch.StartNew();
            if (suspendedUnassignedProcess != IntPtr.Zero)
            {
                // Only a root created by this instance, still suspended, can enter this path.
                if (!TerminateProcess(suspendedUnassignedProcess, 0xEE01)) throw Win32("Terminate unassigned suspended root");
                if (WaitForSingleObject(suspendedUnassignedProcess, (uint)(seconds * 1000)) != 0)
                    throw new TimeoutException("Unassigned suspended root did not exit in cleanup deadline.");
                lastClosedUnassignedProcess = suspendedUnassignedProcess;
                CloseHandle(suspendedUnassignedProcess); suspendedUnassignedProcess = IntPtr.Zero;
            }
            // One termination request only; never enumerate or touch foreign processes.
            // Do not require an accounting query to succeed before issuing the kill:
            // an observation failure must still stop this exact captured job.
            if (!TerminateJobObject(job, 0xEE02))
                throw Win32("Terminate captured job");
            while (ActiveProcesses() != 0)
            {
                if (deadline.Elapsed.TotalSeconds >= seconds)
                    throw new TimeoutException("Captured job did not drain in cleanup deadline.");
                Thread.Sleep(100);
            }
        }

        private uint ActiveProcesses()
        {
            var accounting = new JOBOBJECT_BASIC_ACCOUNTING_INFORMATION();
            if (!QueryAccounting(job, 1, out accounting,
                (uint)Marshal.SizeOf(typeof(JOBOBJECT_BASIC_ACCOUNTING_INFORMATION)), IntPtr.Zero))
                throw Win32("Query captured job accounting");
            return accounting.ActiveProcesses;
        }

        private void RefreshPeak()
        {
            var info = new JOBOBJECT_EXTENDED_LIMIT_INFORMATION();
            if (!QueryLimits(job, 9, out info,
                (uint)Marshal.SizeOf(typeof(JOBOBJECT_EXTENDED_LIMIT_INFORMATION)), IntPtr.Zero))
                throw Win32("Query captured job peak memory");
            PeakJobCommitBytes = Math.Max(PeakJobCommitBytes, info.PeakJobMemoryUsed.ToUInt64());
        }

        private void CheckThread()
        {
            if (Thread.CurrentThread.ManagedThreadId != ownerThread)
                throw new InvalidOperationException("Use the guard synchronously on its mutex-owning thread.");
            if (released || !acquired || job == IntPtr.Zero)
                throw new InvalidOperationException("Guard is not an active reserved session.");
        }

        private void Retain()
        {
            if (!retained) { lock (RetainedUnsafeSessions) RetainedUnsafeSessions.Add(this); retained = true; }
            // No finalizer releases this reservation on an unverified cleanup path.
        }

        private static string BuildEnvironment(IDictionary overrides)
        {
            var values = new SortedDictionary<string, string>(StringComparer.OrdinalIgnoreCase);
            foreach (DictionaryEntry item in Environment.GetEnvironmentVariables())
                values[item.Key.ToString()] = item.Value.ToString();
            foreach (DictionaryEntry item in overrides)
            {
                // PowerShell may wrap a string in PSObject at the IDictionary
                // boundary. ToString preserves that string without requiring
                // a reference to PowerShell's assembly or dumping environment.
                if (item.Key == null || item.Value == null)
                    throw new ArgumentException("Null environment override.");
                string key = item.Key.ToString();
                string value = item.Value.ToString();
                if (key.IndexOf('\0') >= 0 || key.IndexOf('=') >= 0 || value.IndexOf('\0') >= 0)
                    throw new ArgumentException("Invalid environment override.");
                values[key] = value;
            }
            var b = new StringBuilder();
            foreach (var pair in values) b.Append(pair.Key).Append('=').Append(pair.Value).Append('\0');
            return b.Append('\0').ToString();
        }

        private static Exception Win32(string operation) { return new Win32Exception(Marshal.GetLastWin32Error(), operation); }
        private static void CloseValid(IntPtr handle)
        { if (handle != IntPtr.Zero && handle != new IntPtr(-1)) CloseHandle(handle); }

        [StructLayout(LayoutKind.Sequential)] private struct SECURITY_ATTRIBUTES
        { public int nLength; public IntPtr lpSecurityDescriptor; [MarshalAs(UnmanagedType.Bool)] public bool bInheritHandle; }
        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)] private struct STARTUPINFO
        {
            public int cb; public string lpReserved, lpDesktop, lpTitle;
            public uint dwX, dwY, dwXSize, dwYSize, dwXCountChars, dwYCountChars, dwFillAttribute, dwFlags;
            public ushort wShowWindow, cbReserved2;
            public IntPtr lpReserved2, hStdInput, hStdOutput, hStdError;
        }
        [StructLayout(LayoutKind.Sequential)] private struct STARTUPINFOEX
        { public STARTUPINFO StartupInfo; public IntPtr lpAttributeList; }
        [StructLayout(LayoutKind.Sequential)] private struct PROCESS_INFORMATION
        { public IntPtr hProcess, hThread; public uint dwProcessId, dwThreadId; }
        [StructLayout(LayoutKind.Sequential)] private struct JOBOBJECT_BASIC_LIMIT_INFORMATION
        {
            public long PerProcessUserTimeLimit, PerJobUserTimeLimit;
            public uint LimitFlags;
            public UIntPtr MinimumWorkingSetSize, MaximumWorkingSetSize;
            public uint ActiveProcessLimit;
            public UIntPtr Affinity;
            public uint PriorityClass, SchedulingClass;
        }
        [StructLayout(LayoutKind.Sequential)] private struct IO_COUNTERS
        { public ulong ReadOperationCount, WriteOperationCount, OtherOperationCount, ReadTransferCount, WriteTransferCount, OtherTransferCount; }
        [StructLayout(LayoutKind.Sequential)] private struct JOBOBJECT_EXTENDED_LIMIT_INFORMATION
        {
            public JOBOBJECT_BASIC_LIMIT_INFORMATION BasicLimitInformation;
            public IO_COUNTERS IoInfo;
            public UIntPtr ProcessMemoryLimit, JobMemoryLimit, PeakProcessMemoryUsed, PeakJobMemoryUsed;
        }
        [StructLayout(LayoutKind.Sequential)] private struct JOBOBJECT_BASIC_ACCOUNTING_INFORMATION
        {
            public long TotalUserTime, TotalKernelTime, ThisPeriodTotalUserTime, ThisPeriodTotalKernelTime;
            public uint TotalPageFaultCount, TotalProcesses, ActiveProcesses, TotalTerminatedProcesses;
        }

        [DllImport("kernel32.dll", SetLastError = true, CharSet = CharSet.Unicode)] private static extern IntPtr CreateJobObject(IntPtr attributes, string name);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool SetInformationJobObject(IntPtr job, int infoClass, ref JOBOBJECT_EXTENDED_LIMIT_INFORMATION info, uint size);
        [DllImport("kernel32.dll", EntryPoint = "QueryInformationJobObject", SetLastError = true)] private static extern bool QueryAccounting(IntPtr job, int infoClass, out JOBOBJECT_BASIC_ACCOUNTING_INFORMATION info, uint size, IntPtr returned);
        [DllImport("kernel32.dll", EntryPoint = "QueryInformationJobObject", SetLastError = true)] private static extern bool QueryLimits(IntPtr job, int infoClass, out JOBOBJECT_EXTENDED_LIMIT_INFORMATION info, uint size, IntPtr returned);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool AssignProcessToJobObject(IntPtr job, IntPtr process);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool TerminateJobObject(IntPtr job, uint exitCode);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool TerminateProcess(IntPtr process, uint exitCode);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern uint ResumeThread(IntPtr thread);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool GetExitCodeProcess(IntPtr process, out uint code);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern uint WaitForSingleObject(IntPtr handle, uint milliseconds);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool CloseHandle(IntPtr handle);
        [DllImport("kernel32.dll", SetLastError = true, CharSet = CharSet.Unicode)] private static extern IntPtr CreateFile(string name, uint access, uint share, ref SECURITY_ATTRIBUTES attributes, uint creation, uint flags, IntPtr template);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool InitializeProcThreadAttributeList(IntPtr list, int count, int flags, ref IntPtr bytes);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool UpdateProcThreadAttribute(IntPtr list, uint flags, IntPtr attribute, IntPtr value, IntPtr bytes, IntPtr previous, IntPtr returned);
        [DllImport("kernel32.dll")] private static extern void DeleteProcThreadAttributeList(IntPtr list);
        [DllImport("kernel32.dll", SetLastError = true, CharSet = CharSet.Unicode)] private static extern bool CreateProcess(string application, StringBuilder command, IntPtr processAttributes, IntPtr threadAttributes, bool inheritHandles, uint flags, IntPtr environment, string directory, ref STARTUPINFOEX startup, out PROCESS_INFORMATION process);
    }
}
