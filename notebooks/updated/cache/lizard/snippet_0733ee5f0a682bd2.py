def as_dict(config):
    settings = defaultdict(lambda : {})
    for section in config.sections():
        for key, val in config.items(section):
            settings[section][key] = val
    return settings