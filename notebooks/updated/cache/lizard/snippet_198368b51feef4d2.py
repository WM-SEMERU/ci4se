def cast(cls, value_type, value, visitor=None, **kwargs):
    if visitor is None:
        visitor = cls.Visitor(cls.grok, cls.reverse, cls.collect, cls.
            produce, **kwargs)
    return cls.map(visitor, value, value_type)