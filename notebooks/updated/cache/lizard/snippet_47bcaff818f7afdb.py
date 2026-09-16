def parametrized_class(decorator):

    def decorator_builder(*args, **kwargs):

        def meta_decorator(cls):
            return decorator(cls, *args, **kwargs)
        return meta_decorator
    return decorator_builder