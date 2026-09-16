def paramnames(co):
    flags = co.co_flags
    varnames = co.co_varnames
    argcount, kwonlyargcount = co.co_argcount, co.co_kwonlyargcount
    total = argcount + kwonlyargcount
    args = varnames[:argcount]
    kwonlyargs = varnames[argcount:total]
    varargs, varkwargs = None, None
    if flags & Flag.CO_VARARGS:
        varargs = varnames[total]
        total += 1
    if flags & Flag.CO_VARKEYWORDS:
        varkwargs = varnames[total]
    return args, kwonlyargs, varargs, varkwargs