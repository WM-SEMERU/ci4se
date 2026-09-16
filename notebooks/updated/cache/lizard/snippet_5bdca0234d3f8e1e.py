def output(self, key, obj):
    value = get_value(key if self.attribute is None else self.attribute, obj)
    if value is None:
        return self.default
    return self.format(value)