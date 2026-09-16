def create(self):
    self.service.create()
    predix.config.set_env_value(self.use_class, 'uri', self._get_uri())
    predix.config.set_env_value(self.use_class, 'zone_id', self._get_zone_id())