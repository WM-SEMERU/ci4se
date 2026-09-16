def create(self, name, plugin_data_dir, gzip=False):
    self.client.api.create_plugin(name, plugin_data_dir, gzip)
    return self.get(name)