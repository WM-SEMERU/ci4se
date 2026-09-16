def delete_kwargs_s(cls, s, args=None, kwargs=None):
    if not args and not kwargs:
        return s
    types = []
    if args is not None:
        types.append('`?`?\\*%s`?`?' % args)
    if kwargs is not None:
        types.append('`?`?\\*\\*%s`?`?' % kwargs)
    return cls.delete_types_s(s, types)