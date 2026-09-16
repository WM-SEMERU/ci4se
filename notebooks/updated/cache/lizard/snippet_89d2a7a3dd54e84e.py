def _rescale(self, points):
    return [(x, self._scale_diff + (y - self._scale_min_2nd) * self._scale if
        y is not None else None) for x, y in points]