def deprecated(message, stacklevel=2):

    def _decorator(func):

        @wraps(func)
        def _func(*args, **kwargs):
            warnings.warn("'{}' is deprecated. {}".format(func.__name__,
                message), category=DeprecationWarning, stacklevel=stacklevel)
            return func(*args, **kwargs)
        return _func
    return _decorator