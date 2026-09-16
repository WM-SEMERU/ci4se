def volumes(self):
    if not self._is_parsed:
        self._Parse()
        self._is_parsed = True
    return iter(self._volumes.values())