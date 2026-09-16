def check_config(config):
    essential_keys = ['number_earthquakes']
    for key in essential_keys:
        if key not in config:
            raise ValueError(
                'For Kijko Nonparametric Gaussian the key %s needs to be set in the configuation'
                 % key)
    if config.get('tolerance', 0.0) <= 0.0:
        config['tolerance'] = 0.05
    if config.get('maximum_iterations', 0) < 1:
        config['maximum_iterations'] = 100
    if config.get('number_samples', 0) < 2:
        config['number_samples'] = 51
    return config