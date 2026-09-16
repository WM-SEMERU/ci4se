def transpose(vari):
    if isinstance(vari, Poly):
        core = vari.A.copy()
        for key in vari.keys:
            core[key] = transpose(core[key])
        return Poly(core, vari.dim, vari.shape[::-1], vari.dtype)
    return numpy.transpose(vari)