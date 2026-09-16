def scalarDecorator(func):

    @wraps(func)
    def scalar_wrapper(*args, **kwargs):
        if numpy.array(args[1]).shape == ():
            scalarOut = True
            args = args[0], numpy.array([args[1]])
        else:
            scalarOut = False
        result = func(*args, **kwargs)
        if scalarOut:
            return result[0]
        else:
            return result
    return scalar_wrapper