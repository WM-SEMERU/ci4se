def _to_dict(self):
    _dict = {}
    if hasattr(self, 'processed_language'
        ) and self.processed_language is not None:
        _dict['processed_language'] = self.processed_language
    if hasattr(self, 'word_count') and self.word_count is not None:
        _dict['word_count'] = self.word_count
    if hasattr(self, 'word_count_message'
        ) and self.word_count_message is not None:
        _dict['word_count_message'] = self.word_count_message
    if hasattr(self, 'personality') and self.personality is not None:
        _dict['personality'] = [x._to_dict() for x in self.personality]
    if hasattr(self, 'needs') and self.needs is not None:
        _dict['needs'] = [x._to_dict() for x in self.needs]
    if hasattr(self, 'values') and self.values is not None:
        _dict['values'] = [x._to_dict() for x in self.values]
    if hasattr(self, 'behavior') and self.behavior is not None:
        _dict['behavior'] = [x._to_dict() for x in self.behavior]
    if hasattr(self, 'consumption_preferences'
        ) and self.consumption_preferences is not None:
        _dict['consumption_preferences'] = [x._to_dict() for x in self.
            consumption_preferences]
    if hasattr(self, 'warnings') and self.warnings is not None:
        _dict['warnings'] = [x._to_dict() for x in self.warnings]
    return _dict