def nearest_neighbors(query_pts, target_pts=None, metric='euclidean', k=
    None, epsilon=None, return_dists=False, precomputed=False):
    if k is None and epsilon is None:
        raise ValueError('Must provide `k` or `epsilon`.')
    precomputed = precomputed or metric == 'precomputed'
    if precomputed and target_pts is not None:
        raise ValueError(
            '`target_pts` cannot be used with precomputed distances')
    query_pts = np.array(query_pts)
    if len(query_pts.shape) == 1:
        query_pts = query_pts.reshape((1, -1))
    if precomputed:
        dists = query_pts.copy()
    else:
        dists = pairwise_distances(query_pts, Y=target_pts, metric=metric)
    if epsilon is not None:
        if k is not None:
            _, not_nn = _min_k_indices(dists, k, inv_ind=True)
            dists[np.arange(dists.shape[0]), not_nn.T] = np.inf
        is_close = dists <= epsilon
        if return_dists:
            nnis, nnds = [], []
            for i, row in enumerate(is_close):
                nns = np.nonzero(row)[0]
                nnis.append(nns)
                nnds.append(dists[i, nns])
            return nnds, nnis
        return np.array([np.nonzero(row)[0] for row in is_close])
    nns = _min_k_indices(dists, k)
    if return_dists:
        row_inds = np.arange(len(nns))[:, (np.newaxis)]
        nn_dists = dists[row_inds, nns]
        return nn_dists, nns
    return nns