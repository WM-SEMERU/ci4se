def calc_bca_interval(bootstrap_replicates, jackknife_replicates,
    mle_params, conf_percentage):
    check_conf_percentage_validity(conf_percentage)
    ensure_samples_is_ndim_ndarray(bootstrap_replicates, ndim=2)
    ensure_samples_is_ndim_ndarray(jackknife_replicates, name='jackknife',
        ndim=2)
    alpha_percent = get_alpha_from_conf_percentage(conf_percentage)
    bias_correction = calc_bias_correction_bca(bootstrap_replicates, mle_params
        )
    acceleration = calc_acceleration_bca(jackknife_replicates)
    lower_percents = calc_lower_bca_percentile(alpha_percent,
        bias_correction, acceleration)
    upper_percents = calc_upper_bca_percentile(alpha_percent,
        bias_correction, acceleration)
    lower_endpoints = np.diag(np.percentile(bootstrap_replicates,
        lower_percents, interpolation='lower', axis=0))
    upper_endpoints = np.diag(np.percentile(bootstrap_replicates,
        upper_percents, interpolation='higher', axis=0))
    conf_intervals = combine_conf_endpoints(lower_endpoints, upper_endpoints)
    return conf_intervals