def deprecated(function, instead):
    if not isinstance(function, types.FunctionType):
        return function

    @wraps(function)
    def wrap(*args, **kwargs):
        warnings.warn('Deprecated, use %s instead' % instead,
            PyGIDeprecationWarning)
        return function(*args, **kwargs)
    return wrap