def geocode(self, query, exactly_one=True, timeout=DEFAULT_SENTINEL,
    candidates=None):
    if candidates is None:
        candidates = self.candidates
    if candidates is None:
        candidates = 1
    if candidates:
        if not 1 <= candidates <= 10:
            raise ValueError('candidates must be between 1 and 10')
    query = {'auth-id': self.auth_id, 'auth-token': self.auth_token,
        'street': self.format_string % query, 'candidates': candidates}
    url = '{url}?{query}'.format(url=self.api, query=urlencode(query))
    logger.debug('%s.geocode: %s', self.__class__.__name__, url)
    return self._parse_json(self._call_geocoder(url, timeout=timeout),
        exactly_one)