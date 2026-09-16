def _to_dict(self):
    _dict = {}
    if hasattr(self, 'score') and self.score is not None:
        _dict['score'] = self.score
    if hasattr(self, 'tone_id') and self.tone_id is not None:
        _dict['tone_id'] = self.tone_id
    if hasattr(self, 'tone_name') and self.tone_name is not None:
        _dict['tone_name'] = self.tone_name
    return _dict