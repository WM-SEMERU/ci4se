def wrap_iterable(obj):
    was_scalar = not isiterable(obj)
    wrapped_obj = [obj] if was_scalar else obj
    return wrapped_obj, was_scalar