def process(self, data=None, **kwargs):
    self.data = self.handle(data, **kwargs)
    return self