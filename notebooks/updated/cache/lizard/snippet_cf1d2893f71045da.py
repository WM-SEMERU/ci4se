def config():
    conf_args = {'INTERVAL': 60, 'STANDBY': 3}
    config_file = read_file('{0}{1}'.format(conf_path, 'sun.conf'))
    for line in config_file.splitlines():
        line = line.lstrip()
        if line and not line.startswith('#'):
            conf_args[line.split('=')[0]] = line.split('=')[1]
    return conf_args