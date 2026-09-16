def _configure(self):
    configfile = expanduser('~/.ssh/config')
    if not isfile(configfile):
        raise GerritError("ssh config file '%s' does not exist" % configfile)
    config = SSHConfig()
    config.parse(open(configfile))
    data = config.lookup(self.hostname)
    if not data:
        raise GerritError('No ssh config for host %s' % self.hostname)
    if 'hostname' not in data or 'port' not in data or 'user' not in data:
        raise GerritError('Missing configuration data in %s' % configfile)
    self.hostname = data['hostname']
    self.username = data['user']
    if 'identityfile' in data:
        key_filename = abspath(expanduser(data['identityfile'][0]))
        if not isfile(key_filename):
            raise GerritError("Identity file '%s' does not exist" %
                key_filename)
        self.key_filename = key_filename
    try:
        self.port = int(data['port'])
    except ValueError:
        raise GerritError('Invalid port: %s' % data['port'])
    if 'proxycommand' in data:
        self.proxy = ProxyCommand(data['proxycommand'])