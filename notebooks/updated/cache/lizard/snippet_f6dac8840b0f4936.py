def from_array(array):
    if array is None or not array:
        return None
    assert_type_or_raise(array, dict, parameter_name='array')
    from pytgbot.api_types.receivable.media import Location
    data = {}
    data['location'] = Location.from_array(array.get('location'))
    data['title'] = u(array.get('title'))
    data['address'] = u(array.get('address'))
    data['foursquare_id'] = u(array.get('foursquare_id')) if array.get(
        'foursquare_id') is not None else None
    data['foursquare_type'] = u(array.get('foursquare_type')) if array.get(
        'foursquare_type') is not None else None
    data['_raw'] = array
    return Venue(**data)