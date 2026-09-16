def call(cls, iterable, *a, **kw):
    return cls(x(*a, **kw) for x in iterable)