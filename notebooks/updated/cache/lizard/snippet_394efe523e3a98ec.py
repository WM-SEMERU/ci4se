def disable(self):
    self.client.api.disable_plugin(self.name)
    self.reload()