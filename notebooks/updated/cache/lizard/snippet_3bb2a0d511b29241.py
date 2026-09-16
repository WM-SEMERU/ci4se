def add_global(self, **values):
    with self._lock:
        self._ensure_global()
        self._gpayload.update(**values)