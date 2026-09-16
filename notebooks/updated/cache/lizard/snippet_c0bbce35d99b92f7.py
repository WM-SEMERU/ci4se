def request(self, path, method, data=None, **kwargs):
    if self.api_token:
        self.request_headers['X-Cachet-Token'] = self.api_token
    if not path.startswith('http://') and not path.startswith('https://'):
        url = '%s/%s' % (self.api_endpoint, path)
    else:
        url = path
    if data is None:
        data = {}
    response = self.r_session.request(method, url, data=json.dumps(data),
        headers=self.request_headers, timeout=self.timeout, verify=self.
        verify, **kwargs)
    response.raise_for_status()
    try:
        return response.json()
    except ValueError:
        return {'data': response.text}