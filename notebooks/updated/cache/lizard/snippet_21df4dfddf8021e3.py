def search(self, *args, **kwargs):
    return self._query_zendesk(self.endpoint.search, 'request', *args, **kwargs
        )