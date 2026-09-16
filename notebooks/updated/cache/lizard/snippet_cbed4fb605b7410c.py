def _draw(self):
    self._compute()
    self._compute_x_labels()
    self._compute_x_labels_major()
    self._compute_y_labels()
    self._compute_y_labels_major()
    self._compute_secondary()
    self._post_compute()
    self._compute_margin()
    self._decorate()
    if self.series and self._has_data() and self._values:
        self._plot()
    else:
        self.svg.draw_no_data()