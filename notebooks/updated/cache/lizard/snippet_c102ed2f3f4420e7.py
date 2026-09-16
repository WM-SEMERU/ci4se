def euclidean(h1, h2):
    r
    h1, h2 = __prepare_histogram(h1, h2)
    return math.sqrt(scipy.sum(scipy.square(scipy.absolute(h1 - h2))))