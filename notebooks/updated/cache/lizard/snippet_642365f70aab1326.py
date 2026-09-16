def debug(function):

    @wraps(function)
    def _wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        for key, value in kwargs.items():
            args += tuple(['{}={!r}'.format(key, value)])
        if len(args) == 1:
            args = '({})'.format(args[0])
        print('@{0}{1} -> {2}'.format(function.__name__, args, result))
        _wrapper.last_output = [function.__name__, str(args), result]
        return result
    _wrapper.last_output = []
    return _wrapper