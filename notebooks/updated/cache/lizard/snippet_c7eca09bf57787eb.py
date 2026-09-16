def wrap_connection(func_, *args, **kwargs):
    if not args[-1]:
        new_args = list(args)
        new_args[-1] = connect()
        args = tuple(new_args)
    return func_(*args, **kwargs)