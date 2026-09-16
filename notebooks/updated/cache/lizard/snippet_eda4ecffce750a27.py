def SampleDist(samples, lo=None, up=None):
    samples = numpy.asarray(samples)
    if lo is None:
        lo = samples.min()
    if up is None:
        up = samples.max()
    try:
        dist = sample_dist(samples, lo, up)
    except numpy.linalg.LinAlgError:
        dist = Uniform(lower=-numpy.inf, upper=numpy.inf)
    return dist