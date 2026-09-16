def call_with_asked_args(callback, args):
    asked_arg_names = callback.__code__.co_varnames[:callback.__code__.
        co_argcount]
    asked_arg_values = []
    missing_args = []
    for asked_arg_name in asked_arg_names:
        if asked_arg_name in args:
            asked_arg_values.append(args[asked_arg_name])
        else:
            missing_args.append(asked_arg_name)
    if missing_args:
        raise TypeError('{}() missing required positional argument: {}'.
            format(callback.__code__.co_name, ', '.join(missing_args)))
    return callback(*asked_arg_values)