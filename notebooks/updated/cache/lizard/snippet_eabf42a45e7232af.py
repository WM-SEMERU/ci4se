def _get_config_dirs():
    config_dirs = [USER_CONFIG_DIR, os.path.join('/', 'etc', 'rapport'), os
        .path.abspath(os.path.join('rapport', 'config'))]
    return config_dirs