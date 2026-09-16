def fetch(self):
    params = values.of({})
    payload = self._version.fetch('GET', self._uri, params=params)
    return FieldValueInstance(self._version, payload, assistant_sid=self.
        _solution['assistant_sid'], field_type_sid=self._solution[
        'field_type_sid'], sid=self._solution['sid'])