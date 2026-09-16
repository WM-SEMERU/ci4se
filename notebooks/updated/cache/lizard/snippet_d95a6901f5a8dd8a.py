def meter_calls_with_dims(**dims):

    def meter_wrapper(fn):

        @functools.wraps(fn)
        def fn_wrapper(*args, **kwargs):
            meter('%s_calls' % pyformance.registry.get_qualname(fn), **dims
                ).mark()
            return fn(*args, **kwargs)
        return fn_wrapper
    return meter_wrapper