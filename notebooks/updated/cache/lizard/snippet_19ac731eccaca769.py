def monkeypatch_method(cls, patch_name):

    def decorator(func):
        fname = func.__name__
        old_func = getattr(cls, fname, None)
        if old_func is not None:
            old_ref = '_old_%s_%s' % (patch_name, fname)
            old_attr = getattr(cls, old_ref, None)
            if old_attr is None:
                setattr(cls, old_ref, old_func)
            else:
                raise KeyError('%s.%s already exists.' % (cls.__name__,
                    old_ref))
        setattr(cls, fname, func)
        return func
    return decorator