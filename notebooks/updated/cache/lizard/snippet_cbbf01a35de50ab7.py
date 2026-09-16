def cutout_cross(self, x, y, radius):
    n = radius
    wd, ht = self.get_size()
    x0, x1 = max(0, x - n), min(wd - 1, x + n)
    y0, y1 = max(0, y - n), min(ht - 1, y + n)
    xview = np.s_[(y), x0:x1 + 1]
    yview = np.s_[y0:y1 + 1, (x)]
    xarr = self._slice(xview)
    yarr = self._slice(yview)
    return x0, y0, xarr, yarr