def __kullback_leibler(h1, h2):
    result = h1.astype(scipy.float_)
    mask = h1 != 0
    result[mask] = scipy.multiply(h1[mask], scipy.log(h1[mask] / h2[mask]))
    return scipy.sum(result)