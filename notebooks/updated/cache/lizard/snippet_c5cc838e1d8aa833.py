def _convert_args(handler, args):
    args = list(args)
    params = inspect.signature(handler).parameters
    for i, (arg, name) in enumerate(zip(args, params)):
        default = params[name].default
        annotation = params[name].annotation
        if annotation != inspect.Parameter.empty:
            if isinstance(annotation, type) and annotation != str:
                args[i] = annotation(arg)
        elif default != inspect.Parameter.empty:
            if default is not None and not isinstance(default, str):
                args[i] = type(default)(arg)
    return args