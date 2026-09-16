def set_translation_start(self, feature_id, start, organism=None, sequence=None
    ):
    data = {'features': [{'uniquename': feature_id, 'location': {'fmin':
        start}}]}
    data = self._update_data(data, organism, sequence)
    return self.post('setTranslationStart', data)