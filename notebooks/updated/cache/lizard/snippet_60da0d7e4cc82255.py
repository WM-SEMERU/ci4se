def icons(self, left=None):
    if left is not None:
        return self._icons[left]
    else:
        return list(chain.from_iterable(self._icons.values()))