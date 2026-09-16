def check_config(config, data):
    essential_keys = ['input_mmin', 'b-value', 'sigma-b']
    for key in essential_keys:
        if not key in config.keys():
            raise ValueError(
                'For KijkoSellevolBayes the key %s needs to be set in the configuation'
                 % key)
    if 'tolerance' not in config.keys() or not config['tolerance']:
        config['tolerance'] = 1e-05
    if not config.get('maximum_iterations', False):
        config['maximum_iterations'] = 1000
    if config['input_mmin'] < np.min(data['magnitude']):
        config['input_mmin'] = np.min(data['magnitude'])
    if fabs(config['sigma-b'] < 1e-15):
        raise ValueError('Sigma-b must be greater than zero!')
    return config