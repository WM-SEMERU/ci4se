def removeComponent(self, component):
    if isinstance(component, int):
        index = component
    else:
        index = self._getComponentIndex(component)
    index = normalizers.normalizeIndex(index)
    if index >= self._len__components():
        raise ValueError('No component located at index %d.' % index)
    self._removeComponent(index)