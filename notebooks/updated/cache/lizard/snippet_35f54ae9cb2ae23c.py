def _proxy(self):
    if self._context is None:
        self._context = FaxContext(self._version, sid=self._solution['sid'])
    return self._context