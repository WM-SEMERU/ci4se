def enable(self):
    with self._lock:
        if self.filter is None:
            self.filter = self._filter_type(self)