def is_locked(self, key):
    check_not_none(key, "key can't be None")
    key_data = self._to_data(key)
    return self._encode_invoke_on_key(multi_map_is_locked_codec, key_data,
        key=key_data)