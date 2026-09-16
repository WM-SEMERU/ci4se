def execute(*args, **kwargs):
    if kwargs:
        args = list(args)
        args.extend(_kwargs_to_execute_args(kwargs))
    _execute(*args)