def _check_arg_length(fname, args, max_fname_arg_count, compat_args):
    if max_fname_arg_count < 0:
        raise ValueError("'max_fname_arg_count' must be non-negative")
    if len(args) > len(compat_args):
        max_arg_count = len(compat_args) + max_fname_arg_count
        actual_arg_count = len(args) + max_fname_arg_count
        argument = 'argument' if max_arg_count == 1 else 'arguments'
        raise TypeError(
            '{fname}() takes at most {max_arg} {argument} ({given_arg} given)'
            .format(fname=fname, max_arg=max_arg_count, argument=argument,
            given_arg=actual_arg_count))