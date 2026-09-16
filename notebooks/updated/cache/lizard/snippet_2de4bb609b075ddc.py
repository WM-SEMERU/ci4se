def major_axes(ell):
    _ = ell[:-1, :-1]
    U, s, V = N.linalg.svd(_)
    scalar = -(ell.sum() - _.sum())
    return N.sqrt(s * scalar) * V