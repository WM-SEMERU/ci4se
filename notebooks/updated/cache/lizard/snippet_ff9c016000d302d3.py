def get_default_config(self):
    config = super(SockstatCollector, self).get_default_config()
    config.update({'path': 'sockets'})
    return config