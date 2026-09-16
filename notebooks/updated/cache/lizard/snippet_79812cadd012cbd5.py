def add(self, v):
    self._vals_added += 1
    if self._mean is None:
        self._mean = v
    self._mean = self._mean + (v - self._mean) / float(self._vals_added)