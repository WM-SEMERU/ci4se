def propertyNames(self):
    r
    for k in self.data:
        yield k
    if self.defaults is not None:
        for k in self.defaults.propertyNames():
            if k not in self.data:
                yield k