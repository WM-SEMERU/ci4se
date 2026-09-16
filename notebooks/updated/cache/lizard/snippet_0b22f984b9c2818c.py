def insert(self, lines=None):
    for i, (key, line) in enumerate(lines.items()):
        n = key + i
        first_half = self._lines[:n]
        last_half = self._lines[n:]
        self._lines = first_half + [line] + last_half