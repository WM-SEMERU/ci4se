def _to_dict(self):
    _dict = {}
    if hasattr(self, 'from_') and self.from_ is not None:
        _dict['from'] = self.from_
    if hasattr(self, 'to') and self.to is not None:
        _dict['to'] = self.to
    if hasattr(self, 'speaker') and self.speaker is not None:
        _dict['speaker'] = self.speaker
    if hasattr(self, 'confidence') and self.confidence is not None:
        _dict['confidence'] = self.confidence
    if hasattr(self, 'final_results') and self.final_results is not None:
        _dict['final'] = self.final_results
    return _dict