def effsnr(snr, reduced_x2, fac=250.0):
    snr = numpy.array(snr, ndmin=1, dtype=numpy.float64)
    rchisq = numpy.array(reduced_x2, ndmin=1, dtype=numpy.float64)
    esnr = snr / (1 + snr ** 2 / fac) ** 0.25 / rchisq ** 0.25
    if hasattr(snr, '__len__'):
        return esnr
    else:
        return esnr[0]