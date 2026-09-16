def memoize_nonzero(func):


    class _memorizer(dict):

        def __init__(self, func):
            self.func = func

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            ret = self[key] = self.func(*key)
            return ret
    return _memorizer(func)