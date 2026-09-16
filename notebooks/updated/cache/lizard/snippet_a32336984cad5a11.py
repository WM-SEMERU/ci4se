def symmetric_rescaling(A, copy=True):
    if isspmatrix_csr(A) or isspmatrix_csc(A) or isspmatrix_bsr(A):
        if A.shape[0] != A.shape[1]:
            raise ValueError('expected square matrix')
        D = diag_sparse(A)
        mask = D != 0
        if A.dtype != complex:
            D_sqrt = np.sqrt(abs(D))
        else:
            D_sqrt = np.sqrt(D)
        D_sqrt_inv = np.zeros_like(D_sqrt)
        D_sqrt_inv[mask] = 1.0 / D_sqrt[mask]
        DAD = scale_rows(A, D_sqrt_inv, copy=copy)
        DAD = scale_columns(DAD, D_sqrt_inv, copy=False)
        return D_sqrt, D_sqrt_inv, DAD
    else:
        return symmetric_rescaling(csr_matrix(A))