def _to_dict(self):
    _dict = {}
    if hasattr(self, 'word') and self.word is not None:
        _dict['word'] = self.word
    if hasattr(self, 'sounds_like') and self.sounds_like is not None:
        _dict['sounds_like'] = self.sounds_like
    if hasattr(self, 'display_as') and self.display_as is not None:
        _dict['display_as'] = self.display_as
    if hasattr(self, 'count') and self.count is not None:
        _dict['count'] = self.count
    if hasattr(self, 'source') and self.source is not None:
        _dict['source'] = self.source
    if hasattr(self, 'error') and self.error is not None:
        _dict['error'] = [x._to_dict() for x in self.error]
    return _dict