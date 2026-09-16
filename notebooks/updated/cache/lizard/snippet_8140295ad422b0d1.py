def _parse_prop(self, dd, row):
    key = row['name']
    if key.startswith('#'):
        deprecated = True
    else:
        deprecated = False
    v = dd.get(key)
    _value = self._get_value(row)
    if not v:
        v = dd.setdefault(key, {})
        v[_value] = deprecated
    elif not _value in v:
        v[_value] = deprecated