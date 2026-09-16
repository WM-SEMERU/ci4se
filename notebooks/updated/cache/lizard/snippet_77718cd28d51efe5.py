def min(self, numeric_only=None, **kwargs):
    self.check_for_ordered('min')
    if numeric_only:
        good = self._codes != -1
        pointer = self._codes[good].min(**kwargs)
    else:
        pointer = self._codes.min(**kwargs)
    if pointer == -1:
        return np.nan
    else:
        return self.categories[pointer]