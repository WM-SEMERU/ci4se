def cluster_kmeans(data=None, k=None, max_iter=10, tolerance=1e-05, stride=
    1, metric='euclidean', init_strategy='kmeans++', fixed_seed=False,
    n_jobs=None, chunksize=None, skip=0, keep_data=False, clustercenters=
    None, **kwargs):
    r
    from pyemma.coordinates.clustering.kmeans import KmeansClustering
    res = KmeansClustering(n_clusters=k, max_iter=max_iter, metric=metric,
        tolerance=tolerance, init_strategy=init_strategy, fixed_seed=
        fixed_seed, n_jobs=n_jobs, skip=skip, keep_data=keep_data,
        clustercenters=clustercenters, stride=stride)
    from pyemma.util.reflection import get_default_args
    cs = _check_old_chunksize_arg(chunksize, get_default_args(
        cluster_kmeans)['chunksize'], **kwargs)
    if data is not None:
        res.estimate(data, chunksize=cs)
    else:
        res.chunksize = cs
    return res