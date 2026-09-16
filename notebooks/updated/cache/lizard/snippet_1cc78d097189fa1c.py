def get_config(self, hostname):
    version, config = self._get(self.associations.get(hostname))
    return config