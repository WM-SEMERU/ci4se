def get_default_config(self):
    config = super(ExampleCollector, self).get_default_config()
    config.update({'path': 'example'})
    return config