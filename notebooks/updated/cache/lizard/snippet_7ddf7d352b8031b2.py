def no_route(arg=None):

    def wrapper(fn):
        setattr(fn, NO_ROUTES_ATTR, True)
        return fn
    if callable(arg):
        return wrapper(arg)
    return wrapper