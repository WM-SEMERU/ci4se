def unwrap(self, value, session=None):
    self.validate_unwrap(value)
    ret = []
    for field, value in izip(self.types, value):
        ret.append(field.unwrap(value, session=session))
    return tuple(ret)