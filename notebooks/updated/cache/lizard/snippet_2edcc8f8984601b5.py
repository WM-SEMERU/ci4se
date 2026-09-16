def delete(self, album, **kwds):
    return self._client.post('/album/%s/delete.json' % self._extract_id(
        album), **kwds)['result']