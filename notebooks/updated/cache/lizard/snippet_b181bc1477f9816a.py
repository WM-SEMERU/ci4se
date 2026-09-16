def get_root_path(obj):
    try:
        filename = os.path.abspath(obj.__globals__['__file__'])
    except (KeyError, AttributeError):
        if getattr(obj, '__wrapped__', None):
            return get_root_path(obj.__wrapped__)
        filename = inspect.getfile(obj)
    return os.path.dirname(filename)