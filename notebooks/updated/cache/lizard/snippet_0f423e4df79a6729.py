def get_sample_stats_stan3(fit, model=None, log_likelihood=None):
    dtypes = {'divergent__': bool, 'n_leapfrog__': np.int64, 'treedepth__':
        np.int64}
    data = OrderedDict()
    for key in fit.sample_and_sampler_param_names:
        new_shape = -1, fit.num_chains
        values = fit._draws[fit._parameter_indexes(key)]
        values = values.reshape(new_shape, order='F')
        values = np.moveaxis(values, [-2, -1], [1, 0])
        dtype = dtypes.get(key)
        values = values.astype(dtype)
        name = re.sub('__$', '', key)
        name = 'diverging' if name == 'divergent' else name
        data[name] = values
    if log_likelihood is not None:
        log_likelihood_data = get_draws_stan3(fit, model=model, variables=
            log_likelihood)
        data['log_likelihood'] = log_likelihood_data[log_likelihood]
    return data