def pair_distance_centile(X, centile, max_pairs=5000):
    N = X.shape[0]
    n_pairs = min(max_pairs, N ** 2)
    dists = np.zeros(n_pairs)
    for i in range(n_pairs):
        pair = np.random.randint(0, N, 2)
        pairdiff = X[(pair[0]), :] - X[(pair[1]), :]
        dists[i] = np.dot(pairdiff, pairdiff.T)
    dists.sort()
    out = dists[int(n_pairs * centile / 100.0)]
    return np.sqrt(out)