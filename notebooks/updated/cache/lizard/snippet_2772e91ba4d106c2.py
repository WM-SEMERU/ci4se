def bincount(dig, weight, minlength):
    if numpy.isscalar(weight):
        return numpy.bincount(dig, minlength=minlength) * weight
    else:
        return numpy.bincount(dig, weight, minlength)