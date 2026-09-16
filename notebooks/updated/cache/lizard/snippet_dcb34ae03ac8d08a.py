def load_config(config_file, default_config_file, **kwargs):
    if config_file and not os.path.exists(config_file):
        msg = 'config file {} does not exist'.format(config_file)
        raise InsufficientConfiguration(msg)
    if (config_file is None and default_config_file is not None and os.path
        .exists(default_config_file)):
        config_file = default_config_file
    if config_file is not None:
        load_dotenv(config_file)
    _update_environment(**kwargs)