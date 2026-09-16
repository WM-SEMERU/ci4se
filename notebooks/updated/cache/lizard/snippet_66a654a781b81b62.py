def read_configuration(key, path=None, default=None, single_config=False,
    fallback_to_env=True):
    if path and os.path.exists(path):
        with open(path, 'r') as config_file:
            if single_config:
                return config_file.read()
            for line in config_file:
                if line.startswith('%s=' % key):
                    return line.split('=', 1)[1].strip()
    if fallback_to_env and key in os.environ:
        return os.environ[key]
    return default