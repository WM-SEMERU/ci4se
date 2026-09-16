def get_config(config_file='/etc/dnsmasq.conf'):
    dnsopts = _parse_dnamasq(config_file)
    if 'conf-dir' in dnsopts:
        for filename in os.listdir(dnsopts['conf-dir']):
            if filename.startswith('.'):
                continue
            if filename.endswith('~'):
                continue
            if filename.endswith('#') and filename.endswith('#'):
                continue
            dnsopts.update(_parse_dnamasq('{0}/{1}'.format(dnsopts[
                'conf-dir'], filename)))
    return dnsopts