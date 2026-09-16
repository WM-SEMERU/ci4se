def add_bias(X):
    return numpy.hstack((numpy.ones((len(X), 1), dtype=X.dtype), X))