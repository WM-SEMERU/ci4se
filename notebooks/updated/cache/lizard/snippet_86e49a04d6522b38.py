def contains_value(self, value):
    check_not_none(value, "value can't be None")
    value_data = self._to_data(value)
    return self._encode_invoke(multi_map_contains_value_codec, value=value_data
        )