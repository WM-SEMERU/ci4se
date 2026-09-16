def get(self, item, default_value=None):
    found, name = self._contains_and_name(item)
    if found:
        return self._record_map[name]['value']
    else:
        return default_value