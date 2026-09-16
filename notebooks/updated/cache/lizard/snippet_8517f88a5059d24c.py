def _to_dict(self):
    _dict = {}
    if hasattr(self, 'text') and self.text is not None:
        _dict['text'] = self.text
    if hasattr(self, 'normalized') and self.normalized is not None:
        _dict['normalized'] = self.normalized
    if hasattr(self, 'verb') and self.verb is not None:
        _dict['verb'] = self.verb._to_dict()
    return _dict