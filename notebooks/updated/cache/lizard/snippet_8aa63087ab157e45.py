def name(function):
    if isinstance(function, types.FunctionType):
        return function.__name__
    else:
        return str(function)