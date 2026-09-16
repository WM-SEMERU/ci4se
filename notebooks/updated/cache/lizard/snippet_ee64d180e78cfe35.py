def get_config(self, key, default=None):
    for conf in (self.config, self.app.conifg):
        if key in conf:
            return conf[key]
    return default