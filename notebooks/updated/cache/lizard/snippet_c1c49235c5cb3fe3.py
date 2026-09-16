def open_handle(self, dwDesiredAccess=win32.THREAD_ALL_ACCESS):
    hThread = win32.OpenThread(dwDesiredAccess, win32.FALSE, self.dwThreadId)
    if not hasattr(self.hThread, '__del__'):
        self.close_handle()
    self.hThread = hThread