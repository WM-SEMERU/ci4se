def _create_main_config(cls, overrides=None):
    filepaths = []
    filepaths.append(get_module_root_config())
    filepath = os.getenv('REZ_CONFIG_FILE')
    if filepath:
        filepaths.extend(filepath.split(os.pathsep))
    filepath = os.path.expanduser('~/.rezconfig')
    filepaths.append(filepath)
    return Config(filepaths, overrides)