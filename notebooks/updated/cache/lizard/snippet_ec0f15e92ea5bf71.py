def flatten(self, obj):
    return [self._serialize(f, obj) for f in self.fields]