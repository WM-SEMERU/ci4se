def count_calls_with_dims(**dims):

    def counter_wrapper(fn):

        @functools.wraps(fn)
        def fn_wrapper(*args, **kwargs):
            counter('%s_calls' % pyformance.registry.get_qualname(fn), **dims
                ).inc()
            return fn(*args, **kwargs)
        return fn_wrapper
    return counter_wrapper