def precision(Ntp, Nsys, eps=numpy.spacing(1)):
    if Nsys == 0:
        return numpy.nan
    else:
        return float(Ntp / float(Nsys))