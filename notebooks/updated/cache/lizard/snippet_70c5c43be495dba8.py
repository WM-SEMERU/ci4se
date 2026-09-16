def _to_dict(self):
    _dict = {}
    if hasattr(self, 'intent') and self.intent is not None:
        _dict['intent'] = self.intent
    if hasattr(self, 'description') and self.description is not None:
        _dict['description'] = self.description
    if hasattr(self, 'created') and self.created is not None:
        _dict['created'] = datetime_to_string(self.created)
    if hasattr(self, 'updated') and self.updated is not None:
        _dict['updated'] = datetime_to_string(self.updated)
    if hasattr(self, 'examples') and self.examples is not None:
        _dict['examples'] = [x._to_dict() for x in self.examples]
    return _dict