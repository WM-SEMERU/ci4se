def setWriteToShell(self, writeToShell=True):
    if writeToShell and not self._connected:
        self.message.connect(self.stdW)
        self._connected = True
    elif not writeToShell and self._connected:
        try:
            self.message.disconnect(self.stdW)
        except TypeError:
            pass
        self._connected = False