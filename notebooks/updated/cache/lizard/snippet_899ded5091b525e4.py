def get_default_config(self):
    config = super(MultiGraphiteHandler, self).get_default_config()
    config.update({'host': ['localhost'], 'port': 2003, 'proto': 'tcp',
        'timeout': 15, 'batch': 1, 'max_backlog_multiplier': 5,
        'trim_backlog_multiplier': 4})
    return config