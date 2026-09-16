def dot(a, b, ashape=None, bshape=None):
    a = to_potential(a)
    b = to_potential(b)
    if is_const_potential(a) and is_const_potential(b):
        return PotentialConstant(np.dot(a.c, b.c))
    else:
        return DotPotential(a, b, g_shape=ashape, h_shape=bshape)