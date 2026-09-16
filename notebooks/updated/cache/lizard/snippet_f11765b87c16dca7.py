def get_default_config_file(rootdir=None):
    if rootdir is None:
        return DEFAULT_CONFIG_FILE
    for path in CONFIG_FILES:
        path = os.path.join(rootdir, path)
        if os.path.isfile(path) and os.access(path, os.R_OK):
            return path