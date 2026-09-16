def is_generator_function(obj):
    CO_GENERATOR = 32
    return bool((inspect.isfunction(obj) or inspect.ismethod(obj)) and obj.
        func_code.co_flags & CO_GENERATOR)