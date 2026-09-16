def is_default(self):
    for field in self._fields:
        if not field.is_default():
            return False
    return super(Container, self).is_default()