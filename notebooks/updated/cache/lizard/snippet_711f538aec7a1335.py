def get_default_config(self):
    config = super(NfsCollector, self).get_default_config()
    config.update({'path': 'nfs'})
    return config