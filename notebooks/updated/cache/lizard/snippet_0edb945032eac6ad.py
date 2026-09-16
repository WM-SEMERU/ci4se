def float(self, **kwargs):
    for key in kwargs:
        setattr(self, key, kwargs[key])
    self.command = self.COMMAND_FLOAT