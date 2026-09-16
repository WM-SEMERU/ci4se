def PCA_reduce(X, Q):
    assert Q <= X.shape[1], 'Cannot have more latent dimensions than observed'
    evals, evecs = np.linalg.eigh(np.cov(X.T))
    W = evecs[:, -Q:]
    return (X - X.mean(0)).dot(W)