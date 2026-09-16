def distance(a, b, metric='cosine'):
    if metric == 'cosine':
        return np.dot(a, b.T)
    raise Exception("Unknown metric '{metric}'".format(metric=metric))