def ridge_regression(X, Y, c1=0.0, c2=0.0, offset=None, ix=None):
    _, d = X.shape
    if c1 > 0 or c2 > 0:
        penalizer_matrix = (c1 + c2) * np.eye(d)
        A = np.dot(X.T, X) + penalizer_matrix
    else:
        A = np.dot(X.T, X)
    if offset is None or c2 == 0:
        b = np.dot(X.T, Y)
    else:
        b = np.dot(X.T, Y) + c2 * offset
    if ix is not None:
        M = np.c_[X.T[:, (ix)], b]
    else:
        M = np.c_[X.T, b]
    R = solve(A, M, assume_a='pos', check_finite=False)
    return R[:, (-1)], R[:, :-1]