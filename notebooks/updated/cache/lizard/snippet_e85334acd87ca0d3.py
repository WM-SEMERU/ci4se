def _record_extension(self, objective_id, key, value):
    record_bean = {'value': value, 'displayName': self._text_bean(key),
        'description': self._text_bean(key), 'displayLabel': self.
        _text_bean(key), 'associatedId': str(objective_id)}
    return record_bean