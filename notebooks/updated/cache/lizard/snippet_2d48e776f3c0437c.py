def is_type(value):
    if isinstance(value, type):
        return issubclass(value, Type)
    return isinstance(value, Type)