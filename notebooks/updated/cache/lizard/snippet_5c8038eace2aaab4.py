def _to_dict(self):
    _dict = {}
    if hasattr(self, 'limit') and self.limit is not None:
        _dict['limit'] = self.limit
    if hasattr(self, 'mentions') and self.mentions is not None:
        _dict['mentions'] = self.mentions
    if hasattr(self, 'model') and self.model is not None:
        _dict['model'] = self.model
    if hasattr(self, 'sentiment') and self.sentiment is not None:
        _dict['sentiment'] = self.sentiment
    if hasattr(self, 'emotion') and self.emotion is not None:
        _dict['emotion'] = self.emotion
    return _dict