def _compute(self):
    for serie in self.series:
        serie.points, serie.outliers = self._box_points(serie.values, self.
            box_mode)
    self._x_pos = [((i + 0.5) / self._order) for i in range(self._order)]
    if self._min:
        self._box.ymin = min(self._min, self.zero)
    if self._max:
        self._box.ymax = max(self._max, self.zero)