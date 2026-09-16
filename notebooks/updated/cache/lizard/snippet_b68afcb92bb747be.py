def _colorbar_ticks(minval, maxval):
    if not (np.isfinite(minval) and np.isfinite(maxval)):
        return [0, 0, 0]
    elif minval == maxval:
        return [minval]
    else:
        eps = (maxval - minval) / 100000.0
        return [minval + eps, (maxval + minval) / 2.0, maxval - eps]