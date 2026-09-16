def _set_attribute(self, name, value):
    setattr(self, name, value)
    self.namespace.update({name: getattr(self, name)})