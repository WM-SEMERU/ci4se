def url(self, url):
    if url and url.endswith('/'):
        url = url[:-1]
    self._url = url