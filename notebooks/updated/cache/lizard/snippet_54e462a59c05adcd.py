def append(self, value):
    if self.children is None:
        self._parse_children()
    self.children.append(self._make_value(value))
    if self._native is not None:
        self._native.append(self.children[-1].native)
    self._mutated = True