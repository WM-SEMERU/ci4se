def generate(self, id_or_uri):
    uri = self._client.build_uri(id_or_uri) + '/generate'
    return self._client.get(uri)