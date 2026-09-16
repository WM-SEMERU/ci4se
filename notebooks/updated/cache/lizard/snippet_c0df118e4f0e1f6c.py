def Start(self):
    self._shutdown = False
    self._main_thread = threading.Thread(target=self._MainThreadProc)
    self._main_thread.name = 'Cloud Debugger main worker thread'
    self._main_thread.daemon = True
    self._main_thread.start()