def inner(*args):
    haspoly = sum([isinstance(arg, Poly) for arg in args])
    if not haspoly:
        return numpy.sum(numpy.prod(args, 0), 0)
    out = args[0]
    for arg in args[1:]:
        out = out * arg
    return sum(out)