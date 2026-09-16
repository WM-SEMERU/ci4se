def strict_defaults(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        defaults = _get_default_args(fn)
        needed_types = {key: type(defaults[key]) for key in defaults}
        arg_names = _get_arg_names(fn)
        assert not len(arg_names) - len(fn.__defaults__
            ), '{} needs default variables on all arguments'.format(fn.__name__
            )
        for i in range(len(args)):
            if args[i] not in kwargs.keys():
                kwargs[arg_names[i]] = args[i]
        for name in needed_types:
            assert isinstance(kwargs[name], needed_types[name]
                ), 'got {} and expected a {}'.format(kwargs[name],
                needed_types[name])
        return fn(**kwargs)
    return wrapper