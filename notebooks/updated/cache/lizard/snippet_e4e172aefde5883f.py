def apis(self):
    value = self.attributes['apis']
    if isinstance(value, six.string_types):
        value = shlex.split(value)
    return value