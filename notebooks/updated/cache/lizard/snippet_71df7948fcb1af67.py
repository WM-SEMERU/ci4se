def load_symbols(self):
    if win32.PROCESS_ALL_ACCESS == win32.PROCESS_ALL_ACCESS_VISTA:
        dwAccess = win32.PROCESS_QUERY_LIMITED_INFORMATION
    else:
        dwAccess = win32.PROCESS_QUERY_INFORMATION
    hProcess = self.get_process().get_handle(dwAccess)
    hFile = self.hFile
    BaseOfDll = self.get_base()
    SizeOfDll = self.get_size()
    Enumerator = self._SymbolEnumerator()
    try:
        win32.SymInitialize(hProcess)
        SymOptions = win32.SymGetOptions()
        SymOptions |= (win32.SYMOPT_ALLOW_ZERO_ADDRESS | win32.
            SYMOPT_CASE_INSENSITIVE | win32.SYMOPT_FAVOR_COMPRESSED | win32
            .SYMOPT_INCLUDE_32BIT_MODULES | win32.SYMOPT_UNDNAME)
        SymOptions &= ~(win32.SYMOPT_LOAD_LINES | win32.
            SYMOPT_NO_IMAGE_SEARCH | win32.SYMOPT_NO_CPP | win32.
            SYMOPT_IGNORE_NT_SYMPATH)
        win32.SymSetOptions(SymOptions)
        try:
            win32.SymSetOptions(SymOptions | win32.
                SYMOPT_ALLOW_ABSOLUTE_SYMBOLS)
        except WindowsError:
            pass
        try:
            try:
                success = win32.SymLoadModule64(hProcess, hFile, None, None,
                    BaseOfDll, SizeOfDll)
            except WindowsError:
                success = 0
            if not success:
                ImageName = self.get_filename()
                success = win32.SymLoadModule64(hProcess, None, ImageName,
                    None, BaseOfDll, SizeOfDll)
            if success:
                try:
                    win32.SymEnumerateSymbols64(hProcess, BaseOfDll, Enumerator
                        )
                finally:
                    win32.SymUnloadModule64(hProcess, BaseOfDll)
        finally:
            win32.SymCleanup(hProcess)
    except WindowsError:
        e = sys.exc_info()[1]
        msg = 'Cannot load debug symbols for process ID %d, reason:\n%s'
        msg = msg % (self.get_pid(), traceback.format_exc(e))
        warnings.warn(msg, DebugSymbolsWarning)
    self.__symbols = Enumerator.symbols