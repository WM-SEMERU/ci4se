def full_symbol(self):
    if self._full_symbol is None:
        self._full_symbol = self._symbol_extract(cache.RE_FULL_CURSOR,
            brackets=True)
    return self._full_symbol