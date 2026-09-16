def add_metaclass(metaclass):
    vars_to_skip = '__dict__', '__weakref__'

    def wrapper(cls):
        copied_dict = {key: value for key, value in cls.__dict__.items() if
            key not in vars_to_skip}
        return metaclass(cls.__name__, cls.__bases__, copied_dict)
    return wrapper