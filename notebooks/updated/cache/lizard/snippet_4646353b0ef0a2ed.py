def list(self, **params):
    _, _, notes = self.http_client.get('/notes', params=params)
    return notes