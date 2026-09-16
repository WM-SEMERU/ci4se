def _xcorr_interp(ccc, dt):
    if ccc.shape[0] == 1:
        cc = ccc[0]
    else:
        cc = ccc
    cc_curvature = np.concatenate((np.zeros(1), np.diff(cc, 2), np.zeros(1)))
    cc_t = np.arange(0, len(cc) * dt, dt)
    peak_index = cc.argmax()
    first_sample = peak_index
    while first_sample > 0 and cc_curvature[first_sample - 1] <= 0:
        first_sample -= 1
    last_sample = peak_index
    while last_sample < len(cc) - 1 and cc_curvature[last_sample + 1] <= 0:
        last_sample += 1
    num_samples = last_sample - first_sample + 1
    if num_samples < 3:
        msg = ('Less than 3 samples selected for fit to cross ' + 
            'correlation: %s' % num_samples)
        raise IndexError(msg)
    if num_samples < 5:
        msg = ('Less than 5 samples selected for fit to cross ' + 
            'correlation: %s' % num_samples)
        warnings.warn(msg)
    coeffs, residual = scipy.polyfit(cc_t[first_sample:last_sample + 1], cc
        [first_sample:last_sample + 1], deg=2, full=True)[:2]
    if coeffs[0] >= 0:
        msg = 'Fitted parabola opens upwards!'
        warnings.warn(msg)
    if residual > 0.1:
        msg = ('Residual in quadratic fit to cross correlation maximum ' + 
            'larger than 0.1: %s' % residual)
        warnings.warn(msg)
    shift = -coeffs[1] / 2.0 / coeffs[0]
    coeff = (4 * coeffs[0] * coeffs[2] - coeffs[1] ** 2) / (4 * coeffs[0])
    return shift, coeff