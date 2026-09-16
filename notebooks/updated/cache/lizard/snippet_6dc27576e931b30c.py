def _cursorUp(self):
    if self.historyPos > 0:
        self.historyPos -= 1
        clearLen = len(self.inputBuffer)
        self.inputBuffer = list(self.history[self.historyPos])
        self.cursorPos = len(self.inputBuffer)
        self._refreshInputPrompt(clearLen)