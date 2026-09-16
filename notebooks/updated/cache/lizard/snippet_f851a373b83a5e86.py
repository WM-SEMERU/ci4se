def coarsegrain(P, n):
    M = pcca(P, n)
    W = np.linalg.inv(np.dot(M.T, M))
    A = np.dot(np.dot(M.T, P), M)
    P_coarse = np.dot(W, A)
    from msmtools.analysis import stationary_distribution
    pi_coarse = np.dot(M.T, stationary_distribution(P))
    X = np.dot(np.diag(pi_coarse), P_coarse)
    P_coarse = X / X.sum(axis=1)[:, (None)]
    return P_coarse