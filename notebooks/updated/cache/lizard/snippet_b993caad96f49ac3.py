def ignore_exception(exception_class):

    def _decorator(func):

        def newfunc(*args, **kwds):
            try:
                return func(*args, **kwds)
            except exception_class:
                pass
        return newfunc
    return _decorator