def Beta(alpha, beta, low=0, high=1, tag=None):
    assert alpha > 0 and beta > 0, 'Beta "alpha" and "beta" parameters must be greater than zero'
    assert low < high, 'Beta "low" must be less than "high"'
    return uv(ss.beta(alpha, beta, loc=low, scale=high - low), tag=tag)