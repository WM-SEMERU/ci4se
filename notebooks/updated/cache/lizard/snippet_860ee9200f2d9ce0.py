def ctimes(*args):
    n = len(args)
    if n == 0:
        return np.asarray(0)
    elif n == 1:
        return np.asarray(args[0])
    elif n > 2:
        return reduce(plus, args)
    a, b = args
    if sps.issparse(a):
        return a.multiply(b)
    elif sps.issparse(b):
        return b.multiply(a)
    else:
        return np.asarray(a) * b