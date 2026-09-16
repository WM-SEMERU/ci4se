def set_options(self, **kwargs):
    options = self.options
    options.update(kwargs)
    self.update(options=options)