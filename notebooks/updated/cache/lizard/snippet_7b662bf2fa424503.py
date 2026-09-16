def _to_dict(self):
    _dict = {}
    if hasattr(self, 'text') and self.text is not None:
        _dict['text'] = self.text
    if hasattr(self, 'type') and self.type is not None:
        _dict['type'] = self.type
    if hasattr(self, 'evidence') and self.evidence is not None:
        _dict['evidence'] = [x._to_dict() for x in self.evidence]
    return _dict