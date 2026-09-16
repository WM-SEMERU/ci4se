def oauth2(self):
    if self._url.endswith('/oauth2'):
        url = self._url
    else:
        url = self._url + '/oauth2'
    return _oauth2.oauth2(oauth_url=url, securityHandler=self.
        _securityHandler, proxy_url=self._proxy_url, proxy_port=self.
        _proxy_port)