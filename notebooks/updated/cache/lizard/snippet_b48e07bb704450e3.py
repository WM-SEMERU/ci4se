def is_reversible(T, mu=None, tol=1e-12):
    r
    T = _types.ensure_ndarray_or_sparse(T, ndim=2, uniform=True, kind='numeric'
        )
    mu = _types.ensure_float_vector_or_None(mu, require_order=True)
    if _issparse(T):
        return sparse.assessment.is_reversible(T, mu, tol)
    else:
        return dense.assessment.is_reversible(T, mu, tol)