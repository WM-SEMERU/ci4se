def ximplotxy_jupyter(x, y, fmt=None, **args):
    using_jupyter = True
    if fmt is None:
        return ximplotxy(x, y, using_jupyter=using_jupyter, **args)
    else:
        return ximplotxy(x, y, fmt, using_jupyter=using_jupyter, **args)