def text(self):
    if callable(self._text):
        return str(self._text())
    return str(self._text)