def rejected(self, value):
    assert isinstance(value, bool)
    self._rejected = value
    if value:
        self._timeouted = False
        self._acknowledged = False
        self._cancelled = True