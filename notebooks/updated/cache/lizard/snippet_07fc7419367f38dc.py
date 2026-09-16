def count(self, view, include=None):
    return self._get(self._build_url(self.endpoint.count(id=view, include=
        include)))