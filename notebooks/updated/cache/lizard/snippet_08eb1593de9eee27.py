def random_histogram(counts, nbins, seed):
    numpy.random.seed(seed)
    return numpy.histogram(numpy.random.random(counts), nbins, (0, 1))[0]