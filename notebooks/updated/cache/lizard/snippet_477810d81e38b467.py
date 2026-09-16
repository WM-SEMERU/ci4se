def correlation(T, obs1, obs2=None, times=1, maxtime=None, k=None, ncv=None,
    return_times=False):
    r
    T = _types.ensure_ndarray_or_sparse(T, ndim=2, uniform=True, kind='numeric'
        )
    n = T.shape[0]
    obs1 = _types.ensure_ndarray(obs1, ndim=1, size=n, kind='numeric')
    obs2 = _types.ensure_ndarray_or_None(obs2, ndim=1, size=n, kind='numeric')
    times = _types.ensure_int_vector(times, require_order=True)
    if _issparse(T):
        return sparse.fingerprints.correlation(T, obs1, obs2=obs2, times=
            times, k=k, ncv=ncv)
    else:
        return dense.fingerprints.correlation(T, obs1, obs2=obs2, times=
            times, k=k)