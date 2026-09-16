def pairwise_dxy(pos, gac, start=None, stop=None, is_accessible=None):
    if not isinstance(pos, SortedIndex):
        pos = SortedIndex(pos, copy=False)
    gac = asarray_ndim(gac, 3)
    gan = np.sum(gac, axis=2)
    m = gac.shape[1]
    dist = list()
    for i, j in itertools.combinations(range(m), 2):
        ac1 = gac[:, (i), (...)]
        an1 = gan[:, (i)]
        ac2 = gac[:, (j), (...)]
        an2 = gan[:, (j)]
        d = sequence_divergence(pos, ac1, ac2, an1=an1, an2=an2, start=
            start, stop=stop, is_accessible=is_accessible)
        dist.append(d)
    return np.array(dist)