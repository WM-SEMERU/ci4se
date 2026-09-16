def prox_max_entropy(X, step, gamma=1):
    from scipy.special import lambertw
    gamma_ = _step_gamma(step, gamma)
    above = X > 0
    X[above] = gamma_ * np.real(lambertw(np.exp(X[above] / gamma_ - 1) /
        gamma_))
    return X