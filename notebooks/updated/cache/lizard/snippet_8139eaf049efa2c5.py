def option(self, key, value):
    self._jwrite = self._jwrite.option(key, to_str(value))
    return self