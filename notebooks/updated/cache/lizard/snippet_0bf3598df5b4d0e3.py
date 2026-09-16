def _pdist_scipy(x, exponent=1):
    metric = 'euclidean'
    if exponent != 1:
        metric = 'sqeuclidean'
    distances = _spatial.distance.pdist(x, metric=metric)
    distances = _spatial.distance.squareform(distances)
    if exponent != 1:
        distances **= exponent / 2
    return distances