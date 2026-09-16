def default_reply(*args, **kwargs):
    invoked = bool(not args or kwargs)
    matchstr = kwargs.pop('matchstr', '^.*$')
    flags = kwargs.pop('flags', 0)
    if not invoked:
        func = args[0]

    def wrapper(func):
        PluginsManager.commands['default_reply'][re.compile(matchstr, flags)
            ] = func
        logger.info('registered default_reply plugin "%s" to "%s"', func.
            __name__, matchstr)
        return func
    return wrapper if invoked else wrapper(func)