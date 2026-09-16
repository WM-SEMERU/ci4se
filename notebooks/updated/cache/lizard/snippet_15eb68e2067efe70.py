def get_default_config(self):
    config = super(LibratoHandler, self).get_default_config()
    config.update({'user': '', 'apikey': '', 'apply_metric_prefix': False,
        'queue_max_size': 300, 'queue_max_interval': 60, 'include_filters':
        ['^.*']})
    return config