def _validate_params(priors, means, covars):
    for i, (p, m, cv) in enumerate(zip(priors, means, covars)):
        if np.any(np.isinf(p)) or np.any(np.isnan(p)):
            raise ValueError('Component %d of priors is not valid ' % i)
        if np.any(np.isinf(m)) or np.any(np.isnan(m)):
            raise ValueError('Component %d of means is not valid ' % i)
        if np.any(np.isinf(cv)) or np.any(np.isnan(cv)):
            raise ValueError('Component %d of covars is not valid ' % i)
        if not np.allclose(cv, cv.T) or np.any(scipy.linalg.eigvalsh(cv) <= 0):
            raise ValueError(
                'Component %d of covars must be positive-definite' % i)