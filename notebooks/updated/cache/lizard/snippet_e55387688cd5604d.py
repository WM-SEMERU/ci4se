def cutoff(poly, *args):
    if len(args) == 1:
        low, high = 0, args[0]
    else:
        low, high = args[:2]
    core_old = poly.A
    core_new = {}
    for key in poly.keys:
        if low <= numpy.sum(key) < high:
            core_new[key] = core_old[key]
    return Poly(core_new, poly.dim, poly.shape, poly.dtype)