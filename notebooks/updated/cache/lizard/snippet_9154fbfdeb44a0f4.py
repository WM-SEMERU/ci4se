def particle_covariance_mtx(weights, locations):
    warnings.warn(
        'particle_covariance_mtx is deprecated, please use distributions.ParticleDistribution'
        , DeprecationWarning)
    mu = particle_meanfn(weights, locations)
    xs = locations.transpose([1, 0])
    ws = weights
    cov = np.einsum('i,mi,ni', ws, xs, xs) - np.dot(mu[..., np.newaxis], mu
        [np.newaxis, ...])
    assert np.all(np.isfinite(cov))
    if not np.all(la.eig(cov)[0] >= 0):
        warnings.warn(
            'Numerical error in covariance estimation causing positive semidefinite violation.'
            , ApproximationWarning)
    return cov