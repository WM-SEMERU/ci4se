def get(self, var, section=None, **kwargs):
    if not section and self.section:
        section = self.section
    default = kwargs.get('default', None)
    env_var = '{}{}{}'.format(_suffix(self.prefix) if self.prefix else '', 
        _suffix(alphasnake(section)) if section else '', alphasnake(str(var))
        ).upper()
    config = self.config.get(section, {}) if section else self.config
    result = config.get(var, default)
    result = os.getenv(env_var, default=result)
    if result is None and 'default' not in kwargs:
        msg = "Could not find '{}'".format(var)
        if section:
            msg = "{} in section '{}'.".format(msg, section)
        msg = '{} Checked environment variable: {}'.format(msg, env_var)
        if self.config_file:
            msg = '{} and file: {}'.format(msg, self.config_file)
        raise ConfigError(msg)
    return result