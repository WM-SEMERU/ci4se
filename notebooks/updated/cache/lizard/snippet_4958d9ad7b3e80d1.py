def inherit_doc(cls):
    for name, func in vars(cls).items():
        if name.startswith('_'):
            continue
        if not func.__doc__:
            for parent in cls.__bases__:
                parent_func = getattr(parent, name, None)
                if parent_func and getattr(parent_func, '__doc__', None):
                    func.__doc__ = parent_func.__doc__
                    break
    return cls