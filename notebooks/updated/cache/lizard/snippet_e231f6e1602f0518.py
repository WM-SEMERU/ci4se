def is_rate_matrix(K, tol):
    K = K.tocsr()
    row_sum = K.sum(axis=1)
    sum_eq_zero = np.allclose(row_sum, np.zeros(shape=row_sum.shape), atol=tol)
    org_diag = K.diagonal()
    K = K - diags(org_diag, 0)
    values = K.data
    values_gt_zero = np.allclose(values, np.abs(values), atol=tol)
    K = K + diags(org_diag, 0)
    return values_gt_zero and sum_eq_zero