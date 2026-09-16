def setdim(P, dim=None):
    P = P.copy()
    ldim = P.dim
    if not dim:
        dim = ldim + 1
    if dim == ldim:
        return P
    P.dim = dim
    if dim > ldim:
        key = numpy.zeros(dim, dtype=int)
        for lkey in P.keys:
            key[:ldim] = lkey
            P.A[tuple(key)] = P.A.pop(lkey)
    else:
        key = numpy.zeros(dim, dtype=int)
        for lkey in P.keys:
            if not sum(lkey[ldim - 1:]) or not sum(lkey):
                P.A[lkey[:dim]] = P.A.pop(lkey)
            else:
                del P.A[lkey]
    P.keys = sorted(P.A.keys(), key=sort_key)
    return P