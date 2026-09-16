def get_method(self, name, descriptor):
    key = name + str(descriptor)
    if key not in self.methods:
        self.methods[key] = ExternalMethod(self.name, name, descriptor)
    return self.methods[key]