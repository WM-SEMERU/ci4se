def addUsersToRole(self, rolename, users):
    params = {'f': 'json', 'rolename': rolename, 'users': users}
    rURL = self._url + '/roles/addUsersToRole'
    return self._post(url=rURL, param_dict=params, securityHandler=self.
        _securityHandler, proxy_url=self._proxy_url, proxy_port=self.
        _proxy_port)