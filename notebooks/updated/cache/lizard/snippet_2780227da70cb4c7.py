def resize(self, height, width):
    return self.client.api.resize(self.id, height, width)