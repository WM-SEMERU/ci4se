def _fill_and_verify_padding(padding, n):
    if not isinstance(n, numbers.Integral) or n < 1:
        raise TypeError('n must be a positive integer')
    if isinstance(padding, six.string_types) and padding in ALLOWED_PADDINGS:
        return (padding,) * n
    try:
        if len(padding) == n and all(p in ALLOWED_PADDINGS for p in padding):
            return tuple(padding)
    except TypeError:
        pass
    raise TypeError(
        "padding is {}, must be member of '{}' or an iterable of these of size {}"
        .format(padding, ALLOWED_PADDINGS, n))