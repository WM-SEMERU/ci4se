def _get_plugin_dirs():
    plugin_dirs = [os.path.expanduser(os.path.join(USER_CONFIG_DIR,
        'plugins')), os.path.join('rapport', 'plugins')]
    return plugin_dirs