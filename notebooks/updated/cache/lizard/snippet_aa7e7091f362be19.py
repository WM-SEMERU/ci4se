def _to_dict(self):
    _dict = {}
    if hasattr(self, 'text') and self.text is not None:
        _dict['text'] = self.text
    if hasattr(self, 'keywords') and self.keywords is not None:
        _dict['keywords'] = [x._to_dict() for x in self.keywords]
    return _dict