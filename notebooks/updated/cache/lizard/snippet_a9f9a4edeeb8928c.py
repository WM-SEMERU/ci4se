def udf(f):

    @functools.wraps(f)
    def wrapper(*args):
        if any(arg is None for arg in args):
            return None
        return f(*args)
    _SQLITE_UDF_REGISTRY.add(wrapper)
    return wrapper