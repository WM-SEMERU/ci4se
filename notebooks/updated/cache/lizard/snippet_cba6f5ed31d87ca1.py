def deprecated(text='', eos=''):

    def get_location():
        import inspect
        frame = inspect.currentframe()
        if frame:
            callstack = inspect.getouterframes(frame)[-1]
            return '%s:%i' % (callstack[1], callstack[2])
        else:
            stack = inspect.stack(0)
            entry = stack[2]
            return '%s:%i' % (entry[1], entry[2])

    def deprecated_inner(func):

        @functools.wraps(func)
        def new_func(*args, **kwargs):
            name = '{} [{}]'.format(func.__name__, get_location())
            log_deprecated(name, text, eos)
            return func(*args, **kwargs)
        return new_func
    return deprecated_inner