def read_configuration(self):
    c = self._get_pypirc_command()
    c.repository = self.url
    cfg = c._read_pypirc()
    self.username = cfg.get('username')
    self.password = cfg.get('password')
    self.realm = cfg.get('realm', 'pypi')
    self.url = cfg.get('repository', self.url)