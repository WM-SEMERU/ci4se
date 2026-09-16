def _apply2parser(arguments, options, parser):
    for args, kwargs in options:
        parser.option(*args, **kwargs)
    for args, kwargs in arguments:
        parser.argument(*args, **kwargs)
    return parser