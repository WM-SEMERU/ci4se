def copy(self):
    if self._iters:
        a, b = it.tee(self._iters[0])
        self._iters[0] = a
        return Stream(b)
    iter(self)