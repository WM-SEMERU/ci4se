def diffusion_mds(means, weights, d, diffusion_rounds=10):
    for i in range(diffusion_rounds):
        weights = weights * weights
        weights = weights / weights.sum(0)
    X = dim_reduce(means, weights, d)
    if X.shape[0] == 2:
        return X.dot(weights)
    else:
        return X.T.dot(weights)