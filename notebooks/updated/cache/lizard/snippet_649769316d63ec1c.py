def filter(cls, iterable, cond, *a, **kw):
    return cls(x for x in iterable if cond(x, *a, **kw))