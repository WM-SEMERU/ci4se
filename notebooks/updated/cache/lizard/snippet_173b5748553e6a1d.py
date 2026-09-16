def rate_limit(self):
    url = self._build_url('rate_limit')
    return self._json(self._get(url), 200)