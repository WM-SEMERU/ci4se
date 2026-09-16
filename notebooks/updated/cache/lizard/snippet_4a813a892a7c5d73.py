def scale_columns(A, v, copy=True):
    v = np.ravel(v)
    M, N = A.shape
    if not isspmatrix(A):
        raise ValueError('scale columns needs a sparse matrix')
    if N != len(v):
        raise ValueError('scale vector has incompatible shape')
    if copy:
        A = A.copy()
        A.data = np.asarray(A.data, dtype=upcast(A.dtype, v.dtype))
    else:
        v = np.asarray(v, dtype=A.dtype)
    if isspmatrix_csr(A):
        csr_scale_columns(M, N, A.indptr, A.indices, A.data, v)
    elif isspmatrix_bsr(A):
        R, C = A.blocksize
        bsr_scale_columns(int(M / R), int(N / C), R, C, A.indptr, A.indices,
            np.ravel(A.data), v)
    elif isspmatrix_csc(A):
        pyamg.amg_core.csc_scale_columns(M, N, A.indptr, A.indices, A.data, v)
    else:
        fmt = A.format
        A = scale_columns(csr_matrix(A), v).asformat(fmt)
    return A