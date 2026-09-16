def get_client_settings_config_file(**kwargs):
    config_files = ['/etc/softlayer.conf', '~/.softlayer']
    if kwargs.get('config_file'):
        config_files.append(kwargs.get('config_file'))
    config_files = [os.path.expanduser(f) for f in config_files]
    config = utils.configparser.RawConfigParser({'username': '', 'api_key':
        '', 'endpoint_url': '', 'timeout': '0', 'proxy': ''})
    config.read(config_files)
    if config.has_section('softlayer'):
        return {'endpoint_url': config.get('softlayer', 'endpoint_url'),
            'timeout': config.getfloat('softlayer', 'timeout'), 'proxy':
            config.get('softlayer', 'proxy'), 'username': config.get(
            'softlayer', 'username'), 'api_key': config.get('softlayer',
            'api_key')}