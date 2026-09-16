def getp(self, name):
    name = self._mapping.get(name, name)
    return self.params[name]