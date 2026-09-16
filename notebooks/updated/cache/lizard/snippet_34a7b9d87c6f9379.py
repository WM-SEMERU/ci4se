def mul(a, b):
    if a is None:
        if b is None:
            return None
        else:
            return b
    elif b is None:
        return a
    return a * b