def get_temp_url_key(self, cached=True):
    meta = self._cached_temp_url_key
    if not cached or not meta:
        key = 'temp_url_key'
        meta = self.get_account_metadata().get(key)
        self._cached_temp_url_key = meta
    return meta