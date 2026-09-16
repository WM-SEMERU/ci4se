def RS(S, second_pass=False):
    if not isspmatrix_csr(S):
        raise TypeError('expected csr_matrix')
    S = remove_diagonal(S)
    T = S.T.tocsr()
    splitting = np.empty(S.shape[0], dtype='intc')
    influence = np.zeros((S.shape[0],), dtype='intc')
    amg_core.rs_cf_splitting(S.shape[0], S.indptr, S.indices, T.indptr, T.
        indices, influence, splitting)
    if second_pass:
        amg_core.rs_cf_splitting_pass2(S.shape[0], S.indptr, S.indices,
            splitting)
    return splitting