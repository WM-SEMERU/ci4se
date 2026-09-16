def prime(self):
    for d in self.definitions.values():
        self.defined[d.name] = d.default
    return self