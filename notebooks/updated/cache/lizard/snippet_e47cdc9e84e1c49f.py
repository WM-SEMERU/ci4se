def get(self, *, search, limit=0, headers=None):
    return self.transport.forward_request(method='GET', path=self.path,
        params={'search': search, 'limit': limit}, headers=headers)