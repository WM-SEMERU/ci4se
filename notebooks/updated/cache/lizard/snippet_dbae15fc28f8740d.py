def parse(self, value):
    if self.required and value is None:
        raise ValueError('%s is required!' % self.name)
    elif self.ignored and value is not None:
        warn('%s is ignored for this class!' % self.name)
    elif not self.multi and isinstance(value, (list, tuple)):
        if len(value) > 1:
            raise ValueError('%s does not accept multiple values!' % self.name)
        return value[0]
    elif self.multi and value is not None:
        if not isinstance(value, (list, tuple)):
            return [value]
    return value