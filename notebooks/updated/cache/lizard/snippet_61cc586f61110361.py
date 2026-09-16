def get(self, path_segment, owner=None, app=None, sharing=None, **query):
    path = self.authority + self._abspath(path_segment, owner=owner, app=
        app, sharing=sharing)
    logging.debug('GET request to %s (body: %s)', path, repr(query))
    response = self.http.get(path, self._auth_headers, **query)
    return response