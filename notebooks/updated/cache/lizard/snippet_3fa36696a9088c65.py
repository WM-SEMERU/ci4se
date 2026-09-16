def to_string(self, value):
    if isinstance(value, six.binary_type):
        value = value.decode('utf-8')
    return self.to_json(value)