def find_and_parse_config(config, default_config='default.yaml'):

    def load_config(path):
        if os.path.isfile(path):
            with open(path, 'r') as f:
                config_dict_ = yaml.load(f)
            return config_dict_
    config_path = find_file(config)
    default_path = find_file(default_config)
    config = load_config(config_path)
    default_config = load_config(default_path)
    if config is None and default_config is None:
        raise ValueError('Both config and default_config return None')
    if config is None:
        config_dict = default_config
    elif default_config is None:
        config_dict = config
    else:
        config_dict = merge(default_config, config)
    return config_dict