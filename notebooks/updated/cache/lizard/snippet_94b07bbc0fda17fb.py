def attach(func, params):
    sig = inspect.signature(func)
    params = Projection(sig.parameters.keys(), params)
    return functools.partial(func, **params)