def get_default_config(self):
    config = super(MySQLHandler, self).get_default_config()
    config.update({})
    return config