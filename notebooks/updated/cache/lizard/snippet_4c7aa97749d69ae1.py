def execute(self, cmd):
    if not cmd.filePath in self._history.keys():
        self._history[cmd.filePath] = SubtitleUndoStack(self)
        try:
            self._history[cmd.filePath].push(cmd)
        except:
            self._history[cmd.filePath].deleteLater()
            del self._history[cmd.filePath]
            raise
        else:
            self._history[cmd.filePath].clear()
    else:
        self._history[cmd.filePath].push(cmd)