def listify(generator_func):

    def list_func(*args, **kwargs):
        return degenerate(generator_func(*args, **kwargs))
    return list_func