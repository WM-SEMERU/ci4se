def set_property(self, key, value):
    if key in self.RESERVED_ATTRIBUTE_NAMES:
        return
    self.o[key] = value