def system(self):
    url = self._url + '/system'
    return _System(url=url, securityHandler=self._securityHandler,
        proxy_url=self._proxy_url, proxy_port=self._proxy_port)