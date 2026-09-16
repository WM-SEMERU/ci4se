def show(self, item, variant):
    url = self._build_url(self.endpoint.show(item, variant))
    return self._get(url)