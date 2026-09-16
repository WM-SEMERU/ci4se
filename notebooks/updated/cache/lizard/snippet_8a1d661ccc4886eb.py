def reduce(self, start=0, end=None):
    if end is None:
        end = self._capacity - 1
    if end < 0:
        end += self._capacity
    return self._reduce_helper(start, end, 1, 0, self._capacity - 1)