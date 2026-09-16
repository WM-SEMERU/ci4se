def is_set(self, key):
    path = key.split(self._key_delimiter)
    lower_case_key = key.lower()
    val = self._find(lower_case_key)
    if val is None:
        source = self._find(path[0].lower())
        if source is not None and isinstance(source, dict):
            val = self._search_dict(source, path[1:])
    return val is not None