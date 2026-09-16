def validate_check_configs(cls, config):
    if 'checks' not in config:
        raise ValueError('No checks defined.')
    if 'interval' not in config['checks']:
        raise ValueError('No check interval defined.')
    for check_name, check_config in six.iteritems(config['checks']):
        if check_name == 'interval':
            continue
        Check.from_config(check_name, check_config)