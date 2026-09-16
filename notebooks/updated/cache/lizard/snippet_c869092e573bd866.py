def __option(self):
    section = self.section()
    option = self.option_prefix()
    if self.config().has_option(section, option) is False:
        raise NoOptionError(option, section)
    return section, option