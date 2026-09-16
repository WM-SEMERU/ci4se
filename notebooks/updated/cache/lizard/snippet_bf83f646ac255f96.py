def estimate_cont_entropy(X, epsilon=None):
    X = asarray2d(X)
    n_samples, n_features = X.shape
    if n_samples <= 1:
        return 0
    nn = NearestNeighbors(metric='chebyshev', n_neighbors=NUM_NEIGHBORS,
        algorithm='kd_tree')
    nn.fit(X)
    if epsilon is None:
        n_neighbors = NUM_NEIGHBORS
        radius = 0
        while not np.all(radius) and n_neighbors < n_samples:
            distances, _ = nn.kneighbors(n_neighbors=n_neighbors,
                return_distance=True)
            radius = distances[:, (-1)]
            n_neighbors += 1
        if n_neighbors == n_samples:
            raise ValueError('Should not have discrete column to estimate')
        return -digamma(n_neighbors) + digamma(n_samples
            ) + n_features * np.mean(np.log(2 * radius))
    else:
        ind = nn.radius_neighbors(radius=epsilon.ravel(), return_distance=False
            )
        nx = np.array([i.size for i in ind])
        return -np.mean(digamma(nx + 1)) + digamma(n_samples)