def ara_config(key, env_var, default, section='ara', value_type=None):
    path = find_ini_config_file()
    config = configparser.ConfigParser()
    if path is not None:
        config.read(path)
    return get_config(config, section, key, env_var, default, value_type=
        value_type)