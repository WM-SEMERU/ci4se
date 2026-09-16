def discard(self, item):
    index = self._index(item)
    if index >= 0:
        del self._members[index]