def fit(self, t, y, dy=None, filts=0):
    self.unique_filts_ = np.unique(filts)
    if dy is None:
        dy = 1
    all_data = np.broadcast_arrays(t, y, dy, filts)
    self.t, self.y, self.dy, self.filts = map(np.ravel, all_data)
    self._fit(self.t, self.y, self.dy, self.filts)
    self._best_period = None
    if self.fit_period:
        self._best_period = self._calc_best_period()
    return self