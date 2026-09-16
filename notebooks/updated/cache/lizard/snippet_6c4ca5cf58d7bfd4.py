def _timed(_logger=None, level='info'):

    def fun_wrapper(f):

        @functools.wraps(f)
        def wraps(*args, **kwargs):
            with _timer(f.__name__, _logger=logger, level=level):
                results = f(*args, **kwargs)
            return results
        return wraps
    return fun_wrapper