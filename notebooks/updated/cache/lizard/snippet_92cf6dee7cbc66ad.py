def _convert_entry(self, entry):
    result = {}
    for key, value in entry.items():
        if isinstance(value, list):
            result[key] = [self._convert_field(key, val) for val in value]
        else:
            result[key] = self._convert_field(key, value)
    return result