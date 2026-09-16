def local_minima(vector, min_distance=4, brd_mode='wrap'):
    fits = gaussian_filter(numpy.asarray(vector, dtype=numpy.float32), 1.0,
        mode=brd_mode)
    for ii in range(len(fits)):
        if fits[ii] == fits[ii - 1]:
            fits[ii - 1] = numpy.pi / 2.0
    minfits = minimum_filter(fits, size=min_distance, mode=brd_mode)
    minima_mask = fits == minfits
    minima = numpy.transpose(minima_mask.nonzero())
    return numpy.asarray(minima)