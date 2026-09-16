def func_defsig(func, with_name=True):
    import inspect
    argspec = inspect.getargspec(func)
    args, varargs, varkw, defaults = argspec
    defsig = inspect.formatargspec(*argspec)
    if with_name:
        defsig = get_callable_name(func) + defsig
    return defsig