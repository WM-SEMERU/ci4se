def dot(a, b):
    if hasattr(a, '__dot__'):
        return a.__dot__(b)
    if a is None:
        return b
    else:
        raise ValueError(
            'Dot is waiting for two TT-vectors or two TT-    matrices')