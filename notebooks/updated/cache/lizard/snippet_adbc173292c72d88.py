def contribute_to_class(self, cls, name):
    super(StateField, self).contribute_to_class(cls, name)
    parent_property = getattr(cls, self.name, None)
    setattr(cls, self.name, StateFieldProperty(self, parent_property))