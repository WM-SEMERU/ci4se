def _compute_ranks(X, winsorize=False, truncation=None, verbose=True):
    n_samples, n_features = X.shape
    Xrank = np.zeros(shape=X.shape)
    if winsorize:
        if truncation is None:
            truncation = 1 / (4 * np.power(n_samples, 0.25) * np.sqrt(np.pi *
                np.log(n_samples)))
        elif truncation > 1:
            truncation = np.min(1.0, truncation)
    for col in np.arange(n_features):
        Xrank[:, (col)] = rankdata(X[:, (col)], method='average')
        Xrank[:, (col)] /= n_samples
        if winsorize:
            if n_samples > 100 * n_features:
                Xrank[:, (col)] = n_samples * Xrank[:, (col)] / (n_samples + 1)
            else:
                lower_truncate = Xrank[:, (col)] <= truncation
                upper_truncate = Xrank[:, (col)] > 1 - truncation
                Xrank[lower_truncate, col] = truncation
                Xrank[upper_truncate, col] = 1 - truncation
    return Xrank