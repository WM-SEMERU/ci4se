def add(self, element):
    key = self._transform(element)
    if key not in self._elements:
        self._elements[key] = element