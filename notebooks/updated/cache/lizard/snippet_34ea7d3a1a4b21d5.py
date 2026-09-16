def kw_map(**kws):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for actual_name, kwarg_rename in kws.items():
                if kwarg_rename in kwargs:
                    kwargs[actual_name] = kwargs[kwarg_rename]
                    del kwargs[kwarg_rename]
            return func(*args, **kwargs)
        return wrapper
    return decorator