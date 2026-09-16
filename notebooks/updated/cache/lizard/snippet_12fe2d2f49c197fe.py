def cutout_data(self, x1, y1, x2, y2, xstep=1, ystep=1, astype=None):
    view = np.s_[y1:y2:ystep, x1:x2:xstep]
    data = self._slice(view)
    if astype:
        data = data.astype(astype, copy=False)
    return data