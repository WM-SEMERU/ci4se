def squash(self, a, b):
    return (''.join(x) if isinstance(x, tuple) else x for x in itertools.
        product(a, b))