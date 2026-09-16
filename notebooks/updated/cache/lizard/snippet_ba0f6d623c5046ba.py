def generate_config_set(self, config):
    if isinstance(config, dict):
        self.config = [(config, 1.0)]
    elif isinstance(config, list):
        total_weight = 0.0
        self.config = []
        for params in config:
            weight = params['Model_Weight']
            total_weight += params['Model_Weight']
            self.config.append((params, weight))
        if fabs(total_weight - 1.0) > 1e-07:
            raise ValueError(
                'MFD config weights do not sum to 1.0 for fault %s' % self.id)
    else:
        raise ValueError('MFD config must be input as dictionary or list!')