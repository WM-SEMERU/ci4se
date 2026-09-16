def fromkeys(cls, seq, value=None, **kwargs):
    values = ((key, value) for key in seq)
    return cls(values, **kwargs)