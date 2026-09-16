def _orthogonalize(X):
    if X.size == X.shape[0]:
        return X
    from scipy.linalg import pinv, norm
    for i in range(1, X.shape[1]):
        X[:, (i)] -= np.dot(np.dot(X[:, (i)], X[:, :i]), pinv(X[:, :i]))
    return X