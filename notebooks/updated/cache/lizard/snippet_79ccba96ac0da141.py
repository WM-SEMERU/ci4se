def get_default_config(self):
    config = super(TwemproxyCollector, self).get_default_config()
    config.update({'path': 'twemproxy', 'hosts': ['localhost:22222']})
    return config