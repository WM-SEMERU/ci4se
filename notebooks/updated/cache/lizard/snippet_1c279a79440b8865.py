def _to_dict(self):
    _dict = {}
    if hasattr(self, 'score') and self.score is not None:
        _dict['score'] = self.score
    if hasattr(self, 'sentence') and self.sentence is not None:
        _dict['sentence'] = self.sentence
    if hasattr(self, 'type') and self.type is not None:
        _dict['type'] = self.type
    if hasattr(self, 'arguments') and self.arguments is not None:
        _dict['arguments'] = [x._to_dict() for x in self.arguments]
    return _dict