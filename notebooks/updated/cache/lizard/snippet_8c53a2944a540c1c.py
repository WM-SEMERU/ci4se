def flatten(vari):
    if isinstance(vari, Poly):
        shape = int(numpy.prod(vari.shape))
        return reshape(vari, (shape,))
    return numpy.array(vari).flatten()