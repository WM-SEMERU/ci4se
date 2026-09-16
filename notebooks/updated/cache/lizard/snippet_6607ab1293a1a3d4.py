def process(*args, **kwargs):
    timeout = kwargs.get('timeout')
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return _process_wrapper(args[0], timeout)
    else:
        if timeout is not None and not isinstance(timeout, (int, float)):
            raise TypeError('Timeout expected to be None or integer or float')

        def decorating_function(function):
            return _process_wrapper(function, timeout)
        return decorating_function