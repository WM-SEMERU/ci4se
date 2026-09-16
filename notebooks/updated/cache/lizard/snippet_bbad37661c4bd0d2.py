def setCompleter(self, completer):
    if self._completer == completer:
        return
    elif self._completer:
        self._completer.activated.disconnect(self.finishEditing)
    self._completer = completer
    if completer:
        completer.activated.connect(self.finishEditing)