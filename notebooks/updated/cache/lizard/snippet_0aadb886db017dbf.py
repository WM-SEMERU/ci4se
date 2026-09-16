def get_keys_from_value(self, value):
    return [key for key, data in self.iteritems() if data == value]