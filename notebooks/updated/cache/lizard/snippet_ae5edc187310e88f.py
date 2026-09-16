def zDDEClose(self):
    if _PyZDDE.server and not _PyZDDE.liveCh:
        _PyZDDE.server.Shutdown(self.conversation)
        _PyZDDE.server = 0
    elif _PyZDDE.server and self.connection and _PyZDDE.liveCh == 1:
        _PyZDDE.server.Shutdown(self.conversation)
        self.connection = False
        self.appName = ''
        _PyZDDE.liveCh -= 1
        _PyZDDE.server = 0
    elif self.connection:
        _PyZDDE.server.Shutdown(self.conversation)
        self.connection = False
        self.appName = ''
        _PyZDDE.liveCh -= 1
    return 0