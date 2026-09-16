def patch_compat(config):
    if 'web_host' in config:
        config['host'] = config.pop('web_host')
    if 'web_port' in config:
        config['port'] = config.pop('web_port')