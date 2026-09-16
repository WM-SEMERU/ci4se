def prod_sum_var(A, B):
    return A.multiply(B).sum(1).A1 if issparse(A) else np.einsum('ij, ij -> i',
        A, B)