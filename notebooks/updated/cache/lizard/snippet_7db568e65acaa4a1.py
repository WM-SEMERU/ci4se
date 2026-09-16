def _joint_probabilities_nn(distances, neighbors, desired_perplexity, verbose):
    t0 = time()
    n_samples, k = neighbors.shape
    distances = distances.astype(np.float32, copy=False)
    neighbors = neighbors.astype(np.int64, copy=False)
    conditional_P = _utils._binary_search_perplexity(distances, neighbors,
        desired_perplexity, verbose)
    assert np.all(np.isfinite(conditional_P)
        ), 'All probabilities should be finite'
    P = csr_matrix((conditional_P.ravel(), neighbors.ravel(), range(0, 
        n_samples * k + 1, k)), shape=(n_samples, n_samples))
    P = P + P.T
    sum_P = np.maximum(P.sum(), MACHINE_EPSILON)
    P /= sum_P
    assert np.all(np.abs(P.data) <= 1.0)
    if verbose >= 2:
        duration = time() - t0
        print('[t-SNE] Computed conditional probabilities in {:.3f}s'.
            format(duration))
    return P