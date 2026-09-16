def reverse(self, query, exactly_one=True, timeout=DEFAULT_SENTINEL):
    params = {'ak': self.api_key, 'output': 'json', 'location': self.
        _coerce_point_to_string(query)}
    url = self._construct_url(params)
    logger.debug('%s.reverse: %s', self.__class__.__name__, url)
    return self._parse_reverse_json(self._call_geocoder(url, timeout=
        timeout), exactly_one=exactly_one)