def get_default_config(self):
    default_config = super(WebsiteMonitorCollector, self).get_default_config()
    default_config['URL'] = ''
    default_config['path'] = 'websitemonitor'
    return default_config