def _parse_json(self, page, exactly_one):
    if not page.get('success'):
        return None
    latitude = page['latitude']
    longitude = page['longitude']
    place = page.get('place')
    address = ', '.join([place['city'], place['countryCode']])
    result = Location(address, (latitude, longitude), page)
    if exactly_one:
        return result
    else:
        return [result]