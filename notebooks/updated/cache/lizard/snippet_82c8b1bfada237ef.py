def read_boolean_option(self, section, option):
    if self.has_option(section, option):
        self.config[option] = self.getboolean(section, option)