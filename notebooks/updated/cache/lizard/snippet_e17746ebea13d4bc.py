def times(self, factor):
    if factor == 0:
        return self.__class__()
    if factor < 0:
        raise ValueError('The factor must no be negative.')
    result = self.__copy__()
    _elements = result._elements
    for element in _elements:
        _elements[element] *= factor
    result._total *= factor
    return result