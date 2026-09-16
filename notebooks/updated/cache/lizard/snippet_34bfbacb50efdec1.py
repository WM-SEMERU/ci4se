def stop(self, **kwargs):
    return self.client.api.stop(self.id, **kwargs)