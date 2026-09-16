def list(self, **params):
    _, _, deal_sources = self.http_client.get('/deal_sources', params=params)
    return deal_sources