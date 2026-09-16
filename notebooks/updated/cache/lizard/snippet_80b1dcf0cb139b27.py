def func_callsig(func, with_name=True):
    import inspect
    argspec = inspect.getargspec(func)
    args, varargs, varkw, defaults = argspec
    callsig = inspect.formatargspec(*argspec[0:3])
    if with_name:
        callsig = get_callable_name(func) + callsig
    return callsig