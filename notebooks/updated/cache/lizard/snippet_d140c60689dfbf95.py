def get_locations():
    home_dir = _path.expanduser('~')
    conf_dir = _path.join(_environ.get('XDG_CONFIG_HOME', _path.join(
        home_dir, '.config')), IDENT)
    data_dir = _path.join(_environ.get('XDG_DATA_HOME', _path.join(home_dir,
        '.local', 'share')), IDENT)
    return {'home_dir': home_dir, 'call_dir': _path.dirname(_path.abspath(
        _argv[0])), 'conf_dir': conf_dir, 'data_dir': data_dir}