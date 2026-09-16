def __init(self):
    params = {'f': 'json'}
    json_dict = self._get(self._url, params, securityHandler=self.
        _securityHandler, proxy_url=self._proxy_url, proxy_port=self.
        _proxy_port)
    self._json_dict = json_dict
    self._json = json.dumps(self._json_dict)
    attributes = [attr for attr in dir(self) if not attr.startswith('__') and
        not attr.startswith('_')]
    for k, v in json_dict.items():
        if k in attributes:
            if k == 'versions' and json_dict[k]:
                self._versions = []
                for version in v:
                    self._versions.append(Version(url=self._url + 
                        '/versions/%s' % version, securityHandler=self.
                        _securityHandler, proxy_url=self._proxy_url,
                        proxy_port=self._proxy_port, initialize=False))
            elif k == 'replicas' and json_dict[k]:
                self._replicas = []
                for version in v:
                    self._replicas.append(Replica(url=self._url + 
                        '/replicas/%s' % version, securityHandler=self.
                        _securityHandler, proxy_url=self._proxy_url,
                        proxy_port=self._proxy_port, initialize=False))
            else:
                setattr(self, '_' + k, v)
        else:
            print(k, ' - attribute not implemented for GeoData Service')