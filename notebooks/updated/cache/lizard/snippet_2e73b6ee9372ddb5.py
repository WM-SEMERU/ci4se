def next(self):
    if self._iter_n < self.n_blocks:
        result = self[self._iter_n]
        self._iter_n += 1
        return result
    else:
        raise StopIteration