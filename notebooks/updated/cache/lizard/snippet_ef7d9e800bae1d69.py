def prod(vari, axis=None):
    if isinstance(vari, Poly):
        if axis is None:
            vari = chaospy.poly.shaping.flatten(vari)
            axis = 0
        vari = chaospy.poly.shaping.rollaxis(vari, axis)
        out = vari[0]
        for poly in vari[1:]:
            out = out * poly
        return out
    return np.prod(vari, axis)