def qnwlogn(n, mu=None, sig2=None):
    nodes, weights = qnwnorm(n, mu, sig2)
    return np.exp(nodes), weights