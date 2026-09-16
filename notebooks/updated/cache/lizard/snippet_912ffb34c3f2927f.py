def get_default_config(self):
    config = super(MesosCollector, self).get_default_config()
    config.update({'host': 'localhost', 'port': 5050, 'path': 'mesos',
        'master': True})
    return config