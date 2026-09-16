def _get_leftMargin(self):
    bounds = self.bounds
    if bounds is None:
        return None
    xMin, yMin, xMax, yMax = bounds
    return xMin