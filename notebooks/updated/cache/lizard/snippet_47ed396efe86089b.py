def init_config(config_file=None):
    global config
    if config_file and os.path.exists(config_file):
        read = config.read([config_file])
        if not read:
            raise ValueError('Could not read configuration from file: %s' %
                config_file)