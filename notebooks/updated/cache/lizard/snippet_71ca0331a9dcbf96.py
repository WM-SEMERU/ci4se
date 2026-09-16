def _parse_config(config_file_path):
    config_file = open(config_file_path, 'r')
    config = yaml.load(config_file)
    config_file.close()
    return config