def Name(self, number):
    if number in self._enum_type.values_by_number:
        return self._enum_type.values_by_number[number].name
    raise ValueError('Enum %s has no name defined for value %d' % (self.
        _enum_type.name, number))