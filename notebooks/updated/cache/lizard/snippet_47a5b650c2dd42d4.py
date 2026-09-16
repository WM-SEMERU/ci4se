def stSpectralFlux(X, X_prev):
    sumX = numpy.sum(X + eps)
    sumPrevX = numpy.sum(X_prev + eps)
    F = numpy.sum((X / sumX - X_prev / sumPrevX) ** 2)
    return F