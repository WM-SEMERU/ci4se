def length_hint(obj, default=0):
    try:
        return len(obj)
    except TypeError:
        try:
            get_hint = type(obj).__length_hint__
        except AttributeError:
            return default
        try:
            hint = get_hint(obj)
        except TypeError:
            return default
        if hint is NotImplemented:
            return default
        if not isinstance(hint, int):
            raise TypeError('Length hint must be an integer, not %r' % type
                (hint))
        if hint < 0:
            raise ValueError('__length_hint__() should return >= 0')
        return hint