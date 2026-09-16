def rebin_scale(a, scale=1):
    newshape = tuple(side * scale for side in a.shape)
    return rebin(a, newshape)