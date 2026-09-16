def get(self, url):
    self._query()
    return Enclosure(self._resp.get(url), url)