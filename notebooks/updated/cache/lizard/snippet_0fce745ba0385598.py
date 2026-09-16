def get_option(self, key, subkey, in_path_none=False):
    key, subkey = _lower_keys(key, subkey)
    _entry_must_exist(self.gc, key, subkey)
    df = self.gc[(self.gc['k1'] == key) & (self.gc['k2'] == subkey)]
    if df['type'].values[0] == 'bool':
        return bool(df['value'].values[0])
    elif df['type'].values[0] == 'int':
        return int(df['value'].values[0])
    elif df['type'].values[0] == 'path_in':
        if df['value'].values[0] is None and not in_path_none:
            raise ValueError('Unspecified path for {0}.{1}'.format(key, subkey)
                )
        return df['value'].values[0]
    else:
        return df['value'].values[0]