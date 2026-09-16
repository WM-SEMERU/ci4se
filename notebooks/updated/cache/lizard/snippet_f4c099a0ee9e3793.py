def geom_find_rotsymm(g, atwts, ax, improp, nmax=_DEF.SYMM_MATCH_NMAX, tol=
    _DEF.SYMM_MATCH_TOL):
    import numpy as np
    g = make_nd_vec(g, nd=None, t=np.float64, norm=False)
    ax = make_nd_vec(ax, nd=3, t=np.float64, norm=True)
    nval = nmax + 1
    nfac = 1.0
    while nfac > tol and nval > 0:
        nval = nval - 1
        try:
            nfac = geom_symm_match(g, atwts, ax, 2 * np.pi / nval, improp)
        except ZeroDivisionError as zde:
            if nval > 0:
                raise zde
    return nval, nfac