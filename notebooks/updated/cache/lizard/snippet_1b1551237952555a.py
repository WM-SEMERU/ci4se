def get_series(self, key):
    url = make_series_url(key)
    resp = self.session.get(url)
    return resp