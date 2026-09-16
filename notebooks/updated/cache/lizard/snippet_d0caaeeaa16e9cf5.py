def _load_entries(self, func, count, page=1, entries=None, **kwargs):
    if entries is None:
        entries = []
    res = func(offset=(page - 1) * self.max_entries_per_load, limit=self.
        max_entries_per_load, **kwargs)
    loaded_entries = [entry for entry in res['data'][:count]]
    total_count = self.count
    if count > total_count:
        count = total_count
    if count <= self.max_entries_per_load:
        return entries + loaded_entries
    else:
        cur_count = count - self.max_entries_per_load
        return self._load_entries(func=func, count=cur_count, page=page + 1,
            entries=entries + loaded_entries, **kwargs)