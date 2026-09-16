def extend(self, content, zorder):
    if zorder not in self._content:
        self._content[zorder] = []
    self._content[zorder].extend(content)