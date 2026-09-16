def as_uninitialized(fn):

    @wraps(fn)
    def override_initialization(self_, *args, **kw):
        parameterized_instance = self_.self
        original_initialized = parameterized_instance.initialized
        parameterized_instance.initialized = False
        fn(parameterized_instance, *args, **kw)
        parameterized_instance.initialized = original_initialized
    return override_initialization