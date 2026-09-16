def geocode(self, query, exactly_one=True, timeout=DEFAULT_SENTINEL, limit=
    None, typeahead=False, language=None):
    query = self.format_string % query
    params = self._geocode_params(query)
    params['typeahead'] = self._boolean_value(typeahead)
    if limit:
        params['limit'] = str(int(limit))
    if exactly_one:
        params['limit'] = '1'
    if language:
        params['language'] = language
    quoted_query = quote(query.encode('utf-8'))
    url = '?'.join((self.api % dict(query=quoted_query), urlencode(params)))
    logger.debug('%s.geocode: %s', self.__class__.__name__, url)
    return self._parse_json(self._call_geocoder(url, timeout=timeout),
        exactly_one)