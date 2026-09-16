def __init(self):
    params = {'f': 'json'}
    json_dict = self._get(self._url, params, securityHandler=self.
        _securityHandler, proxy_port=self._proxy_port, proxy_url=self.
        _proxy_url)
    self._json = json.dumps(json_dict)
    self._json_dict = json_dict
    self.loadAttributes(json_dict=json_dict)