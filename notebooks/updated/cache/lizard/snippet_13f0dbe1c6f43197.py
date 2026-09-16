def _find_keys(self, identity='image'):
    prefix = add_prefix('', identity)
    raw_keys = self._find_keys_raw(prefix) or []
    for raw_key in raw_keys:
        yield del_prefix(raw_key)