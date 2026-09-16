def hasvar(obj, var):
    if hasattr(obj, var):
        return not callable(getattr(obj, var))
    return False