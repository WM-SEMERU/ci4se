def parse_config(self, config_source):
    self.log('Config   %s' % config_source)
    try:
        raw_config = configparser.RawConfigParser()
        raw_config.read(config_source)
    except Exception as e:
        raise RuntimeError('Invalid configuration file: %s' % e)
    config = {}
    config['source'] = raw_config.get('landslide', 'source').replace('\r', ''
        ).split('\n')
    if raw_config.has_option('landslide', 'theme'):
        config['theme'] = raw_config.get('landslide', 'theme')
        self.log('Using    configured theme %s' % config['theme'])
    if raw_config.has_option('landslide', 'destination'):
        config['destination'] = raw_config.get('landslide', 'destination')
    if raw_config.has_option('landslide', 'linenos'):
        config['linenos'] = raw_config.get('landslide', 'linenos')
    for boolopt in ('embed', 'relative', 'copy_theme'):
        if raw_config.has_option('landslide', boolopt):
            config[boolopt] = raw_config.getboolean('landslide', boolopt)
    if raw_config.has_option('landslide', 'extensions'):
        config['extensions'] = ','.join(raw_config.get('landslide',
            'extensions').replace('\r', '').split('\n'))
    if raw_config.has_option('landslide', 'css'):
        config['css'] = raw_config.get('landslide', 'css').replace('\r', ''
            ).split('\n')
    if raw_config.has_option('landslide', 'js'):
        config['js'] = raw_config.get('landslide', 'js').replace('\r', ''
            ).split('\n')
    return config