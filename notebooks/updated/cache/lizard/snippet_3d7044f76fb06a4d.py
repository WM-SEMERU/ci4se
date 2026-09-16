def removeContour(self, contour):
    if isinstance(contour, int):
        index = contour
    else:
        index = self._getContourIndex(contour)
    index = normalizers.normalizeIndex(index)
    if index >= len(self):
        raise ValueError('No contour located at index %d.' % index)
    self._removeContour(index)