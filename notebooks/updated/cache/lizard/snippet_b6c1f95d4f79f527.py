def zoom_out(self):
    index = self._zoom_factors.index(self._zoom_factor)
    if index == 0:
        return
    self._zoom_factor = self._zoom_factors[index - 1]
    if self._zoom_factors.index(self._zoom_factor) == 0:
        self._button_zoom_out.config(state=tk.DISABLED)
    self._button_zoom_in.config(state=tk.NORMAL)
    self.draw_timeline()