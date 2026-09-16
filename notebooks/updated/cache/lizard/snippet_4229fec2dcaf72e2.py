def lu_factor(A, rho, check_finite=True):
    r
    N, M = A.shape
    if N >= M:
        lu, piv = linalg.lu_factor(A.T.dot(A) + rho * np.identity(M, dtype=
            A.dtype), check_finite=check_finite)
    else:
        lu, piv = linalg.lu_factor(A.dot(A.T) + rho * np.identity(N, dtype=
            A.dtype), check_finite=check_finite)
    return lu, piv