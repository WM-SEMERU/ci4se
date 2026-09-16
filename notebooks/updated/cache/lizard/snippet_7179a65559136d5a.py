def get_current_config_value(self, config_key, use_preliminary=True,
    default=None):
    if use_preliminary and config_key in self.preliminary_config:
        return copy(self.preliminary_config[config_key])
    return copy(self.config.get_config_value(config_key, default))