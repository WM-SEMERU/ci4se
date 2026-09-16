def _to_dict(self):
    _dict = {}
    if hasattr(self, 'emotion') and self.emotion is not None:
        _dict['emotion'] = self.emotion._to_dict()
    return _dict