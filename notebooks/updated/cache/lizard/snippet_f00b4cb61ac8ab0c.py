def reindex(self, mode, includes=''):
    url = self._url + '/indexer/reindex'
    params = {'f': 'json', 'mode': mode, 'includes': includes}
    return self._get(url=url, param_dict=params, securityHandler=self.
        _securityHandler, proxy_port=self._proxy_port, proxy_url=self.
        _proxy_url)