def decorator(caller, _func=None):
    if _func is not None:
        return decorate(_func, caller)
    defaultargs, defaults = '', ()
    if inspect.isclass(caller):
        name = caller.__name__.lower()
        doc = (
            'decorator(%s) converts functions/generators into factories of %s objects'
             % (caller.__name__, caller.__name__))
    elif inspect.isfunction(caller):
        if caller.__name__ == '<lambda>':
            name = '_lambda_'
        else:
            name = caller.__name__
        doc = caller.__doc__
        nargs = caller.__code__.co_argcount
        ndefs = len(caller.__defaults__ or ())
        defaultargs = ', '.join(caller.__code__.co_varnames[nargs - ndefs:
            nargs])
        if defaultargs:
            defaultargs += ','
        defaults = caller.__defaults__
    else:
        name = caller.__class__.__name__.lower()
        doc = caller.__call__.__doc__
    evaldict = dict(_call=caller, _decorate_=decorate)
    dec = FunctionMaker.create('%s(func, %s)' % (name, defaultargs), 
        """if func is None: return lambda func:  _decorate_(func, _call, (%s))
return _decorate_(func, _call, (%s))"""
         % (defaultargs, defaultargs), evaldict, doc=doc, module=caller.
        __module__, __wrapped__=caller)
    if defaults:
        dec.__defaults__ = (None,) + defaults
    return dec