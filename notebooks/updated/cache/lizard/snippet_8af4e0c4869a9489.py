def get_default_config_help(self):
    config = super(StatsiteHandler, self).get_default_config_help()
    config.update({'host': '', 'tcpport': '', 'udpport': '', 'timeout': ''})
    return config