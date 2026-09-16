def all(self, query=None):
    if query is None:
        query = {}
    return self.client._get(self._url(), query)