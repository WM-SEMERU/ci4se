def update(self, rid, data, raise_on_error=True):
    cache_data = {'cache-date': self._dt_to_epoch(datetime.now()),
        'cache-data': data}
    return self.ds.put(rid, cache_data, raise_on_error)