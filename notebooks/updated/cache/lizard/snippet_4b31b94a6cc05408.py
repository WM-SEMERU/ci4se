def fromkeys(cls, seq, value=None, **kwargs):
    other = cls(**kwargs)
    other.update((key, value) for key in seq)
    return other