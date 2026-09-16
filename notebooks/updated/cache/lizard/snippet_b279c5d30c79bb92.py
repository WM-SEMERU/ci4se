def get_envelope(self, component=None, **kwargs):
    kwargs.setdefault('kind', 'envelope')
    return self.get_component(component, **kwargs)