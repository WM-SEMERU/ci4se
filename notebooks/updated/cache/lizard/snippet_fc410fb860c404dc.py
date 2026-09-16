def url(self):
    if self._url is None:
        self._url = request_uri(self.environ, include_query=1)
    return self._url