def overlay(top, bottom, maxval=None):
    if maxval is None:
        maxval = np.maximum(top.max(), bottom.max())
    res = ((2 * top / maxval - 1) * bottom + 2 * top) * bottom / maxval
    return res.clip(min=0)