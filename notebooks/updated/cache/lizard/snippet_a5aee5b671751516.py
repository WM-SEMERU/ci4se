def pitch(ax, ay, az):
    import numpy
    return numpy.arctan(ax, numpy.sqrt(ay ** 2 + az ** 2))