def value(self):
    if self._value:
        return self._value
    if self.formatter:
        return self.formatter(self.raw)
    return self.raw