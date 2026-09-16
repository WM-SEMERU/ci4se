def _pad(X):
    p_above = int(np.floor(np.log2(X.shape[1])))
    M = 2 ** (p_above + 1) - X.shape[1]
    X = np.hstack((np.zeros((X.shape[0], M)), X))
    return X, M