def inline_requests(method_or_func):
    args = get_args(method_or_func)
    if not args:
        raise TypeError('Function must accept at least one argument.')
    if args[0] == 'self':

        def wrapper(self, response, **kwargs):
            callback = create_bound_method(method_or_func, self)
            genwrapper = RequestGenerator(callback, **kwargs)
            return genwrapper(response)
    else:
        warnings.warn('Decorating a non-method function will be deprecated',
            ScrapyDeprecationWarning, stacklevel=1)

        def wrapper(response, **kwargs):
            genwrapper = RequestGenerator(method_or_func, **kwargs)
            return genwrapper(response)
    return wraps(method_or_func)(wrapper)