def _run(self, url_path, headers=None, **kwargs):
    url = self._construct_url(url_path)
    payload = kwargs
    payload.update({'api_token': self.api_token})
    return self._make_request(url, payload, headers)