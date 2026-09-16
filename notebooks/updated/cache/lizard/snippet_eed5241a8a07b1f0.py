def validate(self, instance, value):
    value_type = type(value)
    if not isinstance(value, string_types):
        self.error(instance, value)
    if self.regex is not None and self.regex.search(value) is None:
        self.error(instance, value, extra='Regex does not match.')
    value = value.strip(self.strip)
    if self.change_case == 'upper':
        value = value.upper()
    elif self.change_case == 'lower':
        value = value.lower()
    if self.unicode:
        value = text_type(value)
    else:
        value = value_type(value)
    return value