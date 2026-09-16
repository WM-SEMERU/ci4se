def add_method(obj, func, name=None):
    if name is None:
        name = func.__name__
    if sys.version_info < (3,):
        method = types.MethodType(func, obj, obj.__class__)
    else:
        method = types.MethodType(func, obj)
    setattr(obj, name, method)