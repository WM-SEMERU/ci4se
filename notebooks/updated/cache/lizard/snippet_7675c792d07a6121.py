def destination(self, value):
    if value is not None and (not isinstance(value, tuple) or len(value)) != 2:
        raise AttributeError
    self._destination = value