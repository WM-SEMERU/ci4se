def fit1d(samples, e, remove_zeros=False, **kw):
    samples = samples[~np.isnan(samples)]
    length = len(e) - 1
    hist, _ = np.histogramdd(samples, (e,))
    hist = hist / sum(hist)
    basis, knots = spline_base1d(length, marginal=hist, **kw)
    non_zero = hist > 0
    model = linear_model.BayesianRidge()
    if remove_zeros:
        model.fit(basis[(non_zero), :], hist[:, (np.newaxis)][(non_zero), :])
    else:
        hist[~non_zero] = np.finfo(float).eps
        model.fit(basis, hist[:, (np.newaxis)])
    return model.predict(basis), hist, knots