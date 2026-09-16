def attributes(self, **kwargs):
    path = '/directory-sync-service/v1/attributes'
    r = self._httpclient.request(method='GET', path=path, url=self.url, **
        kwargs)
    return r