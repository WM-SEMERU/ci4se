def object(self, *args, **kwargs):
    kwargs['api'] = self.api
    return Object(*args, **kwargs)