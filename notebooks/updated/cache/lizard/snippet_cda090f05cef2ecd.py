def remove(self, element, multiplicity=None):
    _elements = self._elements
    if element not in _elements:
        raise KeyError
    old_multiplicity = _elements.get(element, 0)
    if multiplicity is None or multiplicity >= old_multiplicity:
        del _elements[element]
        self._total -= old_multiplicity
    elif multiplicity < 0:
        raise ValueError('Multiplicity must be not be negative')
    elif multiplicity > 0:
        _elements[element] -= multiplicity
        self._total -= multiplicity
    return old_multiplicity