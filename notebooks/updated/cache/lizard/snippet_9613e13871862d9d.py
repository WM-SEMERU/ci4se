def BetaPrime(alpha, beta, tag=None):
    assert alpha > 0 and beta > 0, 'BetaPrime "alpha" and "beta" parameters must be greater than zero'
    x = Beta(alpha, beta, tag)
    return x / (1 - x)