def ensure_arg(args, arg, param=None):
    for idx, found_arg in enumerate(args):
        if found_arg == arg:
            if param is not None:
                args[idx + 1] = param
            return args
    args.append(arg)
    if param is not None:
        args.append(param)
    return args