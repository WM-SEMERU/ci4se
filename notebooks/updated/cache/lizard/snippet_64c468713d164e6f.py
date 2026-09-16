def get_hosts_files(option):
    if option is not None:
        return option.split(',')
    if os.path.isfile('hosts'):
        return ['hosts']
    config_locations = ['.', '/etc/ansible/']
    config_dir = util.find_path(config_locations, 'ansible.cfg')
    log.debug('config_dir = {0}'.format(config_dir))
    if config_dir:
        with open(os.path.join(config_dir, 'ansible.cfg'), 'r') as cf:
            for line in cf:
                if line.startswith('hostfile'):
                    return [line.split('=', 1)[1].strip()]