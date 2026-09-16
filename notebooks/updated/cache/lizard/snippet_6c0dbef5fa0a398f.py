def get_config_value(self, section_name, option, default_option='default'):
    if self.config is None:
        self.config = configparser.ConfigParser()
        self.config.read(self.ini_file_name)
    if option:
        try:
            return self.config.get(section_name, option)
        except configparser.NoOptionError:
            log.debug(
                "Didn't find a configuration option for '%s' section and '%s' option"
                , section_name, option)
    return self.config.get(section_name, default_option)