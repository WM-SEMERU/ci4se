def _fill(self):
    try:
        self._head = self._iterable.next()
    except StopIteration:
        self._head = None