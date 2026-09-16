def standard_aggregation(C):
    if not isspmatrix_csr(C):
        raise TypeError('expected csr_matrix')
    if C.shape[0] != C.shape[1]:
        raise ValueError('expected square matrix')
    index_type = C.indptr.dtype
    num_rows = C.shape[0]
    Tj = np.empty(num_rows, dtype=index_type)
    Cpts = np.empty(num_rows, dtype=index_type)
    fn = amg_core.standard_aggregation
    num_aggregates = fn(num_rows, C.indptr, C.indices, Tj, Cpts)
    Cpts = Cpts[:num_aggregates]
    if num_aggregates == 0:
        return csr_matrix((num_rows, 1), dtype='int8'), np.array([], dtype=
            index_type)
    else:
        shape = num_rows, num_aggregates
        if Tj.min() == -1:
            mask = Tj != -1
            row = np.arange(num_rows, dtype=index_type)[mask]
            col = Tj[mask]
            data = np.ones(len(col), dtype='int8')
            return coo_matrix((data, (row, col)), shape=shape).tocsr(), Cpts
        else:
            Tp = np.arange(num_rows + 1, dtype=index_type)
            Tx = np.ones(len(Tj), dtype='int8')
            return csr_matrix((Tx, Tj, Tp), shape=shape), Cpts