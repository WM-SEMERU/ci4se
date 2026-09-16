def dump_func(serializer_type):

    def outer_wrapper(dumper_func):

        def wrapper(*args, **kwargs):
            return _dump(*args, dumper_func=dumper_func, serializer_type=
                serializer_type, **kwargs)
        return wrapper
    return outer_wrapper