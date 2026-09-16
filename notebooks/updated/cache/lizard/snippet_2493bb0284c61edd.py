def services(self):
    self._services = []
    params = {'f': 'json'}
    json_dict = self._get(url=self._currentURL, param_dict=params,
        securityHandler=self._securityHandler, proxy_url=self._proxy_url,
        proxy_port=self._proxy_port)
    if 'services' in json_dict.keys():
        for s in json_dict['services']:
            uURL = self._currentURL + '/%s.%s' % (s['serviceName'], s['type'])
            self._services.append(AGSService(url=uURL, securityHandler=self
                ._securityHandler, proxy_url=self._proxy_url, proxy_port=
                self._proxy_port))
    return self._services