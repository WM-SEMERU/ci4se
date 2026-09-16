def mag_pmf(matrix):
    nmags, ndists, nlons, nlats, neps = matrix.shape
    mag_pmf = numpy.zeros(nmags)
    for i in range(nmags):
        mag_pmf[i] = numpy.prod([(1.0 - matrix[i, j, k, l, m]) for j in
            range(ndists) for k in range(nlons) for l in range(nlats) for m in
            range(neps)])
    return 1.0 - mag_pmf