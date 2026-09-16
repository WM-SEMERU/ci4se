def _iter_process():
    h_process = windll.kernel32.CreateToolhelp32Snapshot(2, 0)
    if h_process == INVALID_HANDLE_VALUE:
        raise WinError()
    pe = PROCESSENTRY32()
    pe.dwSize = sizeof(PROCESSENTRY32)
    success = windll.kernel32.Process32First(h_process, byref(pe))
    while True:
        if not success:
            errcode = windll.kernel32.GetLastError()
            if errcode == ERROR_NO_MORE_FILES:
                return
            elif errcode == ERROR_INSUFFICIENT_BUFFER:
                continue
            raise WinError()
        executable = pe.szExeFile
        if isinstance(executable, bytes):
            executable = executable.decode('mbcs', 'replace')
        info = {'executable': executable}
        if pe.th32ParentProcessID:
            info['parent_pid'] = pe.th32ParentProcessID
        yield pe.th32ProcessID, info
        success = windll.kernel32.Process32Next(h_process, byref(pe))