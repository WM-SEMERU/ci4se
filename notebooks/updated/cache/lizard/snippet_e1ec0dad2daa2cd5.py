def _read_credential_file(self, cfg):
    self.username = cfg.get('rackspace_cloud', 'username')
    try:
        self.password = cfg.get('rackspace_cloud', 'api_key', raw=True)
    except ConfigParser.NoOptionError as e:
        self.password = cfg.get('rackspace_cloud', 'password', raw=True)