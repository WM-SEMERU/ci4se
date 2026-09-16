def wraps(function):

    def wrap(decorator):
        decorator = functools.wraps(function)(decorator)
        if not hasattr(function, 'original'):
            decorator.original = function
        else:
            decorator.original = function.original
            delattr(function, 'original')
        return decorator
    return wrap