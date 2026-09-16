def watched(cls, *args, **kwargs):
    value = cls(*args, **kwargs)
    return value, watch(value)