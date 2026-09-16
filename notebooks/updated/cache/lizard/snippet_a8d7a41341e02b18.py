def _q(self, number, precision='.00001'):
    if np.isinf(number):
        return np.nan
    else:
        return D(D(number).quantize(D(precision)))