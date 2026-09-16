def hyperrectangle(lower, upper, bdy=True):
    lower = _np.array(lower)
    upper = _np.array(upper)
    dim = len(lower)
    if (upper <= lower).any():
        raise ValueError('invalid input; found upper <= lower')
    if bdy:

        def hr_indicator(x):
            if len(x) != dim:
                raise ValueError(
                    'input has wrong dimension (%i instead of %i)' % (len(x
                    ), dim))
            if (lower <= x).all() and (x <= upper).all():
                return True
            return False
    else:

        def hr_indicator(x):
            if len(x) != dim:
                raise ValueError(
                    'input has wrong dimension (%i instead of %i)' % (len(x
                    ), dim))
            if (lower < x).all() and (x < upper).all():
                return True
            return False
    hr_indicator.__doc__ = (
        'automatically generated hyperrectangle indicator function:')
    hr_indicator.__doc__ += '\nlower = ' + repr(lower)[6:-1]
    hr_indicator.__doc__ += '\nupper = ' + repr(upper)[6:-1]
    hr_indicator.__doc__ += '\nbdy   = ' + str(bdy)
    return hr_indicator