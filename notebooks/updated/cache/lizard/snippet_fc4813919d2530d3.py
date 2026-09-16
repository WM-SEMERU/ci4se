def _to_dict(self):
    _dict = {}
    if hasattr(self, 'results') and self.results is not None:
        _dict['results'] = [x._to_dict() for x in self.results]
    if hasattr(self, 'result_index') and self.result_index is not None:
        _dict['result_index'] = self.result_index
    if hasattr(self, 'speaker_labels') and self.speaker_labels is not None:
        _dict['speaker_labels'] = [x._to_dict() for x in self.speaker_labels]
    if hasattr(self, 'warnings') and self.warnings is not None:
        _dict['warnings'] = self.warnings
    return _dict