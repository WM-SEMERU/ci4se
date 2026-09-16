def info(self):
    if self._resources is None:
        self.__init()
    url = self._url + '/info'
    return _info.Info(url=url, securityHandler=self._securityHandler,
        proxy_url=self._proxy_url, proxy_port=self._proxy_port, initialize=True
        )