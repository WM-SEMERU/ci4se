def match(self, item):
    val = getattr(item, self._name) or False
    return bool(val) is self._value