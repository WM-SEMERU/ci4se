def shift(*args):
    if len(args) > 2:
        raise ValueError('shift() takes 0, 1 or 2 arguments.')
    n = 1
    l = ayrton.runner.globals['argv']
    logger.debug2('%s(%d)', args, len(args))
    if len(args) == 1:
        value = args[0]
        logger.debug2(type(value))
        if isinstance(value, int):
            n = value
        elif isinstance(value, Iterable):
            l = value
        else:
            raise ValueError('First parameter must be Iterable or int().')
    elif len(args) == 2:
        l, n = args
    logger.debug2('%s(%d)', args, len(args))
    logger.debug('%s[%d]', l, n)
    if n == 1:
        ans = l.pop(0)
    elif n > 1:
        ans = [l.pop(0) for i in range(n)]
    else:
        raise ValueError('Integer parameter must be >= 0.')
    return ans