def mutate(self, context, handler, args, kw):

    def cast(arg, val):
        if arg not in annotations:
            return
        cast = annotations[key]
        try:
            val = cast(val)
        except (ValueError, TypeError) as e:
            parts = list(e.args)
            parts[0] = parts[0] + " processing argument '{}'".format(arg)
            e.args = tuple(parts)
            raise
        return val
    annotations = getattr(handler.__func__ if hasattr(handler, '__func__') else
        handler, '__annotations__', None)
    if not annotations:
        return
    argspec = getfullargspec(handler)
    arglist = list(argspec.args)
    if ismethod(handler):
        del arglist[0]
    for i, value in enumerate(list(args)):
        key = arglist[i]
        if key in annotations:
            args[i] = cast(key, value)
    for key, value in list(items(kw)):
        if key in annotations:
            kw[key] = cast(key, value)