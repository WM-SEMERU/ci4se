def func_old_kwargs(a, b=None, **kwargs):
    try:
        c = kwargs['c']
    except KeyError:
        c = None
    return a, b, c