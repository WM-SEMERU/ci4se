def remove(self, *keys):
    keys = list(map(self.get_key, keys))
    return self._client.delete(*keys)