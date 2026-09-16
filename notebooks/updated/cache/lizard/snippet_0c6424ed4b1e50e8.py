def append(self, pattern):
    assert isinstance(pattern, Pattern)
    self.patterns.append(pattern)
    if self._all_files is not None:
        self._all_files = self._all_files or pattern.all_files()