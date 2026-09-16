def geocode(self, query, lang='en', exactly_one=True, timeout=DEFAULT_SENTINEL
    ):
    if not self._check_query(query):
        raise exc.GeocoderQueryError("Search string must be 'word.word.word'")
    params = {'addr': self.format_string % query, 'lang': lang.lower(),
        'key': self.api_key}
    url = '?'.join((self.geocode_api, urlencode(params)))
    logger.debug('%s.geocode: %s', self.__class__.__name__, url)
    return self._parse_json(self._call_geocoder(url, timeout=timeout),
        exactly_one=exactly_one)