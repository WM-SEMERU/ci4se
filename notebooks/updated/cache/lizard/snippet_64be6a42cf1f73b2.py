def url(self):
    request_params = self._escaped_pagging()
    sorted_request_params = sorted([(k, v) for k, v in request_params.items()])
    req = requests.Request('get', self.request_url, params=
        sorted_request_params).prepare()
    return req.url