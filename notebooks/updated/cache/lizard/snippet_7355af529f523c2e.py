def get_gam_splines(start=0, end=100, n_bases=10, spline_order=3,
    add_intercept=True):
    assert type(n_bases) == int
    x = np.arange(start, end + 1)
    knots = get_knots(start, end, n_bases, spline_order)
    X_splines = get_X_spline(x, knots, n_bases, spline_order, add_intercept)
    S = get_S(n_bases, spline_order, add_intercept)
    return X_splines, S, knots