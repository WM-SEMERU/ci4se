def set_variable(self, name, value):
    if value is None:
        if name in self._var:
            del self._var[name]
    self._var[name] = value