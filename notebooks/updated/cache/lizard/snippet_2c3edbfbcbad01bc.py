def dir2cart(d):
    ints = numpy.ones(len(d)).transpose()
    d = numpy.array(d)
    rad = old_div(numpy.pi, 180.0)
    if len(d.shape) > 1:
        decs, incs = d[:, (0)] * rad, d[:, (1)] * rad
        if d.shape[1] == 3:
            ints = d[:, (2)]
    else:
        decs, incs = numpy.array(d[0]) * rad, numpy.array(d[1]) * rad
        if len(d) == 3:
            ints = numpy.array(d[2])
        else:
            ints = numpy.array([1.0])
    cart = numpy.array([ints * numpy.cos(decs) * numpy.cos(incs), ints *
        numpy.sin(decs) * numpy.cos(incs), ints * numpy.sin(incs)]).transpose()
    return cart