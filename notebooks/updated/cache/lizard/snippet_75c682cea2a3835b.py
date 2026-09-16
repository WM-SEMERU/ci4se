def _fetch(self, default_path):
    if not self._path:
        path = default_path
    else:
        path = self._path
    req_type = 'GET' if len(self._post_params) == 0 else 'POST'
    url = '/'.join(['http:/', self.spacegdn.endpoint, path])
    resp = requests.request(req_type, url, params=self._get_params, data=
        self._post_params, headers=self._headers)
    response = Response()
    data = None
    if resp.ok:
        data = resp.json()
    response.add(data, resp.status_code, resp.reason)
    return response