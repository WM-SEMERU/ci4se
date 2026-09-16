def make_trans_matrix(y, n_classes, dtype=np.float64):
    indices = np.empty(len(y), dtype=np.int32)
    for i in six.moves.xrange(len(y) - 1):
        indices[i] = y[i] * i + y[i + 1]
    indptr = np.arange(len(y) + 1)
    indptr[-1] = indptr[-2]
    return csr_matrix((np.ones(len(y), dtype=dtype), indices, indptr),
        shape=(len(y), n_classes ** 2))