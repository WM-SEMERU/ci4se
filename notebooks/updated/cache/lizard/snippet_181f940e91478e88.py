def send_request(self, endpoint='ticker', coin_name=None, **kwargs):
    built_url = self._make_url(endpoint, coin_name)
    payload = dict(**kwargs)
    self._process_request(endpoint, built_url, payload)