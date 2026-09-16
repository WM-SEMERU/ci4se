def gradient(self):
    gradFill = self._xPr.get_or_change_to_gradFill()
    self._fill = _GradFill(gradFill)