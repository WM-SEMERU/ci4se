def config_prefix(prefix):
    global register_option, get_option, set_option, reset_option

    def wrap(func):

        def inner(key, *args, **kwds):
            pkey = '{prefix}.{key}'.format(prefix=prefix, key=key)
            return func(pkey, *args, **kwds)
        return inner
    _register_option = register_option
    _get_option = get_option
    _set_option = set_option
    set_option = wrap(set_option)
    get_option = wrap(get_option)
    register_option = wrap(register_option)
    yield None
    set_option = _set_option
    get_option = _get_option
    register_option = _register_option