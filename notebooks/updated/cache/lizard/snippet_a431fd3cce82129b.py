def get_hypergeometric_stats(N, indices):
    assert isinstance(N, (int, np.integer))
    assert isinstance(indices, np.ndarray) and np.issubdtype(indices.dtype,
        np.uint16)
    K = indices.size
    pvals = np.empty(N + 1, dtype=np.float64)
    folds = np.empty(N + 1, dtype=np.float64)
    pvals[0] = 1.0
    folds[0] = 1.0
    n = 0
    k = 0
    p = 1.0
    while n < N:
        if k < K and indices[k] == n:
            p *= float((n + 1) * (K - k)) / float((N - n) * (k + 1))
            k += 1
        else:
            p *= float((n + 1) * (N - K - n + k)) / float((N - n) * (n - k + 1)
                )
        n += 1
        pvals[n] = get_hgp(p, k, N, K, n)
        folds[n] = k / (K * (n / float(N)))
    return pvals, folds