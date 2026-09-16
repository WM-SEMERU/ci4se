def all_points_mutual_reachability(X, labels, cluster_id, metric=
    'euclidean', d=None, **kwd_args):
    if metric == 'precomputed':
        if d is None:
            raise ValueError(
                'If metric is precomputed a d value must be provided!')
        distance_matrix = X[(labels == cluster_id), :][:, (labels ==
            cluster_id)]
    else:
        subset_X = X[(labels == cluster_id), :]
        distance_matrix = pairwise_distances(subset_X, metric=metric, **
            kwd_args)
        d = X.shape[1]
    core_distances = all_points_core_distance(distance_matrix.copy(), d=d)
    core_dist_matrix = np.tile(core_distances, (core_distances.shape[0], 1))
    result = np.dstack([distance_matrix, core_dist_matrix, core_dist_matrix.T]
        ).max(axis=-1)
    return result, core_distances