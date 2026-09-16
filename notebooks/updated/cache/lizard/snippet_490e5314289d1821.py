def _flatten_per_cluster(per_cluster):
    return np.sort(np.concatenate(list(per_cluster.values()))).astype(np.int64)