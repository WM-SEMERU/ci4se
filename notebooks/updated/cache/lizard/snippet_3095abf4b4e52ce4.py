def _maximization_step(X, posteriors):
    sum_post_proba = np.sum(posteriors, axis=0)
    prior_proba = sum_post_proba / (sum_post_proba.sum() + Epsilon)
    means = np.dot(posteriors.T, X) / (sum_post_proba[:, (np.newaxis)] +
        Epsilon)
    n_components = posteriors.shape[1]
    n_features = X.shape[1]
    covars = np.empty(shape=(n_components, n_features, n_features), dtype=float
        )
    for i in range(n_components):
        post_i = posteriors[:, (i)]
        mean_i = means[i]
        diff_i = X - mean_i
        with np.errstate(under='ignore'):
            covar_i = np.dot(post_i * diff_i.T, diff_i) / (post_i.sum() +
                Epsilon)
        covars[i] = covar_i + Lambda * np.eye(n_features)
    _validate_params(prior_proba, means, covars)
    return prior_proba, means, covars