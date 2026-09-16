def process(self, msg, kwargs):
    kwargs['extra'] = {'correlation_id': self.parent.correlation_id,
        'parent': self.parent.name}
    return msg, kwargs