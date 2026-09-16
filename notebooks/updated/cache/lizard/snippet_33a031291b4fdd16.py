def reverse(self, query, exactly_one=True, timeout=DEFAULT_SENTINEL):
    try:
        lat, lon = self._coerce_point_to_string(query).split(',')
    except ValueError:
        raise ValueError('Must be a coordinate pair or Point')
    params = {'lat': lat, 'lon': lon}
    if self.api_key:
        params['key'] = self.api_key
    url = '?'.join((self.reverse_api, urlencode(params)))
    logger.debug('%s.reverse: %s', self.__class__.__name__, url)
    return self._parse_json(self._call_geocoder(url, timeout=timeout),
        exactly_one)