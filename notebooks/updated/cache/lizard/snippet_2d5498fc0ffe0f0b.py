def _unescape(self, value):
    if isinstance(value, (str, unicode)):
        return value.replace(self._escape_character, '.')
    elif isinstance(value, dict):
        return {self._unescape(k): self._unescape(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [self._unescape(v) for v in value]
    return value