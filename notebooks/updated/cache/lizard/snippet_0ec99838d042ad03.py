def get_as_nullable_boolean(self, key):
    value = self.get(key)
    return BooleanConverter.to_nullable_boolean(value)