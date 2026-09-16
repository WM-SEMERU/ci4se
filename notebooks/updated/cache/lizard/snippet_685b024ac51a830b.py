def keyed_ordering(cls):
    if '__key__' not in cls.__dict__:
        raise TypeError('keyed_ordering requires a __key__ method')
    for name in ('__eq__', '__ne__', '__lt__', '__gt__', '__le__', '__ge__'):
        if name in cls.__dict__:
            continue
        method = _keyed_ordering_impl(name, cls)
        setattr(cls, name, method)
    return cls