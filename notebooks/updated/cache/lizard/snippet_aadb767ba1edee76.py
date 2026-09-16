def coerce(self, value):
    if self._coerce is not None:
        value = self._coerce(value)
    return value