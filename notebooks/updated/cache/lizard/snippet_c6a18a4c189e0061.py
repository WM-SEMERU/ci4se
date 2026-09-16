def removePoint(self, point, preserveCurve=False):
    if not isinstance(point, int):
        point = self.points.index(point)
    point = normalizers.normalizeIndex(point)
    if point >= self._len__points():
        raise ValueError('No point located at index %d.' % point)
    preserveCurve = normalizers.normalizeBoolean(preserveCurve)
    self._removePoint(point, preserveCurve)