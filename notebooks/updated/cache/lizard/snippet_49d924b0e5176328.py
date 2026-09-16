def persistentValues(self):
    return dict((k, getattr(self, k)) for k, attr in self.getSchema())