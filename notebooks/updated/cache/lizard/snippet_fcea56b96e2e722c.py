def lineReceived(self, line):
    if line and line.isdigit():
        self._expectedLength = int(line)
        self._rawBuffer = []
        self._rawBufferLength = 0
        self.setRawMode()
    else:
        self.keepAliveReceived()