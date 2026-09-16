def all(self, typ, **kwargs):
    return self._load(self._request(typ, params=kwargs))