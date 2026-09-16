def services(self, *args, **kwargs):
    return self._client.services(*args, scope=self.id, **kwargs)