def stationary_distribution_sensitivity(T, j):
    r
    T = _types.ensure_ndarray_or_sparse(T, ndim=2, uniform=True, kind='numeric'
        )
    if _issparse(T):
        _showSparseConversionWarning()
        stationary_distribution_sensitivity(T.todense(), j)
    else:
        return dense.sensitivity.stationary_distribution_sensitivity(T, j)