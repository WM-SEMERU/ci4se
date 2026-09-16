def register_output_format(name):

    def check_decorator(fn):
        _output_format_map[name] = fn

        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper
    return check_decorator