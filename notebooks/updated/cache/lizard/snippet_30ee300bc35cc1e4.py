def from_sparse(m, order=None, out=None):
    import scipy.sparse
    if not scipy.sparse.isspmatrix(m):
        raise ValueError('not a sparse matrix: %r' % m)
    data = m.toarray(order=order, out=out)
    h = HaplotypeArray(data)
    return h