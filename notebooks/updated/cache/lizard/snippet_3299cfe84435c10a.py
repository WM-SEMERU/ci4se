def batch(self, client=None):
    client = self._require_client(client)
    return Batch(self, client)