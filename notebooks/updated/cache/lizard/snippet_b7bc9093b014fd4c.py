def setInputPoint(self, point):
    self._inputPoint = point
    self.setPath(self.rebuild())