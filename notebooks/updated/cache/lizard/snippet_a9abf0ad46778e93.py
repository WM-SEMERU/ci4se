def append_sources_from(self, other):
    self_aliases = self[self._KEYS.SOURCE].split(',')
    other_aliases = other[self._KEYS.SOURCE].split(',')
    self[self._KEYS.SOURCE] = uniq_cdl(self_aliases + other_aliases)
    return