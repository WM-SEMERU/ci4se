def func_old_args(a, b=None, *args):
    try:
        c = args[0]
    except IndexError:
        c = None
    return a, b, c