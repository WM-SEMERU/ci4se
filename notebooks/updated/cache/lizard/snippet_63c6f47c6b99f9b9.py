def update(self, tag, **kwds):
    result = self._client.post('/tag/%s/update.json' % self._quote_url(self
        ._extract_id(tag)), **kwds)['result']
    return Tag(self._client, result)