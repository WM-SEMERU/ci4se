def geocode(self, query, max_results=25, set_back=0, location_descriptor=
    'any', exactly_one=True, timeout=DEFAULT_SENTINEL):
    params = {'addressString': self.format_string % query}
    if set_back != 0:
        params['setBack'] = set_back
    if location_descriptor not in ['any', 'accessPoint', 'frontDoorPoint',
        'parcelPoint', 'rooftopPoint', 'routingPoint']:
        raise GeocoderQueryError(
            'You did not provided a location_descriptor the webservice can consume. It should be any, accessPoint, frontDoorPoint, parcelPoint, rooftopPoint or routingPoint.'
            )
    params['locationDescriptor'] = location_descriptor
    if exactly_one:
        max_results = 1
    params['maxResults'] = max_results
    url = '?'.join((self.api, urlencode(params)))
    logger.debug('%s.geocode: %s', self.__class__.__name__, url)
    response = self._call_geocoder(url, timeout=timeout)
    if not len(response['features']):
        return None
    geocoded = []
    for feature in response['features']:
        geocoded.append(self._parse_feature(feature))
    if exactly_one:
        return geocoded[0]
    return geocoded