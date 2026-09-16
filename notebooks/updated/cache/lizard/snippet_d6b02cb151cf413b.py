def _dual_decorator(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        if len(args) == 1 and not kwargs and callable(args[0]) and not (
            type(args[0]) == type and issubclass(args[0], BaseException)):
            return func()(args[0])
        elif len(args) == 2 and inspect.isclass(args[0]) and callable(args[1]):
            return func(args[0], **kwargs)(args[1])
        else:
            return func(*args, **kwargs)
    return inner