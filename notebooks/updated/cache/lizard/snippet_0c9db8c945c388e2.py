def create(cls, val):
    if val in cls._invalid:
        raise ValueError('Invalid value %r' % val)
    if val == 0:
        return Zero
    elif val == 1:
        return One
    elif isinstance(val, Scalar):
        return val
    else:
        return cls(val)