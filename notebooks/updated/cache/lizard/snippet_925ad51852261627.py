def bind(self, key, factory):
    if key in self.factories:
        raise AlreadyBoundError(key)
    else:
        self.factories[key] = factory