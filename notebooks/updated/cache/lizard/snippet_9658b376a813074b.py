def _scipy_distribution_positional_args_from_dict(distribution, params):
    params['loc'] = params.get('loc', 0)
    if 'scale' not in params:
        params['scale'] = 1
    if distribution == 'norm':
        return params['mean'], params['std_dev']
    elif distribution == 'beta':
        return params['alpha'], params['beta'], params['loc'], params['scale']
    elif distribution == 'gamma':
        return params['alpha'], params['loc'], params['scale']
    elif distribution == 'uniform':
        return params['min'], params['max']
    elif distribution == 'chi2':
        return params['df'], params['loc'], params['scale']
    elif distribution == 'expon':
        return params['loc'], params['scale']