def rm(self, typ, id):
    return self._load(self._request(typ, id=id, method='DELETE'))