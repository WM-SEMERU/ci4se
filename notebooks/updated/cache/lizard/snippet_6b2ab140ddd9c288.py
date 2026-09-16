def _record_extension(self, key, value):
    record_bean = {'value': value, 'displayName': self._text_bean(key),
        'description': self._text_bean(key), 'displayLabel': self.
        _text_bean(key), 'associatedId': str(self.ident)}
    return record_bean