def read_msr(address):
    if win32.arch not in (win32.ARCH_I386, win32.ARCH_AMD64):
        raise NotImplementedError(
            'MSR reading is only supported on i386 or amd64 processors.')
    msr = win32.SYSDBG_MSR()
    msr.Address = address
    msr.Data = 0
    win32.NtSystemDebugControl(win32.SysDbgReadMsr, InputBuffer=msr,
        OutputBuffer=msr)
    return msr.Data