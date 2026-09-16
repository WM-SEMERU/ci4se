def set_config_from_envs(config):
    for section in config.sections():
        for token in config.options(section):
            set_config_token_from_env(section, token, config)