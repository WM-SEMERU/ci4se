def to_python(self, value):
    if value is None or value == '':
        return value
    if isinstance(value, base.Spec):
        return value
    return base.Spec(value)