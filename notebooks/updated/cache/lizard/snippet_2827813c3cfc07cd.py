def get_as_integer(self, key):
    value = self.get(key)
    return IntegerConverter.to_integer(value)