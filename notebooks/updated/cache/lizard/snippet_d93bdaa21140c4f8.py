def get_for_update(self, key):
    check_not_none(key, "key can't be none")
    return self._encode_invoke(transactional_map_get_for_update_codec, key=
        self._to_data(key))