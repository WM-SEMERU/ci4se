def max_fmeasure(fg_vals, bg_vals):
    x, y = roc_values(fg_vals, bg_vals)
    x, y = x[1:], y[1:]
    p = y / (y + x)
    filt = np.logical_and(p * y > 0, p + y > 0)
    p = p[filt]
    y = y[filt]
    f = 2 * p * y / (p + y)
    if len(f) > 0:
        return np.nanmax(f)
    else:
        return None