def _request(self, uri, method='GET', params=None, files=None, headers=None,
    auth=None):
    if headers:
        headers['Accept'] = 'application/json'
    else:
        headers = {'Accept': 'application/json'}
    if not self.api_token:
        response = sandboxapi.SandboxAPI._request(self, '/auth/login',
            'POST', headers=headers, auth=HTTPBasicAuth(self.username, self
            .password))
        if response.status_code != 200:
            raise sandboxapi.SandboxError("Can't log in, HTTP Error {e}".
                format(e=response.status_code))
        self.api_token = response.headers.get('X-FeApi-Token')
    headers['X-FeApi-Token'] = self.api_token
    response = sandboxapi.SandboxAPI._request(self, uri, method, params,
        files, headers)
    unauthorized = False
    try:
        if json.loads(response.content.decode('utf-8'))['fireeyeapis'][
            'httpStatus'] == 401:
            unauthorized = True
    except (ValueError, KeyError, TypeError):
        pass
    if response.status_code == 401 or unauthorized:
        self.api_token = None
        try:
            headers.pop('X-FeApi-Token')
        except KeyError:
            pass
        return self._request(uri, method, params, files, headers)
    return response