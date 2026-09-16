def map_get(self, key, mapkey):
    op = SD.get(mapkey)
    sdres = self.lookup_in(key, op)
    return self._wrap_dsop(sdres, True)