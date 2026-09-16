def getattrs(value, attrs, default=_no_default):
    try:
        for attr in attrs:
            value = getattr(value, attr)
    except AttributeError:
        if default is _no_default:
            raise
        value = default
    return value