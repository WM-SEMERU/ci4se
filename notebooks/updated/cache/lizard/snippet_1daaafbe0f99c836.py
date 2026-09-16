def rm_field(self, name):
    if not name in self._fields:
        raise ValueError
    self._fields.remove(name)
    del self.__dict__[name]