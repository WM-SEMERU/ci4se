def transform(self, func):
    if func.__code__.co_argcount == 1:
        oldfunc = func
        func = lambda t, rdd: oldfunc(rdd)
    assert func.__code__.co_argcount == 2, 'func should take one or two arguments'
    return TransformedDStream(self, func)