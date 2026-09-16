def impulse_deltav_general_curvedstream(v, x, b, w, x0, v0, pot):
    pot = flatten_potential(pot)
    if len(v.shape) == 1:
        v = numpy.reshape(v, (1, 3))
    if len(x.shape) == 1:
        x = numpy.reshape(x, (1, 3))
    b0 = numpy.cross(w, v0)
    b0 *= b / numpy.sqrt(numpy.sum(b0 ** 2))
    b_ = b0 + x - x0
    return numpy.array(list(map(lambda i: _deltav_integrate(0.0, i[1], i[0],
        pot), zip(w - v, b_))))