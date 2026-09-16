def insertNextCommand(self):
    self._currentHistoryIndex += 1
    if 0 <= self._currentHistoryIndex < len(self._history):
        cmd = self._history[self._currentHistoryIndex]
    else:
        cmd = '>>> '
        self._currentHistoryIndex = -1
    self.replaceCommand(cmd)