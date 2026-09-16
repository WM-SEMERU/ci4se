def import_(path):
    if isinstance(path, str):
        v = path.split(':')
        if len(v) == 1:
            x = path.rsplit('.', 1)
            if len(x) == 2:
                module, func = x
            else:
                module, func = x[0], ''
        else:
            module, func = v
        mod = __import__(module)
        f = mod
        if func:
            for x in func.split('.'):
                f = getattr(f, x)
    else:
        f = path
    return f