def update(self, **kwargs):
    self.inflate()
    for model in self._models:
        model.update(**kwargs)
    return self