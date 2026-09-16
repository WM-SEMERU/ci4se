def stZCR(frame):
    count = len(frame)
    countZ = numpy.sum(numpy.abs(numpy.diff(numpy.sign(frame)))) / 2
    return numpy.float64(countZ) / numpy.float64(count - 1.0)