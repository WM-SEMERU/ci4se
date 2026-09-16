def list_series(self, keys=None, tags=None, attrs=None, limit=1000):
    params = {'key': keys, 'tag': tags, 'attr': attrs, 'limit': limit}
    url_args = endpoint.make_url_args(params)
    url = '?'.join([endpoint.SERIES_ENDPOINT, url_args])
    resp = self.session.get(url)
    return resp