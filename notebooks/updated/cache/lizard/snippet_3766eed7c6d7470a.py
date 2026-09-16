def find_config():
    config_locations = ['/etc/foremast/foremast.cfg', expanduser(
        '~/.foremast/foremast.cfg'), './.foremast/foremast.cfg']
    configurations = ConfigParser()
    cfg_file = configurations.read(config_locations)
    dynamic_config_file = getenv('FOREMAST_CONFIG_FILE',
        DEFAULT_DYNAMIC_CONFIG_FILE)
    if cfg_file:
        LOG.info('Loading static configuration file.')
    elif exists(dynamic_config_file):
        LOG.info('Loading dynamic configuration file.')
        configurations = load_dynamic_config(config_file=dynamic_config_file)
    else:
        config_locations.append(dynamic_config_file)
        LOG.warning('No configuration found in the following locations:\n%s',
            '\n'.join(config_locations))
        LOG.warning('Using defaults...')
    return dict(configurations)