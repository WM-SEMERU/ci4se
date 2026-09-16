def get_as_map_with_default(self, key, default_value):
    value = self.get_as_nullable_map(key)
    return MapConverter.to_map_with_default(value, default_value)