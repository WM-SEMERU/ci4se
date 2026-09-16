def setup(self, phase=None, quantity='', conductance='', **kwargs):
    r
    if phase:
        self.settings['phase'] = phase.name
    if quantity:
        self.settings['quantity'] = quantity
    if conductance:
        self.settings['conductance'] = conductance
    self.settings.update(**kwargs)