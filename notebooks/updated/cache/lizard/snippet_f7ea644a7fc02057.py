def get_system_config_directory():
    if platform.system().lower() == 'windows':
        _cfg_directory = Path(os.getenv('APPDATA') or '~')
    elif platform.system().lower() == 'darwin':
        _cfg_directory = Path('~', 'Library', 'Preferences')
    else:
        _cfg_directory = Path(os.getenv('XDG_CONFIG_HOME') or '~/.config')
    logger.debug('Fetching configt directory for {}.'.format(platform.system())
        )
    return _cfg_directory.joinpath(Path('mayalauncher/.config'))