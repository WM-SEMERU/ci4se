def read_config(config_file):
    config = Storage({'cache_filename': '~/.aadbook_cache',
        'auth_db_filename': '~/.aadbook_auth.json', 'cache_expiry_hours': '24'}
        )
    config_file = os.path.expanduser(config_file)
    parser = _get_config(config_file)
    if parser:
        config.get_dict().update(dict(parser.items('DEFAULT', raw=True)))
    config.cache_filename = realpath(expanduser(config.cache_filename))
    config.auth_db_filename = realpath(expanduser(config.auth_db_filename))
    config.auth = Auth(config.auth_db_filename)
    config.encoding = ENCODING
    log.debug(config)
    return config