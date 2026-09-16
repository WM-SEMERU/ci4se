def VarCircle(XY, Par):
    if type(XY) != numpy.ndarray:
        XY = numpy.array(XY)
    n = len(XY)
    if n < 4:
        raise Warning(
            'Circle cannot be calculated with less than 4 data points.  Please include more data'
            )
    Dx = XY[:, (0)] - Par[0]
    Dy = XY[:, (1)] - Par[1]
    D = numpy.sqrt(Dx * Dx + Dy * Dy) - Par[2]
    result = old_div(numpy.dot(D, D), n - 3)
    return result