def clusters(self):
    if self._clusters is not None:
        self.__init()
        Cs = []
        for c in self._clusters:
            url = self._url + '/%s' % c['clusterName']
            Cs.append(Cluster(url=url, securityHandler=self.
                _securityHandler, proxy_url=self._proxy_url, proxy_port=
                self._proxy_port, initialize=True))
        self._clusters = Cs
    return self._clusters