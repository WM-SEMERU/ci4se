def _post(self, url, **kw):
    headers = kw.pop('headers', {})
    headers.setdefault('Authorization', self.AUTHORIZATION_HEADER)
    kw['headers'] = headers
    resp = self.session.post(url, **kw)
    self._raise_for_status(resp)
    return resp