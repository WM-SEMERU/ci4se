def remove_setting(self, section, name, save=False):
    configfile = get_configfile()
    return _remove_setting(section, name, configfile, save)