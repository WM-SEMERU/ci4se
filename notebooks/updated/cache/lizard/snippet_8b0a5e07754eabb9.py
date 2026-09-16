def show(config, section, opt):
    if section not in config.keys():
        raise ConfigError("section '{}' doesn't exist".format(section))
    if opt not in config[section].keys():
        raise ConfigError("option '{}.{}' doesn't exist".format(section, opt))
    logger.info(config[section][opt])