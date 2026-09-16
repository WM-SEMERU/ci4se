def set_params(self, **kwargs):
    for key, value in list(kwargs.items()):
        setattr(self, key, value)