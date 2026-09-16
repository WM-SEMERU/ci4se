def read_config(config_path=default_config_path):
    config_path = os.path.expanduser(config_path)
    if not os.path.isfile(config_path):
        raise OSError(errno.ENOENT, 
            "Artifactory configuration file not found: '%s'" % config_path)
    p = configparser.ConfigParser()
    p.read(config_path)
    result = {}
    for section in p.sections():
        username = p.get(section, 'username') if p.has_option(section,
            'username') else None
        password = p.get(section, 'password') if p.has_option(section,
            'password') else None
        verify = p.getboolean(section, 'verify') if p.has_option(section,
            'verify') else True
        cert = p.get(section, 'cert') if p.has_option(section, 'cert'
            ) else None
        result[section] = {'username': username, 'password': password,
            'verify': verify, 'cert': cert}
        if result[section]['cert']:
            result[section]['cert'] = os.path.expanduser(result[section][
                'cert'])
    return result