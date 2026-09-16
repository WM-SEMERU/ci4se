def serialize_list(self, value):
    if not isinstance(value, (list, tuple)):
        return value
    return [self.serialize_value(list_value) for list_value in value]