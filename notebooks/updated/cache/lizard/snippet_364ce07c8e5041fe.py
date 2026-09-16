def top(self):
    if self._has_real():
        return self._data.real_top
    return self._data.top