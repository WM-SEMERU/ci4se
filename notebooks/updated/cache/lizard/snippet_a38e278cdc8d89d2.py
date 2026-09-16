def return_self_updater(func):

    @functools.wraps(func)
    def decorator(k, v):
        func(k, v)
        return v
    return decorator