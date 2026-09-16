def generate_row_keys(self):
    keys = self.key
    columns = self.values
    if not self._data:
        self._data = self.get_data()
    for column in columns:
        key_prefix = self.cache_key_prefix() + '#' + column
        self._data['cache_key'] = self._data[keys].apply(lambda xdf: 
            key_prefix + '=' + '#'.join(xdf.astype(str).values), axis=1)
    return list(self._data['cache_key'].values)