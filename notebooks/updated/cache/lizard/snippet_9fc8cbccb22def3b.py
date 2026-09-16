def convert(self):
    if self.is_type():
        return self.force_convert()
    raise TypeConversionError('failed to convert from {} to {}'.format(type
        (self._data).__name__, self.typename))