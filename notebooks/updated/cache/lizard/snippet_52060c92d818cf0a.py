def is_iterable_but_not_string(obj):
    return hasattr(obj, '__iter__') and not isinstance(obj, str
        ) and not isinstance(obj, bytes)