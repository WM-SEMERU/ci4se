def pop(self, index=-1):
    value = self._list.pop(index)
    self._set.remove(value)
    return value