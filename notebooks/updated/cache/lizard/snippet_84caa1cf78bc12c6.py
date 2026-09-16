def sort_by_key(self, keys=None):
    keys = keys or self.key_on
    keys = keys if isinstance(keys, (list, tuple)) else [keys]
    for key in reversed(keys):
        reverse, key = (True, key[1:]) if key[0] == '-' else (False, key)
        self.table.sort(key=lambda row: row[key], reverse=reverse)