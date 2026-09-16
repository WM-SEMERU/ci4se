def _iter_key_ranges(self):
    while True:
        if self._current_key_range is None:
            if self._key_ranges:
                self._current_key_range = self._key_ranges.pop()
                continue
            else:
                break
        for key, o in self._iter_key_range(copy.deepcopy(self.
            _current_key_range)):
            self._current_key_range.advance(key)
            yield o
        self._current_key_range = None