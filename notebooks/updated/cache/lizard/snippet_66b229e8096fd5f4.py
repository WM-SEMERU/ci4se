def get_func_argspec(func):
    if hasattr(func, '_utinfo'):
        argspec = func._utinfo['orig_argspec']
        return argspec
    if isinstance(func, property):
        func = func.fget
    try:
        argspec = inspect.getargspec(func)
    except Exception:
        argspec = inspect.getfullargspec(func)
    return argspec