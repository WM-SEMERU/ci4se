def normcdf(x, log=False):
    y = np.atleast_1d(x).copy()
    flib.normcdf(y)
    if log:
        if (y > 0).all():
            return np.log(y)
        return -np.inf
    return y