def _validate_covars(covars, covariance_type, n_components):
    from scipy import linalg
    if covariance_type == 'spherical':
        if len(covars) != n_components:
            raise ValueError("'spherical' covars have length n_components")
        elif np.any(covars <= 0):
            raise ValueError("'spherical' covars must be non-negative")
    elif covariance_type == 'tied':
        if covars.shape[0] != covars.shape[1]:
            raise ValueError("'tied' covars must have shape (n_dim, n_dim)")
        elif not np.allclose(covars, covars.T) or np.any(linalg.eigvalsh(
            covars) <= 0):
            raise ValueError(
                "'tied' covars must be symmetric, positive-definite")
    elif covariance_type == 'diag':
        if len(covars.shape) != 2:
            raise ValueError(
                "'diag' covars must have shape (n_components, n_dim)")
        elif np.any(covars <= 0):
            raise ValueError("'diag' covars must be non-negative")
    elif covariance_type == 'full':
        if len(covars.shape) != 3:
            raise ValueError(
                "'full' covars must have shape (n_components, n_dim, n_dim)")
        elif covars.shape[1] != covars.shape[2]:
            raise ValueError(
                "'full' covars must have shape (n_components, n_dim, n_dim)")
        for n, cv in enumerate(covars):
            if not np.allclose(cv, cv.T) or np.any(linalg.eigvalsh(cv) <= 0):
                raise ValueError(
                    "component %d of 'full' covars must be symmetric, positive-definite"
                     % n)
    else:
        raise ValueError('covariance_type must be one of ' +
            "'spherical', 'tied', 'diag', 'full'")