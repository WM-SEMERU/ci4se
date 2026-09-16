def unmarshall(self, cls):
    for k, v in self.all_settings().items():
        setattr(cls, k, v)
    return cls