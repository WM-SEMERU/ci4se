def _to_dict(self):
    _dict = {}
    if hasattr(self, 'key') and self.key is not None:
        _dict['key'] = self.key
    if hasattr(self, 'matching_results') and self.matching_results is not None:
        _dict['matching_results'] = self.matching_results
    if hasattr(self, 'event_rate') and self.event_rate is not None:
        _dict['event_rate'] = self.event_rate
    return _dict