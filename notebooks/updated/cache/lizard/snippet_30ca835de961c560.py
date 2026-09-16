def run(self, path=None):
    if path is None:
        path = '.'
    for prop in self._properties.values():
        if not prop.prompt():
            return False
    return self.build(path)