def size(self):
    result = self.grouper.size()
    if isinstance(self.obj, Series):
        result.name = getattr(self.obj, 'name', None)
    return result