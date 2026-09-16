def get_config_dict(self):
    return OrderedDict((prop, getattr(self, prop)) for prop in self.
        _instance.CONFIG_PARAMS)