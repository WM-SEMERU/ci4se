def _CollectArguments(function, args, kwargs):
    all_args = dict(kwargs)
    arg_names = inspect.getargspec(function)[0]
    for position, arg in enumerate(args):
        if position < len(arg_names):
            all_args[arg_names[position]] = arg
    return all_args