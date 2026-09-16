def update(self, **kwargs):
    self.validate(**kwargs)
    for attr, value in kwargs.items():
        setattr(self, attr, value)
    return self