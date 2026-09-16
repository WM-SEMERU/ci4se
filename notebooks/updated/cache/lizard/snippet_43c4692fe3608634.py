def getRolesForUser(self, username, filter=None, maxCount=None):
    uURL = self._url + '/roles/getRolesForUser'
    params = {'f': 'json', 'username': username}
    if filter is not None:
        params['filter'] = filter
    if maxCount is not None:
        params['maxCount'] = maxCount
    return self._post(url=uURL, param_dict=params, securityHandler=self.
        _securityHandler, proxy_url=self._proxy_url, proxy_port=self.
        _proxy_port)