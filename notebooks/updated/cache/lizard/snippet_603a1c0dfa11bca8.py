def get_default_value(self):
    if self.choices:
        return self.choices[0]
    value = self.attribute_type()
    if self.attribute_type is time:
        value = int(value)
    elif self.attribute_type is str:
        value = 'A'
    if self.min_length:
        if self.attribute_type is str:
            value = value.ljust(self.min_length, 'a')
        elif self.attribute_type is int:
            value = self.min_length
    elif self.max_length:
        if self.attribute_type is str:
            value = value.ljust(self.max_length, 'a')
        elif self.attribute_type is int:
            value = self.max_length
    return value