def complex_filter(self, filter_obj):
    if isinstance(filter_obj, Filter):
        clone = self._clone()
        clone._filters.add(filter_obj)
        return clone
    return self._filter_or_exclude(None, **filter_obj)