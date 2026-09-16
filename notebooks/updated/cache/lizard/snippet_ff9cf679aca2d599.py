def get_json(self, key, default=None):
    value = self.get_str(key)
    if value is not None:
        value = from_json(value)
        if value is not None:
            return value
    if isinstance(default, (dict, list)):
        return default
    return from_json(default)