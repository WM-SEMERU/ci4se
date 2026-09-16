def independentlinear60(display=False):
    old_seed = np.random.seed()
    np.random.seed(0)
    N = 1000
    M = 60
    beta = np.zeros(M)
    beta[0:30:3] = 1
    f = lambda X: np.matmul(X, beta)
    X_start = np.random.randn(N, M)
    X = X_start - X_start.mean(0)
    y = f(X) + np.random.randn(N) * 0.01
    np.random.seed(old_seed)
    return pd.DataFrame(X), y