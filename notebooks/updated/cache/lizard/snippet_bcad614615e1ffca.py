def add(self, name, value):
    size = table_entry_size(name, value)
    if size > self._maxsize:
        self.dynamic_entries.clear()
        self._current_size = 0
    elif self._maxsize > 0:
        self.dynamic_entries.appendleft((name, value))
        self._current_size += size
        self._shrink()