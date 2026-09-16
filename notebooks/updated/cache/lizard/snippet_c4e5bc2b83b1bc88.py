def implemented(cls, for_type):
    for function in cls.required():
        if not function.implemented_for_type(for_type):
            raise TypeError(
                "%r doesn't implement %r so it cannot participate in the protocol %r."
                 % (for_type, function.func.__name__, cls))
    cls.register(for_type)