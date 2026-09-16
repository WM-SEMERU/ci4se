def append_elements(self, elements):
    self._elements = self._elements + list(elements)
    self._on_element_change()