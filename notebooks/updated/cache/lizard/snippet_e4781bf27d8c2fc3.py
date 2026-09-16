def pkey(self):
    if self._pkey is None:
        self._pkey = self._get_pkey()
    return self._pkey