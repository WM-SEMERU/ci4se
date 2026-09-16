def get_details(self, language=None):
    if self._details is None:
        if language is None:
            try:
                language = self._query_instance._request_params['language']
            except KeyError:
                language = lang.ENGLISH
        self._details = _get_place_details(self.place_id, self.
            _query_instance.api_key, self._query_instance.sensor, language=
            language)