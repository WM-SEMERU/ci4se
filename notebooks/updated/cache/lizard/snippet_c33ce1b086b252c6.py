def verify(self, id):
    url = self._url('%s/verify' % id)
    return self.client.post(url)