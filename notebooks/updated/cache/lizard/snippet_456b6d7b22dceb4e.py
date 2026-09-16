def read_config(self):
    with open(self.config_file) as cfg:
        try:
            self.config.read_file(cfg)
        except AttributeError:
            self.config.readfp(cfg)
    self.client_id = self.config.get('exist', 'client_id')
    self.client_secret = self.config.get('exist', 'client_secret')
    self.access_token = self.config.get('exist', 'access_token')