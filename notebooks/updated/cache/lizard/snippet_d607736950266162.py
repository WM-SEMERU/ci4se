def rm_blanks(self):
    _blanks = [k for k in self._dict.keys() if not self._dict[k]]
    for key in _blanks:
        del self._dict[key]