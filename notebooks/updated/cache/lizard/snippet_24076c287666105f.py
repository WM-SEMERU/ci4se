def _locals(self, d):
    if not d:
        return self
    c = self._copy()
    c._data.update(d)
    return c