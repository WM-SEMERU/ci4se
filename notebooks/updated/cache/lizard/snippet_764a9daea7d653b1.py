def get_default_config(self):
    config = super(BeanstalkdCollector, self).get_default_config()
    config.update({'path': 'beanstalkd', 'host': 'localhost', 'port': 11300})
    return config