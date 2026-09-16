def retrymethod(count, sleep=0):

    def decorated(func):

        @wraps(func)
        def wrapped(*args, **kwds):
            for i in range(count - 1):
                try:
                    return func(*args, **kwds)
                except StandardError:
                    pass
                if sleep:
                    time.sleep(sleep)
            return func(*args, **kwds)
        return wrapped
    return decorated