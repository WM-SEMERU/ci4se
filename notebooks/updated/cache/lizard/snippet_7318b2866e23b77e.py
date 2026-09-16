def map_throats(self, throats, origin, filtered=True):
    r
    ids = origin['throat._id'][throats]
    return self._map(element='throat', ids=ids, filtered=filtered)