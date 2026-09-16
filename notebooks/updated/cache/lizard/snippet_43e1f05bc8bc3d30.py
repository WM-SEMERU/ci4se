def put_all(self, map):
    entries = {}
    for key, value in six.iteritems(map):
        check_not_none(key, "key can't be None")
        check_not_none(value, "value can't be None")
        entries[self._to_data(key)] = self._to_data(value)
    self._encode_invoke(replicated_map_put_all_codec, entries=entries)