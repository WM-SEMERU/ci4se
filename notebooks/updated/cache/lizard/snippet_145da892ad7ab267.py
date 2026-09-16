def make_step_lcont(transition):
    if not np.isfinite(transition):
        raise ValueError(
            '"transition" argument must be finite number; got %r' % transition)

    def step_lcont(x):
        x = np.asarray(x)
        x1 = np.atleast_1d(x)
        r = (x1 > transition).astype(x.dtype)
        if x.ndim == 0:
            return np.asscalar(r)
        return r
    step_lcont.__doc__ = (
        'Left-continuous step function. Returns 1 if x > %g, 0 otherwise.' %
        (transition,))
    return step_lcont