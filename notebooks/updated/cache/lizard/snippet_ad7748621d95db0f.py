def expected_counts_stationary(T, n, mu=None):
    r
    if n <= 0:
        EC = coo_matrix(T.shape, dtype=float)
        return EC
    else:
        if mu is None:
            mu = stationary_distribution(T)
        D_mu = diags(mu, 0)
        EC = n * D_mu.dot(T)
        return EC