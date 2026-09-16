def update_parameters(self, **kwargs):
    for key, value in list(kwargs.items()):
        if key in dir(self) and not key.startswith('_'):
            setattr(self, key, value)
        else:
            log('Invalid RAPID parameter %s.' % key, 'ERROR')