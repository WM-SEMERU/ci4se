def set_const(const, val):
    try:
        cur = getattr(_c, const)
    except AttributeError:
        raise FSQEnvError(errno.ENOENT, 'no such constant: {0}'.format(const))
    except TypeError:
        raise TypeError(errno.EINVAL,
            'const name must be a string or unicode object, not: {0}'.
            format(const.__class__.__name__))
    should_be = cur.__class__
    try:
        if not isinstance(val, should_be):
            if should_be is unicode or cur is None:
                val = coerce_unicode(val, _c.FSQ_CHARSET)
            elif should_be is int and const.endswith('MODE'):
                val = int(val, 8)
            elif isinstance(cur, numbers.Integral):
                val = int(val)
            else:
                should_be(val)
    except (TypeError, ValueError):
        raise FSQEnvError(errno.EINVAL,
            'invalid type for constant {0}, should be {1}, not: {2}'.format
            (const, should_be.__name__, val.__class__.__name__))
    setattr(_c, const, val)
    return val