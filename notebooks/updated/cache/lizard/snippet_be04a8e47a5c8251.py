def validate(self, value):
    if self.type is not None:
        value = coerce(self.type, value)
    if self.min is not None and value < self.min:
        raise ValueError('%s=%s is less than %s' % (self.name, value, self.min)
            )
    if self.max is not None and value > self.max:
        raise ValueError('%s=%s is greater than %s' % (self.name, value,
            self.max))
    if self.allowed is not None and value not in self.allowed:
        raise ValueError('%s=%s is not one of the allowed values: %s' % (
            self.name, value, ','.join(map(str, self.allowed))))
    return value