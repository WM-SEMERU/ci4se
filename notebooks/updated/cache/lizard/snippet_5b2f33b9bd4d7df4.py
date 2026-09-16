def get(self, uri):
    uri = self.URI + uri
    return self._client.get(uri)