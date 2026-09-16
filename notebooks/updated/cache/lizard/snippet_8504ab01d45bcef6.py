def fetch(self, method, uri, query=None, body=None, **kwargs):
    if not query:
        query = {}
    fetch_url = self.get_fetch_url(uri, query)
    args = [fetch_url]
    kwargs.setdefault('timeout', self.timeout)
    kwargs['headers'] = self.get_fetch_headers(method, kwargs.get('headers',
        {}))
    if body:
        if self.is_json(kwargs['headers']):
            kwargs['json'] = self.get_fetch_body(body)
        else:
            kwargs['data'] = self.get_fetch_body(body)
    res = self.get_fetch_request(method, *args, **kwargs)
    res = self.get_fetch_response(res)
    self.response = res
    return res