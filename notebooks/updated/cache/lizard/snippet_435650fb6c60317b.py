def release(self, id):
    json = None
    if int(id) > 0:
        url = self._build_url('releases', str(id), base_url=self._api)
        json = self._json(self._get(url), 200)
    return Release(json, self) if json else None