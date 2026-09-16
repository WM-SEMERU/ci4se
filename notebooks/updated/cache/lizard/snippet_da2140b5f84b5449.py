def upload_from_url(self, url, **kwds):
    result = self._client.post('/photo/upload.json', photo=url, **kwds)[
        'result']
    return Photo(self._client, result)