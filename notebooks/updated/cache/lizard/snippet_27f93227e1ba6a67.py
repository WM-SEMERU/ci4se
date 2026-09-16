def steppify(x, y):
    dx = 0.5 * (x[1:] + x[:-1])
    xx = numpy.zeros(2 * len(dx), dtype=float)
    yy = numpy.zeros(2 * len(y), dtype=float)
    xx[0::2], xx[1::2] = dx, dx
    yy[0::2], yy[1::2] = y, y
    xx = numpy.concatenate(([x[0] - (dx[0] - x[0])], xx, [x[-1] + (x[-1] -
        dx[-1])]))
    return xx, yy