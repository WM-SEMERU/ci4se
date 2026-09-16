def _typed_value(self, value):
    if value not in self._value_cache:
        new_value = value
        if is_int(value):
            new_value = int(value)
        elif is_float(value):
            new_value = float(value)
        elif is_bool(value):
            new_value = to_bool(value)
        elif is_none(value):
            new_value = None
        self._value_cache[value] = new_value
    return self._value_cache[value]