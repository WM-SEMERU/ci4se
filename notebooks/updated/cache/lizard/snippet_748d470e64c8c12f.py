def clone(src, **kwargs):
    obj = object.__new__(type(src))
    obj.__dict__.update(src.__dict__)
    obj.__dict__.update(kwargs)
    return obj