def namespace(self):
    if self.prefix is None:
        return self.defaultNamespace()
    return self.resolvePrefix(self.prefix)