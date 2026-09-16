def fork(self):
    url = self._build_url('forks', base_url=self._api)
    json = self._json(self._post(url), 201)
    return Gist(json, self) if json else None