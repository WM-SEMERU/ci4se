def get_object_record_with_sync(self, pid):
    try:
        return self._cache['records'][pid]
    except KeyError:
        return self._get_uncached_object_record(pid)