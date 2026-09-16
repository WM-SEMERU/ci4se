def add_to_manifest(self, manifest):
    manifest.add_service(self.service.name)
    host = predix.config.get_env_key(self.use_class, 'host')
    manifest.add_env_var(host, self.service.settings.data['host'])
    password = predix.config.get_env_key(self.use_class, 'password')
    manifest.add_env_var(password, self.service.settings.data['password'])
    port = predix.config.get_env_key(self.use_class, 'port')
    manifest.add_env_var(port, self.service.settings.data['port'])
    manifest.write_manifest()