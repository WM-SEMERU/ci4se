def _getargspec(func):
    argspec = _getspec(func)
    args = list(argspec.args)
    if argspec.varargs:
        args += [argspec.varargs]
    if argspec[2]:
        args += [argspec[2]]
    return _ArgSpec(args, argspec.varargs, argspec[2])