def compose(*functions):

    def inner(func1, func2):
        return lambda *x, **y: func1(func2(*x, **y))
    return functools.reduce(inner, functions)