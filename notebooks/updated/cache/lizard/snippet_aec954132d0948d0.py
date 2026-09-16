def immediate(self, name, value):
    setattr(self, name, value)
    self._all.add(name)