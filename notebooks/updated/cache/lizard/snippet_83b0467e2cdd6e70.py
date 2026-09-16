def discretize_bspline(control, knots, count=None, scale=1.0):
    from scipy.interpolate import splev
    control = np.asanyarray(control, dtype=np.float64)
    degree = len(knots) - len(control) - 1
    if count is None:
        norm = np.linalg.norm(np.diff(control, axis=0), axis=1).sum()
        count = int(np.clip(norm / (res.seg_frac * scale), res.min_sections *
            len(control), res.max_sections * len(control)))
    ipl = np.linspace(knots[0], knots[-1], count)
    discrete = splev(ipl, [knots, control.T, degree])
    discrete = np.column_stack(discrete)
    return discrete