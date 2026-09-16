def _notify_create_process(self, event):
    dwProcessId = event.get_pid()
    if dwProcessId not in self.__attachedDebugees:
        if dwProcessId not in self.__startedDebugees:
            self.__startedDebugees.add(dwProcessId)
    retval = self.system._notify_create_process(event)
    if dwProcessId in self.__breakOnEP:
        try:
            lpEntryPoint = event.get_process().get_entry_point()
        except Exception:
            lpEntryPoint = event.get_start_address()
        self.break_at(dwProcessId, lpEntryPoint)
    if self.__bHostileCode:
        aProcess = event.get_process()
        try:
            hProcess = aProcess.get_handle(win32.PROCESS_QUERY_INFORMATION)
            pbi = win32.NtQueryInformationProcess(hProcess, win32.
                ProcessBasicInformation)
            ptr = pbi.PebBaseAddress + 2
            if aProcess.peek(ptr, 1) == '\x01':
                aProcess.poke(ptr, '\x00')
        except WindowsError:
            e = sys.exc_info()[1]
            warnings.warn('Cannot patch PEB->BeingDebugged, reason: %s' % e
                .strerror)
    return retval