def cache_for(**timedelta_kw):
    max_age_timedelta = timedelta(**timedelta_kw)

    def decorate_func(func):

        @wraps(func)
        def decorate_func_call(*a, **kw):
            callback = SetCacheControlHeadersFromTimedeltaCallback(
                max_age_timedelta)
            registry_provider = AfterThisRequestCallbackRegistryProvider()
            registry = registry_provider.provide()
            registry.add(callback)
            return func(*a, **kw)
        return decorate_func_call
    return decorate_func