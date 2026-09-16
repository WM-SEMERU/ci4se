def brier_score(observations, forecasts):
    machine_eps = np.finfo(float).eps
    forecasts = np.asarray(forecasts)
    if (forecasts < 0.0).any() or (forecasts > 1.0 + machine_eps).any():
        raise ValueError(
            'forecasts must not be outside of the unit interval [0, 1]')
    observations = np.asarray(observations)
    if observations.ndim > 0:
        valid_obs = observations[~np.isnan(observations)]
    else:
        valid_obs = observations if not np.isnan(observations) else []
    if not set(np.unique(valid_obs)) <= {0, 1}:
        raise ValueError('observations can only contain 0, 1, or NaN')
    return (forecasts - observations) ** 2