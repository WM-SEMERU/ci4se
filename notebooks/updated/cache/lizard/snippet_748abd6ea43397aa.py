def _resolve_periods_in_year(scale, frame):
    if scale is None:
        return periodicity(frame)
    elif isinstance(scale, basestring):
        return periodicity(scale)
    elif np.isscalar(scale):
        return scale
    else:
        raise ValueError('scale must be None, scalar, or string, not %s' %
            type(scale))