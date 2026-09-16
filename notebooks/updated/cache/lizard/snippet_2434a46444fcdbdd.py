def unwrap_obj(obj):
    try:
        obj = obj.fget
    except (AttributeError, TypeError):
        pass
    try:
        if obj.func.__doc__ == obj.__doc__:
            obj = obj.func
    except AttributeError:
        pass
    try:
        obj = obj.getter
    except AttributeError:
        pass
    try:
        obj = inspect.unwrap(obj)
    except:
        pass
    return obj