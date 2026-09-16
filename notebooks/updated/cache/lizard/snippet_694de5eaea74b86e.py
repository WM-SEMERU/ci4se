def cluster_regspace(data=None, dmin=-1, max_centers=1000, stride=1, metric
    ='euclidean', n_jobs=None, chunksize=None, skip=0, **kwargs):
    r
    if dmin == -1:
        raise ValueError('provide a minimum distance for clustering, e.g. 2.0')
    from pyemma.coordinates.clustering.regspace import RegularSpaceClustering as _RegularSpaceClustering
    res = _RegularSpaceClustering(dmin, max_centers=max_centers, metric=
        metric, n_jobs=n_jobs, stride=stride, skip=skip)
    from pyemma.util.reflection import get_default_args
    cs = _check_old_chunksize_arg(chunksize, get_default_args(
        cluster_regspace)['chunksize'], **kwargs)
    if data is not None:
        res.estimate(data, chunksize=cs)
    else:
        res.chunksize = cs
    return res