def register(function=None, *, singleton=False, threadlocal=False, name=None):
    warnings.warn(
        'Module level `register` decorator has been deprecated and will be removed in a future release. Use the Injector class instead'
        , DeprecationWarning)

    def decorator(function):
        return manager.register(function, singleton=singleton, threadlocal=
            threadlocal, name=name)
    if function:
        return decorator(function)
    else:
        return decorator