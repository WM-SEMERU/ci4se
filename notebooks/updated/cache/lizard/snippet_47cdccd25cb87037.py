def put_if_absent(self, key, value):
    check_not_none(key, "key can't be none")
    check_not_none(value, "value can't be none")
    return self._encode_invoke(transactional_map_put_if_absent_codec, key=
        self._to_data(key), value=self._to_data(value))