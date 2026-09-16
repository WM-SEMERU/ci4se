def _vmf_normalize(kappa, dim):
    num = np.power(kappa, dim / 2.0 - 1.0)
    if dim / 2.0 - 1.0 < 1e-15:
        denom = np.power(2.0 * np.pi, dim / 2.0) * i0(kappa)
    else:
        denom = np.power(2.0 * np.pi, dim / 2.0) * iv(dim / 2.0 - 1.0, kappa)
    if np.isinf(num):
        raise ValueError('VMF scaling numerator was inf.')
    if np.isinf(denom):
        raise ValueError('VMF scaling denominator was inf.')
    if np.abs(denom) < 1e-15:
        raise ValueError('VMF scaling denominator was 0.')
    return num / denom