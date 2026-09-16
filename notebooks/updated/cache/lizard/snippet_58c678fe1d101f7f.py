def get_calling_prototype(acallable):
    assert callable(acallable)
    if inspect.ismethod(acallable) or inspect.isfunction(acallable):
        args, vargs, vkwargs, defaults = inspect.getargspec(acallable)
    elif not inspect.isfunction(acallable) and hasattr(acallable, '__call__'):
        args, vargs, vkwargs, defaults = inspect.getargspec(acallable.__call__)
        args = args[1:]
    else:
        raise ValueError(
            'Hum, %r is a callable, but not a function/method, nor a instance with __call__ arg...'
             % acallable)
    if vargs or vkwargs:
        raise SyntaxError('variable *arg or **kwarg are not supported.')
    if is_bound(acallable):
        args = args[1:]
    if defaults is None:
        defaults = ()
    return args, defaults