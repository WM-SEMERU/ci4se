def _validate(val, name, expected='any'):
    if not isinstance(val, PixCoord):
        raise TypeError('{} must be a PixCoord'.format(name))
    if expected == 'any':
        pass
    elif expected == 'scalar':
        if not val.isscalar:
            raise ValueError('{} must be a scalar PixCoord'.format(name))
    elif expected == 'not scalar':
        if val.isscalar:
            raise ValueError('{} must be a non-scalar PixCoord'.format(name))
    else:
        raise ValueError('Invalid argument for `expected`: {}'.format(expected)
            )
    return val