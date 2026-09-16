def list(self, **params):
    _, _, lead_sources = self.http_client.get('/lead_sources', params=params)
    return lead_sources