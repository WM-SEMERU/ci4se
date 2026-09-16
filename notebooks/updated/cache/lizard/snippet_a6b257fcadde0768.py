def normalizeInterpolationFactor(value):
    if not isinstance(value, (int, float, list, tuple)):
        raise TypeError(
            'Interpolation factor must be an int, float, or tuple instances, not %s.'
             % type(value).__name__)
    if isinstance(value, (int, float)):
        value = float(value), float(value)
    else:
        if not len(value) == 2:
            raise ValueError(
                'Interpolation factor tuple must contain two values, not %d.' %
                len(value))
        for v in value:
            if not isinstance(v, (int, float)):
                raise TypeError(
                    'Interpolation factor tuple values must be an :ref:`type-int-float`, not %s.'
                     % type(value).__name__)
        value = tuple([float(v) for v in value])
    return value