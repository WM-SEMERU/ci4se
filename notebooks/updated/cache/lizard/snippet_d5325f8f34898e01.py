def where(self, params):
    self.params = dict(self.params, **params)
    return self