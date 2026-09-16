def terminate(self):
    self.text = ''
    self._completer.terminate()
    if self._highlighter is not None:
        self._highlighter.terminate()
    if self._vim is not None:
        self._vim.terminate()