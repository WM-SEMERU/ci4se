def check_option(self, key, subkey, value):
    key, subkey = _lower_keys(key, subkey)
    _entry_must_exist(self.gc, key, subkey)
    df = self.gc[(self.gc['k1'] == key) & (self.gc['k2'] == subkey)]
    ev.value_eval(value, df['type'].values[0])
    if df['values'].values[0] is not None:
        return value in df['values'].values[0]
    return True